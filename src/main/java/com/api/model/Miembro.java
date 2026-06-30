package com.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;

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
    private Date fecha_registro;
    
    @Column(name = "comuna_id")
    private Integer comuna_id;
    
    public Miembro(){}

    public String getNombre() {
        return nombre;
    }

    public String getEmail() {
        return email;
    }
}
