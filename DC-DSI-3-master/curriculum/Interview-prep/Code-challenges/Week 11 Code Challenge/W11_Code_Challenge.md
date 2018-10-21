![GA Logo](https://raw.github.com/generalassembly/ga-ruby-on-rails-for-devs/master/images/ga.png)

## Week 11 Code Challenge

This week will consist of 1 large data science code challenge broken up into 4 parts, with one part being administered every day of the week.

All 4 parts should be conducted and completed in a single notebook.
A general summary of a days challenge is provided, however specifics of what is expected will not be posted until the day of.

**Hey, Listen!!!**  
Keep in mind that interviewers are considering the following when evaluating 'Take home' code challenges..
- Does the candidate run tests? Do they do enough testing?
- Does the thing actually work when they say it works? 
- Do they pay attention to the requirements?
- What technologies do they use?
- Are they using technologies they’re competent working in? Or are they using some odd or shiny things in order to impress us?
- What kind of design decisions do they make when presented with the freedom to do so?


**Monday - Constructing SQL Relational Database**  
Set up a SQL relational database. We want you to use the information in both the 'credit_info.csv' and 'customer_info.csv' to create a relational database using SQL. 'ID' is a unique value (or at least it should be).
Your database must contain 4 different tables.
- One with the customer demographic info (including if they defaulted or not)
- One with user's Payment Status History (PAY_STAT_XXX).
- One with user's Bill Amount history (BILL_AMT_XXX).
- One with user's Payment amount history (BILL_PAY_XXX)


You can use PostGres, SQLite or any other SQL system you are familiar with.
Include a written copy of the Data structure and all Keys (Primary and Secondary)

**Tuesday - Database Querying and EDA**  
- Identify and interpret summary statistics.  
  * Mean, Median, Mode  
  * Moving Averages and changes  
  * Distributions
- Handle missing values and justify your rational.
- Evaluate features for importance.
- Use visualizations (Tableau or Python plotting) to show a few of your findings.

- _Bonus_ - Engineer a Feature 
- _Super-Bonus_ Determine the relative importance of your engineered feature.


There is now a Data Dictionary in the 'Data' folder.

_Please add your notebook with your name to this 'Week 11 Code Challenge' folder and push it today._

**Wednesday - Model Building and implicit findings**  
Construct a predictive model to identify if a user is going to default on their credit (y = 'default payment next month'.)
- Use whatever model you feel would perform the best, but be sure to justify your choice.
- Identify a benchmark score and scoring criteria to consider a successful model.
- Utilize a means to tune your model
- Implement a means of cross validation (K-folds, TTS) to assess you model.

_Bonus_ - Construct what you would believe to be the worst performing model for the task at hand and summerize why you believe it would perform poorly.

_Consider the distributions of those the defaulted to those that did not when selecting data to train your model._


**Thursday - Output & Implementation**  
Last week members of the hiring panel spoke about how they are looking for data scientists that can do more than just 

- Create a plan to implement or utilize your model on the back end along with a complete live process which will ultimately result in a front end user interaction or deliverable.
    
Things like...
- The data flow.
>- Data Gathering
>- Data Storage
>- Data Extraction
>- Data Manipulation / modelling

- Front end to back end interaction.
>- What will be gathered on the front end. 
>- How will it interact with the backend.
>- How will it be processed. 
>- What will be returned to the fron end.
>- How will it return information to the front end. 


Visual diagrams are encouraged.  

Reminder <![Image caption]><(file/name.jpg)> will allow you to insert images into a MD cell (without the arrows).

_This is all theoretical so the exacts as far as 'hows' will not be expected, but the more detail you can include the better such as 'We'll set up an AWS instance to handle the computational portion'_

**_Friday - Blogs and Portfolios_**
- Over the course of this week long challenge we hope that you learn something new on your own whether that be about SQL, Python, Model building or product implementation that you can write about (if you're short on blog requirements).
