from flask import Flask, render_template, request, flash, session, redirect
import requests
from bs4 import BeautifulSoup
import inspect
import json
 
 #http://chakoteya.net/NextGen/episodes.htm


URL = "http://chakoteya.net/NextGen/118.htm"
# class_list=set()
page = requests.get(URL)

soup0 = BeautifulSoup(page.text, "html.parser")
soup = soup0.get_text()  #this gets back a text file with no characters but can't filter it?
Picard_file = open ("Picard_quotes.txt", "w")

counter=0
Picard_quotes=[]
Picard_quotes_str=""
for item in soup.splitlines(keepends=True):  #for each line in the soup text - keep each line split to the end
    counter+=1 #just checking the number of quotes have - if these are enough
    if "PICARD" in item:  #search for PICARD in the item
        #Picard_quotes.append(str(item).replace("\r\n",""))
        temp_quote=str(item).replace("\r\n","") #at the end of the line replace it with sempty string - when keepends = true linebreaks are included in new list
        temp_quote2=temp_quote.rstrip() #sometimes was still a few empty whitespaces - removed this
        if temp_quote2[-1]==".":  #some sentences flowed across lines - if the last character fo the line was a full stop - add to the list
            Picard_quotes.append(temp_quote2)
            Picard_quotes_str+=temp_quote2+"\n" #new line so it's not one long line.
            print(counter,type(item),item)

d_counter=0
for quote_item in Picard_quotes:
    d_counter+=1
    print(d_counter,quote_item)
Picard_file.write(Picard_quotes_str)
Picard_file.close()