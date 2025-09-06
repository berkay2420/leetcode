DROP TABLE Person;

CREATE TABLE Person(
	id int,
    email VARCHAR(255)
);

INSERT INTO Person
VALUES (1,  "john@example.com" );
INSERT INTO Person
VALUES (2,  "bob@example.com" );
INSERT INTO Person
VALUES (3,  "john@example.com" );

SELECT * 
FROM Person;

SELECT email, COUNT(email)
FROM Person 
GROUP BY email
HAVING COUNT(email) > 1;

SELECT * 
FROM Person p1
INNER JOIN Person p2
	ON p1.id = p2.id;

SELECT * FROM Person p1 
INNER JOIN Person p2
WHERE
	p1.id > p2.id AND
    p1.email = p2.email;

-- SOLUTION1
-- This query returns table with 3x3 = 9 length (Cartesian Product). Because we are using WHERE instead of ON
-- From that table SQL finds row(s) where p1 id is bigger and both email columns are identical
-- And deletes it
DELETE p1 FROM Person p1 
INNER JOIN Person p2
WHERE
	p1.id > p2.id AND
    p1.email = p2.email;
    
    
    
-- SOLUTION 2
DELETE p1
FROM Person p1
INNER JOIN Person p2 
    ON p1.email = p2.email 
   AND p1.id > p2.id;
