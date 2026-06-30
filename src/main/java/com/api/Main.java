package com.api;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.RestController;

import com.api.model.*;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@SpringBootApplication
@RestController
public class Main {
    public static void main(String args[]){
        SpringApplication.run(Main.class, args);  
    }



    @GetMapping("/")
    public String getTest() {
        return "Hallo Wold";
    }
    
}