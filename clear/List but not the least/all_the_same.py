#!/home/j.moreno/.local/bin/checkio --domain=py run all-the-same

# In this mission you should check if all elements in the given sequence are equal.
# 
# 
# 
# Input:List.
# 
# Output:Logic value(bool).
# 
# The idea for this mission was found onPython Tricks series by Dan Bader
# 
# Precondition:all elements of the input list are hashable
# 
# 
# END_DESC

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    list_ok = 0
    size_elements = len(elements)
    
    for c in elements:
        if c == all(elements):
            list_ok += 1 
        else:
            list_ok -=  1
        if c == []:
            list_ok += 1
            
                       
    if size_elements == list_ok:
        answer = True
        
    else:
        answer = False   
    
    if len(elements) == 1:
        answer = True
        
    return answer
    


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")