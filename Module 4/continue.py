scores = [68, 42, 57, 78, 35, 62, 50, 92]
total = 0
count = 0

#Iterate through each score in the list
for score in scores:
    #Check if the score is below 50, if so skip to the next iteration
    if score < 50:
        #If the score is above 50, add it to the total and increment the count
        total += score
        count += 1

#Calculate te average score for scores above 50, handling the case where count is 0 to avoid division by 0
average = total / count if count > 0 else 0

print("Average score for scores above 50:", average)


