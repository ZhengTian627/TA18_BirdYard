import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image # Pillow for image handling
import cv2 # OpenCV for image decoding
import numpy as np
import torch # To check device, though we force CPU
import traceback # For detailed error logging

# --- Configuration ---
# ADJUST THIS PATH to where you copied your best.pt file on the EC2 instance
MODEL_PATH = '/home/ubuntu/bird_model/best.pt' # <<<--- CHANGE THIS PATH
CONFIDENCE_THRESHOLD = 0.4
DEVICE = 'cpu' # Force CPU for EC2 free tier

# --- Load Model ---
# Load the model ONCE when the application starts for efficiency
model = None # Initialize model as None
try:
    print(f"Loading model from {MODEL_PATH} onto device '{DEVICE}'...")
    if MODEL_PATH: # Basic check if path is set
        model = YOLO(MODEL_PATH)
        print("Model loaded successfully.")
    else:
        print("Error: MODEL_PATH is not set.")
except Exception as e:
    print(f"Error loading model at startup: {e}")
    traceback.print_exc()
    # Keep model as None, requests will fail until fixed and restarted

# --- Create FastAPI App ---
app = FastAPI(title="Endangered Bird Detection API")

@app.on_event("startup")
async def startup_event():
    # Log model status at startup
    if model is None:
        print("WARNING: Model failed to load at startup. Prediction endpoint will return errors.")
    else:
        print("FastAPI application started. Model is loaded and ready.")

@app.get("/")
async def read_root():
    """ Basic endpoint to check if the API is running. """
    return {"message": "Welcome to the Bird Detection API. Use the /predict/ endpoint (POST) to upload an image."}

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    """
    Receives an image file, performs YOLOv8 prediction, and returns results.
    """
    # Check if model loaded correctly during startup
    if model is None:
        print("Error: Prediction attempted but model is not loaded.")
        raise HTTPException(status_code=503, detail="Model is not available or failed to load. Check server logs.")

    print(f"Received file: {file.filename}, Content-Type: {file.content_type}")

    # Validate image type
    if not file.content_type.startswith("image/"):
         print(f"Error: Invalid file type received: {file.content_type}")
         raise HTTPException(status_code=400, detail=f"Invalid file type: {file.content_type}. Please upload an image (e.g., JPEG, PNG).")

    try:
        # Read image content into memory
        contents = await file.read()

        # --- Convert image bytes to OpenCV format ---
        # Using OpenCV directly is generally efficient
        nparr = np.frombuffer(contents, np.uint8)
        open_cv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Check if image decoding was successful
        if open_cv_image is None:
             print("Error: cv2.imdecode returned None. Image format might be invalid or corrupted.")
             raise HTTPException(status_code=400, detail="Could not decode image file. Ensure it's a valid, uncorrupted image format (like JPEG or PNG).")
        # --- End image conversion ---

        print(f"Image decoded successfully, shape: {open_cv_image.shape}")

        # --- Perform Prediction ---
        # Using the globally loaded model instance
        print(f"Running model prediction on device '{DEVICE}'...")
        results = model.predict(
            source=open_cv_image,       # Use the decoded image data
            conf=CONFIDENCE_THRESHOLD,
            device=DEVICE,              # Explicitly use CPU
            verbose=False               # Suppress detailed YOLO console output per prediction
        )
        print("Prediction complete.")

        # --- Process Results ---
        output_data = []
        # Check if results list is populated
        if results and len(results) > 0:
            result = results[0] # Process the first result object
            boxes = result.boxes.cpu().numpy() # Get boxes on CPU as numpy array for easier handling

            print(f"Found {len(boxes)} potential objects above threshold.")

            # Iterate through detected boxes
            for box in boxes:
                # Extract information for each detection
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                bbox_coords = box.xyxy[0].tolist() # [x1, y1, x2, y2]

                # Prepare detection dictionary
                detection = {
                    "class_id": class_id,
                    "class_name": model.names.get(class_id, f"Unknown ID: {class_id}"), # Safely get class name
                    "confidence": round(confidence, 4), # Round confidence
                    "bounding_box": [round(coord, 2) for coord in bbox_coords], # Round coordinates
                }
                output_data.append(detection)
                print(f"  - Detected: {detection['class_name']} (Conf: {detection['confidence']}) @ {detection['bounding_box']}")

        if not output_data:
             print(f"No objects detected above the confidence threshold ({CONFIDENCE_THRESHOLD}).")

        # Return results as JSON
        return JSONResponse(content={"detections": output_data})

    # Handle specific exceptions we might anticipate
    except HTTPException as http_err:
        # Re-raise HTTP exceptions (like 400 Bad Request) directly
        raise http_err
    # Catch any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred during prediction for file {file.filename}: {e}")
        traceback.print_exc() # Log the full traceback for debugging
        # Return a generic server error response to the client
        raise HTTPException(status_code=500, detail=f"An internal server error occurred while processing the image.")
