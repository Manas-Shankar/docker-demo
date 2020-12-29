CREATE DATABASE employees;
use employees;

CREATE TABLE employees (
  name VARCHAR(20),
  eid VARCHAR(10)
);

INSERT INTO employees
  (name, eid)
VALUES
  ('Lancelot', '1'),
  ('Galahad', '2');