package com.ta18.birdyard.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "plants")
public class RecommendedPlant {

  @Id
  private Integer id;

  @Column(name = "plant_name")
  private String plantName;

  @Column(name = "state")
  private String state;

  @Column(name = "postcode")
  private Integer postcode;

  @Column(name = "season")
  private String season;

  @Column(name = "description")
  private String description;

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public String getPlantName() {
    return plantName;
  }

  public void setPlantName(String plantName) {
    this.plantName = plantName;
  }

  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }

  public Integer getPostcode() {
    return postcode;
  }

  public void setPostcode(Integer postcode) {
    this.postcode = postcode;
  }

  public String getSeason() {
    return season;
  }

  public void setSeason(String season) {
    this.season = season;
  }

  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }
}
