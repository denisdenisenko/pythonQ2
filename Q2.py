import pandas as pd

data_frame = pd.read_csv("./corona_tested_individuals_short.csv")


def positive_corona_per_cough():
    print(data_frame['cough'].value_counts())


positive_corona_per_cough()
