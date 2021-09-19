from flask import Flask, render_template, request, flash, session, redirect
import requests
from bs4 import BeautifulSoup
import inspect
import json
 
 #http://chakoteya.net/NextGen/episodes.htm


URL = "http://chakoteya.net/NextGen/106.htm"
# class_list=set()
page = requests.get(URL)

soup0 = BeautifulSoup(page.text, "html.parser")
soup = soup0.get_text()  #this gets back a text file with no characters but can't filter it?
Picard_file = open ("Picard_quotes.txt", "w")

c=0
Picard_quotes=[]
Picard_quotes_str=""
for item in soup.splitlines(keepends=True):
    c+=1
    if "PICARD" in item:
        #Picard_quotes.append(str(item).replace("\r\n",""))
        temp_quote=str(item).replace("\r\n","")
        temp_quote2=temp_quote.rstrip()
        if temp_quote2[-1]==".":
            Picard_quotes.append(temp_quote2)
            Picard_quotes_str+=temp_quote2+"\n"
            print(c,type(item),item)

d=0
for quote_item in Picard_quotes:
    d+=1
    print(d,quote_item)
Picard_file.write(Picard_quotes_str)
Picard_file.close()


Riker_file = open ("Riker_quotes.txt", "w")

c=0
Riker_quotes=[]
Riker_quotes_str=""
for item in soup.splitlines(keepends=True):
    c+=1
    if "RIKER" in item:
        temp_quote=str(item).replace("\r\n","")
        temp_quote2=temp_quote.rstrip()
        if temp_quote2[-1]==".":
            Riker_quotes.append(temp_quote2)
            Riker_quotes_str+=temp_quote2+"\n"
            print(c,type(item),item)

d=0
for quote_item in Riker_quotes:
    d+=1
    print(d,quote_item)


Riker_file.write(Riker_quotes_str)
Riker_file.close()

combined_file = open ("riker_piccard.txt", "w")
combined_file.write(Picard_quotes_str + Riker_quotes_str)
combined_file.close()

