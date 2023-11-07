package com.floranauten.floranauten.model;

import java.util.List;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@RequiredArgsConstructor
@Getter
@Document("fleache")
public class flaeche {
    @Id
    private String name;
    private String eigenschaft;
    private String kategorie;

    @NonNull
    private List<String> massnahmen;

}
