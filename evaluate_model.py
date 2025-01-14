import pandas as pd 
import re
import os

from table import*


def evaluate_model(filename):

    #TODO
    #loads file from phones_csv
    #selects title column 
    #extracts model number from filename using re 
    #goes through every row and checks what memory if any is specified in file
    #checks whether or not phone is a pro model or not
    #chceck if filename+model and storage csv file exists -> if not create one and write to it 
    #remove that row from original filename 

    #TO REMEBER 
    #need to change filenames in send_message, or not?????

    #call in main 
    phone_list = []

    path = os.path.join("phones_csv", filename)

    df = pd.read_csv(path)

    for index, row in df.iterrows():
        title = row['title']
        olx = False
        if 'OLX' in filename:
            phone = {
                "link": row['link'],
                "title" : title,
                "price" : row['price'],
                "time_location" : row["time_location"],
                "id" : row['id'] # for database purpouses
            }
            olx = True
        else:
            phone = {
                "link": row['link'],
                "title" : title,
                "price" : row['price'],
                "id" :None,
                "time_location":None
            }

        phone_list.append(phone)
        #chceck parameters
        # 256 128 64 PRO
        new_filename = str(re.match(r"^(.*?)_list", filename).group(0))
        print(new_filename)

        if olx == True:
            new_filename = f"{new_filename}_OLX_"
        else:
            new_filename = f"{new_filename}_fb_"

        if 'pro' in title.lower() and ('128gb' in title.lower() or '128 gb' in title.lower()):
            new_filename = f"{new_filename}128GB_PRO.csv"
            createTable(phone_list, new_filename)
            df.drop(index=index)

        elif 'pro' in title.lower() and ('256gb' in title.lower() or '256 gb' in title.lower()):
            new_filename = f"{new_filename}256GB_PRO.csv"
            createTable(phone_list, new_filename)
            df.drop(index=index)

        elif 'pro' not in title.lower() or ('128gb' in title.lower() or '128 gb' in title.lower()):
            new_filename = f"{new_filename}128GB.csv"
            createTable(phone_list, new_filename)
            df.drop(index=index)

        elif 'pro' not in title.lower() and ('256gb' in title.lower() or '256 gb' in title.lower()):
            new_filename = f"{new_filename}256GB.csv"
            createTable(phone_list, new_filename)
            df.drop(index=index)
          
    df = df.reset_index(drop=True)

    df.to_csv(path, index=False)
        


    





    





    pass


