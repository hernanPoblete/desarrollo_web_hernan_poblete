package com.api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;

@Entity(name="actividad")
public class Actividad {

    @Id
    @Column(name = "id")
    private Integer id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "miembro_id")
    private Miembro miembro;
    
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

    public Integer getId(){
        return id;
    }

    public Miembro getMiembro() {
        return miembro;
    }

    public String getDescripcion() {
        return descripcion;
    }
    public String getDia() {
        return dia;
    }
    public String getHora_inicio() {
        return hora_inicio;
    }
    public String getTipo() {
        return tipo;
    }
}
