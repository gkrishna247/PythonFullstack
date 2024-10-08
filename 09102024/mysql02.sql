create database employee;
use employee;
create table emp_details (emp_id int primary key auto_increment,
	emp_name varchar(50), emp_domain varchar(50),
    emp_role varchar(20), emp_sal int,
    emp_phone varchar(15), emp_email varchar(20));
desc emp_details;
insert into emp_details (emp_name,emp_domain,emp_role,
	emp_sal,emp_phone,emp_email) values 
    ("Raja","IT","Senior Dev",50000,"9876543211","raja001@gmail.com"),
    ("Ram","IT","Junior Dev",30000,"9876543212","ram001@gmail.com"),
    ("Kumar","HR","HR Manager",60000,"9876543213","kumar001@gmail.com"),
    ("John","Sales","Sales Rep",25000,"9876543213","john001@gmail.com"),
    ("Selva","Finance","Auditor",80000,"9876543214","selva001@gmail.com");
select * from emp_details;

create table HR_department (HR_id int primary key auto_increment,emp_id int,
	emp_name varchar(50), emp_domain varchar(50),
    emp_role varchar(20), emp_sal int,
    emp_phone varchar(15), emp_email varchar(20),
    foreign key (emp_id) references emp_details(emp_id));
    
desc hr_department;
insert into hr_department values(21,8,"Kumar","HR","HR Manager",60000,"9876543213","kumar001@gmail.com");
insert into hr_department values
	(31,6,"Raja","IT","Senior Dev",50000,"9876543211","raja001@gmail.com"),
    (54,7,"Ram","IT","Junior Dev",30000,"9876543212","ram001@gmail.com"),
    (34,9,"John","Sales","Sales Rep",25000,"9876543213","john001@gmail.com");
select * from emp_details;
select * from hr_department;
delete from emp_details where emp_id=10;
insert into emp_details values (10,"Selva","Finance","Auditor",80000,"9876543214","selva001@gmail.com");

delete from emp_details where emp_id=8;

delete from hr_department where emp_id=7;

commit;  
drop table hr_department;
set sql_safe_updates=0