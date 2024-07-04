package com.example.books.domain;

public class Author {
    private Long id;
    private String name;
    private Integer age;

    // Constructors
    public Author() {
    }

    public Author(Long id, String name, Integer age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }


}
