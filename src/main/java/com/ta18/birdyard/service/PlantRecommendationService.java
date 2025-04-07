package com.ta18.birdyard.service;

import com.ta18.birdyard.entity.RecommendedPlant;
import com.ta18.birdyard.repository.RecommendedPlantRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PlantRecommendationService {

  @Autowired
  private RecommendedPlantRepository plantRepository;

  public List<RecommendedPlant> getPlantsByStateAndSeason(String state, String season) {
    return plantRepository.findTop4ByStateAndSeason(state, season);
  }

  public List<RecommendedPlant> getAllPlants() {
    return plantRepository.findAll();
  }
}
