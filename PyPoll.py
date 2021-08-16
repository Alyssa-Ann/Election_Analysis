#The data we need to retrieve
#The total number of votes cast
#A complete list of candidates who recieved votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on the popular vote
#.....................................................
#add dependencies
import csv
import os
#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the with statement open the file as a text file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    print(headers)