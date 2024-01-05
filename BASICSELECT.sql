/*Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
The CITY table is described as follows:
CITY.jpg*/

SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';


/* Query a list of CITY and STATE from the STATION table.
The STATION table is described as follows:
*/

SELECT CITY,STATE FROM STATION;

/*Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
The STATION table is described as follows:

*/

SELECT DISTINCT CITY FROM STATION WHERE ID%2=0;

/*Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:

*/

SELECT COUNT(CITY)-COUNT(DISTINCT CITY) FROM STATION;

/*Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/

SELECT CITY,LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY),CITY LIMIT 1;
SELECT CITY,LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY)DESC,CITY LIMIT 1;


/*Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%';

/*Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE '%A' OR CITY LIKE '%E' OR CITY LIKE '%I' OR CITY LIKE '%O' OR CITY LIKE '%U';

/*Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU].*[AEIOU]$';    

/*Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^AEIOU]';

/*Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[^AEIOU]$';

/*Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^AEIOU].*' OR CITY REGEXP '.*[^AEIOU]$';

/*Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

*/

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^AEIOU].*[^AEIOU]$';

/*Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

*/

SELECT NAME FROM STUDENTS WHERE MARKS>75 ORDER BY RIGHT(NAME,3), ID;

/*Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

*/

SELECT NAME FROM EMPLOYEE ORDER BY NAME;

/*Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.

*/

SELECT NAME FROM EMPLOYEE WHERE SALARY>2000 AND MONTHS<10 ORDER BY EMPLOYEE_ID;

/*Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to  decimal places.

*/

SELECT MIN(ROUND(LAT_N,4)) FROM STATION WHERE LAT_N>38.7780 LIMIT 1;

/*Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.

*/

SELECT ROUND(LONG_W,4)
FROM STATION
WHERE
LAT_N=(SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);


/*Consider  and  to be two points on a 2D plane.

 happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.

Input Format

*/

SELECT ROUND(MAX(LAT_N)-MIN(LAT_N)+MAX(LONG_W)-MIN(LONG_W),4) AS MANHATTAN_DISTANCE FROM STATION;


/*Consider  and  to be two points on a 2D plane where  are the respective minimum and maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

*/

SELECT ROUND(SQRT(POW((MIN(LAT_N)-MAX(LAT_N)),2)+POW((MIN(LONG_W)-MAX(LONG_W)),2)),4) FROM STATION;


/*A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

*/


SELECT ROUND(LAT_N,4) AS Median
FROM (
  SELECT LAT_N, ROW_NUMBER() OVER (ORDER BY LAT_N) as rn, COUNT(*) OVER () as cnt
  FROM STATION
) t
WHERE rn = (cnt + 1) / 2


/*Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
*/

SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE='JPN';


/*Query the difference between the maximum and minimum populations in CITY.

*/

SELECT MAX(POPULATION)-MIN(POPULATION) FROM CITY;



/*Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.

*/
SELECT CEIL(AVG(SALARY)-AVG(CAST(REPLACE(SALARY,'0','') AS DECIMAL))) AS MISCALCULATED FROM EMPLOYEES;


/*We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
*/

select max(salary*months) as EARNINGS, COUNT(*) AS EMPLOYEECOUNT FROM EMPLOYEE WHERE
  SALARY*MONTHS=(select max(salary*months) from employee);


/*Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of  decimal places.
The sum of all values in LONG_W rounded to a scale of  decimal places.
*/

SELECT ROUND(SUM(LAT_N),2) AS LAT, ROUND(SUM(LONG_W),2) AS LON FROM STATION;


/*Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than  and less than . Truncate your answer to  decimal places.

*/

SELECT ROUND(SUM(LAT_N),4) FROM STATION WHERE LAT_N>38.7880 AND LAT_N<137.2345;

/*Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than . Truncate your answer to  decimal places.

*/

SELECT ROUND(MAX(LAT_N),4) FROM STATION WHERE LAT_N<137.2345;

/*Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

*/

SELECT ROUND(LONG_W,4) FROM STATION WHERE LAT_N=
(SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345);




/*You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date. It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row in the table.
If the End_Date of the tasks are consecutive, then they are part of the same project. Samantha is interested in finding the total number of different projects completed.

Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.


*/

Select Start_Date, MIN(End_Date)
From
    (Select b.Start_Date
    From Projects as a
    RIGHT Join Projects as b
    ON b.Start_Date = a.End_Date
    WHERE a.Start_Date IS NULL
    ) sd,
    (Select a.End_Date
    From Projects as a
    Left Join Projects as b
    ON b.Start_Date = a.End_Date
    WHERE b.End_Date IS NULL
    ) ed
Where Start_Date < End_Date
GROUP BY Start_Date
ORDER BY datediff(MIN(End_Date), Start_Date), Start_Date


/*Handling dates part 2

Dates cannot be added or subtracted like numbers. To perform calculations on dates, we must convert them to numbers using the JULIANDAY function. This function converts dates to the Julian day, a continuous count of days since January 1, 4713 BC, which is used by astronomers for time intervals and comparisons between different calendars.

*/

SELECT ID FROM EVENTS WHERE JULIANDAY(END)-JULIANDAY(START)<3;




/*A quartic function is defined:

f(x) = ax4+bx3+cx2+dx+e

Let's define the constant parameters:

a = 3
b = 5
c = 0.9
d = 2.2
e = 0
Fetch the ids and the quartic function where x is the id, and rename the column to quartic
*/


SELECT IDS, 3*ID*ID*ID*ID+5*ID*ID*ID+0.9*ID*ID+2.2*ID+0 AS QUATRIC FROM ITEMS;