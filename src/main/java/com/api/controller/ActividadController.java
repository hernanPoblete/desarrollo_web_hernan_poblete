package com.api.controller;

import org.springframework.web.bind.annotation.RestController;

import com.api.model.ActividadRepo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;


@RestController
public class ActividadController {
    private final ActividadRepo repo;
    
    public ActividadController(ActividadRepo repo){
        this.repo=repo;
    }

    @GetMapping("/actividad/getById/{id}")
    public String getActividadById( @PathVariable Integer id) {
        return repo.getReferenceById(id).getNombre();
    }
    
}
