package com.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;

@Entity(name = "nota")
public class Nota {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;

    @Column(name = "nota")
    private Integer nota;


    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="actividad_id")
    private Actividad actividad;

    public Nota(){

    }


    public Nota (Actividad actividad, Integer nota){
        this.actividad = actividad;
        this.nota = nota;
    }
    public Integer getNota() {
        return nota;
    }
}
