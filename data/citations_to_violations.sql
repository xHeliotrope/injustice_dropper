/*
	Full outer join of citations to violations (a citation comprises of one or more violations).
	Grabs all columns from both tables, except primary keys.
	Comment out columns as needed.
	
	Either data set could be incomplete, hence coalesce.
	
	Someone test if this actually runs...
*/

select	distinct
		coalesce(c.citation_number, -1)				as		citation_number,
		coalesce(c.citation_date, '9999-12-31')		as		citation_date,
		coalesce(c.first_name, '')					as		first_name,
		coalesce(c.last_name, '')					as		last_name,
		coalesce(c.date_of_birth, '9999-12-31')		as		date_of_birth,
		coalesce(c.defendant_address, '')			as		defendant_address,
		coalesce(c.defendant_city, '')				as		defendant_city,
		coalesce(c.defendant_state, '')				as		defendant_state,
		coalesce(c.drivers_license_number, '')		as		drivers_license_number,
		coalesce(c.court_date, '9999-12-31')		as		court_date,
		coalesce(c.court_location, '')				as		court_location,
		coalesce(c.court_address, '')				as		court_address,
		coalesce(v.violation_number, '')			as		violation_number,
		coalesce(v.violation_description, '')		as		violation_description,
		coalesce(v.warrant_status, false)			as		warrant_status,			-- Or true. What should the default be?
		coalesce(v.warrant_number, '')				as		warrant_number,
		coalesce(v.status, '')						as		status,
		coalesce(v.status_date, '9999-12-31')		as		status_date,
		coalesce(v.fine_amount, 0.00)				as		fine_amount,
		coalesce(v.court_cost, 0.00)				as		court_cost
from		citations	c
full join	violations	v
on			c.citation_number = v.citation_number
order by	citation_number, violation_number
;