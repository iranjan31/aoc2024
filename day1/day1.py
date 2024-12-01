# read in day_input.txt
with open('day1_input.txt', 'r') as file:
    data = file.read().splitlines()

# Two lists to store the data points
data_pair1 = []
data_pair2 = []

# Split the data points and store them in the two lists
for datapoints in data:
    
    # Split the data points from the file parse
    datapoint = datapoints.split('   ')
    
    # Save the data points in the two lists
    point1 = int(datapoint[0])
    point2 = int(datapoint[1])
    data_pair1.append(point1)
    data_pair2.append(point2)

# Sort the two lists  
data_pair1.sort()
data_pair2.sort()

# Find the total sum of differences between the two lists
sum = 0
for i in range(len(data_pair1)):
    sum += abs(data_pair1[i] - data_pair2[i])

print(f"The sum of the differences between the two lists is: {sum}")

# Set a variable for the similarity between the two lists
similarity_score = 0
for point1 in data_pair1:

    # Calculate the similarity score between the two lists as follows
    #      1. For each point in the first list, check if it is in the second list
    #      2. If it is in the second list, multiply the point by the number of times it appears in the second list
    #      3. Add the product to the similarity score
    similarity_score += point1*data_pair2.count(point1)

print(f"The similarity score between the two lists is: {similarity_score}")