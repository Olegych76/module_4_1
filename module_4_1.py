from fake_math import divide as false_divide
from true_math import divide as true_divide

print(false_divide(69, 3))
print(false_divide(3, 0))
print(true_divide(49, 7))
print(true_divide(15, 0))