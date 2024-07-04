package com.example.books.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

@Configuration
public class DatabaseConfig {

    @Bean // will return an object that should be registered as a bean in the Spring application context.
    public JdbcTemplate jdbcTemplate(final DataSource dataSource){
        // It handles the creation and release of resources, which helps to avoid potential resource leaks.
        // It also provides methods for querying and updating the database.
        return new JdbcTemplate(dataSource);

        // Data Source: This is a standard interface to interact with the database.
        // Spring will automatically inject the appropriate DataSource bean into this method when it calls it.
    }
}
