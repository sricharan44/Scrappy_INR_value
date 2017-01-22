from urllib.request import urlopen
import re
import csv
import time
from datetime import date
today = date.today()
if __name__ == "__main__":
    #print("Enter the number of STOCK value you want?")
    #N = int(input())
      CC = ["USD","BWP","SLL","BDT","CNY","SYP","UGX","MRO","WST","DJF","OMR","ISK","PLN","VND","RUB","XAF","TWD","SZL","INR",
      "JPY","MYR","XOF","LBP","KGS","KHR","CZK","ZAR","TZS","MWK","STD","NPR","HUF","TTD","CRC","DKK","MZN",
      "PGK","PHP","AFN","HNL","AMD","GYD","SHP","HTG","PKR","LAK","AUD","KMF","ETB","LTL","LVL","GIP","HKD","LSL","SCR",
      "NIO","TMT","SDG","MUR","NAD","CHF","BTN","PEN","KES","MMK","PYG","ALL","COP","SVC","KRW","RON","KPW","VUV",
      "NOK","GNF","DZD","THB","XPF","AWG","ERN","AED","BOB","TJS","CUP","PAB","CAD","ECS","CLP","RSD","MKD","KWD","SRD",
      "LRD","GMD","SBD","ARS","SOS","TRY","NGN","GHS","MDL","KYD","HRK","MVR","SEK","UZS","KZT","ZMW","BSD","SAR",
      "NZD","BAM","BRL","BZD","SGD","FKP","IDR","JOD","ILS","BND","LYD","ANG","DOP","BIF","GEL","GBP","CVE","BMD","TND",
      "AOA","JMD","AZN","EGP","LKR","IRR","BGN","MXN","UAH","YER","MNT","MAD","MOP","IQD","TOP","QAR","BHD","FJD",
      "BBD","VEF","EUR","UYU","XCD","CDF","RWF","BYR"]
      C = ["USD", "BWP", "SLL","BYR"]
      j = 0
      c1 = "INR"
    #while j<N:
        #c1 = input("Enter the first country code")
        #c2 = input("Enter the second country code")
      f2 = open(str(today) + '.txt','w')
      print(today)
      f2.write(str(today)+"\n")
      for each in CC:
          print(c1 + each)
          j+=1
          c2 = each
          urls = "https://in.finance.yahoo.com/q?s="+c1.lower()+c2.lower()+"=x"
          htmlfile = urlopen(urls)
          htmltext = htmlfile.read()
          regex = '<span id="yfs_l10_' + c1.lower()+c2.lower()+ '=x">(.+?)</span>'
          pattern = re.compile(regex)
          price = re.findall(pattern,str(htmltext))
          #if(int(price)>0):
              #print(c1+"-->"c2+"="+price)
          print(price)
          val = str(price)
          #value = c1+","+c2+","+str(val).strip("['']")+"\n"
          f2.write(val.strip("['']")+"\n")

    #   j+=1
      f2.close()