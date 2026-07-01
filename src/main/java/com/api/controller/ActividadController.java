package com.api.controller;

import org.springframework.web.bind.annotation.RestController;

import com.api.model.ActividadRepo;
import com.api.model.Nota;
import com.api.model.NotaRepo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import com.api.model.Actividad;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import com.api.DTO.*;


@CrossOrigin(origins = "127.0.0.1:5000")
@RestController
public class ActividadController {
    
    @Autowired
    private ActividadRepo repo;

    @Autowired
    private NotaRepo notaRepo;
    
    public ActividadController(ActividadRepo repo, NotaRepo notaRepo){
        this.repo=repo;

        this.notaRepo = notaRepo;
    }

    @GetMapping("/actividad/getById/{id}")
    public Actividad getActividadById( @PathVariable Integer id) {
        return repo.getReferenceById(id);
    }

    @GetMapping("/actividad/getByPattern/{pattern}")
    public List<Actividad> getActividadesByPattern( @PathVariable String pattern){
        return repo.findByNombreContaining(pattern);
    }

    @PostMapping("/actividad/agregarNota")
    public String grade(@RequestBody SubirNota body) {
        
        Actividad actividad = repo.getReferenceById(body.getIdActividad());

        if (body.getNota() > 7 || body.getNota()<1) return "Nota fuera de límites";
        
        Nota nota = new Nota(actividad, body.getNota());
        notaRepo.save(nota);

        return "OK";
    }
    
    
    
}
