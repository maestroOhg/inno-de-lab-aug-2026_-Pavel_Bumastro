create table departments (
department_id	serial  primary key,
department_name		varchar(50) UNIQUE NOT NULL,
location 	varchar(50)
)

