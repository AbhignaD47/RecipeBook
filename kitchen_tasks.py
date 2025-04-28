#Manages stacks and queues
from collections import deque

def manage_tasks():
    stack = []
    queue = deque()
    tasks = ["mix", "bake", "serve"]
    orders = ["cake", "pie"]
    # Stack tasks
    for task in tasks:
        stack.append(task)
        print("Added task:", stack)
    while stack:
        print("Completed:", stack.pop())
    # Queue orders
    for order in orders:
        queue.append(order)
        print("New order:", queue)
    while queue:
        print("Served:", queue.popleft())

try:
    manage_tasks()
    stack = []
    stack.pop()  # Test error handling
except IndexError:
    print("No tasks left!")
