import pandas as pd
import csv
import tkinter as tk
import numpy as ny
import matplotlib.pyplot as mt
from matplotlib.backends.backend_pdf import PdfPages as pp
f=pd.read_csv("E:\Instagram\COVID.csv")
print(f.head)
root=tk.Tk()
can=tk.Canvas(root,width=500,height=350)
can.pack()
def export():
    with pp(r"E:\Instagram\new.pdf")as new:
        g=f.Date_reported[10169:10315]
        h=f.New_cases[10169:10315]
        mt.plot(h,g,color="red",marker="o")
        mt.grid(True)
        mt.title("COVID-19 Daily Updates in INDIA")
        mt.ylabel("Date")
        mt.xlabel("No. of cases")
        new.savefig()
        mt.close()
but=tk.Button(root,text="Click to Save",command=export,bg="black",fg="white")
can.create_window(200,150,window=but)
root.mainloop()
