## Project Overview ##

_**The Scheduler**_

**Description**: The Scheduler is a web app that's automates the process of signing up for classes.

**Proposal**: The Scheduler is a program that will make the process of signing up for classes quick and easy by automating the entire thing. When a student first enters our site 
all they need to do is enter their TU credentials,Major, and course numbers and The Scheduler will handle the rest. A huge appeal of this program is how custamizable it is, At 
the moment The Scheduler's functionality is very basic in that it only does its one primary function, my plan is to elaborate on foundation and make it more user freindly. Me 
and my team are going to intergrate two major components. The first major component is Twilio, which is an SMS service that we are going to use to alert student if there are any 
issues during the scheduling process (I.E. Class is full, Time constraints, etc.). The second will be to give the user the option to simply insert their major and then The 
Scheduler will sign the student up for the courses based on temple recommended timeline (This will be done using a web scrapper to pull the recommend course timeline from the 
bulletin and then populate it into the program).

**Installation Instructions**: http://thescheduler.pythonanywhere.com/

## How to Build ##

**Step 1**: Download python IDE of choice. (For this project we used Pycharm by JetBrains)

**Step 2**: Download additional libraries (Flask,Selenium,Twilio)

**Step 3**: In order for Flask to build/Run your web app you need to add the frame work. (app = Flask(__name__) and app.run)

**Step 4**: Program web wrapper pathway (I.E. code where you want the selenium code to send you)

**Step 5**: Uppload necessary files to Host site, and update web page

## Vision Statement ##


For Temple Students who need to register for classes, The Scheduler is a web app that automates part of the registration process. Unlike Temple's Banner service, our product will automatically determine potential schedule possibilities based on your desired classes.


## Members ##

Felix Rabinovich 

Abin Cheriyan

Ethan Lewis

Dylan Dunda

Erik Rodriguez

Ryan Babala


## Weekly contribution ##

https://github.com/CIS3296SoftwareDesignF21/prj-02-thescheduler/blob/main/Week1.md

## Personas ##

***

**Tom, a CST junior**

***

Tom, age 20, is a CST major junior at Temple University. On top of achieving dean's list each semester, Tom is also the vice president of the ACM club. Tom also spends a large portion of his free time working on his own programming projects and browsing open-source code managers like GitHub. Tom is a large supporter of automation and frequently goes out of his way to learn more about emerging technologies to integrate them into his everyday life and improve his own productivity.

Tom's experience with computer science concepts at Temple combined with his own exploration into related technologies on his own time make him proficient at digital technology. He has enjoyed some of the more recent additions to Temple's Banner system, but feels that there is room for more automation.

***

**Sylvia, an IST freshman**
***

Sylvia, age 18, is a freshman at Temple University. She is new to both Temple and the city of Philadelphia, and she is learning her ways around the school as well as the city. Sylvia is enrolled in the "Fly in 4" program and plans to graduate with a bachelor’s degree in 4 years or less. The registration day is close, and Sylvia has yet to create a plan for next semester. Sylvia is taking 18 credits this semester and is always busy with classwork and because of that, she hasn’t been able to make any friends. She doesn’t know which classes she has to take and is stressed out not knowing what to do and she doesn’t have any friends to ask for help regarding these things. Sylvia wishes for an app or a web app she can use, that will give her plans based on her major or time preferences.

***
**Jacob, a CJ senior**
***

Jacob, age 22 and a criminal justice senior, works multiple jobs and pays for his own tuition by working overnight shifts. He barely has enough time to do school work or study. Because Jacob is focused on graduation, writing thesis papers for his law classes, and dealing with overnight shifts, he hasent even bothered trying to figure out the classes he needs to schedule. Because it's his last year, and he put in the work to pass all of his classes in previous years on time, he is over the credit limit by quite a lot, so he has some breathing room in what classes he can choose from. Because of this, Jacob would greatly benefit from a system that could easily and seamlessly schedule his classes for him based on his preferences for classes  that dont relate to criminal justice since he has that breathing room along with picking the right capstone class at his allotted time for him.


***
**Rachel, an Anthro senior**
***

Rachel, age 23 is an Anthropology senior, works a part time job outside of school, and commutes to school daily. She has very little free-time available to her since she's busy with classes  and clubs on top of her job which requires her to work late. Getting up at 7am for registration proves extremely difficult for her as she often doesn't get home until 2am because of work. She also has to take a very high course-load to graduate on time, normally 5-6 classes per semester. Setting up a course plan normally takes her multiple hours or sometimes several days worth of her free-time. She would benefit greatly from a system that automatically registers her classes for her in the morning. However she would benefit even more greatly from a program that could accept her desired courses and/or requirements that would then give her every possible (valid) schedule combination if any exist. This would eliminate a recurring chore that eats up a lot of her time and relieve some of the stresses she faces.


***
**Tony, Graphic Design Junior**
***

Tony, age 20 is a Junior who recently transfered to Temple Universuty, seeking a degree in Graphic Design.
This is Tony's first time in philadelphia and interacting with any of Temple registration features. Tony was not given a proper rundown 
on how to sign up for classes and is not familiar with temple system. He is very stressed because he does not know which classes he needs to 
take for his major, and is worried that he will miss priorty registration thus missing the oppertunity to sign up for classes that he 
needs.Tony has been asking faculty if there is a application that will register course for him in a timely manner and recommend ones he 
should take for his major. 

***
**Andrew, Business Freshman**
***

Andrew is a freshman, undeclared business student at Temple University. He's a bit of a procrastinator, but has no problems doing everything he needs to pass his classes. Unfortunately, his priority registration date is tomorrow, and he never scheduled a meeting with an advisor to help schedule his classes. Being an undeclared sttudent, he can't find any information to help him pick any specific classes. Even though he lives on campus and doesn't have any time restrictions, he's lost, and has no clue what classes to take. He's fine with taking any classes at any time, but at this point ahe can't quite figure out exactly what classes he can take to fulfill certain requirements and graduate on time.

## Trello ##
https://trello.com/b/iZgkH5XX/the-scheduler

## UML ##
![](../../Desktop/Screen Shot 2021-11-07 at 10.55.02 PM.png)
