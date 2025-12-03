use testdatabase;

-- 4.민혁 사원의 데이터를 삭제하세요
DELETE FROM employees  WHERE name = '민혁';
SELECT * FROM employees;

-- 5.모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.
SELECT position, AVG(salary) FROM employees GROUP BY position;

-- 6.employees 테이블을 삭제하세요.
DROP TABLE employees;

