import random

three_digit_code = ""
four_digit_code = ""

for i in range(3):
    three_digit_code += str(random.randint(0, 9))

for i in range(4):
    four_digit_code += str(random.randint(1, 6))

print(f"3-digit code: {three_digit_code}")
print(f"4-digit code: {four_digit_code}")