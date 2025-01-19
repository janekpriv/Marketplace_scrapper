import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import os
import pandas as pd
import re 

def visualizeTableBubles(filename, phone_name):

    path = os.path.join("phones_csv", filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.read_csv(path)

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])

    price = df['price']
    index = price.index
    sizes = (df['price'] / df['price'].max()) * 300  
    colors = df['price']



    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
    index, price,
    s=sizes,           # Rozmiar bąbelków
    c=colors,          # Kolor bąbelków
    cmap='viridis',    # Kolor gradientu
    alpha=0.7,         # Przezroczystość
    edgecolors="black" # Krawędź bąbelków
    )


    
    plt.xlabel('index')
    plt.ylabel('Cena')
    plt.title(f'Cena {phone_name}')
    plt.colorbar(scatter, label='Cena')
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    plt.gca().set_facecolor('#d3d3d3')
    #plt.show()
    
    folder_name = str(re.match(r"^(.*?)_", phone_name).group(0))  

    figName =f"{phone_name}_buble_figure.png"
    savepath = os.path.join("visualizations",folder_name,figName)

    os.makedirs(os.path.dirname(savepath), exist_ok=True)

    plt.savefig(savepath)

    plt.close()

    
def visualizeTableBar(filename, phone_name):

    #df=df.tail(25)
    path = os.path.join("phones_csv", filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.read_csv(path)

    
    price = df['price']

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])

    norm = plt.Normalize(df['price'].min(), df['price'].max())  # Min = 100, Max = 1000
    colors = cm.plasma(norm(df['price']))

    plt.figure(figsize=(10,6))
    plt.bar(price.index,price, color=colors, width =0.3, label="cena")
    plt.xlabel('Nazwy ogłoszeń')
    plt.ylabel('Cena [zł]')
    plt.title(f'Ceny {phone_name}')
    plt.colorbar(cm.ScalarMappable(norm=norm, cmap='plasma'), label='Cena')
    #plt.show()

    folder_name = str(re.match(r"^(.*?)_", phone_name).group(0))  

    figName =f"{phone_name}_bar_figure.png"
    savepath = os.path.join("visualizations",folder_name,figName)

    os.makedirs(os.path.dirname(savepath), exist_ok=True)

    plt.savefig(savepath)
    plt.close()
    
def visualizeBoxPlot(filename, phone_name):

    path = os.path.join("phones_csv", filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.read_csv(path)

    
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])


    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['price'], color="orange")


    plt.title(f"Boxplot cen {phone_name}", fontsize=16)
    plt.xlabel("Cena (zł)", fontsize=12)


    plt.tight_layout()
    #plt.show()
    folder_name = str(re.match(r"^(.*?)_", phone_name).group(0))  
    figName =f"{phone_name}_box_plot_figure.png"
    savepath = os.path.join("visualizations",folder_name,figName)

    os.makedirs(os.path.dirname(savepath), exist_ok=True)

    plt.savefig(savepath)
    plt.close()

def visualizeTime(filename,phone_name):
    
    path = os.path.join("phones_csv", filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.read_csv(path)

    
    df['scrape_date'] = pd.to_datetime(df['scrape_date'])  
    df['price'] = pd.to_numeric(df['price'], errors='coerce')  
    df = df.dropna(subset=['price'])


    avg_price_by_date = df.groupby('scrape_date')['price'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=avg_price_by_date, x='scrape_date', y='price', marker='o', color='blue')

    plt.title(f"Średnia cena {phone_name} w zależności od daty", fontsize=16)
    plt.xlabel("Data zbierania danych", fontsize=12)
    plt.ylabel("Średnia cena (zł)", fontsize=12)
    plt.xticks(
        avg_price_by_date['scrape_date'],
        rotation=45,  
        fontsize=10 
    ) 
    plt.grid(True)


    plt.tight_layout()


    folder_name = str(re.match(r"^(.*?)_", phone_name).group(0))  

    # match = re.search(r"(fb|OLX)(\d+GB)?(_PRO)?", filename)
    # print(match)
    # model_folder= match.group(0)
    figName =f"{phone_name}_over_time_figure.png"
    savepath = os.path.join("visualizations",folder_name,figName)

    os.makedirs(os.path.dirname(savepath), exist_ok=True)

    plt.savefig(savepath)
    plt.close()

def visualizeHistPlot(filename, phone_name):

    path = os.path.join("phones_csv", filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    df = pd.read_csv(path)


    df['price'] = pd.to_numeric(df['price'], errors='coerce')  
    df = df.dropna(subset=['price']) 


    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], bins=20, kde=True, color='blue')


    plt.title(f"Rozkład cen {phone_name}", fontsize=16)
    plt.xlabel("Cena (zł)", fontsize=12)
    plt.ylabel("Liczba ofert", fontsize=12)


    plt.tight_layout()

    #plt.show()
    folder_name = str(re.match(r"^(.*?)_", phone_name).group(0))   

    figName =f"{phone_name}_Hist_Plot_figure.png"
    savepath = os.path.join("visualizations",folder_name,figName)

    os.makedirs(os.path.dirname(savepath), exist_ok=True)

    plt.savefig(savepath)

    plt.close()



def visualizeALL(filename, phone_name):
    visualizeTableBar(filename, phone_name)
    visualizeTableBubles(filename, phone_name)
    visualizeBoxPlot(filename, phone_name)
    visualizeTime(filename, phone_name)
    visualizeHistPlot(filename, phone_name)
