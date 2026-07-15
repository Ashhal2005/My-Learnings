use Assignment;

-- Task 1--
SELECT name,salary
FROM employees 
WHERE salary < (SELECT AVG(salary) FROM employees);

-- Task 2--
SELECT name, budget
FROM projects
WHERE budget > (SELECT AVG(budget) FROM projects);

-- Task 3--
SELECT name, hire_date
FROM employees 
WHERE hire_date > (SELECT AVG(hire_date) FROM employees);

-- Task 4--
SELECT name
FROM departments d
WHERE (SELECT COUNT(*) FROM employees WHERE dept_id = d.id) > 
      (SELECT AVG(dept_size) FROM (SELECT COUNT(*) AS dept_size FROM employees GROUP BY dept_id) AS sizes);

-- Task 5--
SELECT name, salary,
(SELECT MAX(salary) FROM employees e2 WHERE e2.dept_id = e1.dept_id) AS max_in_dept
FROM employees e1;

-- Task 6--
SELECT e.name, (SELECT SUM(hours_worked) FROM projects p WHERE p.employee_id = e.id) AS
total_hours
FROM employees e
WHERE (SELECT SUM(hours_worked) FROM projects p WHERE p.employee_id = e.id) >
(SELECT AVG(total_hours) FROM (SELECT SUM(hours_worked) AS total_hours FROM
projects GROUP BY employee_id) AS t);

-- Task 7--
SELECT name, salary
FROM employees e1
WHERE salary >= 0.9 * (
    SELECT MAX(salary) 
    FROM employees e2 
    WHERE e2.dept_id = e1.dept_id
);

-- Task 8--
SELECT e.name
FROM employees e
WHERE (
    SELECT COUNT(*) 
    FROM projects p 
    WHERE p.employee_id = e.id
) = (
    SELECT MAX(proj_count)
    FROM (
        SELECT COUNT(*) AS proj_count 
        FROM projects p2 
        JOIN employees e2 ON p2.employee_id = e2.id 
        WHERE e2.dept_id = e.dept_id 
        GROUP BY p2.employee_id
    ) AS counts
);

-- Task 9--
SELECT d.name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.id
GROUP BY d.name
HAVING SUM(e.salary) > (
    SELECT AVG(total) 
    FROM (SELECT SUM(salary) AS total FROM employees GROUP BY dept_id) AS dept_totals
);

-- Task 10--
SELECT e.name, e.salary, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;

-- Task 11--
SELECT name
FROM employees e
WHERE NOT EXISTS (SELECT 1 FROM projects p WHERE p.employee_id = e.id);

-- Task 12--
SELECT name 
FROM departments d
WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.dept_id = d.id);

-- task 13--
SELECT e.name
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM projects p 
    JOIN employees pe ON p.employee_id = pe.id
    WHERE pe.dept_id = e.dept_id 
      AND p.employee_id <> e.id);

-- Task 14--
SELECT name 
FROM projects 
WHERE employee_id IS NULL;

-- Task 15--
SELECT name 
FROM employees m
WHERE (SELECT COUNT(*) FROM employees e WHERE e.manager_id = m.id) >= 3;

-- Task 16--
SELECT name, salary
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = (SELECT id FROM
departments WHERE name = 'IT'));

-- Task 17--
SELECT name, salary
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = (SELECT id FROM
departments WHERE name = 'IT'));

-- Task 18--
SELECT e1.name, e1.salary
FROM employees e1
WHERE EXISTS (
    SELECT 1 
    FROM employees e2 
    WHERE e2.salary = e1.salary 
      AND e2.dept_id <> e1.dept_id
);

-- Task 19--
SELECT e1.name, e1.salary
FROM employees e1
WHERE EXISTS (
    SELECT 1 
    FROM employees e2 
    WHERE e2.salary = e1.salary 
      AND e2.dept_id <> e1.dept_id
);

-- Task 20--
SELECT p.name, p.budget
FROM projects p
WHERE p.budget > ANY (
    SELECT p2.budget 
    FROM projects p2 
    JOIN employees e ON p2.employee_id = e.id 
    WHERE e.dept_id = (SELECT id FROM departments WHERE name = 'Engineering')
);

-- Task 21--
SELECT d.name, dept_avg
FROM (
SELECT dept_id, AVG(salary) AS dept_avg
FROM employees
GROUP BY dept_id
) AS avg_salaries
JOIN departments d ON avg_salaries.dept_id = d.id
ORDER BY dept_avg DESC
LIMIT 1;

-- Task 22--
SELECT e.name, e.salary
FROM employees e
WHERE e.manager_id IS NOT NULL
AND e.salary > (
    SELECT AVG(salary) 
    FROM employees e2 
    WHERE e2.manager_id = e.manager_id
);

-- Task 23--
SELECT p.name, p.budget
FROM projects p
JOIN employees e ON p.employee_id = e.id
WHERE p.budget > (
    SELECT AVG(p2.budget)
    FROM projects p2 
    JOIN employees e2 ON p2.employee_id = e2.id 
    WHERE e2.dept_id = e.dept_id
);

-- Task 24--
SELECT DISTINCT e.name
FROM employees e
JOIN projects p ON p.employee_id = e.id
WHERE p.budget > ANY (
    SELECT p2.budget 
    FROM projects p2 
    JOIN employees e2 ON p2.employee_id = e2.id 
    WHERE e2.dept_id = (SELECT id FROM departments WHERE name = 'Marketing')
);

-- Task 25--
SELECT e.name, COUNT(p.id) AS num_projects
FROM employees e
LEFT JOIN projects p ON e.id = p.employee_id
GROUP BY e.id, e.name
HAVING COUNT(p.id) > (
    SELECT AVG(cnt) 
    FROM (
        SELECT COUNT(p2.id) AS cnt 
        FROM employees e2 
        LEFT JOIN projects p2 ON e2.id = p2.employee_id 
        GROUP BY e2.id
    ) AS counts
);
