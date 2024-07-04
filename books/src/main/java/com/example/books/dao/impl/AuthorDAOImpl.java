package com.example.books.dao.impl;

import com.example.books.dao.AuthorDAO;
import com.example.books.domain.Author;
import org.springframework.jdbc.core.JdbcTemplate;

public class AuthorDAOImpl implements AuthorDAO { // Methods in DAO class are CRUD operations for the Author entity.
    private final JdbcTemplate jdbcTemplate; // Jdbc Template is a bean
    // Spring’s dependency injection mechanism will automatically inject an instance of JdbcTemplate when creating an instance of AuthorDAOImpl
    public AuthorDAOImpl(final JdbcTemplate jdbcTemplate){
        this.jdbcTemplate = jdbcTemplate;
    }

    @Override
    public void create(Author author) {
        jdbcTemplate.update(
                "INSERT INTO authors (id, name, age) VALUES (?, ?, ?)",
                author.getId(), author.getName(), author.getAge()
        );
    }
}
