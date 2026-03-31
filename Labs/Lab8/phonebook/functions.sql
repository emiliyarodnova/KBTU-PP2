-- search by pattern
CREATE OR REPLACE FUNCTION search_phonebook_pattern(p_pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.surname, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || p_pattern || '%'
       OR p.surname ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%'
    ORDER BY p.id;
END;
$$ LANGUAGE plpgsql;


-- get contacts with pagination
CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.surname, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
