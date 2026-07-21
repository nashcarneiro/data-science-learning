/*Scenario: 
Data Scientist at USDA (United States Department of Agriculture)
Context: 
You are a Data Scientist working at the USDA. Your department has been tracking the production of various agricultural commodities across different states. 
Your datasets include:
`milk_production`, `cheese_production`, `coffee_production`, `honey_production`, `yogurt_production`, and a `state_lookup` table. 
The data spans multiple years and states, with varying levels of production for each commodity.
Your manager has requested that you generate insights from this data to aid in future planning and decision-making. You'll need to use SQL queries to answer the questions that come up in meetings, reports, or strategic discussions.
Objectives:
Assess state-by-state production for each commodity.
Identify trends or anomalies.
Offer data-backed suggestions for areas that may need more attention.
*/

-- Can you find out the total milk production for 2023? Your manager wants this information for the yearly report.
-- What is the total milk production for 2023?

SELECT SUM(value) AS TotalMilkProduction2023
FROM milk_production 
WHERE year = 2023;

-- Which states had cheese production greater than 100 million in April 2023? The Cheese Department wants to focus their marketing efforts there. 
-- How many states are there?

SELECT c.State_ANSI,
s.State,
c.Value,
c.Period,
c.Year
FROM cheese_production c
JOIN state_lookup s ON c.State_ANSI = s.State_ANSI
WHERE c.Value >= 100*1e6 AND c.Period = 'APR' AND c.year = 2023;

-- Your manager wants to know how coffee production has changed over the years. 
-- What is the total value of coffee production for 2011?

SELECT Year, value
FROM coffee_production;

-- There's a meeting with the Honey Council next week. Find the average honey production for 2022 so you're prepared.

SELECT AVG(Value) AS AverageHoneyProduction, Year
FROM honey_production
GROUP BY Year;

-- The State Relations team wants a list of all states names with their corresponding ANSI codes. Can you generate that list?
-- What is the State_ANSI code for Florida?

SELECT * FROM state_lookup;

-- For a cross-commodity report, can you list all states with their cheese production values, even if they didn't produce any cheese in April of 2023?
-- What is the total for NEW JERSEY?

SELECT s.State_ANSI, s.State, c.Value
FROM state_lookup s
LEFT JOIN cheese_production c ON s.State_ANSI = c.State_ANSI
WHERE c.Period = 'APR' AND c.Year = 2023;

-- Can you find the total yogurt production for states in the year 2022 which also have cheese production data from 2023? This will help the Dairy Division in their planning.

SELECT SUM(y.Value) AS TotalYoghurtProduction
FROM yoghurt_production y 
WHERE y.Year = 2022 and y.State_ANSI IN(
SELECT DISTINCT c.State_ANSI FROM cheese_production c WHERE c.year = 2023);

-- List all states from state_lookup that are missing from milk_production in 2023.
-- How many states are there?

SELECT COUNT(s.State_ANSI) AS StateCount 
FROM state_lookup s
WHERE s.State_ANSI NOT IN (
SELECT  DISTINCT m.State_ANSI
FROM milk_production m 
WHERE m.year = 2023 
);

-- List all states with their cheese production values, including states that didn't produce any cheese in April 2023.
-- Did Delaware produce any cheese in April 2023?

SELECT s.State, c.Value
FROM state_lookup s 
LEFT JOIN cheese_production c ON s.State_ANSI = c.State_ANSI AND c.Year = 2023 AND c.Period = 'APR';

-- Find the average coffee production for all years where the honey production exceeded 1 million.

SELECT AVG(c.Value)
FROM coffee_production c
WHERE c.year in (select distinct h.year from honey_production h
WHERE h.Value > 1000000);

