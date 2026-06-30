package com.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity(name="region")
public class Region {

    @Id
    @Column(name="id", nullable = false)
    private Integer id;

    @Column(name="nombre", nullable = false)
    private String nombre;
    

    public Region() {}
    public Region(Integer id, String nombre){
        this.nombre = nombre;
    }


    public Integer getID(){
        return id;
    }


    public String getName(){
        return nombre;
    }
}
