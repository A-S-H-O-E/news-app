from email import message
from msilib import text
from tkinter import *
import requests 
from tkinter import messagebox
root = Tk()
root.title('News App')
root.geometry('600x450')
root.configure(background = 'lightgreen')
def fetchcc():
    country = countryn.get()
    response = requests.get('https://api.printful.com/countries')
    data = response.json()
    results = data['result']
    cc = ''
    for r in results:
        if(r['name'].lower() == country.lower()):
            cc = r['code'].lower()
    if(cc == ''):
        messagebox.showerror('Error','country not found {}'.format(country))
    else:
        fetchnews(cc)
   
def fetchnews(cc):
    pass
header = Label(root,text = 'Entry country name for news', font = ('Times 20 bold',18))
header.place(x = 140, y = 40)
countryn = StringVar()
country_entry = Entry(root,textvariable = countryn)
country_entry.place(x = 230, y = 120)
srcbutn = Button(root,text = 'Search',font = 'Times 20 bold',height = 1,width = 6,command = lambda:fetchcc())
srcbutn.place(x = 235, y = 180)
root.mainloop()