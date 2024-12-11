import datetime

input_name = input("Name: ")
input_age = int(input("Christian Era: "))
input_score = int(input("Software testing score: "))

def calculate_age(input_age):
    current_year = datetime.datetime.now().year
    return current_year - input_age

def calculate_grade(input_score):
    if input_score >= 80:
        return "A"
    elif input_score >= 75:
        return "B+"
    elif input_score >= 70:
        return "B"
    elif input_score >= 65:
        return "C+"
    elif input_score >= 60:
        return "C"
    elif input_score >= 55:
        return "D+"
    elif input_score >= 50:
        return "D"
    elif input_score < 50:
        return "F"

with open("textfile.txt", "w") as file:
    file.write(f"Name: {input_name}\n")
    file.write(f"Age: {calculate_age(input_age)}\n")
    file.write(f"Software testing grade: {calculate_grade(input_score)}\n")
