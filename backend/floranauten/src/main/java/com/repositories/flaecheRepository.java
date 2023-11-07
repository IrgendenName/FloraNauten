package com.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.entities.massnahme;

public interface flaecheRepository extends JpaRepository<massnahme, Long>{

    //BSP:
    //@Query("SELECT co FROM Company co WHERE co.name LIKE %?1%")
    // public List<Company> getCompanyByName(String name);
    
}
