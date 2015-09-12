CREATE TABLE citations
(
	id int,
	citation_number bigint,
	citation_date date,
	first_name char(200),
	last_name char(200),
	date_of_birth date,
	defendant_address char(200),
	defendant_city char(200),
	defendant_state char(2),
	drivers_license_number char(200),
	court_date date,
	court_location char(200),
	court_address char(200),
	PRIMARY KEY(id)
);

CREATE TABLE violations
(
	id int,
	citation_number bigint,
	violation_number char(200),
	violation_description char(500),
	warrant_status boolean,
	warrant_number char(200),
	status char(200),
	status_date date,
	fine_amount money,
	court_cost money,
	PRIMARY KEY(id)
);