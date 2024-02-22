#Written by Andrew
from tkinter import * 
from forex_python.converter import CurrencyCodes,CurrencyRates

#tkinter allows me to create a GUI and forex-python to fetch live currency exchange rates

converter = Tk() 
converter.title("Currency Converter")
converter.geometry("300x300")

#this is used to create a GUI window, change its title and size

title = Label(converter,text="Andrew's Currency Converter")
title.pack()

#creates a label,a type of widget in tkinter,the pack.() forces it to be placed at the next available space at the top of the GUI

Label1 = Label(converter,text="Select currency to convert from:")
Label1.pack()

#another label

c = CurrencyRates()
convertfrombutton = ""
converttobutton = ""

#here i defined the necessary variables to be used for the currency conversion in tkinter variables 


def convert_currency():
    global c
    global convertfrombutton
    global converttobutton
    convertfunction = c.get_rate(convertfrombutton, converttobutton)
    convertamount = float(currencyamount.get())
    convertedamount = round(convertamount * convertfunction, 2)
    converttext.config(text=f"{convertamount}{convertfrombutton}={convertedamount}{converttobutton}")

#this is one of the def tkinter variables, this is the equation to convert the currency, global is used to acknowledge global variables(outside of tkinter)
#in this tkinter variable i set up variables that are used in other tkinter def variables to be able to get the type of currency, and amount of currency
#I have also used the round function to round the conversion to 2 decimal places
# the c.get_rate function allows me to get the current exchange rate of a given currency

def clear():
    global convertfrombutton
    global converttofrombutton
    convertfrombutton = ""
    converttobutton = ""
    aud2.config(state="disabled")
    gbp2.config(state="disabled")
    usd2.config(state="disabled")
    eur2.config(state="disabled")
    chf2.config(state="disabled")
    currencyamount.delete(0, "end")
    currencyamount.config(state="disabled")
    converttext.config(text="")

#this is a command that i use for a clear button, it greys out the buttons and clears all the conversion text
    
      
def convertaud():
    global convertfrombutton
    currencyamount.config(state="normal")
    aud2.config(state="disabled")
    gbp2.config(state="normal")
    usd2.config(state="normal")
    eur2.config(state="normal")
    chf2.config(state="normal")
    convertfrombutton = ('AUD')

def convertgbp():
    global convertfrombutton
    currencyamount.config(state="normal")
    aud2.config(state="normal")
    gbp2.config(state="disabled")
    usd2.config(state="normal")
    eur2.config(state="normal")
    chf2.config(state="normal")
    convertfrombutton = ('GBP')
    

def convertusd():
    global convertfrombutton
    currencyamount.config(state="normal")
    aud2.config(state="normal")
    gbp2.config(state="normal")
    usd2.config(state="disabled")
    eur2.config(state="normal")
    chf2.config(state="normal")
    convertfrombutton = ('USD')

def converteur():
    global convertfrombutton
    currencyamount.config(state="normal")
    aud2.config(state="normal")
    gbp2.config(state="normal")
    usd2.config(state="normal")
    eur2.config(state="disabled")
    chf2.config(state="normal")
    convertfrombutton = ('EUR')

def convertchf():
    global convertfrombutton
    currencyamount.config(state="normal")
    aud2.config(state="normal")
    gbp2.config(state="normal")
    usd2.config(state="normal")
    eur2.config(state="normal")
    chf2.config(state="disabled")
    convertfrombutton = ('CHF')

#these set of def variables are commands for all the currency buttons, which define what currency needs to be converted
#it also greys out the same currency on the second row, as converting to the same currency just gives the user the same output, using state=normal/disabled

def converttoaud():
    global converttobutton
    aud2.config(state="normal")
    gbp2.config(state="disabled")
    usd2.config(state="disabled")
    eur2.config(state="disabled")
    chf2.config(state="disabled")
    converttobutton = ('AUD')

def converttogbp():
    global converttobutton
    aud2.config(state="disabled")
    gbp2.config(state="normal")
    usd2.config(state="disabled")
    eur2.config(state="disabled")
    chf2.config(state="disabled")
    converttobutton = ('GBP')

def converttousd():
    global converttobutton
    aud2.config(state="disabled")
    gbp2.config(state="disabled")
    usd2.config(state="normal")
    eur2.config(state="disabled")
    chf2.config(state="disabled")
    converttobutton = ('USD')

def converttoeur():
    global converttobutton
    aud2.config(state="disabled")
    gbp2.config(state="disabled")
    usd2.config(state="disabled")
    eur2.config(state="normal")
    chf2.config(state="disabled")
    converttobutton = ('EUR')

def converttochf():
    global converttobutton
    aud2.config(state="disabled")
    gbp2.config(state="disabled")
    usd2.config(state="disabled")
    eur2.config(state="disabled")
    chf2.config(state="normal")
    converttobutton = ('CHF')

#these def variables are the same as before, except its for the buttons on the second row and defines which currency it needs to be converted to
#it also greys out the remaining currencies
    
    
    
currency1 = Frame(converter)
currency1.pack(side=TOP)

aud = Button(currency1,text="AUD",command=convertaud)
aud.pack(side=LEFT)

gbp = Button(currency1,text="GBP",command=convertgbp)
gbp.pack(side=LEFT)

usd = Button(currency1,text="USD",command=convertusd)
usd.pack(side=LEFT)

eur = Button(currency1,text="EUR",command=converteur)
eur.pack(side=LEFT)

chf = Button(currency1,text="CHF",command=convertchf)
chf.pack(side=LEFT)

#these are the first row of buttons,pack(side=LEFT) is used to stick the buttons next to eachother on the left side
#the commands of the buttons are the def variables as explained before
#I create a new frame for every tkinter widget as it gives a bit of spacing in between buttons and labels 

inputbox = Frame(converter)
inputbox.pack(side=TOP)

currencyamount_label = Label(inputbox,text="Input the amount to convert:")
currencyamount_label.pack(side=TOP)

currencyamount = Entry(inputbox,width=20,state="disabled")
currencyamount.pack(side=TOP)

#this is the entry widget, it displays the user with a text box to input the amount of currency they wish to convert

currency2 = Frame(converter)
currency2.pack(side=TOP)

currency2text = Label(currency2,text="Select currency to convert to:")
currency2text.pack(side=TOP)

#another label asking the user to select currency to convert to

aud2 = Button(currency2,text="AUD",state="disabled",command=converttoaud)
aud2.pack(side=LEFT)

gbp2 = Button(currency2,text="GBP",state="disabled",command=converttogbp)
gbp2.pack(side=LEFT)

usd2 = Button(currency2,text="USD",state="disabled",command=converttousd)
usd2.pack(side=LEFT)

eur2 = Button(currency2,text="EUR",state="disabled",command=converttoeur)
eur2.pack(side=LEFT)

chf2 = Button(currency2,text="CHF",state="disabled",command=converttochf)
chf2.pack(side=LEFT)

#second row of buttons which define the second variable to convert the currency to, 'converttobutton'
#these buttons are disabled at the beginning of the program, later enabled when the first currency is selected

convertframe = Frame(converter)
convertframe.pack(side=TOP)

convertbutton = Button(convertframe,text="Convert",command=convert_currency)
convertbutton.pack(side=TOP)

#this button is the most important one
#the command that is assigned to this collects the first currency, second currency, calculates the exchange rate, and calculates what the amount is equal to

converttext = Label(convertframe,text="")
converttext.pack()

#this is the conversion that is outputted from the convert button
#the text is blank at the start of the program, however once convert button is pressed it is changed using the .config function in tkinter

clearframe = Frame(converter)
clearframe.pack(side=TOP)

clearbutton = Button(clearframe,text="Clear",command=clear)
clearbutton.pack(side=TOP)

#this clear button is assigned to the command mentioned in the beginning
#it greys out the second row of buttons, disables the entry widget (currencyamount) and removes the text inside the entry widget using the .delete function


converter.mainloop()

#this is very important as it allows the gui to update information about variables infinitely, rather than updating them once and never being changed again











