North-South-Divide
==================

A program to calculate where the North-South divide is based on various data. Made for YRS2013

#Dependencies
The only dependencies, other than Python, are Flask and Postcodes. To install do

    pip install flask
    pip install postcodes


#Code and Directory Structure
The 'divide.py' file is the entry-point of the program. It is a webserver that displays a map of the North-South divide.

Inside the 'lib' directory there is

* loaddata.py - This contains the base class DataSet which all data sets must inherit. It provides some useful functions like one which finds out how much of the country the data covers

* tiles.py - This splits the data into tiles 

* work.py - This finds the lines to draw and returns the data that can be converted into json for the web app

* loaders/ - All the data loaders live here and inherit DataSet

#Copyright notices

* data/land_registry - Data produced by Land Registry © Crown copyright 2013. This data covers the transactions received at Land Registry in the period of June 2013. © Crown copyright 2013.
