def line_count(path):
    with open(path, 'r') as f:
        return sum(1 for _ in f)

"""
|
|
|
"""

def word_search(path, word):
    with open(path, 'r') as f:
        return any(word in line for line in f)

"""
|
|
|
"""

def longest_line(path):
    with open(path, 'r') as f:
        return max((len(line) for line in f), default=0)
