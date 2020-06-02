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
        
    #3. The percentage of votes each candidate won
        for candidate in candidate_tally:
            percentages[candidate] = (candidate_tally[candidate]/ total_votes) * 100

   
  
  
    

with open(output_file, 'w', newline = '') as txtfile:
    election_output = (f"\nElection Results\n"
          f"----------------------------\n"
    f"Total Votes: {total_votes}\n" 
    f"----------------------------\n"
    f" \n"
    )  
    
     #5. The winner of the election based on popular vote
    winner = max(candidate_tally, key = candidate_tally.get)
    winner_output = (f"---------------------------- \n"
                     f"Winner: {winner} \n"
                     f"---------------------------- \n")
    
    txtfile.write(election_output)
    txtfile.write(winner_output)
    
    for candidate, tally in percentages.items():
        vote_count_output = (f"{candidate}: {percentages[candidate]:.3f}%\n")    

        txtfile.write(vote_count_output)
        
    
    
#6. export text file
            ##loop through dictionaries and write to file with proper syntax
            #convert "percentages"  values to percentages
#7. print to terminal


#print(f"total votes cast: {total_votes}")
#print(f"list of candidates: {list_of_candidates}") #alphabetize to cross-check spelling
#print(f"candidate vote tally: {candidate_tally}")
#print(f"percentages: {percentages}")
print(winner)