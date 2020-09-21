# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:00:19 2020

@author: Rated R
"""


from tkinter import Tk,simpledialog,messagebox



def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line=line.rstrip('\n')
            country,city=line.split('/')
            the_world[country]=city


def write_to_file(country,capital):    
    with open('capital_data.txt','a') as file:
        file.write('\n'+country+'/'+capital)
        
    
print("Ask the expert- Capital Cities of the World")
root=Tk()
root.withdraw()
the_world={}
read_from_file()
while True:
    cont=input("Want to play(y/n)?")
    if cont=='y':
        query_country=simpledialog.askstring('Country','Type the name of country')
        if query_country in the_world:
            result=the_world[query_country]
            messagebox.showinfo('Answer','The capital of '+query_country+' is '
                            +result+'!')
        else:
            new_city=simpledialog.askstring('Teach Me','I don\'t know!'+
                'What is the capital of'+query_country+'?')
            the_world[query_country]=new_city
            write_to_file(query_country,new_city)
        
    else:
        break
        
root.mainloop()