package com.ta18.birdyard.controller;

import com.ta18.birdyard.entity.RecommendedPlant;
import com.ta18.birdyard.service.PlantRecommendationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/plants")
@CrossOrigin
public class PlantController {

  @Autowired
  private PlantRecommendationService plantService;

  @GetMapping
  public List<RecommendedPlant> getRecommendedPlants(
      @RequestParam String state,
      @RequestParam String season
  ) {
    System.out.println("Received request - State: [" + state + "], Season: [" + season + "]");
    return plantService.getPlantsByStateAndSeason(state, season);
  }

  @GetMapping("/debug")
  public List<RecommendedPlant> debugAll() {
    return plantService.getAllPlants();
  }
}
