#!/home/j.moreno/.local/bin/checkio --domain=py run digits-multiplication

# You are given a positive number.    Your function should calculate the product of the digits excluding any zeroes.
# 
# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
# 
# 
# 
# Input:A positive integer(int).
# 
# Output:The product of the digits as an integer(int).
# 
# Precondition:
# 0 < number < 106
# 
# 
# END_DESC

def checkio(number: int) -> int:
    # your code here
    return 0


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")