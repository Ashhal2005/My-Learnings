CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);

INSERT INTO Departments VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics');

INSERT INTO Students VALUES
(101, 'Ali', 1),
(102, 'Ahmed', 1),
(103, 'Sara', 2),
(104, 'Ayesha', 3);

SELECT s.StudentName, d.DeptName
FROM Students s
INNER JOIN Departments d
ON s.DeptID = d.DeptID;

CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(50)
);

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

INSERT INTO Authors VALUES
(1, 'J.K. Rowling'),
(2, 'George Orwell'),
(3, 'Mark Twain');

INSERT INTO Books VALUES
(1, 'Harry Potter 1', 1),
(2, 'Harry Potter 2', 1),
(3, '1984', 2),
(4, 'Tom Sawyer', 3);

SELECT b.Title, a.AuthorName
FROM Books b
INNER JOIN Authors a
ON b.AuthorID = a.AuthorID;

CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    TeacherName VARCHAR(50)
);

CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY,
    SubjectName VARCHAR(50),
    TeacherID INT,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

INSERT INTO Teachers VALUES
(1, 'Mr. Khan'),
(2, 'Ms. Ali'),
(3, 'Mr. Ahmed');

INSERT INTO Subjects VALUES
(1, 'Math', 1),
(2, 'Science', 2);

SELECT t.TeacherName, s.SubjectName
FROM Teachers t
LEFT JOIN Subjects s
ON t.TeacherID = s.TeacherID;

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(50)
);

CREATE TABLE Emp (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    ProjectID INT,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

INSERT INTO Projects VALUES
(1, 'AI System'),
(2, 'Web App'),
(3, 'Mobile App');

INSERT INTO Emp VALUES
(1, 'Ali', 1),
(2, 'Sara', 2);

SELECT e.EmpName, p.ProjectName
FROM Emp e
RIGHT JOIN Projects p
ON e.ProjectID = p.ProjectID;

CREATE TABLE Students2 (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

INSERT INTO Students2 VALUES
(1, 'Ali'),
(2, 'Sara');

INSERT INTO Courses VALUES
(1, 'Database'),
(2, 'Programming');

SELECT s.StudentName, c.CourseName
FROM Students2 s
CROSS JOIN Courses c;



SELECT * from Students;