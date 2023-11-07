package com.floranauten.floranauten.entitis;

import java.util.List;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import lombok.NonNull;
import lombok.Getter;
import lombok.AllArgsConstructor;

@AllArgsConstructor
@Getter
@Entity
public class flaeche {
    @Id
    private String name;
    private String eigenschaft;
    private String kategorie;

    @OneToMany
    @JoinColumn(name = "name", nullable = false)
    private List<String> massnahmen;

}
