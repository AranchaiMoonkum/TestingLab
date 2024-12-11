import datetime

def calAge(age):
    age = int(age)
    this_year = datetime.date.today().year
    birthYear = (this_year + 543) - age
    return str(birthYear)


def calRank(grade):
    grade = grade.upper()
    allGrade = ["A","B+","B","C+","C","D+","D","F"]
    if grade in allGrade:
        match grade:
            case "A":
                return "High Distinction"
            case "B" | "B+":
                return "Distinction"
            case "C" | "C+":
                return "Good"
            case "D" | "D+":
                return "Normal"
            case _:
                return "Failed"
    else :
        return ValueError


def ShowEditedData(file):
    content = file.read()
    data_list = content.splitlines()

    my_list = []
    my_dict = {}

    #put in list
    for i in data_list:
        line = i.split(":")
        for data in line:
            my_list.append(data.strip())
    #make dict
    for i in range(0, len(my_list), 2):
        my_dict[my_list[i]] = my_list[i + 1]

    for i in my_dict:
            match i.lower():
                case "name":
                    print("Name : " + my_dict.get(i))
                case "age" :
                    print("BuddhistEra : " + calAge(my_dict.get(i)))
                case "software testing grade":
                    print("Software Testing Rank : " + calRank(my_dict.get(i)))
                case _:
                    print(f"this function can't read this data name \" {i} \".")


file = open("lab.txt","r")
ShowEditedData(file)