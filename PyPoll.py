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
#initalize a total vote counter.
total_votes = 0
#candidate options
candidate_options=[]
#declare the empty dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#using the with statement open the file as a text file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read header row
    headers = next(file_reader)
    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #print te candidate name for each row
        candidate_name = row[2]
        #add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            #add it to the list of candidates 
            candidate_options.append(candidate_name)
            #begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] +=1
#save the results to our text fike
with open(file_to_save, "w") as txt_file:
    #print the final vote count to termina
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")  
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    #determine the percentage of votes for each candidate by looping
    ##iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print the candidate name with percentage of votes
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print candidate voter count and percentage to terminal
        print(candidate_results)
        #save the results to the text file
        txt_file.write(candidate_results)
        #determine if winning votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count =votes
            winning_percentage = vote_percentage
            # and set the winning_candidate = to candidates name
            winning_candidate = candidate_name
            #print winning candidate, vote count and percentage
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #winning candidate summary
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
    print(winning_candidate_summary)
    #save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)