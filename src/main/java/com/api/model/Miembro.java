package com.api.model;

import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;

@Entity(name = "miembro")
public class Miembro {
    

    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name="nombre")
    private String nombre;

    @Column(name="email")
    private String email;

    @Column(name = "telefono")
    private String telefono;


    @Column(name = "fecha_registro")
    private LocalDate fecha_registro;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "comuna_id")
    private Comuna comuna;
    
    public Miembro(){}

    public String getNombre() {
        return nombre;
    }

    public String getEmail() {
        return email;
    }

    public Comuna getComuna() {
        return comuna;
    }
}
