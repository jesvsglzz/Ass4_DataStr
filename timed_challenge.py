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