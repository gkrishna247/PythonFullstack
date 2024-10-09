show databases;
use schooldb;
show tables;
select * from student_city;
select * from student_details;
select * from student_marks;

set sql_safe_updates=0;

delete from student_details where mobile_no="9876543210";

alter table student_details modify column s_id int primary key;

select * from student_details;

insert into student_details values ("kumar",4,"9876543299");

insert into student_details values ("John",6,"9876543216");

create table bus (bus_id int primary key auto_increment,bus_no int,s_id int,
foreign key (s_id) references student_details(s_id));

desc bus;

insert into bus values (11,81,1),(12,85,2),(13,21,3),(14,89,4),(15,41,5);
select * from bus;

commit;