import pandas as pd 
import re
import os

from table import*

        
def evaluate_model(filename):

    path = os.path.join("phones_csv", filename)

    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku {filename}: {e}")
        return

    for index, row in df.iterrows():
        title = row['title']

        if 'OLX' in filename:
            phone = {
                "link": row['link'],
                "title": title,
                "price": row['price'],
                "scrape_date" : row['scrape_date'],
                "time_location": row["time_location"],
                "id": row['id']
            }
        else:
            phone = {
                "link": row['link'],
                "title": title,
                "price": row['price'],
                "scrape_date" : row['scrape_date'],
                "id": None,
                "time_location": None
            }

        base_name = re.match(r"^(.*?)_list_(OLX|fb)", filename).group(0)
        if 'pro' in title.lower() and '128gb' in title.lower().replace(" ", ""):
            new_filename = f"{base_name}_128GB_PRO.csv"
        elif 'pro' in title.lower() and '256gb' in title.lower().replace(" ", ""):
            new_filename = f"{base_name}_256GB_PRO.csv"
        elif 'pro' not in title.lower() and '128gb' in title.lower().replace(" ", ""):
            new_filename = f"{base_name}_128GB.csv"
        elif 'pro' not in title.lower() and '256gb' in title.lower().replace(" ", ""):
            new_filename = f"{base_name}_256GB.csv"
        else:
            continue

        print(f"Zapisuję do pliku {new_filename}: {phone['title']}")
        addTable(phone, new_filename)

    print("Przetwarzanie zakończone.")



