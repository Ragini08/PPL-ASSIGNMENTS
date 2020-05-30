%ASSIGNMENT8.

/*flight is a prolog fact as flight(source, airline, destination, fare in dollars, duration in minutes 	)
*/

flight(toronto,aircanada,london,550,420).
flight(toronto,united,london,700,480).
flight(toronto,united,madrid,1000,600).
flight(toronto,ibeira,madrid,850,540).
flight(toronto,aircanada,madrid,950,540).

flight(london,aircanada,toronto,575,440).
flight(london,united,toronto,725,500).
flight(london,ibeira,barcelona,295,320).

flight(barcelona,ibeira,london,260,270).
flight(barcelona,ibeira, valencia,150,105).
flight(barcelona,ibeira, madrid,160,95).
flight(barcelona,aircanada,madrid,140,90).

flight(madrid, aircanada, barcelona, 175, 105).
flight(madrid, ibeira, barcelona, 205, 110).
flight(madrid, ibeira, valencia, 115, 95).
flight(madrid, ibeira, malaga, 125, 105).
flight(madrid, ibeira, toronto, 875, 525).
flight(madrid, united, toronto, 1025, 585).
flight(madrid, aircanada, toronto, 975, 525).

flight(valencia, ibeira, barcelona, 150, 95).
flight(valencia, ibeira, madrid, 80, 70).
flight(valencia, ibeira, malaga, 120, 140).

flight(malaga, ibeira, valencia, 130, 150).
flight(malaga, ibeira, madrid, 100, 90).

flight(paris, united, toulouse, 85,  180).

flight(toulouse, united, paris, 75, 150).

/*airport is a prolog fact as airpost(city, airporttax, minsecuritydelay)
*/

airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).


/* Is there a flight from Toronto to Madrid?
*/
q1(X, Y) :- flight(X, _, Y, _, _).

/*A flight from city A to city B with airline C is cheap if its price is less than $400. 
*/
q2(A, C, B):-flight(A, C, B, P, _), P < 400 .

/* Is it possible to go from Toronto to ::Paris in two flights? 
*/
q3(A, B):-flight(A, _,Z, _, _),flight(Z, _, B, _, _), Z \== A, Z \== B.

/* A flight from city A to city B with airline C is preferred if it’s cheap (see (b)) or it’s with Air Canada. 
*/
q4(A, C, B):-flight(A, C, B, P, _), P < 400 ; C == aircanada.

/*If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. 
*/
q5(A, B):-flight(A, C, B, _, _), C == united -> flight(A, D, B, _, _), D==aircanada.













