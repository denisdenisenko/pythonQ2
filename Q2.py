import pandas as pd

data_frame = pd.read_csv("./corona_tested_individuals_short.csv")
POSITIVE = 'חיובי'
NEGATIVE = 'שלילי'
RESULT = 'corona_result'

# Gives a number of  and negative to COVID individuals

NUMBER_OF_POSITIVE_WHO_TESTED = data_frame[data_frame[RESULT] == POSITIVE].shape[0]
NUMBER_OF_NEGATIVE_WHO_TESTED = data_frame[data_frame[RESULT] == NEGATIVE].shape[0]


# --------------Maybe usefull for further research ----

# print(data_frame['cough'].value_counts())
# print(data_frame[['cough','corona_result']])
# print(data_frame.groupby('cough')[RESULT].count())
# print(data_frame.groupby('cough')[RESULT].count())


# print(number_of_positive_who_tested)

# print(data_frame.groupby(RESULT).count())


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
    print('\n Q3 - Cough as indicator \n')

    # Extracting the amount of people with covid and have cough
    positive_corona_cough_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('cough')['cough'].count()
    positive_with_cough = positive_corona_cough_data_frame[1]
    # Extracting the amount of people without covid and have cough
    negative_corona_cough_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('cough')['cough'].count()
    negative_with_cough = negative_corona_cough_data_frame[1]

    print("Number of positive people:", number_of_positive_who_tested, "Number of negative people:",
          number_of_negative_who_tested)
    print("Positive to Covid people with cough:", positive_with_cough, "Negative to Covid people with cough:",
          negative_with_cough)
    # Calculating the percentage of cough as indicator
    cough_as_indicator_in_positive_covid = ((positive_with_cough / number_of_positive_who_tested) * 100)
    print("Percentage of people with cough who diagnosed with Covid-19")
    print("%.2f" % cough_as_indicator_in_positive_covid + " %")
    cough_as_indicator_in_negative_covid = ((negative_with_cough / number_of_negative_who_tested) * 100)
    print("Percentage of people with cough who NOT diagnosed with Covid-19")
    print("%.2f" % cough_as_indicator_in_negative_covid + " %")

    if cough_as_indicator_in_positive_covid > 70.0 and cough_as_indicator_in_negative_covid <= 30.0:
        print("Only cough is a good indicator for COVID-19")
    else:
        print("Only cough is not a good indicator for COVID-19")


def positive_corona_per_fever():
    print("Number of positive to Covid-19 people by fever")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('fever')['fever'].count())


def negative_corona_per_fever():
    print("Number of negative to Covid-19 people by fever")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('fever')['fever'].count())


def fever_as_indicator():
    print('\n Q3 - Fever as indicator \n')

    # Extracting the amount of people with covid and have cough
    positive_corona_fever_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('fever')['fever'].count()
    positive_with_fever = positive_corona_fever_data_frame[1]
    # Extracting the amount of people without covid and have cough
    negative_corona_fever_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('fever')['fever'].count()
    negative_with_fever = negative_corona_fever_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with fever:", positive_with_fever, "Negative to Covid people with fever:",
          negative_with_fever)
    # Calculating the percentage of cough as indicator
    fever_as_indicator_in_positive_covid = ((positive_with_fever / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with fever who diagnosed with Covid-19")
    print("%.2f" % fever_as_indicator_in_positive_covid + " %")
    fever_as_indicator_in_negative_covid = ((negative_with_fever / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with fever who NOT diagnosed with Covid-19")
    print("%.2f" % fever_as_indicator_in_negative_covid + " %")

    if fever_as_indicator_in_positive_covid > 70.0 and fever_as_indicator_in_negative_covid <= 30.0:
        print("Fever by itself is a good indicator for having COVID-19")
    else:
        print("Fever by itself is not a good indicator for having COVID-19")


fever_as_indicator()
