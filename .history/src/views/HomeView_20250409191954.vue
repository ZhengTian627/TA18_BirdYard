<template>
  <div class="home-page">
    <!-- Hero Section -->
    <section class="hero">
      <!-- Content remains the same -->
    </section>

    <!-- About Section -->
    <section class="about-section">
      <!-- Content remains the same -->
    </section>

    <!-- Information Section with Modal Popups -->
    <section class="info-section">
      <div class="container">
        <h2 class="info-title">Discover Garden Wisdom</h2>
        <div class="info-cards">
          <div class="info-card">
            <div class="card-image" @click="showPlantModal = true">
              <img src="@/assets/images/plant-importance.jpg" alt="Plant importance" />
              <div class="card-overlay">
                <h3>Plants: The Garden Foundation</h3>
                <span class="learn-more">Learn More</span>
              </div>
            </div>
          </div>
          <div class="info-card">
            <div class="card-image" @click="showBirdModal = true">
              <img src="@/assets/images/attracting-birds.jpg" alt="Attracting birds" />
              <div class="card-overlay">
                <h3>Attracting Birds with Plants</h3>
                <span class="learn-more">Learn More</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Plant Importance Modal -->
      <transition name="slide-fade">
        <div class="modal" v-if="showPlantModal">
          <div class="modal-overlay" @click="showPlantModal = false"></div>
          <div class="modal-container">
            <div class="modal-header">
              <h2>The Importance of Plants in Your Garden</h2>
              <button class="close-button" @click="showPlantModal = false">&times;</button>
            </div>
            <div class="modal-content">
              <img
                src="@/assets/images/plant-importance.jpg"
                alt="Plant importance"
                class="modal-image"
              />
              <div class="modal-text">
                <h3>Building a Thriving Ecosystem</h3>
                <p>Plants are the foundation of every healthy garden ecosystem. They provide:</p>
                <ul>
                  <li>
                    <strong>Oxygen production:</strong> Plants release oxygen and absorb carbon
                    dioxide, improving air quality.
                  </li>
                  <li>
                    <strong>Soil health:</strong> Root systems prevent erosion and add organic
                    matter to soil.
                  </li>
                  <li>
                    <strong>Water filtration:</strong> Plants help filter rainwater, reducing runoff
                    and pollution.
                  </li>
                  <li>
                    <strong>Biodiversity:</strong> Native plants support local insects, which are
                    essential food for birds.
                  </li>
                  <li>
                    <strong>Climate regulation:</strong> Gardens help cool urban areas and reduce
                    the heat island effect.
                  </li>
                </ul>

                <h3>Choosing the Right Plants</h3>
                <p>
                  Native plants are always the best choice for a bird-friendly garden. They've
                  evolved alongside local wildlife for thousands of years, providing the perfect
                  food sources, shelter, and nesting materials. Native plants also typically require
                  less water and maintenance once established.
                </p>

                <router-link to="/plantadvice" class="modal-link"
                  >Get Plant Recommendations →</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- Attracting Birds Modal -->
      <transition name="slide-fade">
        <div class="modal" v-if="showBirdModal">
          <div class="modal-overlay" @click="showBirdModal = false"></div>
          <div class="modal-container">
            <div class="modal-header">
              <h2>How to Attract Birds with Plants</h2>
              <button class="close-button" @click="showBirdModal = false">&times;</button>
            </div>
            <div class="modal-content">
              <img
                src="@/assets/images/attracting-birds.jpg"
                alt="Attracting birds"
                class="modal-image"
              />
              <div class="modal-text">
                <h3>Creating a Bird Haven</h3>
                <p>
                  Birds need four essential things from your garden: food, water, shelter, and
                  nesting sites. The right plants can provide most of these needs!
                </p>

                <h3>Food Sources</h3>
                <ul>
                  <li>
                    <strong>Berry-producing shrubs:</strong> Elderberry, serviceberry, and dogwood
                    provide seasonal fruits.
                  </li>
                  <li>
                    <strong>Seed-bearing flowers:</strong> Coneflowers, sunflowers, and black-eyed
                    Susans offer winter food.
                  </li>
                  <li>
                    <strong>Host plants for insects:</strong> Oak, willow, and native perennials
                    support caterpillars and bugs that birds feed to their young.
                  </li>
                </ul>

                <h3>Shelter & Nesting</h3>
                <ul>
                  <li>
                    <strong>Evergreen trees and shrubs:</strong> Provide year-round protection from
                    predators and weather.
                  </li>
                  <li>
                    <strong>Dense thickets:</strong> Create safe spaces for small birds to hide and
                    nest.
                  </li>
                  <li>
                    <strong>Varying heights:</strong> Different bird species prefer nesting at
                    different levels.
                  </li>
                </ul>

                <h3>Additional Tips</h3>
                <p>
                  Combine your plant strategy with a clean water source like a bird bath, avoid
                  pesticides that kill insect food sources, and maintain some "messy" areas with
                  fallen leaves and natural debris where birds can forage.
                </p>

                <router-link to="/birdguide" class="modal-link">Explore Bird Species →</router-link>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section">
      <!-- Content remains the same -->
    </section>

    <!-- Grow in 4 Steps Section -->
    <section class="steps-section">
      <!-- Content remains the same -->
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomePage',
  data() {
    return {
      showPlantModal: false,
      showBirdModal: false,
    }
  },
})
</script>

<style scoped>
/* Existing styles remain the same */

/* Info Section Styles */
.info-section {
  padding: 80px 0;
  background-color: #f9f9f9;
}

.info-title {
  font-size: 2.2rem;
  text-align: center;
  margin-bottom: 50px;
  color: #0a3200;
}

.info-cards {
  display: flex;
  justify-content: center;
  gap: 40px;
}

.info-card {
  flex: 1;
  max-width: 500px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.info-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.card-image {
  position: relative;
  height: 350px;
  cursor: pointer;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(10, 50, 0, 0.8));
  padding: 20px;
  color: white;
  transition: background 0.3s ease;
}

.card-overlay h3 {
  margin-bottom: 8px;
  font-size: 1.4rem;
}

.learn-more {
  display: inline-block;
  font-weight: 600;
  border-bottom: 2px solid #c2e59c;
  padding-bottom: 2px;
  transition: transform 0.3s ease;
}

.card-image:hover .card-overlay {
  background: linear-gradient(transparent, rgba(10, 50, 0, 0.9));
}

.card-image:hover .learn-more {
  transform: translateX(5px);
}

/* Modal Styles */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 101;
}

.modal-container {
  position: relative;
  width: 90%;
  max-width: 900px;
  max-height: 90vh;
  background-color: white;
  border-radius: 8px;
  overflow-y: auto;
  z-index: 102;
}

.modal-header {
  padding: 20px;
  border-bottom: 1px solid #eee;
  position: relative;
}

.modal-header h2 {
  color: #0a3200;
  margin: 0;
}

.close-button {
  position: absolute;
  top: 15px;
  right: 20px;
  font-size: 30px;
  background: none;
  border: none;
  cursor: pointer;
  color: #333;
}

.modal-content {
  padding: 0;
}

.modal-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.modal-text {
  padding: 30px;
}

.modal-text h3 {
  color: #0a3200;
  margin-top: 25px;
  margin-bottom: 15px;
}

.modal-text ul {
  margin-bottom: 25px;
}

.modal-text li {
  margin-bottom: 10px;
  line-height: 1.6;
}

.modal-link {
  display: inline-block;
  margin-top: 20px;
  color: #0a3200;
  font-weight: 600;
  text-decoration: none;
  border-bottom: 2px solid #c2e59c;
  transition: all 0.3s ease;
}

.modal-link:hover {
  color: #4a7d32;
  transform: translateX(5px);
}

/* Transition Animation */
.slide-fade-enter-active {
  transition: all 0.3s ease;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .info-cards {
    flex-direction: column;
    align-items: center;
  }

  .info-card {
    width: 100%;
  }

  .modal-content {
    flex-direction: column;
  }

  .modal-image {
    height: 200px;
  }
}
</style>
