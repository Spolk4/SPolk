import os
import csv
#Where is my file
election_data_csv = os.path.join("election_data.csv")
Output_path2 = os.path.join("Output2.txt")

with open(election_data_csv, newline="" ) as csvfile:

    #treat as csv data and read across
    csvreader = csv.reader(csvfile, delimiter=",")
    #read the header rows
    header = next(csvreader)

    #create something to capture the votes in
    votes = 0
    #variables to filter candidates out
    nomineeslist =[]
    candidateslist = []
    
    #loop through to find specific nominees and append candidates list
    for row in csvreader:
        candidate = row[2]
        nomineeslist.append(candidate)

    #fill candidates list with unique values of candidates
    candidateslist = set(nomineeslist)
    #start again
    candidateslist = list(candidateslist)
    candidateslist.append(candidateslist)
    
    #create variables of nominees 
    nominee1 = "Li"
    nominee2 = "Khan"
    nominee3 = "O'Tooley"
    nominee4 = "Correy"

    # create lists to fill with their votes
    Li= []
    Khan = []
    Otooley = []
    Correy = []
    
    #variable and function to collect votes
    Li_v = nomineeslist.count("Li")
    Khan_v = nomineeslist.count("Khan")
    Otooley_v = nomineeslist.count("O'Tooley")
    Correy_v = nomineeslist.count("Correy")

    #find the total votes minus the [...] for getting the percents
    votes = Li_v + Khan_v + Otooley_v + Correy_v
    #print(votes)

    #calculate percentage of votes of the nominees
    Lipercent = round(Li_v/votes, 3)*100
    Khanpercent = round(Khan_v/votes, 3)*100
    Otooleypercent = round(Otooley_v/votes, 3)*100
    Correypercent = round(Correy_v/votes)*100

    #print(Lipercent)

    #find the winner to print in terminal
    winner = max([(nomineeslist.count(chr),chr) for chr in set(nomineeslist)])

    print(f"Election Results")
    print(f"-------------------------------------------")
    print(f"Total Votes: {votes}")
    print(f"Khan: {Khanpercent} ({Khan_v})")
    print(f"Correy: {Correypercent} ({Correy_v})")
    print(f"Li: {Lipercent} ({Li_v})")
    print(f"O'Tooley: {Otooleypercent} ({Otooley_v})")
    print(f"-------------------------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------------------------")
    
with open(Output_path2, 'w') as txt_file:

    Election_Results = (f" Electrion Results \n"
        f"---------------------------------- \n"
        f"Total Votes: {votes} \n"
        f" Khan: {Khanpercent} ({Khan_v} \n"
        f"Correy: {Correypercent} ({Correy_v} \n"
        f"Li: {Lipercent} ({Li_v}) \n "
        f"O'Tooley: {Otooleypercent} ({Otooley_v}) \n"
        f"------------------------------------------ \n"
        f"Winner: {winner} \n"
        f"---------------------------------------- \n")
    print(Election_Results)
    
    txt_file.write(Election_Results)