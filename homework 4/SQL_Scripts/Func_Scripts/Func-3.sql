create view IT_Department_View
as 
	select
		e.employeeid,
		e.firstname,
		e.lastname,
		e.salary
	from employees e
	where e.department = 'IT';