create database Schooldb;
show databases;
use Schooldb;
create table student_details ( s_name varchar(50), s_id int);
create table student_marks (s_name varchar(50), marks int);
create table student_city (s_name varchar(50), city varchar(50));

desc student_details;
insert into student_details values("Raj",1),("Raja",2),("Siva",3),("John",4),("Rohan",5);
insert into student_marks values("Raj",98),("Raja",88),("Siva",77),("John",89),("Rohan",89);
insert into student_city values("Raj","Salem"),("Raja","Tirupur"),("Siva","Tgode"),("John","Erode"),("Rohan","Salem");

alter table student_details add (phone_no varchar(15));
alter table student_marks add (s_rank int);
alter table student_city add (pincode int);

insert into student_details (phone_no) values ("9876543210");
insert into student_marks (s_rank) values (1);
insert into student_city (pincode) values (600001);

select * from student_details;
select * from student_marks;
select * from student_city;

desc student_details;

insert into student_details (s_id,phone_no) values (6,"9876543216");

alter table student_details modify column phone_no varchar(20);

alter table student_details rename column phone_no to mobile_no;

drop table student_details;

select * from student_details; 

delete from student_details where mobile_no="9876543210";
delete from student_details where s_id=6;

update student_details set mobile_no="9876543211" where s_id=1;
update student_details set mobile_no="9876543212" where s_name="Raja";
update student_details set mobile_no="9876543213" where s_id=3;
update student_details set mobile_no="9876543214" where s_id=4;
update student_details set mobile_no="9876543215" where s_id=5;

delete from student_details where s_id=4;
delete from student_details;


show databases;
commit;
use schooldb;
create table student_s1 (id int);
commit;
rollback;
show tables;

SET SQL_SAFE_UPDATES = 0;

drop database schooldb;

create database empdb;

use empdb;

create table emp_details ( e_name varchar(50), e_id int,city varchar(50));
create table emp_sal ( e_id int,pos varchar(50),sal int);

insert into emp_details values("Raj",1,"Salem"),("Raja",2,"Chennai"),
	("Siva",3,"Tgode"),("John",4,"Salem"),("Rohan",5,"Erode");
insert into emp_sal values (1,"junior dev",30000), (2,"senior dev",50000), (3,"manager",50000),
	(4,"assistant",10000), (5,"auditor",60000);
    
show tables;
    
alter table emp_sal rename emp_salary;
alter table emp_details rename column city to e_city;

alter table emp_details modify column e_id varchar(20);
alter table emp_salary modify column pos varchar(20);

select * from emp_details;

SET SQL_SAFE_UPDATES = 0;
update emp_details set e_city="Coimbatore" where e_city="Erode";

select * from emp_details;

insert into emp_details (e_id,e_name) values (6,"Ravi");
insert into emp_details (e_id) values (7);

select * from emp_details;

update emp_details set e_city="Erode" where e_name="Ravi";
update emp_details set e_name="Ragu",e_city="Tirchy" where e_id=7;

select * from emp_details;

delete from emp_details where e_id=5;

select * from emp_details;

create table demo (id int,ename varchar(50));
insert into demo values (12,"suren"),(13,"Gova");

drop table demo;

commit;

