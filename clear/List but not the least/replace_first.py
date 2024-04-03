#!/home/j.moreno/.local/bin/checkio --domain=py run replace-first

# 
# 
# In a given sequence the first element should become the last one. An empty sequence or with only one element should stay the same.
# 
# 
# 
# Input:List.
# 
# Output:Listor anotherIterable(tuple,iterator,generator).
# 
# 
# END_DESC

from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if items == []:
        return items
    items.append(items[0])
    items.pop(0)               
    return items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")