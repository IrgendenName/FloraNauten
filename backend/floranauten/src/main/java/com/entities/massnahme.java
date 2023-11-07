package com.entities;


import java.util.List;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import lombok.AllArgsConstructor;
import lombok.Getter;

@AllArgsConstructor
@Getter
@Entity
public class massnahme {
    @Id
    private String name;
    private String beschreibung;
    private String spezifizierung;
    private int kosten;

    @OneToMany
    @JoinColumn(name = "name", nullable = false)
    private List<String> pflanzen;

    @OneToOne
    @JoinColumn(name = "name", nullable = false)
    private String pflege;
}
