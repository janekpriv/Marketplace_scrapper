import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from visuailzations import *
from table import *

from olx_search import olxSearcher

def main():
    #Iphone 11 scrape:
    iphone11 = olxSearcher(
        OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-11/?search%5Border%5D=created_at:desc",
        OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-11/?page=2&search%5Border%5D=created_at%3Adesc",
        MAXPRICE=900,
        MINPRICE=200, #this helps filter all accesories
        PHONE_NAME="iphone 11" # this is case insesitive
    )

    iphone11_list = iphone11.getPhonesinfo()   
    df = createTable(iphone11_list, "iphone_11_list.csv")
    visualizeTableBar(df,"iphone11")
    visualizeTableBubles(df,"iphone_11")






if __name__=="__main__":
    main()
