#!/home/j.moreno/.local/bin/checkio --domain=py run number-length

# You have a non-negative integer. Try to find out how many digits it has.
# 
# 
# 
# Input:A non-negative integer(int).
# 
# Output:An integer(int).
# 
# 
# END_DESC

def number_length(value: int) -> int:
    resultado = str(value)
    return len(resultado)


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")