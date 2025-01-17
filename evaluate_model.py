import pandas as pd 
import re
import os

from table import*


def evaluate_model(filename):


    

    path = os.path.join("phones_csv", filename)

    df = pd.read_csv(path)

    for index, row in df.iterrows():

        title = row['title']
        if 'OLX' in filename:
            phone = {
                "link": row['link'],
                "title" : title,
                "price" : row['price'],
                "time_location" : row["time_location"],
                "id" : row['id'] # for database purpouses
            }
        else:
            phone = {
                "link": row['link'],
                "title" : title,
                "price" : row['price'],
                "id" :None,
                "time_location":None
            }
        #chceck parameters
        # 256 128 64 PRO
        new_filename = str(re.match(r"^(.*?)_list_(OLX|fb)", filename).group(0))

        
        

        if 'pro' in title.lower() and '128gb' in title.lower().replace(" ", ""):
            new_filename = f"{new_filename}_128GB_PRO.csv"
            addTable(phone, new_filename)
            print(f"1zapisuje  do pliku{new_filename} tytuł:\n{phone['title']}")
            df = df.drop(index=index)

        elif 'pro' in title.lower() and '256gb' in title.lower().replace(" ", ""):
            new_filename = f"{new_filename}_256GB_PRO.csv"
            print(f"2zapisuje  do pliku{new_filename} tytuł:\n{phone['title']}")
            addTable(phone, new_filename)
            df = df.drop(index=index)

        elif 'pro' not in title.lower() and '128gb' in title.lower().replace(" ", ""):
            new_filename = f"{new_filename}_128GB.csv"
            print(f"3zapisuje  do pliku{new_filename} tytuł:\n{phone['title']}")
            addTable(phone, new_filename)
            df = df.drop(index=index)

        elif 'pro' not in title.lower() and '256gb' in title.lower().replace(" ", ""):
            new_filename = f"{new_filename}_256GB.csv"
            print(f"4zapisuje  do pliku{new_filename} tytuł:\n{phone['title']}")
            addTable(phone, new_filename)
            df = df.drop(index=index)
          
    df = df.reset_index(drop=True)

    df.to_csv(path, index=False)
        



