# Author : Ardra P
# Date   : 13-05-2023
# 
# Extract the job posting info from url and 
# save extracted information in a json file

import requests
import json
from bs4 import BeautifulSoup
import os
import re

# create function for scarp sub url
def scarpSubUrl(url,dic):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contents = str(soup)

    json_data = json.loads(contents)
    jobDescription = re.split(r'<.*?>',(json_data['jobAd']['sections']['jobDescription']['text']))
    jobDescription = [element for element in jobDescription if element]
    # add job description to the dictonary
    dic["jobDescription"] = jobDescription
    qualifications = re.split(r'<.*?>',(json_data['jobAd']['sections']['qualifications']['text']))
    qualifications = [element for element in qualifications if element]
    # add qualifications to the dictonary
    dic["qualifications"] =qualifications
    dic['posted by'] = json_data['creator']['name']

def extractAndFilldata():

    # Send a GET request to the URL
    url = "https://www.cermati.com/karir"

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        script_tag = soup.find('script', id='initials')
        # access the content within a <script> tag as a string.
        json_string = script_tag.string 
        # parse a JSON-formatted string and convert it into a corresponding Python object
        json_data = json.loads(json_string)

        smart_rc = json_data['smartRecruiterResult']
        json_data=[]

        # extract the required details from "smartRecruiterResult" container
        for content in smart_rc:
            if content == "all": # selecting content under all
                for item in smart_rc[content]['content']:
                    #create empty dictonary
                    dic= {}
                    if(len(item['department']) > 0):
                            Department_name = item['department']['label']                            
                            json_data.append(Department_name)
                            # append to json_data
                            dic["Name"]=item["name"]
                            location=item['location']['city']
                            dic["location"]=location
                            for field in item['customField']:
                                if "COUNTRY" == field['fieldId']:
                                    location += ","+field['valueLabel']
                                    dic["location"]=location
                            scarpSubUrl(item['ref'],dic)
                            json_data.append(dic)
                    else:
                            Department_name = 'Others'
                            json_data.append(Department_name)
                            # append to json_data
                            dic["Name"]=item["name"]
                            location=item['location']['city']
                            dic["location"]=location
                            for field in item['customField']:
                                if "COUNTRY" == field['fieldId']:
                                    location += ","+field['valueLabel']
                                    dic["location"]=location
                            scarpSubUrl(item['ref'],dic)
                            json_data.append(dic)
            department_list=[]
            # create the list contains the departments
            for i in range(len(json_data)):
                if(i%2)==0:
                    department= json_data[i]
                    if department not in department_list:
                        department_list.append(department)

            final_list=[]
            # Fill extracted data to each department list
            for i in department_list:
                final_list.append(i)
                inner_list=[]
                for j in range(len(json_data)-1):
                    if (json_data[j]==i):
                        inner_list.append(json_data[j+1])
                final_list.append(inner_list)

    else:
        print("Failed to retrieve the page:", response.status_code)

    # create json file
    filename = 'solution.json'
    with open(filename, 'w') as file:
        json.dump(final_list, file,indent=4,ensure_ascii=True)
    print(f"JSON file '{filename}' with extracted data has been created in '{os.getcwd()}'.")

extractAndFilldata()