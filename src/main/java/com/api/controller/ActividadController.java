package com.api.controller;

import org.springframework.web.bind.annotation.RestController;

import com.api.model.ActividadRepo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import com.api.model.Actividad;


@RestController
public class ActividadController {
    
    @Autowired
    private ActividadRepo repo;
    
    public ActividadController(ActividadRepo repo){
        this.repo=repo;
    }

    @GetMapping("/actividad/getById/{id}")
    public Actividad getActividadById( @PathVariable Integer id) {
        return repo.getReferenceById(id);
    }
    
}
