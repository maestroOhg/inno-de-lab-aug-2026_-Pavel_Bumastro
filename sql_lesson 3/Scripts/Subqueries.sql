select
	c.first_name,
	c.last_name,
	o.amount
from customers as c
join orders as o on c.customer_id = o.customer_id
where o.amount = (
	select MAX(amount)
	from orders
)
