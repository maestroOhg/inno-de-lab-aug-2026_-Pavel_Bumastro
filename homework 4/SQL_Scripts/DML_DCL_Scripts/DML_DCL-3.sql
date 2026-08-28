delete from employees e
where not exists (
	select 1
	from employeeprojects e2
	where e.employeeid = e2.employeeid
);