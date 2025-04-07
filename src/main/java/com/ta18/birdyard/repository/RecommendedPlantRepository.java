package com.ta18.birdyard.repository;

import com.ta18.birdyard.entity.RecommendedPlant;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RecommendedPlantRepository extends JpaRepository<RecommendedPlant, Integer> {
  List<RecommendedPlant> findTop4ByStateAndSeason(String state, String season);
}
