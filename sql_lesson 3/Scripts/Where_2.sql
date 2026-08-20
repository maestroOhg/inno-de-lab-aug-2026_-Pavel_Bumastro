select
	order_id,
	item,
	amount
	customer_id
from orders
where amount > 1000;