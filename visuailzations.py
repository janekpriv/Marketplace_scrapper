import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import os
import pandas as pd


def visualizeTableBubles(filename, phone_name):

    path = os.path.join("phones_csv", filename)

    df = pd.read_csv(path)

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

    # Oznaczenia osi
    
    plt.xlabel('index')
    plt.ylabel('Cena')
    plt.title(f'Cena {phone_name}')
    plt.colorbar(scatter, label='Cena')
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    plt.gca().set_facecolor('#d3d3d3')  # Tło wykresu
    plt.show()


    
def visualizeTableBar(df, phone_name):

    #df=df.tail(25)

    title = df['title']
    price = df['price']

    norm = plt.Normalize(df['price'].min(), df['price'].max())  # Min = 100, Max = 1000
    colors = cm.plasma(norm(df['price']))

    plt.figure(figsize=(10,6))
    plt.bar(price.index,price, color=colors, width =0.3, label="cena")
    plt.xlabel('Nazwy ogłoszeń')
    plt.ylabel('Cena [zł]')
    plt.title(f'Ceny {phone_name}')
    plt.colorbar(cm.ScalarMappable(norm=norm, cmap='plasma'), label='Cena')
    plt.show()
    

