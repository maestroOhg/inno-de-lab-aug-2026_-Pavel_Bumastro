select
	o.order_id,
	o.customer_id,
	o.item,
	o.amount,
	sum(o.amount) over(partition by  o.customer_id) as total_by_customer
from orders as o 
join customers as c on c.customer_id = o.customer_id