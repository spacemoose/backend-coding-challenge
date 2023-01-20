# Backend Coding Challenge

At aspaara a squad of superheroes works on giving superpowers to planning teams.
Through our product dashboard, we give insights into data – a true super-vision
superpower. Join forces with us and build a dashboard of the future!

![aspaara superhero](aspaara_superhero.png)

## Dear reviewer

As I mentioned in my cover letter, and is probably apparent from my CV, my tech stack is pretty different from what you guys do, and what this coding challenge involved.  It was a useful exersize for me, so I thank you for your time.

I didn't get done... I reserved all day to work on it today, and spent some time earlier in the week reading through some tutorials and documentation on SQLAlchemy and FastAPI, but I couldn't learn the tools fast enough to get finished in one day.  I do appreciate being given a preferred tech stack, and it was really fun to learn about the tools.

This submission represents my "learning by doing" efforts today.  Most of my DB experience is pretty far back in the rear-view mirror, so some of the questions, doubts and decisions I made might be a bit naive.  I wanted to do an initial commit today to meet the deadline, but if my family obligations let me I might continue to work on it over the weekend.  Should I do so, I'll leave it to you whether you want to consider the later additions.

Regarding the selection criteria, I can only ask that you consider this as an indication of how quickly (or not) I can learn the necessary tech stack.  I do of course have other skills & expertise I bring to the table.

In case you find yourself asking wtf in places, here are a few bullet points that might clarify my thought process:

   * Based on the fact that all client id's in sample data had the same industry, I put the industry in the client table.  In practice I'd look into that more before going ahead -- some clients might be active in multiple industries, and I'd want to know how best to handle that.
   * Similar with officeCity and officePostalCode.  I guess that's where the engagement takes place and so kept it in the bookings table.
   * I didn't bother specifying any indexes, as I didn't have any real insight into how the data will be used.
   * For hopefully obvious reasons I'd normally use an integer for a primary key for clientId and talentId.  I used a string  since that's is what the data model specified.   Given that the actual id is just a prefix plus an integer, I suspect I missed an obvious implication.  I was deeply tempted to strip the prefix and store the table entries with an integer id.  Instead I assumed there was a reason for doing it as specified.

### Implementation notes
   * Before running the api, run the script "initialize_db.py" to create tables and populate the db.
#### Dependancies
	* sqlalchemy 1.4.46
	* databases[sqlite] (Encode databases library)
    * sqlite 3.36.0

   What little works was tested using "unicorn api:app" within "api_app" directory.
## Goal

Create a simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.

You will find the corresponding data that needs to be imported into the database
in `planning.json`, which contains around 10k records.

## Requirements

1. Create proper database tables that can fit the data model.
2. Create a script that imports the data into the database (sqlite).
3. Create REST APIs to get the planning data from the database.
    1. The APIs don't need to be complete, just create what you can in the
       available time.
    2. Please include at least one example on how to do each of the following:
        1. pagination
        2. sorting
        3. filtering / searching

## Data Model

* ID: integer (unique, required)
* Original ID: string (unique, required)
* Talent ID: string (optional)
* Talent Name: string (optional)
* Talent Grade: string (optional)
* Booking Grade: string (optional)
* Operating Unit: string (required)
* Office City: string (optional)
* Office Postal Code: string (required)
* Job Manager Name: string (optional)
* Job Manager ID: string (optional)
* Total Hours: float (required)
* Start Date: datetime (required)
* End Date: datetime (required)
* Client Name: string (optional)
* Client ID: string (required)
* Industry: string (optional)
* Required Skills: array of key-value pair (optional)
* Optional Skills: array of key-value pair (optional)
* Is Unassigned: boolean

## Preferred Tech Stack

* Python 3.8+
* FastAPI
* SQLAlchemy

## Submission

* Please fork the project, commit and push your implementation and add
  `sundara.amancharla@aspaara.com` as a contributor.
* Please update the README with any additional details or steps that are
  required to run your implementation.
* We understand that there is a limited amount of time, so it does not have to
  be perfect or 100% finished. Plan to spend no more than 2-3 hours on it.

For any additional questions on the task please feel free to email
`sundara.amancharla@aspaara.com`.
