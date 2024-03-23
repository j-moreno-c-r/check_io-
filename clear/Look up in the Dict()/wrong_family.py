#!/home/j.moreno/.local/bin/checkio --domain=py run wrong-family

# Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of it.
# 
# Michael should figure this out. He's spent almost a month parsing the family archives. He has all father-son connections of his entire family collected in one place.
# 
# With all that data Michael can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let's see.
# 
# You have a list of family ties between father and son. Each element on this list has two elements. The first is the father's name, the second is the son's name. All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.
# 
# Input:A list of lists. Each element has two strings.    The list has at least one element
# 
# Output:Bool. Is the family tree correct.
# 
# 
# 
# 
# Precondition:1 <= len(tree) < 100
# 
# 
# END_DESC

def is_family(tree: list[list[str]]) -> bool:
    # your code here
    return True


print("Example:")
print(
    is_family(
        [
            ["Jack", "Mike"],
            ["Logan", "Mike"],
            ["Logan", "Jack"],
        ]
    )
)

assert is_family([["Logan", "Mike"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == True
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]) == False
assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]) == False
assert (
    is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]]) == False
)
assert is_family([["Jack", "Mike"], ["Logan", "Mike"], ["Logan", "Jack"]]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")