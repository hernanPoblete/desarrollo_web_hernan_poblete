package com.api.model;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;


public interface ActividadRepo extends JpaRepository<Actividad, Integer>{
    List<Actividad> findByNombreContaining(String pattern);
}
