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
@Document("pflanzen")
@Entity
public class Pflanze {
    @Id
    private String name;
    private String biologischerName;
    private String katArt;
    
    
}
