package com.example.books.dao;

import com.example.books.dao.impl.AuthorDAOImpl;
import com.example.books.domain.Author;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.jdbc.core.JdbcTemplate;

import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.verify;


@ExtendWith(MockitoExtension.class) // for testing
public class AuthorDAOImplTests {
    @Mock // @Mock annotation indicates that jdbcTemplate will be mocked by Mockito
    private JdbcTemplate jdbcTemplate;

    @InjectMocks // @InjectMocks annotation injects mocked dependencies into the underTest object
    private AuthorDAOImpl underTest;

// - @Mock: Mockito will create a mock instance of JdbcTemplate.
// - @InjectMocks: Mockito will inject the mocked JdbcTemplate into underTest.

    @Test
    public void testThatCreateAuthorGeneratesCorrectSQL(){
        // Create an Author object using the builder pattern
        Author author = new Author(1L, "Abigail Rose", 80);

        underTest.create(author);
        verify(jdbcTemplate).update(
                eq("INSERT INTO authors (id, name, age) VALUES (?, ?, ?)"),
                eq(1L), eq("Abigail Rose"), eq(80)
        );
    }

}
