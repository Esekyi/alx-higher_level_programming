-- a script that displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending)
USE hbtn_0c_0;
SOURCE temperatures.sql;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY value DESC;