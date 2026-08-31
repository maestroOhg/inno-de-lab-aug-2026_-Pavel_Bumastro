update projects as p
set budget = budget * 1.10
where exists(
	select 1
	from employees as empls
	inner join employeeprojects empproj on empproj.employeeid = empls.employeeid
	where empls.department = 'IT' and empproj.projectid = p.projectid
);
