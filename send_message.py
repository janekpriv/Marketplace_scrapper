import requests
import os
import pandas as pd

def sendMsg(dataframe_list):





    filename_list=[
        "iphone_11_list_OLX.csv",
        "iphone_11_list_fb.csv",
        "iphone_13_list_OLX.csv",
        "iphone_13_list_fb.csv",
        "iphone_14_list_OLX.csv",
        "iphone_14_list_fb.csv",
        "iphone_15_list_OLX.csv",
        "iphone_15_list_fb.csv",
        "iphone_16_list_OLX.csv",
        "iphone_16_list_fb.csv"
    ]

    SERVER_API = "https://discord.com/api/v9/channels/1326608051154849833/messages"
    
    headers = {
        "authorization": "NDg5MTE4ODEzMTIwMzY0NTU1.GZH0bz.MLCOquvpF-503oTyPPbxo8EJfwvxJZ4Bc_p3hk"
    }

    # for filename in filename_list:
    #     message =""
    #     path = os.path.join("phones_csv", filename)
    #     df=pd.read_csv(path)
    #     sorted_pd = df.sort_values(by='price')
    #     sorted_pd = sorted_pd.reset_index(drop=True)
    #     cheapest = sorted_pd.head(3)

    #     for i, price in cheapest.iterrows():

    #         message +=f"{i}. {price['title']} \n   {price['price']} \n   {price['link']} \n \n" 
        
    #     message+=f"from file: {filename}"
    #     payload ={
    #         "content": message
    #     }
    #     response = requests.post(SERVER_API, payload, headers=headers)
    

    for df in dataframe_list:
        message =""

        sorted_pd = df.sort_values(by='price')
        sorted_pd = sorted_pd.reset_index(drop=True)
        cheapest = sorted_pd.head(3)

        for i, price in cheapest.iterrows():

            message +=f"{i}. {price['title']} \n   {price['price']} \n   {price['link']} \n \n" 
        
        message+=f"from dataframe: {df}"
        payload ={
            "content": message
        }
        response = requests.post(SERVER_API, payload, headers=headers)


