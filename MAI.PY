sub1 = float(input("Enter mark for subject 1: "))
sub2 = float(input("Enter mark for subject 2: "))
sub3 = float(input("Enter mark for subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3

if average >= 80:
  grade = "A"
elif average >= 65:
  grade = "B"
elif average >= 50:
  grade = "C"
else:
  grade = "F"

print(f"Total: {total}, Average: {average:.2f}, Grade: {grade}")