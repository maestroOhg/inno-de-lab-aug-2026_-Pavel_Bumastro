update projects
set enddate = null
where projectid = 1;

update projects
set enddate = startdate + interval '1 year'
where startdate is not null and enddate is null;