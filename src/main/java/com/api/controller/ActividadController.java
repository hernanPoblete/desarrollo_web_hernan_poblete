package com.api.controller;

import org.springframework.web.bind.annotation.RestController;

import com.api.model.ActividadRepo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import com.api.model.Actividad;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@CrossOrigin(origins = "127.0.0.1:5000")
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

    @GetMapping("/actividad/getByPattern/{pattern}")
    public List<Actividad> getActividadesByPattern( @PathVariable String pattern){
        return repo.findByNombreContaining(pattern);
    }
    
    
}
