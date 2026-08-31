create or replace function CalculateAnnualBonus(employee_id integer, salary numeric)
returns numeric
as $$
begin
	return salary * 0.1;
end;
$$ language plpgsql;