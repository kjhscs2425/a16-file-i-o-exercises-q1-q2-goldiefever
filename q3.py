# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
with open("romeo_and_juliet.txt", "r")as f:
    text = f.read()
####
#### YOUR CODE HERE 
####
# Count how many times the word "Juliet" appears
with open("romeo_and_juliet.txt", "r")as f:
    juliet_count = 0
    for line in f:
        if "Juliet" in line:
            juliet_count+=1
        else:
            pass

print(juliet_count)
####
#### YOUR CODE HERE 
####
