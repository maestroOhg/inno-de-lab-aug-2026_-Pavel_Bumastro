select
	c.country,
	count(*)
from customers as c
group by c.country