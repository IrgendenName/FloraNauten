package com.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Abfrage {
    @GetMapping("/abfrage")
    public String helloWorld(@RequestParam String name) {
        return "Hello " + name + "\n";
    }

}
