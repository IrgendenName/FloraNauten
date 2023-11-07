package com.floranauten.floranauten.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;

@Getter
@Document("pflege")
public class pflege {
    @Id
    private String name;
    private String intervall;
    private String rhytmus;
}
