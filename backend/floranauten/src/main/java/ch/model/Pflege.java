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
@Document("pflege")
@Entity
public class Pflege {
    @Id
    private String name;
    private String intervall;
    private String rhytmus;
    
}
