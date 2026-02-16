--1. Combine two tables
SELECT p.firstName, p.lastName,a.city,a.state FROM
Person p LEFT JOIN Address a on
p.personId=a.personID;

--2. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE offset_val INT;
  SET offset_val = N - 1;
  RETURN (
      SELECT DISTINCT Salary 
      FROM Employee 
      ORDER BY Salary DESC
      LIMIT 1 OFFSET offset_val
    );
END

--3. Rank Scores
SELECT score,
DENSE_RANK() OVER (ORDER BY score DESC) as `rank`
FROM Scores
ORDER BY score DESC;

--4. Consecutive Numbers
SELECT DISTINCT num AS ConsecutiveNums
FROM (  SELECT num,
            LAG(num,1) OVER (ORDER BY id) AS prev1,
            LAG(num,2) OVER (ORDER BY id) AS prev2
        FROM Logs
    ) t 
WHERE prev1=num AND prev2=num;


--5. Employees Earning More Than Their Managers
SELECT e1.name as Employee
FROM Employee e1 LEFT JOIN Employee e2
ON e1.managerID=e2.id
WHERE e1.salary>e2.salary;

--6. Duplicate Emails
SELECT DISTINCT email
FROM Person
GROUP BY email
HAVING COUNT(email)>1;

--7. Customers Who Never Order
SELECT c.name AS Customers
FROM Customers c LEFT JOIN Orders o
ON c.id=o.customerId
WHERE o.id IS NULL;

--8.Department Highest Salary
SELECT 
d.name AS Department, 
e.name AS Employee, 
e.salary AS Salary
FROM Employee e LEFT JOIN Department d
ON e.departmentID=d.id
JOIN (
    SELECT 
    departmentId,
    MAX(salary) AS maxSalary
    FROM Employee
    GROUP BY departmentId) t
WHERE e.departmentID = t.departmentId
AND e.salary=t.maxSalary;

--9. Exchange Seats
SELECT
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;

--10. Second Highest Salary
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
