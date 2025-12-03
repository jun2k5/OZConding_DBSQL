use testdatabase;

-- 1. employees 테이블을 생성해주세요.
CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- 2.직원 데이터를 employees에 추가해주세요
INSERT INTO employees (name, position, salary) VALUES 
('혜린', 'PM', 90000) ,
('은우', 'Frontend', 80000),
('가을', 'Backend', 92000),
('지수', 'Frontend', 7800),
('민혁', 'Frontend', 96000),
('하온', 'Backend', 130000);
