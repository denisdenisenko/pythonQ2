import pandas as pd

data_frame = pd.read_csv("./Students.csv")

# Final variables, they are the column names
ID = "ID"
GENDER = "Gender"
JAVA = "Java"
PYTHON = "Python"
PHYSICS = "Physics"
MATH = "Math"
REGION = "Region"
AVERAGE_PROGRAMMING = "AvgProgramming"
AVERAGE_PHYSMATH = "AvgPhysMath"
AVERAGE_PROG_PSYMATH = "AvgGrade_70_30"
AVERAGE_GRADE = "AverageGrade"


def print_all_averages():
    print("The mean of JAVA is : ", data_frame[JAVA].mean())
    print("The mean of Python is : ", data_frame[PYTHON].mean())
    print("The mean of Physics is : ", data_frame[PHYSICS].mean())
    print("The mean of Math is : ", data_frame[MATH].mean())


def print_all_maximum_gades():
    print("The maximum grade of JAVA is : ", data_frame[JAVA].max())
    print("The maximum grade of Python is : ", data_frame[PYTHON].max())
    print("The maximum grade of Physics is : ", data_frame[PHYSICS].max())
    print("The maximum grade of Math is : ", data_frame[MATH].max())


def print_all_id_failed_java():
    failed_java_exam = data_frame.Java <= 59
    print(" \n The ID's who failed Java exam \n")
    print(data_frame[ID][failed_java_exam])


def adding_average_of_programming():
    data_frame[AVERAGE_PROGRAMMING] = (data_frame[JAVA] + data_frame[PYTHON]) / 2
    return data_frame


data_frame = adding_average_of_programming()


def print_id_with_best_programming_average():
    average_programming = (data_frame.AvgProgramming == data_frame.AvgProgramming.max())

    print(" \n The ID's who has best programming average ")
    print(data_frame[ID][average_programming])


def adding_average_of_physics_and_math():
    data_frame[AVERAGE_PHYSMATH] = (data_frame[PHYSICS] + data_frame[MATH]) / 2
    return data_frame


data_frame = adding_average_of_physics_and_math()


def adding_average_grade_70_30():
    data_frame[AVERAGE_PROG_PSYMATH] = ((data_frame[AVERAGE_PROGRAMMING] * 0.7) + (data_frame[AVERAGE_PHYSMATH] * 0.3))
    return data_frame


data_frame = adding_average_grade_70_30()


def print_sorted_data_frame():
    print(data_frame.sort_values(by=[AVERAGE_PROG_PSYMATH], ascending=False))


def print_java_math_grade():
    print(" \n The ID's who got 80 + at Java and 70 - at Math")
    print(data_frame.loc[(data_frame[JAVA] >= 80) & (data_frame[MATH] <= 70), [ID]])


def print_the_average_of_all_classes():
    print("The average of all student's grades is: ")
    print(((data_frame[JAVA].mean()) + data_frame[PYTHON].mean() + (data_frame[PHYSICS].mean()) + (
        data_frame[MATH].mean())) / 4)


def adding_averages_of_all_students():
    data_frame[AVERAGE_GRADE] = (data_frame[JAVA] + data_frame[PYTHON] + data_frame[PHYSICS] + data_frame[MATH]) / 4
    return data_frame


data_frame = adding_averages_of_all_students()


def printing_averages_of_all_students():
    print(" \n The average grades are: ")
    print(data_frame[[ID, AVERAGE_GRADE]])


def printing_average_by_region():
    print(" \n The averages by regions are: ")
    print(data_frame.groupby(REGION)[AVERAGE_GRADE].mean())


def printing_average_by_gender():
    print(" \n The averages by gender are: ")
    print(data_frame.groupby(GENDER)[AVERAGE_GRADE].mean())
    gender_dataframe = data_frame.groupby(GENDER)[AVERAGE_GRADE].mean()
    print("\n {} has the better average, ant its ".format(gender_dataframe.index.values[0], sep='\n'))


printing_average_by_gender()
