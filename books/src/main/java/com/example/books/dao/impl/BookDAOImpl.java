package com.example.books.dao.impl;

import com.example.books.dao.BookDAO;
import org.springframework.jdbc.core.JdbcTemplate;

public class BookDAOImpl implements BookDAO {
    private final JdbcTemplate jdbcTemplate; // Jdbc Template is a bean
    // Spring’s dependency injection mechanism will automatically inject an instance of JdbcTemplate when creating an instance of AuthorDAOImpl
    public BookDAOImpl(final JdbcTemplate jdbcTemplate){
        this.jdbcTemplate = jdbcTemplate;
    }

}
