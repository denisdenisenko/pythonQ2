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
    print("-"*75)



def negative_corona_per_cough():
    print("Number of negative to Covid-19 people by cough")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('cough')['cough'].count())
    print("-"*75)



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
    print("-"*75)

    # Calculating the percentage of cough as indicator
    cough_as_indicator_in_positive_covid = ((positive_with_cough / number_of_positive_who_tested) * 100)
    print("Percentage of people with cough who diagnosed with Covid-19")
    print("%.2f" % cough_as_indicator_in_positive_covid + " %")
    cough_as_indicator_in_negative_covid = ((negative_with_cough / number_of_negative_who_tested) * 100)
    print("Percentage of people with cough who NOT diagnosed with Covid-19")
    print("%.2f" % cough_as_indicator_in_negative_covid + " %")
    print("-"*75)


    if cough_as_indicator_in_positive_covid > 70.0 and cough_as_indicator_in_negative_covid <= 30.0:
        print("Cough by itself  is a good indicator if someone having a COVID-19")
    else:
        print("Cough by itself not a good indicator if someone having a COVID-19")


def positive_corona_per_fever():
    print("Number of positive to Covid-19 people by fever")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('fever')['fever'].count())
    print("-"*75)



def negative_corona_per_fever():
    print("Number of negative to Covid-19 people by fever")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('fever')['fever'].count())
    print("-"*75)



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
    print("-"*75)

    # Calculating the percentage of cough as indicator
    fever_as_indicator_in_positive_covid = ((positive_with_fever / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with fever who diagnosed with Covid-19")
    print("%.2f" % fever_as_indicator_in_positive_covid + " %")
    fever_as_indicator_in_negative_covid = ((negative_with_fever / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with fever who NOT diagnosed with Covid-19")
    print("%.2f" % fever_as_indicator_in_negative_covid + " %")
    print("-"*75)


    if fever_as_indicator_in_positive_covid > 70.0 and fever_as_indicator_in_negative_covid <= 30.0:
        print("Fever by itself is a good indicator if someone having having a COVID-19")
    else:
        print("Fever by itself is not a good indicator if someone having a COVID-19")


def positive_corona_per_sore_throat():
    print("Number of positive to Covid-19 people by Sore Throat")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('sore_throat')['sore_throat'].count())
    print("-"*75)



def negative_corona_per_sore_throat():
    print("Number of negative to Covid-19 people by Sore Throat")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('sore_throat')['sore_throat'].count())
    print("-"*75)



def sore_throat_as_indicator():
    print('\n Q3 - Sore Throat as indicator \n')

    # Extracting the amount of people with covid and have cough
    positive_corona_sore_throat_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('sore_throat')['sore_throat'].count()
    positive_with_sore_throat = positive_corona_sore_throat_data_frame[1]
    # Extracting the amount of people without covid and have cough
    negative_corona_sore_throat_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('sore_throat')['sore_throat'].count()
    negative_with_sore_throat = negative_corona_sore_throat_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with Sore throat:", positive_with_sore_throat, "Negative to Covid people with Sore throat:",
          negative_with_sore_throat)
    print("-"*75)

    # Calculating the percentage of cough as indicator
    sore_throat_as_indicator_in_positive_covid = ((positive_with_sore_throat / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with Sore throat who diagnosed with Covid-19")
    print("%.2f" % sore_throat_as_indicator_in_positive_covid + " %")
    sore_throat_as_indicator_in_negative_covid = ((negative_with_sore_throat / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with Sore throat who NOT diagnosed with Covid-19")
    print("%.2f" % sore_throat_as_indicator_in_negative_covid + " %")
    print("-"*75)

    if sore_throat_as_indicator_in_positive_covid > 70.0 and sore_throat_as_indicator_in_negative_covid <= 30.0:
        print("Sore Throat by itself is a good indicator if someone having a COVID-19")
    else:
        print("Sore Throat by itself is not a good indicator if someone having a COVID-19")


def positive_corona_per_shortness_of_breath():
    print("Number of positive to Covid-19 people by Shortness of breath")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('shortness_of_breath')['shortness_of_breath'].count())
    print("-"*75)



def negative_corona_per_shortness_of_breath():
    print("Number of negative to Covid-19 people by Shortness of breath")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('shortness_of_breath')['shortness_of_breath'].count())
    print("-"*75)



def shortness_of_breath_as_indicator():
    print('\n Q3 - Shortness of breath as indicator \n')

    # Extracting the amount of people with covid and have cough
    positive_corona_shortness_of_breath_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('shortness_of_breath')['shortness_of_breath'].count()
    positive_with_shortness_of_breath = positive_corona_shortness_of_breath_data_frame[1]
    # Extracting the amount of people without covid and have cough
    negative_corona_shortness_of_breath_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('shortness_of_breath')['shortness_of_breath'].count()
    negative_with_shortness_of_breath = negative_corona_shortness_of_breath_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with Shortness of breath:", positive_with_shortness_of_breath, "Negative to Covid people with Shortness of breath:",
          negative_with_shortness_of_breath)
    print("-"*75)

    # Calculating the percentage of cough as indicator
    shortness_of_breath_as_indicator_in_positive_covid = ((positive_with_shortness_of_breath / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with Shortness of breath who diagnosed with Covid-19")
    print("%.2f" % shortness_of_breath_as_indicator_in_positive_covid + " %")
    shortness_of_breath_as_indicator_in_negative_covid = ((negative_with_shortness_of_breath / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with Shortness of breath who NOT diagnosed with Covid-19")
    print("%.2f" % shortness_of_breath_as_indicator_in_negative_covid + " %")
    print("-"*75)

    if shortness_of_breath_as_indicator_in_positive_covid > 70.0 and shortness_of_breath_as_indicator_in_negative_covid <= 30.0:
        print("Shortness of breath by itself is a good indicator if someone having a COVID-19")
    else:
        print("Shortness of breath by itself is not a good indicator if someone having a COVID-19")


positive_corona_per_shortness_of_breath()
negative_corona_per_shortness_of_breath()
shortness_of_breath_as_indicator()