import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from visuailzations import *
from table import *
from send_message import *

from olx_search import olxSearcher
from facebook import FacebookSearcher
from evaluate_model import *

def main():

    dataframe_list = []

    csv_files = os.listdir('phones_csv')


    #Iphone 11 scrape:
    print("Choose mode:")
    print("1- visualization only")
    print("2 - only gathering data")
    print("0 - both (default)")

    inpt = int(input(""))

    if inpt == 1:
        Visualizations(csv_files)
    elif inpt == 2:
        FbSearch()
        OlxSearch()
    elif inpt == 0:

        #FbSearch()
        OlxSearch()
        Visualizations(csv_files)

    elif inpt == 4:
        sendMsg()
    elif inpt == 6:
        for file in csv_files:
            print(file)
            evaluate_model(file)
    elif inpt == 7:
        print(csv_files)
    else:
        print("Default")
        FbSearch()
        OlxSearch()
        sendMsg()
 

def OlxSearch():
    iphone11OLX = olxSearcher(
    OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-11/?search%5Border%5D=created_at:desc",
    OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-11/?page=2&search%5Border%5D=created_at%3Adesc",
    MAXPRICE=4000,
    MINPRICE=200, #this helps filter all accesories
    PHONE_NAME="iphone 11" # this is case insesitive
    )
    
    iphone11_list_OLX = iphone11OLX.getPhonesinfo()   
    df_olx_11 = createTable(iphone11_list_OLX, "iphone_11_list_OLX.csv")
   # dataframe_list.append(df_olx_11)

    iphone13OLX = olxSearcher(
        OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-13/?search%5Border%5D=created_at:desc",
        OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-13/?page=2&search%5Border%5D=created_at%3Adesc",
        MAXPRICE=4000,
        MINPRICE=200, #this helps filter all accesories
        PHONE_NAME="iphone 13" # this is case insesitive
    )
    
    iphone13_list_OLX = iphone13OLX.getPhonesinfo()   
    df_olx_13 = createTable(iphone13_list_OLX, "iphone_13_list_OLX.csv")
    #dataframe_list.append(df_olx_13)

    iphone14OLX = olxSearcher(
        OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-14/?search%5Border%5D=created_at:desc",
        OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-14/?page=2&search%5Border%5D=created_at%3Adesc",
        MAXPRICE=4000,
        MINPRICE=200, #this helps filter all accesories
        PHONE_NAME="iphone 14" # this is case insesitive
    )
    
    iphone14_list_OLX = iphone14OLX.getPhonesinfo()   
    df_olx_14 = createTable(iphone14_list_OLX, "iphone_14_list_OLX.csv")    
    #dataframe_list.append(df_olx_14)

    iphone15OLX = olxSearcher(
        OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-15/?search%5Border%5D=created_at:desc",
        OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-15/?page=2&search%5Border%5D=created_at%3Adesc",
        MAXPRICE=4000,
        MINPRICE=200, #this helps filter all accesories
        PHONE_NAME="iphone 15" # this is case insesitive
    )    
    
    iphone15_list_OLX = iphone15OLX.getPhonesinfo()   
    df_olx_15 = createTable(iphone15_list_OLX, "iphone_15_list_OLX.csv")    
    #dataframe_list.append(df_olx_15)
    
    iphone16OLX = olxSearcher(
        OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-16/?search%5Border%5D=created_at:desc",
        OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-16/?page=2&search%5Border%5D=created_at%3Adesc",
        MAXPRICE=4000,
        MINPRICE=200, #this helps filter all accesories
        PHONE_NAME="iphone 16" # this is case insesitive
    )
    #dataframe_list.append(df_olx_16)
    
    iphone16_list_OLX = iphone16OLX.getPhonesinfo()   
    df_olx_16 = createTable(iphone16_list_OLX, "iphone_16_list_OLX.csv")    

    #return dataframe_list

def FbSearch():
    iphone11FB = FacebookSearcher(
    product="iphone 11"
    )
    
    iphone11_list = iphone11FB.getProductsInfo()
    df_fb_11 = createTable(iphone11_list, "iphone_11_list_fb.csv")
    #dataframe_list.append(df_fb_11)

    iphone14FB = FacebookSearcher(
        product="iphone 14"
    )
    

    iphone14_list = iphone14FB.getProductsInfo()
    df_fb_14 = createTable(iphone14_list, "iphone_14_list_fb.csv")    
    #dataframe_list.append(df_fb_14)
    iphone15FB = FacebookSearcher(
        product="iphone 15"
    )
    
    iphone15_list = iphone15FB.getProductsInfo()
    df_fb_15 = createTable(iphone15_list, "iphone_15_list_fb.csv")
    #dataframe_list.append(df_fb_15)
    iphone16FB = FacebookSearcher(
        product="iphone 16"
    )
    
    iphone16_list = iphone16FB.getProductsInfo()
    df_fb_16 = createTable(iphone16_list, "iphone_16_list_fb.csv")    
    #dataframe_list.append(df_fb_16)
    iphone13FB = FacebookSearcher(
        product="iphone 13"
    )
    
    iphone13_list = iphone13FB.getProductsInfo()
    df_fb_13 = createTable(iphone13_list, "iphone_13_list_fb.csv")
    #dataframe_list.append(df_fb_13)


def Visualizations(list):
    # visualizations ------------------------------------
    # Grouped by phone type
    #Iphone11



    for file in list:
        print(type(file))
        print(file)
        phone_name = file.replace("list_","").replace(".csv","")
        print(phone_name)
        visualizeALL(file, phone_name)



    # visualizeALL("iphone_11_list_OLX.csv","iphone11_olx") 
    # visualizeALL("iphone_11_list_fb.csv","iphone11_fb")
   
    # #Iphone 13
    # visualizeALL("iphone_13_list_OLX.csv","iphone13_olx")
    # visualizeALL("iphone_13_list_fb.csv","iphone13_fb")

    # #Iphone 14
    # visualizeALL("iphone_14_list_OLX.csv","iphone14_olx")
    # visualizeALL("iphone_14_list_fb.csv","iphone14_fb")

    # #Iphone 15   
    # visualizeALL("iphone_15_list_OLX.csv","iphone15_olx")
    # visualizeALL("iphone_15_list_fb.csv","iphone15_fb")

    # #Iphone 16
    # visualizeALL("iphone_16_list_OLX.csv","iphone16_olx")
    # visualizeALL("iphone_16_list_fb.csv","iphone16_fb")




    
    

if __name__=="__main__":
    main()
