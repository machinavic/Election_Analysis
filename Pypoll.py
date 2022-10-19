#The data we need to retrieve.
#1. The total number of votes cast.
#2. A Complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular votes.

#Add our dependencies
import csv

import os

#Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

#Open the electon results and read the file.
with open(file_to_load) as election_data:

#To do: read and analyze the data here.
     file_reader=csv.reader(election_data)

#Print each header row in the csv file.
     headers=next(file_reader)
     print(headers)




#Use the open statement to open the file as a text file.
outfile=open(file_to_save, "w")

#Write some data to the file.
outfile.write("Hello World")

#Close the file
outfile.close()

#using the with statement open the file as a txt file.
with open(file_to_save,"w") as txt_file:

#Write some data to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")




