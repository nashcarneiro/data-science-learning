SELECT SUM(value) AS TotalMilkProduction2023
FROM milk_production
WHERE year = 2023;

SELECT year, SUM(value) AS TotalCoffeeProduction2015
FROM coffee_production
WHERE year = 2015;

SELECT AVG(value) AS AverageHoneyProduction2022
FROM honey_production
WHERE year = 2022;

SELECT * 
FROM state_lookup
WHERE State = 'Iowa';

SELECT MAX(value) AS HighestYoghurtProduction2022
FROM yoghurt_production
WHERE year = 2022;

SELECT milk.State_ANSI, milk.year, honey.year, milk.value, honey.value
FROM milk_production as milk
JOIN honey_production as honey 
ON milk.State_ANSI = honey.State_ANSI
AND milk.year = honey.year
WHERE milk.State_ANSI = '35' AND milk.year = 2022;

SELECT SUM(yoghurt.value) AS TotalYoghurtProdcution2022,
yoghurt.year
FROM yoghurt_production as yoghurt
JOIN cheese_production as cheese
ON yoghurt.State_ANSI = cheese.State_ANSI AND yoghurt.year = cheese.year
WHERE yoghurt.year = 2022
GROUP BY yoghurt.year;

SELECT SUM(y.value) AS TotalYoghurtProduction
FROM yoghurt_production y
WHERE y.year =2022 AND y.State_ANSI IN (
SELECT DISTINCT c.State_ANSI 
FROM cheese_production c 
WHERE C.year = 2022);