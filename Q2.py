import pandas as pd

data_frame = pd.read_csv("./corona_tested_individuals_dec_2020.csv")
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
    """
    printing the number of positive to Covid - 19 people with/without cough
    :return:
    """
    print("Number of positive to Covid-19 people by cough")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('cough')['cough'].count())
    print("-" * 105)


def negative_corona_per_cough():
    """
    printing the number of negative to Covid - 19 people with/without cough
    :return:
    """
    print("Number of negative to Covid-19 people by cough")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('cough')['cough'].count())
    print("-" * 105)


def cough_as_indicator():
    """
    this function calculates if cough by itself is enough to
    say that someone has Covid-19
    :return:
    """
    print('\n  - Cough as indicator -  \n')

    # Extracting the amount of people with covid and have cough
    positive_corona_cough_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('cough')['cough'].count()
    positive_with_cough = positive_corona_cough_data_frame[1]
    # Extracting the amount of people without covid and have cough
    negative_corona_cough_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('cough')['cough'].count()
    negative_with_cough = negative_corona_cough_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with cough:", positive_with_cough, "Negative to Covid people with cough:",
          negative_with_cough)
    print("-" * 105)

    # Calculating the percentage of cough as indicator
    cough_as_indicator_in_positive_covid = ((positive_with_cough / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with cough who diagnosed with Covid-19")
    print("%.2f" % cough_as_indicator_in_positive_covid + " %")
    cough_as_indicator_in_negative_covid = ((negative_with_cough / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with cough who NOT diagnosed with Covid-19")
    print("%.2f" % cough_as_indicator_in_negative_covid + " %")
    print("-" * 105)

    if cough_as_indicator_in_positive_covid > 70.0 and cough_as_indicator_in_negative_covid <= 30.0:
        print("Cough by itself  is a good indicator to say if someone having a COVID-19")
        print("-" * 105)

    else:
        print("Cough by itself not a good indicator to say if someone having a COVID-19")
        print("-" * 105)


def positive_corona_per_fever():
    """
    printing the number of positive to Covid - 19 people with/without fever
    :return:
    """
    print("Number of positive to Covid-19 people by fever")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('fever')['fever'].count())
    print("-" * 105)


def negative_corona_per_fever():
    """
    printing the number of negative to Covid - 19 people with/without fever
    :return:
    """
    print("Number of negative to Covid-19 people by fever")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('fever')['fever'].count())
    print("-" * 105)


def fever_as_indicator():
    """
    this function calculates if fever by itself is enough to
    say that someone has Covid-19
    :return:
    """
    print('\n - Fever as indicator -  \n')

    # Extracting the amount of people with covid and have fever
    positive_corona_fever_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('fever')['fever'].count()
    positive_with_fever = positive_corona_fever_data_frame[1]
    # Extracting the amount of people without covid and have fever
    negative_corona_fever_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('fever')['fever'].count()
    negative_with_fever = negative_corona_fever_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with fever:", positive_with_fever, "Negative to Covid people with fever:",
          negative_with_fever)
    print("-" * 105)

    # Calculating the percentage of fever as indicator
    fever_as_indicator_in_positive_covid = ((positive_with_fever / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with fever who diagnosed with Covid-19")
    print("%.2f" % fever_as_indicator_in_positive_covid + " %")
    fever_as_indicator_in_negative_covid = ((negative_with_fever / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with fever who NOT diagnosed with Covid-19")
    print("%.2f" % fever_as_indicator_in_negative_covid + " %")
    print("-" * 105)

    if fever_as_indicator_in_positive_covid > 70.0 and fever_as_indicator_in_negative_covid <= 30.0:
        print("Fever by itself is a good indicator to say if someone having having a COVID-19")
        print("-" * 105)

    else:
        print("Fever by itself is not a good indicator to say if someone having a COVID-19")
        print("-" * 105)


def positive_corona_per_sore_throat():
    print("Number of positive to Covid-19 people by Sore Throat")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('sore_throat')['sore_throat'].count())
    print("-" * 105)


def negative_corona_per_sore_throat():
    print("Number of negative to Covid-19 people by Sore Throat")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('sore_throat')['sore_throat'].count())
    print("-" * 105)


def sore_throat_as_indicator():
    print('\n - Sore Throat as indicator -  \n')

    # Extracting the amount of people with covid and have sore throat
    positive_corona_sore_throat_data_frame = data_frame[data_frame[RESULT] == POSITIVE].groupby('sore_throat')[
        'sore_throat'].count()
    positive_with_sore_throat = positive_corona_sore_throat_data_frame[1]
    # Extracting the amount of people without covid and have sore throat
    negative_corona_sore_throat_data_frame = data_frame[data_frame[RESULT] == NEGATIVE].groupby('sore_throat')[
        'sore_throat'].count()
    negative_with_sore_throat = negative_corona_sore_throat_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with Sore throat:", positive_with_sore_throat,
          "Negative to Covid people with Sore throat:",
          negative_with_sore_throat)
    print("-" * 105)

    # Calculating the percentage of sore throat as indicator
    sore_throat_as_indicator_in_positive_covid = ((positive_with_sore_throat / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with Sore throat who diagnosed with Covid-19")
    print("%.2f" % sore_throat_as_indicator_in_positive_covid + " %")
    sore_throat_as_indicator_in_negative_covid = ((negative_with_sore_throat / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with Sore throat who NOT diagnosed with Covid-19")
    print("%.2f" % sore_throat_as_indicator_in_negative_covid + " %")
    print("-" * 105)

    if sore_throat_as_indicator_in_positive_covid > 70.0 and sore_throat_as_indicator_in_negative_covid <= 30.0:
        print("Sore Throat by itself is a good indicator to say if someone having a COVID-19")
        print("-" * 105)

    else:
        print("Sore Throat by itself is not a good indicator to say if someone having a COVID-19")
        print("-" * 105)


def positive_corona_per_shortness_of_breath():
    print("Number of positive to Covid-19 people by Shortness of breath")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('shortness_of_breath')['shortness_of_breath'].count())
    print("-" * 105)


def negative_corona_per_shortness_of_breath():
    print("Number of negative to Covid-19 people by Shortness of breath")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('shortness_of_breath')['shortness_of_breath'].count())
    print("-" * 105)


def shortness_of_breath_as_indicator():
    print('\n - Shortness of breath as indicator -  \n')

    # Extracting the amount of people with covid and have shortness of breath
    positive_corona_shortness_of_breath_data_frame = \
        data_frame[data_frame[RESULT] == POSITIVE].groupby('shortness_of_breath')['shortness_of_breath'].count()
    positive_with_shortness_of_breath = positive_corona_shortness_of_breath_data_frame[1]
    # Extracting the amount of people without covid and have shortness of breath
    negative_corona_shortness_of_breath_data_frame = \
        data_frame[data_frame[RESULT] == NEGATIVE].groupby('shortness_of_breath')['shortness_of_breath'].count()
    negative_with_shortness_of_breath = negative_corona_shortness_of_breath_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with Shortness of breath:", positive_with_shortness_of_breath,
          "Negative to Covid people with Shortness of breath:",
          negative_with_shortness_of_breath)
    print("-" * 105)

    # Calculating the percentage of shortness of breath as indicator
    shortness_of_breath_as_indicator_in_positive_covid = (
            (positive_with_shortness_of_breath / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with Shortness of breath who diagnosed with Covid-19")
    print("%.2f" % shortness_of_breath_as_indicator_in_positive_covid + " %")
    shortness_of_breath_as_indicator_in_negative_covid = (
            (negative_with_shortness_of_breath / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with Shortness of breath who NOT diagnosed with Covid-19")
    print("%.2f" % shortness_of_breath_as_indicator_in_negative_covid + " %")
    print("-" * 105)

    if shortness_of_breath_as_indicator_in_positive_covid > 70.0 and \
            shortness_of_breath_as_indicator_in_negative_covid <= 30.0:
        print("Shortness of breath by itself is a good indicator to say if someone having a COVID-19")
        print("-" * 105)

    else:
        print("Shortness of breath by itself is not a good indicator to say if someone having a COVID-19")
        print("-" * 105)


def positive_corona_per_head_ache():
    print("Number of positive to Covid-19 people by Head ache")
    print(data_frame[data_frame[RESULT] == POSITIVE].groupby('head_ache')['head_ache'].count())
    print("-" * 105)


def negative_corona_per_head_ache():
    print("Number of negative to Covid-19 people by Head ache")
    print(data_frame[data_frame[RESULT] == NEGATIVE].groupby('head_ache')['head_ache'].count())
    print("-" * 105)


def head_ache_as_indicator():
    print('\n - Head ache as indicator -  \n')

    # Extracting the amount of people with covid and have head ache
    positive_corona_head_ache_data_frame = \
        data_frame[data_frame[RESULT] == POSITIVE].groupby('head_ache')['head_ache'].count()
    positive_with_head_ache = positive_corona_head_ache_data_frame[1]
    # Extracting the amount of people without covid and have head ache
    negative_corona_head_ache_data_frame = \
        data_frame[data_frame[RESULT] == NEGATIVE].groupby('head_ache')['head_ache'].count()
    negative_with_head_ache = negative_corona_head_ache_data_frame[1]

    print("Number of positive people:", NUMBER_OF_POSITIVE_WHO_TESTED, "Number of negative people:",
          NUMBER_OF_NEGATIVE_WHO_TESTED)
    print("Positive to Covid people with Head ache:", positive_with_head_ache,
          "Negative to Covid people with Head ache:",
          negative_with_head_ache)
    print("-" * 105)

    # Calculating the percentage of head ache as indicator
    head_ache_as_indicator_in_positive_covid = (
            (positive_with_head_ache / NUMBER_OF_POSITIVE_WHO_TESTED) * 100)
    print("Percentage of people with Head ache who diagnosed with Covid-19")
    print("%.2f" % head_ache_as_indicator_in_positive_covid + " %")
    head_ache_as_indicator_in_negative_covid = (
            (negative_with_head_ache / NUMBER_OF_NEGATIVE_WHO_TESTED) * 100)
    print("Percentage of people with Head ache who NOT diagnosed with Covid-19")
    print("%.2f" % head_ache_as_indicator_in_negative_covid + " %")
    print("-" * 105)

    if head_ache_as_indicator_in_positive_covid > 70.0 and head_ache_as_indicator_in_negative_covid <= 30.0:
        print("Head ache by itself is a good indicator to say if someone having a COVID-19")
        print("-" * 105)

    else:
        print("Head ache by itself is not a good indicator to say if someone having a COVID-19")
        print("-" * 105)


def printing_number_of_sick_and_healthy_by_gender():
    print('\n Q5 - Number of sick by gender \n')

    print("Sick by gender")
    number_of_sick_by_gender = data_frame[data_frame[RESULT] == POSITIVE].groupby('gender')['gender'].count()
    print(number_of_sick_by_gender)
    print("-" * 105)

    number_of_healthy_by_gender = data_frame[data_frame[RESULT] == NEGATIVE].groupby('gender')['gender'].count()
    print("Healthy by gender")
    print(number_of_healthy_by_gender)
    print("-" * 105)


def printing_number_of_sick_and_healthy_by_age():
    print('\n Q6 - Number of sick by age \n')

    print("Sick by age")
    number_of_sick_by_age = data_frame[data_frame[RESULT] == POSITIVE].groupby('age_60_and_above')[
        'age_60_and_above'].count()
    print(number_of_sick_by_age)
    print("-" * 105)

    # Extracting the amount of people without covid and have fever
    number_of_healthy_by_age = data_frame[data_frame[RESULT] == NEGATIVE].groupby('age_60_and_above')[
        'age_60_and_above'].count()
    print("Healthy by age")
    print(number_of_healthy_by_age)
    print("-" * 105)


def printing_data_by_gender_age_result():
    data_by_groups = data_frame[data_frame[RESULT] == POSITIVE].groupby(['gender', 'age_60_and_above']).sum()
    pd.set_option('display.max_columns', None)
    data_by_groups.to_csv("1.csv")
    print(data_by_groups)
    print("-" * 105)

    data_by_groups.plot.hist()
    data_by_groups = data_frame[data_frame[RESULT] == NEGATIVE].groupby(['gender', 'age_60_and_above']).sum()
    pd.set_option('display.max_columns', None)
    data_by_groups.to_csv("2.csv")
    print(data_by_groups)
    print("-" * 105)


positive_corona_per_cough()
negative_corona_per_cough()
cough_as_indicator()
positive_corona_per_fever()
negative_corona_per_fever()
fever_as_indicator()
positive_corona_per_shortness_of_breath()
negative_corona_per_shortness_of_breath()
shortness_of_breath_as_indicator()
positive_corona_per_sore_throat()
negative_corona_per_sore_throat()
sore_throat_as_indicator()
positive_corona_per_head_ache()
negative_corona_per_head_ache()
head_ache_as_indicator()
printing_data_by_gender_age_result()
