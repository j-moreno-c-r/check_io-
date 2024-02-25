#!/home/j.moreno/.local/bin/checkio --domain=py run duplicate-zeros

# "Sometimes, zeros resemble very tasty donut. And every time we finish a donut, we want another, and then another, and then another..."
# 
# You are givenlistof integers(int). Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) all zeros (think about donuts ;-P) and return the result as anyIterable. Let's look on the example:
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:Aliston anotherIterable(tuple,generator,iterator) of integers(int).
# 
# If you have solved this mission, you can enjoy a 🍩 with peace of mind!=)
# 
# 
# END_DESC

from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    answer = []
    for don in donuts:
        if don == 0:
            answer.append(don * 2)
        if don != 0:
            answer.append(don)
    return answer


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")