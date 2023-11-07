package com.floranauten.floranauten.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;

@Getter
@Document("pflanze")
public class pflanze {
    @Id
    private String name;
    private String bioName;
    private String zusatz;
    private String katArt;
}
