select
	concat(c.first_name, ' ', c.last_name) as full_name,
	count(distinct o.order_id) as total_orders,
	sum(o.amount) as total_amount,
	c.country
from customers as c
join orders as o 
	on c.customer_id = o.customer_id
-- Проверяем наличие хотя бы одной доставки статуса 'Delivered' для клиента
where exists (
	select 1
	from orders as o2
	join shippings as s 
		on o2.customer_id = s.customer
	where o2.customer_id = c.customer_id
	  and s.status = 'Delivered'
)
group by 
	c.customer_id, 
	c.first_name, 
	c.last_name, 
	c.country
-- Фильтруем клиентов, у которых общее количество заказов больше или равно 2
having count(distinct o.order_id) >= 2;