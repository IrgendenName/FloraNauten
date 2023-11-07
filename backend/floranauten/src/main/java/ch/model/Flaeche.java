package ch.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@RequiredArgsConstructoer
@Getter
@Document("flaeche")
@Entitiy
public class Flaeche {
    @Id
    private String name;
    private String eigenschaft; //Grünfläche oder Verkehrsfläche
    private String kategorie;

    @NonNull
    private List<String> massnahmen; //Liste der passenden Massnahmen
    
}
