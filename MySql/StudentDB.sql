use db;
CREATE TABLE students(
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    Id varchar(8) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students(FirstName, Surname,Id)
VALUES("Asambaev", "Al-Turar","19B0616")  