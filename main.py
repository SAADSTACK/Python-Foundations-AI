
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# BUILD A CALCULATOR
print("Select Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter Choice (1/2/3/4): ")
if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    print(num1, "/", num2, "=", num1 / num2)
weight = float(input("Enter your weight in kg: "))
print("Weight is:", weight)
num = int(input("Enter a number to check Even/Odd: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
score = int(input("Enter score: "))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
count = 1
while count <= 5:
    print(count)
    count += 1
for i in range(1, 10):
    if i == 5:
        break
    print(i)
def greet():
    print("Hello World from Function!")
def greet_user(name):
      print("Hello", name)
def add(a, b):
    return a + b
def calculate_area(length, width):
      return length * width
# CALCULATE AREA OF A RECTANGLE
length = float(input("Enter length of rectangle: "))    
width = float(input("Enter width of rectangle: "))
area = calculate_area(length, width)
print("Area of rectangle is:", area)
skills = ["Python", "AI", "Automation"]
print(skills)
print(skills[0])
print(skills[1])
print(skills[-1])
print(len(skills))
skills.append("LLMs")
print(skills)
skills.remove("Automation")
print(skills)
for skill in skills:
    print("Skill:", skill)
favorite_tools = {
    "IDE": "VS Code",
    "Version Control": "Git",   
    "Containerization": "Docker"
}
print(favorite_tools)
mixed_list = ["Saad", 21, True, 3.8]
students = []
favorite_tools = ["VS Code", "GitHub", "ChatGPT"]
for tool in favorite_tools:
    print("Tool:", tool)
student = {
      "name": "Saad",
      "semester": 6,
      "department": "IEM"
  }
print(student)
student["goals"] = "AI Engineer"
print(student)
for value in student.values():
    print("Value:", value)
    for key, value in student.items():
      print(f"{key}: {value}")