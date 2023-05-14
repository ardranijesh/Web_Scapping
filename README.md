# Web_Scapping
We want you to write a scraper for all the job postings at https://www.cermati.com/karir
As you can see there are multiple departments/teams in cermati.com for example: engineering
department, product department, people ops department, etc. Please create a code that can
explore each department and scrape the job opening using code written in Python 3/ Java.
We prefer Java. Use python only if you don’t know java. Do not hard code the URL in your
code for each job posting. Your code should parse the HTML on https://www.cermati.com/karir
and explore the link dynamically. You’re only allowed to hard code this URL
https://www.cermati.com/karir as the starting point.
We want you to get all the information about the job openings that cermati.com has. So explore
the jobs in each department and get all the job and job details in that department. For example:
In the Engineering department there is a “Software Quality Assurance” job. If you explore the
link, you can get the Job Location, Job Description, Job Qualification, Posted By Whom.
Please assume that the number of departments, the number of jobs, the type of jobs can
change in the future so your code must scrape and parse the html in anticipation of that (but
you can assume that the structure of the html should still be the same)
After your code finishes scraping all the job openings, your code should put all the info in a
single json file.
The JSON file has a format like this:
{
“<Department name>”: [
{ “title”: “<job title>”,
“location”: “<job location>”,
“description”: [“<job desc>”, “<job desc>”, “<job desc>”],
“qualification”: [“<qualification>”, “<qualification>”,

“<qualification>”],

“posted by”: “<job poster>”
},
]
}
