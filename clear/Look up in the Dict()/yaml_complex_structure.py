#!/home/j.moreno/.local/bin/checkio --domain=py run yaml-complex-structure

# The 4th task in the series of missions about the YAML format will be devoted to a complex structure.
# 
# YAMLPython/TypeScriptA list element can be another list.
# 
# 
#         - Alex
#         -
#           - odessa
#           - dnipro
#         - Li
#       
#         [
#           "Alex", 
#           [
#             "odessa", 
#             "dnipro"
#           ], 
#           "Li"
#         ]
#         A dictionary can also be an element of an list.
# 
# 
#         - 67
#         -
#           name: Irv
#           game: Mario
#         -
#         - 56
#       
#         [
#           67, 
#           {
#             "game": "Mario", 
#             "name": "Irv"
#           }, 
#           None/null, 
#           56
#         ]
#       A dictionary element can be another dictionary.
# 
# 
#         name: Alex
#         study:
#           type: school
#           number: 78
#         age: 14
#       
#         {
#           "age": 14, 
#           "study": {
#             "type": "school", 
#             "number": 78
#           }, 
#           "name": "Alex"
#         }
#       A list can also be an element of dictionary.
# 
# 
#         name: Alex
#         study:
#           - 89
#           - 89
#           - "Hell"
#         age: 14
#       
#         {
#           "age": 14, 
#           "study": [
#             89, 
#             89, 
#             "Hell"
#           ], 
#           "name": "Alex"
#         }
#       And, of course, data can have more than one nesting level.
# 
# 
#         name: Alex
#         study:
#           -
#             type: school
#             num: 89
#           -
#             type: school
#             num: 12
#         age: 14
#       
#         {
#           "age": 14, 
#           "study": [
#             {
#               "num": 89, 
#               "type": "school"
#             }, 
#             {
#               "num": 12, 
#               "type": "school"
#             }
#           ], 
#           "name": "Alex"
#         }
#       Input:Format string.
# 
# Output:An object (list/dictionary).
# 
# Precondition:The YAML 1.2 standard is being used.
# 
# 
# END_DESC

def yaml(a: str) -> list | dict:
    # your code here
    return None


print("Example:")
print(yaml("- Alex\n" "-\n" "  - odessa\n" "  - dnipro\n" "- Li"))

# These "asserts" are used for self-checking
assert yaml("- Alex\n-\n  - odessa\n  - dnipro\n- Li") == [
    "Alex",
    ["odessa", "dnipro"],
    "Li",
]
assert yaml("- 67\n-\n  name: Irv\n  game: Mario\n-\n- 56") == [
    67,
    {"game": "Mario", "name": "Irv"},
    None,
    56,
]
assert yaml("name: Alex\nstudy:\n  type: school\n  number: 78\nage: 14") == {
    "age": 14,
    "study": {"type": "school", "number": 78},
    "name": "Alex",
}
assert yaml('name: Alex\nstudy:\n  - 89\n  - 89\n  - "Hell"\nage: 14') == {
    "age": 14,
    "study": [89, 89, "Hell"],
    "name": "Alex",
}
assert yaml(
    "name: Alex\nstudy:\n  -\n    type: school\n    num: 89\n  -\n    type: school\n    num: 12\nage: 14"
) == {
    "age": 14,
    "study": [{"num": 89, "type": "school"}, {"num": 12, "type": "school"}],
    "name": "Alex",
}
assert yaml(
    "name: Alex\nstudy:\n  -\n    type: school\n    nums:\n      - 12\n      - 67\n  -\n    type: school\n    num: 12\nage: 14"
) == {
    "age": 14,
    "study": [{"type": "school", "nums": [12, 67]}, {"num": 12, "type": "school"}],
    "name": "Alex",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")