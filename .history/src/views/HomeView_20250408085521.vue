<template>
  <div class="home-page">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">WHERE PLANTS TAKE ROOTS,<br />BIRDS FIND HOME.</h1>
        <p class="hero-subtitle">
          "Bird Yard helps you build a safe, healthy, bird-friendly backyard — a true home for
          birds."
        </p>
        <div class="hero-buttons">
          <router-link to="/contact" class="btn btn-primary">Get In Touch</router-link>
          <router-link to="/about" class="btn btn-secondary">Who We Are</router-link>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="cta-section">
      <router-link to="/plantadvice" class="btn btn-large">Let's Build Your Backyard</router-link>
    </section>

    <!-- Seasonal Images Section -->
    <section class="seasonal-section">
      <div class="container">
        <h2 class="seasonal-title">Birds Through the Seasons</h2>
        <div class="seasonal-content">
          <div class="seasonal-image-container">
            <transition name="fade" mode="out-in">
              <img
                :src="require(`@/assets/images/${currentSeasonImage}`)"
                :key="currentSeasonImage"
                alt="Seasonal backyard"
                class="seasonal-image"
              />
            </transition>
          </div>
          <div class="seasonal-text">
            <h3>{{ currentSeasonTitle }}</h3>
            <p>{{ currentSeasonDescription }}</p>
            <div class="season-selector">
              <button
                v-for="(season, index) in seasons"
                :key="index"
                @click="setCurrentSeason(index)"
                :class="['season-btn', currentSeasonIndex === index ? 'active' : '']"
              >
                {{ season.name }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section class="about-section">
      <div class="container">
        <div class="about-content">
          <div class="about-text">
            <h2>Welcome to Bird-Yard,<br />Where Birds Feel at Home, Right in Your Backyard.</h2>
            <router-link to="/about" class="about-link">
              About Us
              <span class="arrow">→</span>
            </router-link>
          </div>
          <div class="about-description">
            <p>
              Established with a love for nature and a mission to protect what sings in our skies,
              Bird-Yard helps people transform everyday backyards into thriving bird habitats. We're
              dedicated to guiding you in cultivating gardens that are not only beautiful, but safe,
              sustainable sanctuaries for local wildlife. From native plant recommendations to
              habitat-friendly landscaping tips, Bird-Yard is your partner in preserving
              biodiversity—one backyard at a time.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Grow in 4 Steps Section -->
    <section class="steps-section">
      <div class="container">
        <h2 class="steps-title">"Grow in 4 Steps:"</h2>
        <div class="steps-container">
          <!-- Step 1 -->
          <div class="step">
            <h3>01. Plan with Purpose:</h3>
            <ul>
              <li>Observe sunlight, shade, and wind direction.</li>
              <li>Choose native plants suited to your climate and soil.</li>
              <li>Design layers: trees, shrubs, ground-covers.</li>
            </ul>
          </div>

          <!-- Step 2 -->
          <div class="step">
            <h3>02. Prepare the Ground:</h3>
            <ul>
              <li>Clear weeds and debris (ditch those invasives).</li>
              <li>Improve soil with compost or organic matter.</li>
              <li>Lay mulch to retain moisture and suppress weeds.</li>
            </ul>
          </div>

          <!-- Step 3 -->
          <div class="step">
            <h3>03. Plant & Position:</h3>
            <ul>
              <li>Group plants with similar water/light needs.</li>
              <li>Space properly—plants grow more than you think!</li>
              <li>Add habitat boosters: rocks, logs, bird baths, and nesting boxes.</li>
            </ul>
          </div>

          <!-- Step 4 -->
          <div class="step">
            <h3>04. Maintain with Care:</h3>
            <ul>
              <li>Water consistently, especially in the early weeks.</li>
              <li>Prune gently and seasonally.</li>
              <li>Re-mulch every few months.</li>
              <li>Avoid chemicals—let nature handle pests.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomePage',
  data() {
    return {
      currentSeasonIndex: 0,
      seasons: [
        {
          name: 'Spring',
          image: 'homespring.jpg',
          title: 'Spring: A Time of Renewal',
          description:
            'Welcome migratory birds back to your garden as new life sprouts. Early bloomers provide crucial nectar for pollinators, while nesting birds seek dense shrubs and trees for protection.',
        },
        {
          name: 'Summer',
          image: 'homesummer.jpg',
          title: 'Summer: The Season of Abundance',
          description:
            'Vibrant summer gardens offer shelter, nesting materials, and plentiful food sources. Flowering plants attract insects that become food for birds, while bird baths provide essential hydration during hot days.',
        },
        {
          name: 'Autumn',
          image: 'homeautumn.jpg',
          title: 'Autumn: Preparing for Change',
          description:
            'Fall-fruiting plants provide energy-rich food before migration or winter. Seed-bearing plants and berries sustain birds through changing seasons, while fallen leaves create habitat for insects birds feed on.',
        },
        {
          name: 'Winter',
          image: 'homewinter.jpg',
          title: 'Winter: A Time of Resilience',
          description:
            'Evergreen plants offer shelter from harsh elements, while seed heads and berries provide vital nourishment. Your winter garden becomes a sanctuary for year-round residents when resources are scarce.',
        },
      ],
      autoRotateInterval: null,
    }
  },
  computed: {
    currentSeasonImage() {
      return this.seasons[this.currentSeasonIndex].image
    },
    currentSeasonTitle() {
      return this.seasons[this.currentSeasonIndex].title
    },
    currentSeasonDescription() {
      return this.seasons[this.currentSeasonIndex].description
    },
  },
  methods: {
    setCurrentSeason(index) {
      this.currentSeasonIndex = index
      // Reset auto-rotation timer when manually changed
      this.startAutoRotate()
    },
    nextSeason() {
      this.currentSeasonIndex = (this.currentSeasonIndex + 1) % this.seasons.length
    },
    startAutoRotate() {
      // Clear any existing interval
      if (this.autoRotateInterval) {
        clearInterval(this.autoRotateInterval)
      }
      // Set up a new interval
      this.autoRotateInterval = setInterval(this.nextSeason, 8000) // Change every 8 seconds
    },
  },
  mounted() {
    this.startAutoRotate()
  },
  beforeUnmount() {
    // Clean up interval when component is destroyed
    if (this.autoRotateInterval) {
      clearInterval(this.autoRotateInterval)
    }
  },
})
</script>

<style scoped>
/* Global styles */
.container {
  max-width: 1200px;
  top: 0;
  margin: 0 auto;
  padding: 0 auto;
}

.btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 30px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  text-align: center;
}

.btn-primary {
  background-color: rgba(194, 229, 156, 0.8);
  color: #0a3200;
  border: 2px solid #c2e59c;
}

.btn-secondary {
  background-color: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  border: 2px solid rgba(255, 255, 255, 0.6);
  margin-left: 15px;
}

.btn-large {
  padding: 15px 30px;
  font-size: 18px;
  background-color: rgba(194, 229, 156, 0.9);
  color: #0a3200;
  border: 2px solid #c2e59c;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

/* Hero Section */
.hero {
  height: 100vh;
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('@/assets/images/homepage.jpeg');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 20px;
}

.hero-content {
  max-width: 900px;
}

.hero-title {
  font-size: 3.5rem;
  color: #ffffff;
  margin-bottom: 20px;
  line-height: 1.2;
  font-weight: bold;
}

.hero-subtitle {
  font-size: 1.3rem;
  color: #ffffff;
  margin-bottom: 40px;
  line-height: 1.5;
}

.hero-buttons {
  margin-top: 30px;
}

/* CTA Section */
.cta-section {
  padding: 40px 0;
  text-align: center;
  background-color: #f9f9f9;
}

/* Seasonal Images Section */
.seasonal-section {
  padding: 80px 0;
  background-color: #f9f9f9;
}

.seasonal-title {
  font-size: 2.2rem;
  text-align: center;
  margin-bottom: 40px;
  color: #0a3200;
}

.seasonal-content {
  display: flex;
  gap: 40px;
  align-items: center;
}

.seasonal-image-container {
  flex: 1;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  height: 400px;
}

.seasonal-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.seasonal-image:hover {
  transform: scale(1.05);
}

.seasonal-text {
  flex: 1;
  padding: 20px;
}

.seasonal-text h3 {
  font-size: 1.8rem;
  color: #0a3200;
  margin-bottom: 20px;
}

.seasonal-text p {
  font-size: 1.1rem;
  line-height: 1.7;
  color: #333;
  margin-bottom: 30px;
}

.season-selector {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.season-btn {
  padding: 8px 16px;
  background-color: #f1f1f1;
  border: 2px solid #ddd;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  color: #0a3200;
}

.season-btn.active {
  background-color: #c2e59c;
  border-color: #0a3200;
}

.season-btn:hover {
  background-color: #e9e9e9;
  transform: translateY(-2px);
}

.season-btn.active:hover {
  background-color: #b8dc8a;
}

/* Fade transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* About Section */
.about-section {
  padding: 80px 0;
  background-color: #ffffff;
}

.about-content {
  display: flex;
  gap: 60px;
}

.about-text {
  flex: 1;
}

.about-text h2 {
  font-size: 2.2rem;
  color: #0a3200;
  line-height: 1.3;
  margin-bottom: 30px;
}

.about-description {
  flex: 1;
}

.about-description p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #333;
}

.about-link {
  display: inline-flex;
  align-items: center;
  color: #0a3200;
  font-weight: 600;
  text-decoration: none;
  font-size: 1.1rem;
}

.about-link .arrow {
  margin-left: 8px;
  transition: transform 0.3s ease;
}

.about-link:hover .arrow {
  transform: translateX(5px);
}

/* Steps Section */
.steps-section {
  padding: 80px 0;
  background-color: #0a3200;
  color: #ffffff;
}

.steps-title {
  font-size: 2.2rem;
  text-align: center;
  margin-bottom: 60px;
  color: #c2e59c;
}

.steps-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 40px;
}

.step h3 {
  color: #c2e59c;
  font-size: 1.4rem;
  margin-bottom: 20px;
}

.step ul {
  list-style-type: disc;
  padding-left: 20px;
}

.step li {
  margin-bottom: 10px;
  line-height: 1.6;
}

/* Responsive Design */
@media (max-width: 992px) {
  .about-content,
  .seasonal-content {
    flex-direction: column;
    gap: 30px;
  }

  .steps-container {
    grid-template-columns: 1fr;
  }

  .footer-columns {
    grid-template-columns: repeat(2, 1fr);
  }

  .seasonal-image-container {
    width: 100%;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.1rem;
  }

  .btn-secondary {
    margin-left: 0;
    margin-top: 15px;
  }

  .hero-buttons {
    display: flex;
    flex-direction: column;
    gap: 15px;
    align-items: center;
  }

  .about-text h2,
  .seasonal-title {
    font-size: 1.8rem;
  }

  .footer-columns {
    grid-template-columns: 1fr;
  }

  .seasonal-text h3 {
    font-size: 1.5rem;
  }
}
</style>
