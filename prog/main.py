import pandas as pd
import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modulis import StatsData


dati = pd.read_csv('THE World University Rankings 2016-2024.csv', encoding="ISO-8859-1")
latvia = len(dati[dati["Country"] == "Latvia"])
lithuania = len(dati[dati["Country"] == "Lithuania"])
estonia = len(dati[dati["Country"] == "Estonia"])

statsData=StatsData()
data = {
    'Valsts': ['Lietuva', 'Latvija', 'Igaunija'],
    'Skaits sarakstā': [lithuania, latvia, estonia],
    'Reitings': [statsData.getVidejaijslit(),statsData.getVidejaijsl(),statsData.getVidejaijsest()]
}

df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values=['Reitings','Skaits sarakstā'], index='Valsts', aggfunc={'Reitings': 'first', 'Skaits sarakstā': 'first'})
print(pivot_table)


def plot_bar_chart1():
    ax.clear()
    x = np.arange(3)
    ax.bar(x, [lithuania, latvia, estonia])
    ax.set_title('Universitāšu kopējais skaits sarakstā')
    ax.set_xticks(x)
    ax.set_xticklabels(['Lietuva', 'Latvija', 'Igaunija'])
    canvas.draw()

def plot_bar_chart2():
    ax.clear()
    x = np.arange(3)
    ax.bar(x, [statsData.getVidejaijslit(),statsData.getVidejaijsl(),statsData.getVidejaijsest()], color='orange')
    ax.set_title('Universitāšu vidējais reitings')
    ax.set_xticks(x)
    ax.set_xticklabels(['Lietuva', 'Latvija', 'Igaunija'])
    canvas.draw()

root = tk.Tk()
root.title('Baltijas universitātes')

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

button1 = tk.Button(root, text='Skaits sarakstā', command=plot_bar_chart1)
button1.pack(side=tk.LEFT)
button2 = tk.Button(root, text='Reitings', command=plot_bar_chart2)
button2.pack(side=tk.LEFT)

root.mainloop()