import os
import pandas as pd


def createTable(phones_list, filename):

    path = os.path.join("phones_csv", filename)

    if os.path.exists(path):
        existing_df = pd.read_csv(path)
        print(existing_df)
        exit
    else:
        if "fb" in filename:
            existing_df = pd.DataFrame(
                columns=["title","price","link"]
            )
        else:
            existing_df = pd.DataFrame(
                columns=["title","price","id","link","time_location"]
            )


    if "fb" in filename:
        data ={
            "title" : [phone['title'] for phone in phones_list ],
            "price" : [phone['price']for phone in phones_list],
            "link" : [phone['link'] for phone in phones_list]
        }
    else:
        data = {
            "title" : [phone['title'] for phone in phones_list ],
            "price" : [phone['price']for phone in phones_list],
            "id" : [phone['id']for phone in phones_list],
            "link" : [phone['link'] for phone in phones_list],
            "time_location" : [phone['time_location'] for phone in phones_list ] 
        }

    new_df = pd.DataFrame(data)

    new_df['scrape_date'] = pd.Timestamp.now().date()


    merged_df = pd.concat([existing_df, new_df], ignore_index=True)
    if "fb" in filename:
       merged_df = merged_df.drop_duplicates(subset='title', keep='first')
       pass
    else :
        merged_df = merged_df.drop_duplicates(subset='id', keep='first')
    

    merged_df=merged_df.reset_index(drop=True)

    merged_df['price'] = pd.to_numeric(merged_df['price'], errors='coerce')
    merged_df = merged_df.dropna(subset=['price'])
 
    merged_df.to_csv(path, index=False)
    return merged_df


def addTable(phone, filename):


    path = os.path.join("phones_csv", filename)

    if os.path.exists(path) and os.path.getsize(path) > 0: 
        try:
            existing_df = pd.read_csv(path)
        except Exception as e:
            print(f"Błąd podczas odczytu pliku {filename}: {e}")
            existing_df = pd.DataFrame()
    else:

        if "fb" in filename:
            existing_df = pd.DataFrame(columns=["title", "price", "link", "scrape_date"])
        else:
            existing_df = pd.DataFrame(columns=["title", "price", "id", "link", "time_location", "scrape_date"])

    if "fb" in filename:
        data = {
            "title": phone['title'],
            "price": phone['price'],
            "link": phone['link'],
            "scrape_date" : phone['scrape_date']
        }
    else:
        data = {
            "title": phone['title'],
            "price": phone['price'],
            "id": phone['id'],
            "link": phone['link'],
            "scrape_date" : phone['scrape_date'],
            "time_location": phone['time_location']
        }


    new_df = pd.DataFrame([data])


    merged_df = pd.concat([existing_df, new_df], ignore_index=True)

    merged_df = merged_df.drop_duplicates()

    merged_df['price'] = pd.to_numeric(merged_df['price'], errors='coerce')
    merged_df = merged_df.dropna(subset=['price'])


    try:
        merged_df.to_csv(path, index=False)
    except Exception as e:
        print(f"Błąd podczas zapisywania do pliku {filename}: {e}")

    return merged_df
