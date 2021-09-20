from flask import Flask, render_template, request, flash, session, redirect
import requests
from bs4 import BeautifulSoup
import inspect
import json
 
 #http://chakoteya.net/NextGen/episodes.htm


URL = "http://chakoteya.net/NextGen/114.htm"
# class_list=set()
page = requests.get(URL)

soup0 = BeautifulSoup(page.text, "html.parser")
soup = soup0.get_text()  #this gets back a text file with no characters but can't filter it?
Data_file = open ("Data_quotes.txt", "w")

c=0
Data_quotes=[]
Data_quotes_str=""
for item in soup.splitlines(keepends=True):
    c+=1
    if "DATA" in item:
        #Picard_quotes.append(str(item).replace("\r\n",""))
        temp_quote=str(item).replace("\r\n","")
        temp_quote2=temp_quote.rstrip()
        if temp_quote2[-1]==".":
            Data_quotes.append(temp_quote2)
            Data_quotes_str+=temp_quote2+"\n"
            print(c,type(item),item)

d=0
for quote_item in Data_quotes:
    d+=1
    print(d,quote_item)
Data_file.write(Data_quotes_str)
Data_file.close()


Data_file = open ("Data_quotes.txt", "w")

c=0
Data_quotes=[]
Data_quotes_str=""
for item in soup.splitlines(keepends=True):
    c+=1
    if "DATA" in item:
        temp_quote=str(item).replace("\r\n","")
        temp_quote2=temp_quote.rstrip()
        if temp_quote2[-1]==".":
            Data_quotes.append(temp_quote2)
            Data_quotes_str+=temp_quote2+"\n"
            print(c,type(item),item)

d=0
for quote_item in Data_quotes:
    d+=1
    print(d,quote_item)


Data_file.write(Data_quotes_str)
Data_file.close()

 

