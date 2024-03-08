# python-challenge

# Description for the PyPoll
For the PyPoll problem I started off by declaring the variables I needed. They were total_votes (a vraiable that would keep back of the total votes cast in this election), a list of the candidates (to keep track of the candidates), candidates_votes (a list equivalent to the length of the candidates list to keep track of how many votes were cast for each candidate), candidate_percentages (to keep track of the percentages) and the variable i to be used in a while loop later.

The first hurtle I overcame that I solved with Sam was reading in the file. Upon solving some issues with the kernel we ended up cd(ing) into the folder "python-challenge" to run this code. I couldn't get the os.path to work so this was what I did (and duplicated it for the other part of the project). After reading in election_data.csv as "file" I chopped off the first row with the command "next".

I then utilized a for loop to go through every single row in "file". For every iteration it incrimented the amount of votes by 1. I then used a variable called "test" and designated it's value equivalent to the third entry of the file (since python lists start at 0, the third entry will be entered in as "2"). If the entry is not in the candidates list I appended the test to the array and I appended a singular vote for them in candidates_votes. If the test was in the array I found it's index in the candidates list and I used that index and placed it in candidadte_votes to incriment the correct candidate votes by 1.

I could not get another For loop to work in this project no matter what I tried. I ended up resorting to a while loop to go through the candidate_votes to calculate the percentages so that I could append them to candidate_percentages. The variable i was used for this while loop and was incrimented after each operation until i was no longer less than the length of candidate_votes.

As stated above, the length of my list was 3, so I printed off the results one at a time. First the total votes, then the candidates with how many votes they got and what percentage they got. Then, I printed off the winner. After that, I used the "with open" operation to put my results into a file and exported it.

# Description for the PyBank
I started off by declaring my variables. My variables were months (to keep track of all the months), profit_change (to keep track of the profit changes), total (to keep track of my totals) and 2 variables to be used in a while loop. I had a problem in the assignment where a second for loop would just never be read. I tried it with a while loop and it worked.

After reading in my budget_data.csv I removed the header. I then appeneded the months and totals to their respectives lists. I then incriment my total length.

After I got my necessary information I then calculated all my profit changes in a while loop. I then appended the values to their profit changes.

To make my printed out results easier for me to read I calculated out all the values I needed. After I calculated them out I printed them out and then used a "with open" to export it.

# Data Files
election_data.csv
budget_data.csv
PyBank.py
PyPoll.py

# Dependencies
Python 3
csv
os
