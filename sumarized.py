import pandas as pd
import os

def sumarize_data():

    csv_files = os.listdir('phones_csv')

    for file in csv_files:

        path = os.path.join('phones_csv', file)

        df = pd.read_csv(path)

        # get average value, mean, and something
        # check if any new finds from today are bellow average, highligth them
        # create new csv file (with great deals)
        # check wheter or not value you want to wright exists
        # create REST API out of this???

        