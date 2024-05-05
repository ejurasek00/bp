from collections import Counter

# Define the data
data = """
354C31,DBCEEF,6CE255,199D26,D59553,331981,869F50
B2895C,B0FAAD,9ED0E8,D11884,269963,ADC8A2,999999
1520D1,49E95E,A6463C,D11884,269963,ADC8A2,999999
0BEA8D,B0FAAD,A6463C,D11884,269963,ADC8A2,999999
7EA60D,B0FAAD,C5B9CC,D11884,269963,420666,999999
"""

# Split the data into lines
lines = data.strip().split("\n")

# Initialize a Counter object
counter = Counter()

# Iterate over each line
for line in lines:
    # Split the line into items and update the counter
    counter.update(line.split(","))

# Find and print all frequent itemsets of length 1 with a minimum support of 2
for item, count in counter.items():
    if count >= 2:
        print(f"Item: {item}, Support: {count}")
