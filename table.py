import os
import pandas as pd


def createTable(phones_list, filename):

    path = os.path.join("phones_csv", filename)

    if os.path.exists(path):
        #load existing csv file
        existing_df = pd.read_csv(path)
    else:
        #create empty table
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
    #create table with scraped info
    new_df = pd.DataFrame(data)

    #add scrap date to all elements in the table
    new_df['scrape_date'] = pd.Timestamp.now().date()


    #merge and remove duplicates 
    merged_df = pd.concat([existing_df, new_df], ignore_index=True)
    if "fb" in filename:
       merged_df = merged_df.drop_duplicates(subset='title', keep='first')
       pass
    else :
        merged_df = merged_df.drop_duplicates(subset='id', keep='first')
    
    #reset index
    merged_df=merged_df.reset_index(drop=True)

    #remove NAN price values -> problems with plotting later
    merged_df['price'] = pd.to_numeric(merged_df['price'], errors='coerce')
    merged_df = merged_df.dropna(subset=['price'])

    #save to file 
    merged_df.to_csv(path, index=False)
    return merged_df

def addTable(phone, filename):

    path = os.path.join("phones_csv", filename)

    if os.path.exists(path):
        #load existing csv file
        existing_df = pd.read_csv(path)
    else:
        #create empty table
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
            "title" : phone['title'],
            "price" : phone['price'],
            "link" : phone['link']
        }
    else:
        data = {
            "title" : phone['title'],
            "price" : phone['price'],
            "id" : phone['id'],
            "link" : phone['link'],
            "time_location" : phone['time_location'] 
        }


        #create table with scraped info
    new_df = pd.DataFrame([data])

    #add scrap date to all elements in the table
    new_df['scrape_date'] = pd.Timestamp.now().date()


    #merge and remove duplicates 
    merged_df = pd.concat([existing_df, new_df], ignore_index=True)
    
    #reset index
    merged_df=merged_df.reset_index(drop=True)

    #remove NAN price values -> problems with plotting later
    merged_df['price'] = pd.to_numeric(merged_df['price'], errors='coerce')
    merged_df = merged_df.dropna(subset=['price'])

    #save to file 
    merged_df.to_csv(path, index=False)
    return merged_df