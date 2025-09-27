# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

## QUESTION: 3. Remove Duplicates (Keep Order)
#Return the values in the order they first appeared, without duplicates.
#Input: ["apple", "banana", "apple", "kiwi", "banana"]
#Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(values):
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result

# Testing the solution
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"])) # Expected ['apple', 'banana', 'kiwi']
print(remove_duplicates_keep_order(["1", "1", "2", "3", "2", "1", "4"])) # Expected ['1', '2', '3', '4']
print(remove_duplicates_keep_order(["a", "a", "b", "a", "b", "a"])) # Expected ['a', 'b']
print(remove_duplicates_keep_order([])) # Expected []


## Reflection:
# I chose to use a set along with a list for this solution. The set allows me to quickly check whether a 
# value has already been added, and the list keeps the order of the first appearance of each value. This 
# combination ensures that the final output has no duplicates while maintaining the original order, which 
# was the main requirement. 

# The time limit influenced my decision to keep the solution simple and easy to write. Using a set is 
# efficient and avoids nested loops, which could slow down the program on large inputs. By choosing this 
# structure, I could quickly implement and test the solution without worrying about performance problems 
# for normal input sizes. 

# Under time pressure, the main trade-off I accepted was using extra memory for the set to track seen 
# values. This slightly increases space usage but greatly reduces complexity and improves speed. I also 
# focused on making the code clear and readable rather than using more compact methods, because clarity 
# helps prevent mistakes when working quickly. Overall, the approach balances speed, correctness, and 
# simplicity, which was important under the time limit.
