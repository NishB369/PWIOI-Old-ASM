use project;

-- A
select * from olympics;

-- B
select name, count(medal) from olympics
group by name; 

-- C
select count(distinct(name)) from olympics;

-- D
select distinct(name) from olympics
where medal="Gold";

-- E
select name from olympics
where medal='Silver'
order by year;

-- F
select team,
sum(medal='Gold'),
sum(medal='Silver'),
sum(medal='Bronze')
from olympics
group by team;

-- G
select team, sum(medal='Gold') from olympics
group by team
having um(medal='Gold');

-- H
SELECT country, COUNT(medal) AS total_medals
FROM olympics
WHERE population > 10000000
GROUP BY country;

-- I
select name, count(medal)
from olympics
group by name 
order by count(medal) DESC
limit 1;

-- J
select event from olympics
where event like '%Freestyle%';

-- M
select team from olympics
group by team
having sum(season='Summer')<>0 and sum(season='Winter')<>0;

-- S
select team from olympics
group by team
having count(distinct(sport))>10;

-- N
SELECT team, MAX(year) - MIN(year) AS year_difference
FROM olympics
GROUP BY team
order by team;

-- O
SELECT team, count(medal)/count(distinct(name)) AS avg_medals_per_athlete
FROM olympics
group by team;

-- R
SELECT DISTINCT olympics.athlete
FROM medals m
JOIN coaches c ON m.athlete = c.athlete
WHERE c.year > m.year;
