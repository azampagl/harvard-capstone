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