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
@Document("massnahme")
public class massnahme {
    @Id
    private String name;
    private String beschreibung;
    private String spezifizierung;
    private int kosten;

    @NonNull
    private List<String> pflanzen;
    @NonNull
    private String pflege;
}
