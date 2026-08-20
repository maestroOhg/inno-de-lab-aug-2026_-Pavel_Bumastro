select
	o.order_id,
	o.item,
	o.amount,
	c.first_name,
	c.last_name
from orders as o
join customers as c
	on o.customer_id = c.customer_id;