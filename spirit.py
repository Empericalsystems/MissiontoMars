
from flask import Flask, render_template, request, flash, session, redirect
import requests
from bs4 import BeautifulSoup
import inspect
import json
 
 #http://chakoteya.net/NextGen/episodes.htm


URL = "http://chakoteya.net/NextGen/105.htm"
# class_list=set()
page = requests.get(URL)

soup0 = BeautifulSoup(page.text, "html.parser")
soup = soup0.get_text()  #this gets back a text file with no characters but can't filter it?
Troi_file = open ("Troi_quotes.txt", "w")

c=0
Troi_quotes=[]
Troi_quotes_str=""
for item in soup.splitlines(keepends=True):
    c+=1
    if "TROI" in item:
        #Picard_quotes.append(str(item).replace("\r\n",""))
        temp_quote=str(item).replace("\r\n","")
        temp_quote2=temp_quote.rstrip()
        if temp_quote2[-1]==".":
            Troi_quotes.append(temp_quote2)
            Troi_quotes_str+=temp_quote2+"\n"
            print(c,type(item),item)

d=0
for quote_item in Troi_quotes:
    d+=1
    print(d,quote_item)
Troi_file.write(Troi_quotes_str)
Troi_file.close()