Readings
===

*Making Data  Matter: The Role of Information Design...*, Dominick Tribone

* **Quick summary:** Focuses on performance metrics using real-time location, expected arrivals, etc. 
May not be as applicable to us, but it's a good resource to get familiar with the MBTA.
* List of acronyms referencing statistics, organizations, data collection methods, etc
* pg 26: Table of the most pertinent statistics using vehicle tracking and fair collection data
* pg 27: Measuring the severity of service disruptions using RBT (reliability buffer time): the 
amount of extra time that passengers must budget above the typical journey time in order to arrive 
on time with a specified level of certainty --> 95th percentile minus median running time for an 
Origin-Dest pair. Can measure severity by looking at RBT for typical day compared to disrupted.
* pg 35: general background information to familiarize yourself with the MBTA and its ops.
* pg 70: Discusses the re-weighting of performance metrics using the number of expected customers.
Focuses on moving people rather than just moving trains/buses. Presents good metrics estimating
total passenger wait time using arrival rate of passengers and headway, and follows up with metrics
for branched service, like Braintree/Ashmont, and for wait times over all stations.
* pg 82: Section titled *Generating Institutional Interest in and Support for Performance Improvement*.
Talks about certain areas of the T, like the Red Line, which are known to be more problematic and have 
drawn more attention in terms of ways to improve the operations. 
* pg 113: Small paragraph the discusses the possibility for further research in estimating crowds from 
fare collection data and the methods from pages 70-72. Since we will be working primarily with aggregate
entry numbers, if we could find a way to estimate crowding and examine changes as a result of storms,
alerts, etc this could lead to insights about when/where service should be added.

*Intermodel Passenger Flows on London's...*, Jason Gordon

* **Quick summary:** Focuses on inferring the origin, destination, and exchange location for passengers
in the London transportation system using fare-collection data as well as vehicle-tracking and passenger
exit data. Worth reading the two paragraphs on pg 94 just to have a comparison to what we'll see with the
MBTA data.

* pg 36: Addresses some previous analyses using bus fare-collection data cross-referenced with the 
positional tracking systems to detect anomalies in the system due to truncation and time-keeping. Was
able to observe the phenomenon of large clusters of boarding immediately following bus arrival with more
dispersed boardings right before the bus departs, showing that many people tend to wait for the bus before
it arrives. Not particularly pertinent to our problem, but I thought it was an interesting way to observe
a well known phenomenon through fare-collection data. 
* pg 39: method of inferring the bus stop which a person got on using the fare-collection and positional
tracking data. May not be of use to us, but presents a thorough methodology by which we could estimate 
origin if needed.
* pg 88: Detailed explanation of methodology used to model passenger flow for Origin-Destination pairs and 
the intermediate stops.
* pg 94: Short paragraphs explain Gordon's bus and rail fare-collection data and some of the concerns he 
saw when dealing with them. This part isn't long but it may be qualitatively of use to us as a comparison
to the MBTA system.
* pg 139: Looks at change in passenger behaviors, but relies on the unique identification of passengers
through their fare-collection ID.

*Automatic Data for Applied Railway Management: Passenger Demand...*, Michael Frumin

* **Quick summary:** A detailed study in passenger behavior using fare-collection data and historical 
schedules of planned departures. This extra dimension of scheduled planned departures may make these
analyses inapplicable for our research

* pg 93: This chapter will be of the most use to us as it studies 'Passenger Incidence Behavior'. The term
refers to people arriving somewhereand is incident to public transport. This is a particular interest to us
as there is a part dedicated to studying the London Overground (akin to the MBTA buses)
* pg 95: Recapping some work done by Jolliffe and Hutchinson in which they studied the rates at which 
passengers arrived at a stop to wait for the bus, one key finding was that "passengers adjust their incidence
behavior...based on knowledge of the bus timetable and historical bus performance." Could be useful if we 
look at effectiveness of MBTA alerts on arrival times. We may run into problems with the fact that MBTA bus
data includes the route, but not the particular stop.
* pg 95-97: Some of the studies use a very special subset to gain their insights; bus stops that don't 
intersect with other routes, aren't terminal stops, with constant headways.
* pg 108: Plots showing a good way to display the distribution of waiting times (normalized by headway) 
for several of London's transportation routes. We can take note of the way that they've subdivided the day.
Note the local peak at 0 for many of the histograms as evidence of many people timing their arrival based 
on the schedule but arriving late. Most show a larger peak towards the end of the headway 'indicating some 
type of safety margin or waiting-time minimization behavior'. 
* pg 108-110: We could perform many of these analyses on our own data using just the fare-collection data
and knowledge of the headway for a particular route at a given time of day. Might be tough if the bus fare-
collection data only gives us the route and not the stop.

*MBTA Blue Book,2014*

* **Quick summary:** Good summary of stats put out by the MBTA as well as general info about how the rail and
bus systems are run.

* Quick Subway facts: 
 * 121 stops (6 shared stations: North Station, Haymarket, Govt center, State,Park, Downtown Crossing)
 
* Ch 2, pg 4: Charts showing the highest volume stations. For the shared stations, shows the estimated
breakdown according to the lines flowing into the station. Good ground for any weighting system we may be 
interested in. 
* Ch 2, pg 5: MBTA Subway Ops Line Statistics show the number of trains, size of t he trains, and the 
headway of each at the various times throughout the day.
* Ch 2, pg 8: Shows frequency of trains for all lines throughout the day. 
* When performing our analysis, refer to the sections below to validate findings or to get additional 
information for any of the lines.
	* Ch 2, pg 9: Avg weekday entries on RED LINE aggregated by stop for successive years
	* Ch 2, pg 16: Avg weekday entries on GREEN LINE aggregated by stop for successive years
	 * pg 17: Shows weekday boarding numbers for the Green Line light rail (once it goes above ground).
	 Figures take into account boarding in either direction.
	* Ch 2, pg 21: Avg weekday entries on ORANGE LINE aggregated by stop for successive years
	* Ch 2, pg 25: Avg weekday entries on BLUE LINE aggregated by stop for successive years
	* Ch 3: Silver Line. Not sure whether or not we want to include this into our models but similar figures 
	to the ones for the main rail lines are also available here.

* Quick bus facts:
 * 170 routes, not including emergency routes in place for rail interruptions or shuttle service in high-
 demand times
 * approx 1,000 vehicles
* Ch 3b, pg 2-5: Bus ridership figures in both directions by weekday/weekend
* Ch 3b, pg 6-8: Ranking of busiest bus routes according to boarding. No separation of direction.

 