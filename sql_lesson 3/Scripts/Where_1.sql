select
    first_name,
    last_name,
    age,
    country
from customers
where age > 25 and country = 'USA';