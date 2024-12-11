import datetime

def get_input():
    input_name = input("Enter your name: ")

    try:
        input_age = int(input("Enter year of birth in christian era: "))
        input_score = int(input("Software testing score: "))
    except ValueError:
        print("Invalid input")
        exit()

    return input_name, input_age, input_score

def calculate_age(year):
    current_year = datetime.datetime.now().year
    age = current_year - year

    return age

def calculate_grade(score):
    if not (0 <= score <= 100):
        return "Invalid score"

    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"

def write_to_file(input_name, year_of_birth, score):
    file_path = "lab.txt"

    with open(file_path, "w") as file:
        file.write(f"Name: {input_name} \n")
        file.write(f"Age: {calculate_age(year_of_birth)} \n")
        file.write(f"Grade: {calculate_grade(score)} \n")

    print(f"Data was written to the file path: {file_path}")

def main():
    input_name, input_age, input_score = get_input()

    write_to_file(input_name, input_age, input_score)

if __name__ == "__main__":
    main()
