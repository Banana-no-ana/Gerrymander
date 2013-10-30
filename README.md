Gerrymander
===========

The project aims to look at opportunities for  electoral districts in BC that can have their election results changed as a result of gerrymandering. 

Election data is provided by Election BC, a non-partisan government body. 

This project includes a few manual steps, for sake of performance (including adding clients to the map reduce server).

Overview of how the algorithm calculates:
	1. Calculate which Electoral district had the least differentiation between the winning and runner-up parties
	2. Pick the top electoral district, find a Voting Area on the border 
	3. TODO: Finish the rest


How the code works: 
The election data file is loaded in and each Voting area is created as an object individually. The coordinates of each area is loaded into the objects. 

Electoral districts are also created as an object. Each electoral district is created by aggregating all the Voting areas. The borders are redrawn by eliminating all coordinate points that are duplicated. (If the points are duplicated, it means that the border is either on the inside of the district, or that it's on the outside and shared by 2 districts. In the latter case, the removal of one point is not a big deal)

Electoral district objects now contain a list of the Voting area objects. 

If a Voting Area 
TODO: Finish this too lol
The Voting Area objects are then calculated for their neighbours. If two Voting areas share more than one coordinate, then they are neighbors. 

Electoral districts are done the same. 
