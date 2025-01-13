import pandas as pd

artikel = ["Goldbären", "Wine Gums", "Clementinen"]
gewicht = [350, 300, 1000]
preis = [1.19, 0.89, 2.99]
steuer = ["B", "B", "B"]

kassenzettel = pd.DataFrame({
    "Artikel": artikel,
    "Gewicht": gewicht,
    "Preis": preis,
    "Steuer": steuer
})

print(kassenzettel)
print("----------------------")
print(kassenzettel.shape)  # Tuple (number of rows, number of columns)
print("----------------------")
print(kassenzettel[['Artikel', 'Preis']])  # Returns both full columns (DATAFRAME)
print("-----------------------")
print(kassenzettel[['Preis', 'Artikel']])  # Returns both full columns (DATAFRAME)
print("-----------------------")
print(kassenzettel['Artikel'][0])  # First value of 'Artikel' column
print("-----------------------")
print(kassenzettel['Artikel'][0:3])  # Dataframe: First three values of 'Artikel' column
print("-----------------------")
print(kassenzettel.iloc[0:2, 0:3])  # Access rows and columns by index
print("------------------------")
print(kassenzettel[kassenzettel['Preis'] < 1.0])  # All rows where 'Preis' < 1.0 (DATAFRAME)
print("------------------------")
print(kassenzettel[(kassenzettel['Preis'] < 1.0) &
                   (kassenzettel['Gewicht'] < 1000)])
print("-------------------------")
for index, zeilen in kassenzettel.iterrows():
    print(f"{index + 1}: {zeilen['Artikel']}, {zeilen['Preis']}")  # Iterate row by row
print("--------------------------")
kassenzettel['Warengruppe'] = ['Süß.', 'Süß.', 'Obst']  # Add a new column
print(kassenzettel)
print("---------------------------")

# Add a new row to the DataFrame
zeile = pd.DataFrame(
    columns=kassenzettel.columns,  # columns ist eine reservierte Variable
    data=[["Äpfel", 1500, 4.99, "B", "Obst"]] # data ist eine reservierte Variable
)

kassenzettel = pd.concat(
    [kassenzettel, zeile], ignore_index=True
)
print(kassenzettel)
print("-----------------------------")
print(f"Summieren Sie die Preise zum Endbetrag")
print(f"Option 1")
endbetrag = kassenzettel['Preis'].sum()
print(endbetrag)
print("----------------------------")
print(f"Option 2")
endbetrag = 0
for index, zeilen in kassenzettel.iterrows():
    endbetrag += zeilen['Preis']
print(f"{endbetrag}")
print("---------------------------")
endbetrag = 0 
for index, zeilen in kassenzettel.iterrows():
    endbetrag += zeilen['Preis']
print(f"Durschnittpreis aller Artikel: {endbetrag/len(kassenzettel)}")
endbetrag_mean = kassenzettel['Preis'].mean()   
print(f"Durschnittpreis mit .mean() Funktion: {endbetrag_mean}")
print("----------------------------")
print(f"Berechnen Sie den Kilopreis aller Artikel \n")
for index, zeilen in kassenzettel.iterrows():
    kilopreis = (zeilen['Preis']/zeilen['Gewicht']) * 1000
    print(f"{zeilen['Artikel']}     Kilopreis: {kilopreis} \n")
print("-----------------------------")
print(f"Anzahl der Spalten: {len(zeilen)}")
num_columns = kassenzettel.shape[1]
print(f"Number of columns: {num_columns}")
num_columns = len(kassenzettel.columns)
print(f"Number of columns: {num_columns}")


