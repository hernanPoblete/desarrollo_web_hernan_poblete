package com.api.controller;

import org.springframework.web.bind.annotation.RestController;

import com.api.model.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import java.util.Optional;


@RestController
public class RegionController {
    
    @Autowired
    private final RegionRepo repo;

    public RegionController(RegionRepo repo){
        this.repo=repo;
    }

    @GetMapping("/region/get/{id}")
    public String getRegionById(@PathVariable Integer id) {
        
        Optional<Region> region = repo.findById(id);


        if(!region.isEmpty()){
            return region.get().toString();
        }
        return id.toString();
    }
    
}
