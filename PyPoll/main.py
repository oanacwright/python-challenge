import csv

# Path to collect the data from the Resource Folder
csvpath = "C:/Users/oanaw/python-challenge/PyPoll/Resources/election_data.csv"

# Open csv file and skip header row

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Defining a lists and variables to be used
    candidate = []                  # holds all entires in candidate column
    uniquecandidates = []           # holds only unique candidates  
    voters = 0                      # counder for totla voters
    candidatesumvotes = {}          # dictionary that holds Candidate/total votes

    # For every row, we are going to assign the value in column index 2 to candidate
    for row in csvreader:
        candidate = row[2]
        # If that particular candidate is not in uniquecandidates list, add to the list and set initial value for the sum of votes to 0 
        if candidate not in uniquecandidates:
            uniquecandidates.append(candidate)
            candidatesumvotes[candidate] = 0
        # increase by one the voter count and the numbers of votes associated with each candidate in the candidatesumvotes dictionary
        candidatesumvotes[candidate] += 1
        voters += 1
        
# Print out results in the terminal. 
# Printing of all unique candidates with the votes will be done here with a for loop.
# Winning candidate is found by using the max function on dictionary (https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary)

print("Election Results")
print("---------------------------------------")
print("Total Votes: " + format(voters,'.0f'))
print("---------------------------------------")
for i in candidatesumvotes:
    print(i + ": " + format((candidatesumvotes[i]/voters)*100,'.3f') +
              "% (" + format(candidatesumvotes[i],'.0f') + ")")
print("---------------------------------------")
print("Winner:  " + max(candidatesumvotes, key=candidatesumvotes.get))
print("---------------------------------------")

# Printing results to file "PyPoll_analysis.txt" 
output_file = "C:/Users/oanaw/python-challenge/PyPoll/Analysis/PyPoll_analysis.txt"

with open(output_file,"w+") as file:
    file.write("Election Results\n")
    file.write("---------------------------------------\n")
    file.write("Total Votes: " + format(voters,'.0f')+"\n")
    file.write("---------------------------------------\n")
    for i in candidatesumvotes:
        file.write(i + ": " + format((candidatesumvotes[i]/voters)*100,'.3f') +
              "% (" + format(candidatesumvotes[i],'.0f') + ")\n")
    file.write("---------------------------------------\n")
    file.write("Winner:  " + max(candidatesumvotes, key=candidatesumvotes.get)+"\n")
    file.write("---------------------------------------") 