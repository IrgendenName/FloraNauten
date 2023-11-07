package ch.model;

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
@Document("massnahmen")
@Entitiy
public class Massnahmen {
    @Id
    private String name;
    @NonNull
    private String beschreibung;
    private String spetifizierung;
    private int kosten;

    @NonNull
    private List<String> pflanzen;

    @NonNull
    private String pflege;

}
