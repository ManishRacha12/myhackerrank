/*Dates in SQL have a specific format and we can query them similarly like numbers. To write a date in a query we will use the format: YYYY-MM-DD (2012-09-24)

To query dates we can use all the operators we already know - bigger, smaller or equal within the WHERE keyword:

Fetch all of the game ids that are not played in the winter.
Winter dates are: 21 December 2022  - 20 March 2023.

Sort them by the date in descending order and rename the column to game

*/

select ID AS game from games where DATE NOT BETWEEN '2022-12-21' AND '2023-03-20' ORDER BY date desc


/*Dates cannot be added or subtracted like numbers. To perform calculations on dates, we must convert them to numbers using the JULIANDAY function. This function converts dates to the Julian day, a continuous count of days since January 1, 4713 BC, which is used by astronomers for time intervals and comparisons between different calendars.
Fetch all of the events that last less than three days


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

SELECT ID, 3*ID*ID*ID*ID+5*ID*ID*ID+0.9*ID*ID+2.2*ID+0 AS quartic FROM ITEMS;

