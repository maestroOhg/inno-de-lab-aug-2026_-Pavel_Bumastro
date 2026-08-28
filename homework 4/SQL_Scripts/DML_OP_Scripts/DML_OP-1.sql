select 
	p.projectname
from projects p
inner join employeeprojects e
	on e.projectid = p.projectid
inner join employees empls
	on empls.employeeid = e.employeeid
where empls.firstname ='Bob' and empls.lastname = 'Johnson' and e.hoursworked >150;