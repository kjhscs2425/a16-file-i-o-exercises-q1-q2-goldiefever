import os
import json

# Check if the file "data.json" exists.
if os.path.isfile("data.json"):
    with open("data.json","r") as f:
        data = json.load(f)
    # If it does, read "data.json" into the variable `data`

    ####
    #### YOUR CODE HERE 
    ####
else:
    # If it doesn't, make an empty dictionary called data
    data = {}

# Get a new recommendation for a new user
name = input("What is your name? ")
recommendation = input("What book/movie/podcast/etc. would you recommend? ")

# Add the new user and recommendation to the `data` dictionary
data[name] = recommendation

# Write the `data` variable to the file "data.json"
with open("data.json","w") as f:
    json.dump(data, f)
####
#### YOUR CODE HERE
####

