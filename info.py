from olx_search import olxSearcher
from facebook import FacebookSearcher
from evaluate_model import *
from sumarized import *


#TODO:
#get new phones from olx
#check if phone price is less than mean - value in stats.csv
#check if it is in sent_list if not add
#if it is not send notification and send visualization(with point selected??)
#save it to table

notification_list = []

def check(phone_list):
    csv_files = os.listdir('phones_csv')
    stats_df = pd.read_csv(os.path.join('stats', 'stats.csv'))

    for file in csv_files:

        mean_price = stats_df.loc[stats_df['filename'] == file, 'mean'].values[0]


    pass






def OlxSearchTMP(filename):

    new_filename = folder_name = str(re.match(r"^(.*?)_", filename).group(0))

    if "11" in new_filename:

        iphone11OLX = olxSearcher(
        OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-11/?search%5Border%5D=created_at:desc",
        OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-11/?page=2&search%5Border%5D=created_at%3Adesc",
        MAXPRICE=4000,
        MINPRICE=200, #this helps filter all accesories
        PHONE_NAME="iphone 11" # this is case insesitive
        )
    
        iphone11_list_OLX = iphone11OLX.getPhonesinfo()   
        return iphone11_list_OLX
        df_olx_11 = createTable(iphone11_list_OLX, "iphone11_list_OLX.csv")
        #dataframe_list.append(df_olx_11)
    elif "13" in new_filename:
        iphone13OLX = olxSearcher(
            OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-13/?search%5Border%5D=created_at:desc",
            OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-13/?page=2&search%5Border%5D=created_at%3Adesc",
            MAXPRICE=4000,
            MINPRICE=200, #this helps filter all accesories
            PHONE_NAME="iphone 13" # this is case insesitive
        )
    
        iphone13_list_OLX = iphone13OLX.getPhonesinfo()   

        return iphone13_list_OLX
        df_olx_13 = createTable(iphone13_list_OLX, "iphone13_list_OLX.csv")
        #dataframe_list.append(df_olx_13)
    elif "14" in new_filename:
        iphone14OLX = olxSearcher(
            OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-14/?search%5Border%5D=created_at:desc",
            OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-14/?page=2&search%5Border%5D=created_at%3Adesc",
            MAXPRICE=4000,
            MINPRICE=200, #this helps filter all accesories
            PHONE_NAME="iphone 14" # this is case insesitive
        )
        
        iphone14_list_OLX = iphone14OLX.getPhonesinfo()   

        return iphone14_list_OLX
        df_olx_14 = createTable(iphone14_list_OLX, "iphone14_list_OLX.csv")    
        #dataframe_list.append(df_olx_14)
    elif "15" in new_filename:
        iphone15OLX = olxSearcher(
            OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-15/?search%5Border%5D=created_at:desc",
            OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-15/?page=2&search%5Border%5D=created_at%3Adesc",
            MAXPRICE=4000,
            MINPRICE=200, #this helps filter all accesories
            PHONE_NAME="iphone 15" # this is case insesitive
        )    
        
        iphone15_list_OLX = iphone15OLX.getPhonesinfo()   

        return iphone15_list_OLX
    
        df_olx_15 = createTable(iphone15_list_OLX, "iphone15_list_OLX.csv")    
        #dataframe_list.append(df_olx_15)
    elif "16" in new_filename:
        iphone16OLX = olxSearcher(
            OLX_URL_PAGE1="https://www.olx.pl/warszawa/q-iphone-16/?search%5Border%5D=created_at:desc",
            OLX_URL_PAGE2="https://www.olx.pl/warszawa/q-iphone-16/?page=2&search%5Border%5D=created_at%3Adesc",
            MAXPRICE=4000,
            MINPRICE=200, #this helps filter all accesories
            PHONE_NAME="iphone 16" # this is case insesitive
        )
        #dataframe_list.append(df_olx_16)
        
        iphone16_list_OLX = iphone16OLX.getPhonesinfo()

        return iphone16_list_OLX
        #df_olx_16 = createTable(iphone16_list_OLX, "iphone16_list_OLX")   

def FbSearch():
    iphone11FB = FacebookSearcher(
    product="iphone 11"
    )
    
    iphone11_list = iphone11FB.getProductsInfo()
    df_fb_11 = createTable(iphone11_list, "iphone11_list_fb.csv")
    #dataframe_list.append(df_fb_11)

    iphone14FB = FacebookSearcher(
        product="iphone 14"
    )
    

    iphone14_list = iphone14FB.getProductsInfo()
    df_fb_14 = createTable(iphone14_list, "iphone14_list_fb.csv")    
    #dataframe_list.append(df_fb_14)
    iphone15FB = FacebookSearcher(
        product="iphone 15"
    )
    
    iphone15_list = iphone15FB.getProductsInfo()
    df_fb_15 = createTable(iphone15_list, "iphone15_list_fb.csv")
    #dataframe_list.append(df_fb_15)
    iphone16FB = FacebookSearcher(
        product="iphone 16"
    )
    
    iphone16_list = iphone16FB.getProductsInfo()
    df_fb_16 = createTable(iphone16_list, "iphone16_list_fb.csv")    
    #dataframe_list.append(df_fb_16)
    iphone13FB = FacebookSearcher(
        product="iphone 13"
    )
    
    iphone13_list = iphone13FB.getProductsInfo()
    df_fb_13 = createTable(iphone13_list, "iphone13_list_fb.csv")
    #dataframe_list.append(df_fb_13)