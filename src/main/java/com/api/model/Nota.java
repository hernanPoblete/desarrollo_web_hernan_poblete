package com.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.FetchType;

@Entity(name = "nota")
public class Nota {
    
    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "nota")
    private Integer nota;


    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="actividad_id")
    private Actividad actividad;


    public Integer getNota() {
        return nota;
    }
}
