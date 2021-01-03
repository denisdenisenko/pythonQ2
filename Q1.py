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
    """
    printing all subjects average score
    :return:
    """
    print("This is an average score by courses")
    print("- -" * 30)
    print("The mean of JAVA is : ", "%.2f" % data_frame[JAVA].mean())
    print("The mean of Python is : ", "%.2f" % data_frame[PYTHON].mean())
    print("The mean of Physics is : ", "%.2f" % data_frame[PHYSICS].mean())
    print("The mean of Math is : ", "%.2f" % data_frame[MATH].mean())


def print_all_maximum_grades():
    """
    printing all subjects maximum score
    :return:
    """
    print("This is an maximum score by courses")
    print("- -" * 30)
    print("The maximum grade of JAVA is : ", "%.2f" % data_frame[JAVA].max())
    print("The maximum grade of Python is : ", "%.2f" % data_frame[PYTHON].max())
    print("The maximum grade of Physics is : ", "%.2f" % data_frame[PHYSICS].max())
    print("The maximum grade of Math is : ", "%.2f" % data_frame[MATH].max())


def print_all_id_failed_java():
    """
    printing all ID's who failed java (had score of less or equal than 59)
    :return:
    """
    failed_java_exam = data_frame.Java <= 59
    print("The ID's who failed Java exam")
    print("- -" * 30)
    print(data_frame[ID][failed_java_exam])


def adding_average_of_programming():
    """
    adding column that represent average score of programming courses
    :return: data frame object
    """
    data_frame[AVERAGE_PROGRAMMING] = (data_frame[JAVA] + data_frame[PYTHON]) / 2
    return data_frame


# Updating the data_frame after adding colum
data_frame = adding_average_of_programming()


def print_id_with_best_programming_average():
    """
    printing the ID's with best average score in programming
    :return:
    """
    average_programming = (data_frame.AvgProgramming == data_frame.AvgProgramming.max())

    print("The ID's who has best programming average ")
    print("- -" * 30)
    print(data_frame[ID][average_programming])


def adding_average_of_physics_and_math():
    """
    adding column that represent average score of physics combined with math courses
    :return: data frame object
    """
    data_frame[AVERAGE_PHYSMATH] = (data_frame[PHYSICS] + data_frame[MATH]) / 2
    return data_frame


# Updating the data_frame after adding colum
data_frame = adding_average_of_physics_and_math()


def adding_average_grade_70_30():
    """
    adding column that represent average score of programming courses
    and phys/math corses by calculating 70/30 rule
    :return: data frame object
    """
    data_frame[AVERAGE_PROG_PSYMATH] = ((data_frame[AVERAGE_PROGRAMMING] * 0.7) + (data_frame[AVERAGE_PHYSMATH] * 0.3))
    return data_frame


# Updating the data_frame after adding colum
data_frame = adding_average_grade_70_30()


def print_sorted_data_frame():
    """
    printing the sorted column of programming/phys/math dataframe
    that was calculated by 70/30 rule before
    :return:
    """
    print("This is a sorted average data frame by 70/30 rule ")
    print("- -" * 30)
    print(data_frame.sort_values(by=[AVERAGE_PROG_PSYMATH], ascending=False))


def print_java_math_grade():
    """
    printing the ID's who got score of 80 at Java and less than 70 at math.
    :return:
    """
    print("The ID's who got 80 + at Java and 70 - at Math")
    print("- -" * 30)
    print(data_frame.loc[(data_frame[JAVA] >= 80) & (data_frame[MATH] <= 70), [ID]])


def print_the_average_of_all_classes():
    """
    printing the average score off all students in all courses
    :return:
    """
    print("The average of all student's grades is: ")
    print(((data_frame[JAVA].mean()) + data_frame[PYTHON].mean() + (data_frame[PHYSICS].mean()) + (
        data_frame[MATH].mean())) / 4)


def adding_averages_of_all_students():
    """
    adding a column of average score for each student at all couses together
    :return: data frame object
    """
    data_frame[AVERAGE_GRADE] = (data_frame[JAVA] + data_frame[PYTHON] + data_frame[PHYSICS] + data_frame[MATH]) / 4
    return data_frame


# Updating the data_frame after adding colum
data_frame = adding_averages_of_all_students()


def printing_averages_of_all_students():
    """
    printing the average score of each student
    :return:
    """
    print("The average grades are:")
    print("- -" * 30)
    print(data_frame[[ID, AVERAGE_GRADE]])


def printing_average_by_region():
    """
    printing the average score by region
    :return:
    """
    print("The averages by regions are: ")
    print("- -" * 30)
    print(data_frame.groupby(REGION)[AVERAGE_GRADE].mean())


def printing_average_by_gender():
    """
    printing the average score by gender
    :return:
    """
    print("The averages by gender are: ")
    print("- -" * 30)
    print(data_frame.groupby(GENDER)[AVERAGE_GRADE].mean())
    gender_dataframe = data_frame.groupby(GENDER)[AVERAGE_GRADE].mean()
    print("- -" * 30)
    print("{} has the better average, and its {} ".format(gender_dataframe.index.values[0], gender_dataframe.iloc[0],
                                                          sep='\n'))


print(data_frame)
print("- -" * 30)
print_all_averages()
print("- -" * 30)
print_all_maximum_grades()
print("- -" * 30)
print_all_id_failed_java()
adding_average_of_programming()
print("- -" * 30)
print_id_with_best_programming_average()
adding_average_of_physics_and_math()
adding_average_grade_70_30()
print("- -" * 30)
print_sorted_data_frame()
print("- -" * 30)
print_java_math_grade()
print("- -" * 30)
print_the_average_of_all_classes()
adding_averages_of_all_students()
print("- -" * 30)
printing_averages_of_all_students()
print("- -" * 30)
printing_average_by_region()
print("- -" * 30)
printing_average_by_gender()
print("- -" * 30)
