def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

"""Remove duplicate elements while preserving order."""

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
"""Flatten a nested list recursively."""


def second_largest(lst):
    unique = sorted(set(lst))
    return unique[-2] if len(unique) >= 2 else None
