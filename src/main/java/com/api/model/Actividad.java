package com.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity(name="actividad")
public class Actividad {

    @Id
    @Column(name = "id")
    private Integer id;

    private Integer miembro_id;
    
    @Column(name="dia")
    private String dia;

    @Column(name="hora_inicio")
    private String hora_inicio;

    @Column(name="duracion")
    private String duracion;

    @Column(name="tipo")
    private String tipo;

    @Column(name="nombre")
    private String nombre;

    @Column(name="descripcion")
    private String descripcion;

    
    public Actividad(){}


    public String getNombre(){
        return nombre;
    }


}
