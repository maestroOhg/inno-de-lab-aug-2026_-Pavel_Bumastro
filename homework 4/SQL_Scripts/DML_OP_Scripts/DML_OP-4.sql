begin;
	with new_employee as(
		insert into employees (firstname, lastname, department, salary, email)
		values 
			('Jagon','Don','IT',2,null)
		returning employeeid
	)
	insert into employeeprojects(employeeid, projectid, hoursworked)
		select 
		employeeid,
		(select projectid from projects where projectname = 'Website Redesign' limit 1),
		-- тк подзапрос выдет несколько айдишников, то я использовал limit 1 чтобы взять один айди
		80
		from new_employee;
commit;

