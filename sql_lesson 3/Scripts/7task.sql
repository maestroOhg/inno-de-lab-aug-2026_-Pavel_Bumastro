select
	concat(c.first_name, ' ', c.last_name) as full_name,
	count(o.order_id) as total_orders,
	sum(o.amount) as total_amount,
	c.country
from customers as c
join orders as o 
	on c.customer_id = o.customer_id
-- Проверяем наличие доставки через c.customer_id и s.customer
where exists (
	select 1
	from shippings as s
	where s.customer = c.customer_id
	  and s.status = 'Delivered'
)
group by 
	c.customer_id, 
	c.first_name, 
	c.last_name, 
	c.country
-- Фильтруем клиентов, у которых общее количество заказов больше или равно 2
having count(o.order_id) >= 2;