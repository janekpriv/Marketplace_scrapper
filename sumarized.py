import pandas as pd
import os
from scipy.stats import trim_mean

def sumarize_data():

    csv_files = os.listdir('phones_csv')

    path = os.path.join('stats', 'stats.csv')

    for file in csv_files:

        
        
        if os.path.exists(path):
            existing_df = pd.read_csv(path)
        else:
            existing_df = pd.DataFrame(
                columns=["filename","avg","mean","deviation","skewness"]
            )
        path_ = os.path.join('phones_csv', file) 

        df = pd.read_csv(path_)


        avg = df['price'].mean() # normal average
        deviation = df['price'].std() 
        skewness = df['price'].skew()

        mean = trim_mean(df['price'], 0.1) #mean without edge values 

        data = {
            "filename": file,
            "avg": avg,
            "mean":mean,
            "deviation" : deviation,
            "skewness" :skewness

        }


        new_df = pd.DataFrame([data])


        merged_df = pd.concat([existing_df, new_df], ignore_index=True)

        merged_df = merged_df.drop_duplicates()

        try:
            merged_df.to_csv(path, index=False)
        except Exception as e:
            print(f"Błąd podczas zapisywania do pliku {file}: {e}")
