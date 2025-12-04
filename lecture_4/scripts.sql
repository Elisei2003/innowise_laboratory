-- Создание базы данных
CREATE DATABASE SchoolDB;
GO

USE SchoolDB;
GO

-- 1. Создание таблицы students
-- Используем IDENTITY(1,1) для автоматической генерации ID,
-- что решает проблему Msg 515, так как нам не нужно вставлять NULL или значение.
CREATE TABLE students (
    id INT PRIMARY KEY IDENTITY(1,1),
    full_name NVARCHAR(100) NOT NULL,
    birth_year INT NOT NULL
);
GO

-- 2. Создание таблицы grades
CREATE TABLE grades (
    id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT NOT NULL,
    subject NVARCHAR(50) NOT NULL,
    grade INT NOT NULL CHECK (grade >= 1 AND grade <= 100),
    -- Определение внешнего ключа
    FOREIGN KEY (student_id) REFERENCES students(id)
);
GO

USE SchoolDB;
GO

-- Вставка студентов
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);
GO

-- Вставка оценок
-- В SQL Server мы можем вставить все сразу, используя IDs, которые были сгенерированы
-- последовательно (1, 2, 3, ..., 9)
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
(2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
(3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
(4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
(5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
(6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
(7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
(8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
(9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);
GO

USE SchoolDB;
GO

SELECT
    s.full_name,
    g.subject,
    g.grade
FROM
    grades g
JOIN
    students s ON g.student_id = s.id
WHERE
    s.full_name = 'Alice Johnson';

USE SchoolDB;
GO

SELECT
    s.full_name,
    COUNT(g.id) AS NumberOfGrades,
    AVG(CAST(g.grade AS DECIMAL(5, 2))) AS AverageGrade
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
GROUP BY
    s.id, s.full_name
ORDER BY
    AverageGrade DESC;

USE SchoolDB;
GO

SELECT
    full_name,
    birth_year
FROM
    students
WHERE
    birth_year > 2004;

USE SchoolDB;
GO
-- Теперь выполняйте запрос 6
SELECT
    subject,
    AVG(CAST(grade AS DECIMAL(5, 2))) AS AverageSubjectGrade
FROM
    grades
GROUP BY
    subject
ORDER BY
    AverageSubjectGrade DESC;

-- Создание индекса для оптимизации запросов по студентам
CREATE INDEX IX_Grades_StudentID ON grades (student_id);
GO

USE SchoolDB;
GO

SELECT TOP 3
    s.full_name,
    AVG(CAST(g.grade AS DECIMAL(5, 2))) AS TopAverageGrade
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
GROUP BY
    s.id, s.full_name
ORDER BY
    TopAverageGrade DESC;


USE SchoolDB;
GO

SELECT DISTINCT
    s.full_name,
    s.birth_year
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
WHERE
    g.grade < 80;
