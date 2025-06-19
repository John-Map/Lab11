"""SDM: this program will conduct a series of statistics on an inputted string of grades. the stats will be saved to a text file. the stats will include: max, min, mean avg, quantity of numvers, sum total, evens, and odds

Steps to Solve: (pseudo-code)
1. get the numbers from the user
2. calculate the stats
    1. max: firn the biggetst number
    2. min: find the smallest number
    3. avg: sum up the numbers and divide by the quantity of numbers
    4. quantity: count up how many numbers there are
    5. sum: add up all the numbers
    6. evens: look at the list of numbers, check each number to see if its even, if so, add it to a new list of even numbers
    7 oods: basically the same as evens
3. save the stats to a text file
"""

# get the numbers from the user
grades = input("Please unter grade numbers seperated by spaces: ") # get a string of numbers
grades = grades.split() # convert the string into a list of numbers strings
grades = [int(g) for g in grades] # convert the list of number strings into a list of integers
# 1. quantity
quantity = len(grades)

# 2. sum
total = 0
print(f"sum: {sum(grades)}")
for g in grades:
    total += g

#3. max
max_grade = max(grades)
print(f"max: {max_grade}")

#4. min
min_grade = min(grades)
print(f"min: {min_grade}")
#5. avg
average = total/quantity
print(f"avg1: {average}")
# 6. evens
evens = []
for g in grades:
    if g % 2 == 0:
        evens.append(g)
print(f"evens: {evens}")
#7. odds
odds = []
for g in grades:
    if g % 2 == 1:
        odds.append(g)
print(f"odds: {odds}")

# 3. write the stats and their labes to a file
quantity_string = "quantity: " + str(quantity)
total_string = "sum: " + str(total)
max_string = "max: " + str(max_grade)
min_string = "min: " +  str(min_grade)
avg_string = "avg: " + str(average)
evens_string = "evens: " + str(evens)
odds_strings = "odds: " + str(odds)
# first, I neeed to create a list of stat strings
stats = [
    quantity_string,
    total_string,
    max_string,
    min_string,
    avg_string,
    evens_string,
    odds_strings
]

try:
    with open("stats.txt", "w") as file:
        for item in stats:
            file.write(item+"\n")
except IOError:
    print("there was a problem saving your list.")