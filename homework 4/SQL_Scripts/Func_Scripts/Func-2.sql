select 
	e.employeeid,
	e.firstname,
	e.lastname,
	e.salary,
	calculateannualbonus(e.employeeid,e.salary) as bonus_salary
from employees e