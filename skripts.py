import pandas

dati=pandas.read_csv('THE World University Rankings 2016-2024.csv',encoding="ISO-8859-1")
latvia = len(dati[dati["Country"] == "Latvia"])
print(latvia)