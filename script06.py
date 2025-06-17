class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, amount=1):
        self.value += amount

    def decrement(self, amount=1):
        self.value -= amount

    def reset(self):
        self.value = 0

"""
|
|
|
"""

def new_counter():
    return Counter()
