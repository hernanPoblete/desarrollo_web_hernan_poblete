package com.api.model;

import java.util.ArrayList;
import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;

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

    @OneToMany(mappedBy = "actividad", cascade = CascadeType.REFRESH, orphanRemoval = true)
    private List<Nota> notas;

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

    public Double getNotaAvg(){
        return notas.stream().mapToDouble(x->x.getNota()).average().orElse(0.0);
    }
}
