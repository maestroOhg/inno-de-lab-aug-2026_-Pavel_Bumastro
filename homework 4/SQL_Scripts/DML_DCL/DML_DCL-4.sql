begin;
 	with new_project as(
	insert into projects(projectname, budget, startdate, enddate)
		values ('Website Sosiska', 10000, '2026-01-01', '2026-01-02')
	returning projectid
)
	insert into employeeprojects(employeeid, projectid, hoursworked)
	--values (1,(select projectid from projects where projectname = 'Website Sosiska'),100);
	--В начале сделал так, но узнал что может быть ошибка если есть дубликат названия, использую RETURNING(хз, правильно или нет)
		select 1, projectid, 100 from new_project
		union all
		select 2, projectid, 80 from new_project;
commit