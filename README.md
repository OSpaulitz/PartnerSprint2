Hello.  This is a stumbling path through figuring out a microservice.  The files that did not work remain here for posterity.

The first attempt at the microservice was a lot of trial and error.  
The final push uses my partners driver.py and a trial database to test that the microservice works.  The working microservice file is cooklog_microservice.py
This file both logs a cook date AND can also return all cook dates.

The method cooklog allows to add a cooked on date with the format: "recipe_name recipe_date" from the CLI user input
The method getcooklog pulls the log of a recipe object using a recipe_name and returns a string of comma separated dates of when a cook date was logged in the CLI


example call_1: getcooklog Cowboy_Pizza
example call_2: cooklog Cowboy_Pizza
example call_1 response: "Error.  Recipe Not Found" or "cooklog {recipe_name) {dates cooked}
example call_2 response: "Error" or "Success"

<img width="829" alt="UML" src="https://github.com/OSpaulitz/PartnerSprint2/assets/114098824/aea944ea-3ec9-4306-87dc-468740645205">

Communication Contract:
1. How will you communicate with each other? Email for normal communications, Jira and
Asana for projects, regular Thursday check-ins.
2. Expectations for responsiveness. 24 hours for normal correspondence.
3. Collaboration: when working on deliverables for each other's projects, Aidan will work in
Jacqueline's Asana workspace and Jacqueline will work in Aidan's Jira workspace
4. Working style and deadlines: quick synchronous Thursday meeting to discuss upcoming
work.
5. Discuss potential conflicts in advance.
a. Jacqueline:
i. I will be unavailable 2/3 and 2/17 as my kids have all day tournaments.
ii. Most Fridays, I try to use that time to recenter with my family. I am happy
to meet and communicate from 9AM through 4PM. I do not work that day
and am free.
b. Aidan:
i. 2/12 is my anniversary so I will try to finish my deliverables early but be
available if needed but hoping to avoid
ii. 2/18 I will have low availability
iii. 2/24-26 and 3/1-3 I may be traveling so I will try to finish my deliverables
early; available if needed
