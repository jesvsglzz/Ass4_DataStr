"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

# Justification:
# I used a set because it is good for checking if a value is already present and for keeping only unique
# values. We go through each product ID, check if we have seen it before, and add it if we have not. A list
# would have been slower because we would need to look through all items each time we check for duplicates.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)  # Enqueue

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.pop(0)  # Dequeue
        return None
        
# Justification:
# I used a list to act like a queue because it keeps the order of tasks, which matches first-in-first-out 
# behavior. We add tasks to the end and remove them from the front so the oldest task is removed first.
# A stack would have removed the newest task first, which would not match what the problem asks for.

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

# Justification:
# I used a set because it only keeps unique values and ignores duplicates automatically. We add each 
# value to the set and use len() to get how many unique values have been seen. A list would have required
# checking each item before adding, which would take longer.
