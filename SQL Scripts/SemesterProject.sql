/*
 * Copyright (c) 2023 - All rights reserved.
 * Created by Curtis Poon for PROCTECH 4IT3/SEP 6IT3.
 * SoA Notice: I Curtis Poon, 400263978 certify that this material is my original work.
 * I certify that no other person's work has been used without due acknowledgement.
 * I have also not made my work available to anyone else without their due acknowledgement.
 */

CREATE USER IF NOT EXISTS learningdjango@'%' IDENTIFIED BY 'learningdjangoPW,.,.';
create schema if not exists SemesterProject;
grant all on SemesterProject.* to learningdjango;

alter table SemesterProject.dashboard_sinedata
    max_rows 10000000;

insert into SemesterProject.dashboard_sinedata (data_val, label)
VALUES (100, 1)