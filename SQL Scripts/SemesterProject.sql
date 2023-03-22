CREATE USER IF NOT EXISTS learningdjango@'%' IDENTIFIED BY 'learningdjangoPW,.,.';
create schema if not exists SemesterProject;
grant all on SemesterProject.* to learningdjango;

alter table dashboard_sinedata
    max_rows 10000000;

insert into SemesterProject.dashboard_sinedata (data_val, label)
VALUES (100, 1)