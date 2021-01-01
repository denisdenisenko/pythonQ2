import pandas as pd

data_frame = pd.read_csv("./corona_tested_individuals_short.csv")
POSITIVE = 'חיובי'
NEGATIVE = 'שלילי'
RESULT = 'corona_result'


# --------------Maybe usefull for further research ----

# print(data_frame['cough'].value_counts())
# print(data_frame[['cough','corona_result']])
# print(data_frame.groupby('cough')[RESULT].count())
# print(data_frame.groupby('cough')[RESULT].count())


# print(number_of_positive_who_tested)

# # Number of people without cough
# positive_without = (len(data_frame.groupby(['cough']).groups[0]))
# # Number of people with cough
# positive_with = (len(data_frame.groupby(['cough']).groups[1]))
#
# # Number of people without cough
# negative_without = (len(data_frame.groupby(['cough']).groups[0]))
# # Number of people with cough
# negative_with = (len(data_frame.groupby(['cough']).groups[1]))
#
# # Number of people without cough
# tested_with_cough = (len(data_frame.groupby(['cough']).groups[0]))
# # Number of people with cough
# tested_without_cough = (len(data_frame.groupby(['cough']).groups[1]))


# -------------------------------------------------------


def positive_corona_per_cough():
    print("Number of positive to Covid-19 people by cough")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('cough')['cough'].count())


def negative_corona_per_cough():
    print("Number of negative to Covid-19 people by cough")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('cough')['cough'].count())


def cough_as_indicator():
    print(data_frame.groupby(RESULT).count())
    # Gives a number of positive to COVID individuals
    number_of_positive_who_tested = data_frame[data_frame[RESULT] == POSITIVE].shape[0]
    number_of_negative_who_tested = data_frame[data_frame[RESULT] == NEGATIVE].shape[0]

    # Extracting the amount of people with covid and have cough
    positive_corona_cough_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('cough')['cough'].count()
    positive_with_cough = positive_corona_cough_data_frame[1]
    # Extracting the amount of people without covid and have cough
    negative_corona_cough_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('cough')['cough'].count()
    negative_with_cough = negative_corona_cough_data_frame[1]



    cough_as_indicator_in_positive_covid = ((positive_with_cough / number_of_positive_who_tested) * 100)
    print("%.2f" % cough_as_indicator_in_positive_covid + " %")
    cough_as_indicator_in_negative_covid = ((negative_with_cough / number_of_negative_who_tested) * 100)
    print("%.2f" % cough_as_indicator_in_negative_covid + " %" )
    print(positive_with_cough, negative_with_cough)
    print(number_of_positive_who_tested, number_of_negative_who_tested)


positive_corona_per_cough()
negative_corona_per_cough()
cough_as_indicator()
