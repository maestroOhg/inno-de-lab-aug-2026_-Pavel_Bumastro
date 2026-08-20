select
	o.item,
	AVG(o.amount) as avg_amount,
	count(*)
from orders as o
group by o.item