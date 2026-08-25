create user hr_user with password 'pivo';
create role 'postgresql_role';
grant select on table employees to postgresql_role;
grant postgresql_role to hr_user;