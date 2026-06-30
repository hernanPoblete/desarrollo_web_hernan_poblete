package com.api.model;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Column;

@Entity(name = "comuna")
public class Comuna {
    

    @Id
    private Integer id;
    
    @Column(name="nombre")
    private String nombre;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "region_id")
    private Region region;

    public Comuna(){}

    public String getNombre() {
        return nombre;
    }

    public String getRegion(){
        return region.getName();
    }

}
