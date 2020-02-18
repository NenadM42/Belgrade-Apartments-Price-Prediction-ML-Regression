from functools import cmp_to_key
from bs4 import BeautifulSoup
import requests
import re
import csv

squares = list()
number_of_rooms = list()
addresses = list()
prices = list()

sq_foot = dict()
sq_count = dict()

def obradiStranu(x):
    page = "https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd?page=" + str(x)
    source = requests.get(page).text

    soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())

    cena = soup.findAll(class_ = 'central-feature')
#cena = BeautifulSoup(str(cena),'lxml')
    estate_info = soup.findAll(class_= 'col-p-1-3')
    
    for line in cena:
        prices.append(line.text)
        
    address = soup.findAll(class_ = 'subtitle-places')
    
    
    #address = BeautifulSoup(str(address),'lxml')
    #address = soup.findAll('li')
    
    #print(address)

    
    
    for line in address:
        st1 = line.find('li')
        #print(st1)
        st2 = line.find('li').next_element.next_element
        #print(st2)
        address_t = line.text
        addresses.append(st1.text + st2.text)
        #print(line)

    cnt = 0
    for line in estate_info:
        estate_info_t = line.text
        #print(estate_info_t)
        cnt+=1
        cnt = cnt%3
        if(cnt == 2):
            curr = estate_info_t.split('m')
            squares.append(curr[0])
        if(cnt == 0):
            curr = estate_info_t.split('B')
            number_of_rooms.append(curr[0])
                
            
for i in range(0,900):
    obradiStranu(i)
    
counter = 0
for i in range(0, len(squares)):
    squares[i] = squares[i][:-1]
    squares[i] = squares[i].replace(',','.')
    prices[i] = prices[i][:-2]
    prices[i] = prices[i].replace(',','.')
    prices[i] = prices[i].replace('.','')

    addresses[i] = addresses[i][:-1]
    number_of_rooms[i] = number_of_rooms[i][:-1]
    sq_count[addresses[i]] = 0
    sq_foot[addresses[i]] = 0

for i in range(0, len(squares)):
    sq_foot[addresses[i]] += float(prices[i])
    sq_count[addresses[i]] += float(squares[i])

for i in sq_foot:
    sq_foot[i] = float(sq_foot[i]) / float(sq_count[i])    



with open('RealEstateBelgrade.csv','w',newline = '',encoding="utf-8") as f:
    thewriter = csv.writer(f)    
    
    thewriter.writerow(['ID','Squares','No_of_rooms','Address','Price','One_Sq'])
      
    for i in range(0, len(squares)):
        
        
        #print("ID: ",end = ' ')
        #print(i,end = '|')
        #print("Kvadratura:", end = ' ')
        #br = int(squares[i])
        #print(squares[i],end = '|')
        #print("Broj soba:",end = ' ')
        #print(number_of_rooms[i],end = '|')
        #print("Adresa:",end = ' ')
        #print(addresses[i],end = '|')
        #print("Cena:",end = ' ')
        #prices[i] = prices[i].replace('.','')
        #print(prices[i])
        #print("-------------")
        if(float(prices[i]) < 20000 or float(prices[i]) > 300000):
            continue
        thewriter.writerow([i,squares[i],number_of_rooms[i],addresses[i],prices[i],sq_foot[addresses[i]]])    
