import csv
import os

election_data_file = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('Resources', 'election_results.txt') 

total_votes = 0
list_of_candidates = []
candidate_tally = {}
percentages = {}

#The total number of votes each candidate won
def vote_counts(candidate):
    if candidate in candidate_tally:
        candidate_tally[candidate] += 1
    else:
        candidate_tally[candidate] = 1
   
            
with open(election_data_file, newline = "") as election_file:
    reader = csv.reader(election_file, delimiter=',')
    header = next(reader) #to skip first row
    
    for row in reader:
    #The total number of votes cast
        total_votes += 1
        
    #The list of candidates who received votes
        if (row[2] not in list_of_candidates):    
            list_of_candidates.append(row[2])

        vote_counts(row[2])
        
    #The percentage of votes each candidate won
        for candidate in candidate_tally:
            percentages[candidate] = (candidate_tally[candidate]/ total_votes) * 100

   
#write to file
with open(output_file, 'w', newline = '') as txtfile:
    election_output = (f"\nElection Results\n"
          f"----------------------------\n"
    f"Total Votes: {total_votes}\n" 
    f"----------------------------\n")  
    
     #5. The winner of the election based on popular vote
    winner = max(candidate_tally, key = candidate_tally.get)
    winner_output = (f"Winner: {winner} \n"
                     f"---------------------------- \n")
    
    txtfile.write(election_output)
    txtfile.write(winner_output)
    
    for candidate, tally in percentages.items():
        vote_count_output = (f"{candidate}: {percentages[candidate]:.3f}% ({candidate_tally[candidate]})\n")    

        txtfile.write(vote_count_output)
    

#Print to terminal
print(f"\nElection Results\n"
          f"---------------------------- \n"
    f"Total Votes: {total_votes} \n" 
    f"----------------------------")
for candidate in percentages:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_tally[candidate]})")

print(f"---------------------------- \n"
    f"Winner: {winner}\n" 
    f"----------------------------\n")

