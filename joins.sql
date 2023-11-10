/*Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

*/

select sum(CITY.population)  from
COUNTRY
INNER JOIN
CITY
on
Country.Code=city.CountryCode
where country.continent='asia';


/*Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows:*/

SELECT CITY.NAME FROM 
CITY
INNER JOIN
COUNTRY
ON
CITY.COUNTRYCODE=COUNTRY.CODE
WHERE COUNTRY.CONTINENT='AFRICA';



/*Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

*/


SELECT CITY.NAME FROM 
CITY
INNER JOIN
COUNTRY
ON
CITY.COUNTRYCODE=COUNTRY.CODE
WHERE COUNTRY.CONTINENT='AFRICA';


/*You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

*/


select  
CASE
WHEN GRADES.GRADE<8 THEN 'NULL'
ELSE
STUDENTS.NAME
END,
GRADES.GRADE,STUDENTS.MARKS 
FROM
STUDENTS,
GRADES
WHERE
STUDENTS.MARKS BETWEEN GRADES.MIN_MARK AND GRADES.MAX_MARK 
ORDER BY GRADES.GRADE DESC,STUDENTS.NAME;


/*Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

*/


SELECT S.HACKER_ID,NAME
FROM
    SUBMISSIONS AS S 
    JOIN HACKERS AS H ON S.HACKER_ID=H.HACKER_ID
    JOIN CHALLENGES AS C ON S.CHALLENGE_ID=C.CHALLENGE_ID
    JOIN DIFFICULTY AS D ON D.DIFFICULTY_LEVEL=C.DIFFICULTY_LEVEL
WHERE
D.SCORE=S.SCORE
GROUP BY NAME, S.HACKER_ID
HAVING COUNT(S.CHALLENGE_ID)>1
ORDER BY COUNT(S.CHALLENGE_ID) DESC,S.HACKER_ID




/*Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

*/

SELECT W.ID,WP.AGE,W.COINS_NEEDED,W.POWER FROM
WANDS AS W JOIN WANDS_PROPERTY AS WP ON W.CODE=WP.CODE
JOIN
(SELECT AGE AS AG, MIN(COINS_NEEDED) AS MCN, POWER AS PW FROM WANDS AS A JOIN WANDS_PROPERTY AS B ON A.CODE=B.CODE WHERE IS_EVIL=0 GROUP BY PW,AG)AS Q
ON
WP.AGE=AG AND W.COINS_NEEDED=MCN AND W.POWER=PW
ORDER BY W.POWER DESC,WP.AGE DESC;