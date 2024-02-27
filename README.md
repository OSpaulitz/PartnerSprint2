Hello.  This is a stumbling path through figuring out a microservice.  The files that did not work remain here for posterity.

The first attempt at the microservice was a lot of trial and error.  
The final push uses my partners driver.py and a trial database to test that the microservice works.  The working microservice file is cooklog_microservice.py
This file both logs a cook date AND can also return all cook dates.

The method cooklog allows to add a cooked on date with the format: "recipe_name recipe_date" from the CLI user input
The method getcooklog pulls the log of a recipe object using a recipe_name and returns a string of comma separated dates of when a cook date was logged in the CLI


example call: getcooklog Cowboy_Pizza
example call: cooklog Cowboy_Pizza
