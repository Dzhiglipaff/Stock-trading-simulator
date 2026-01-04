import yfinance as yf
import math
from datetime import datetime
import sqlite3
class portfolio:
    def __init__(self,username,password):
        self.owner = username
        self.password = password
        self.balance = 0
        self.stocks = {}
        self.stockvalue=0
   
    def add_funds(self,amount):
        self.balance += amount

    def assetValue(self):
        s=0
        for item in self.stocks:
            s+=round(yf.Ticker(item).fast_info['last_price'],2)*self.stocks[item]
        self.stockvalue=s
    
    def add_stock(self,ticker,quantity):
        buy = quantity*(round(yf.Ticker(ticker).fast_info['last_price'],2))
        if buy > self.balance:
            print("You can't do that")
            return
        self.balance-=buy
        self.stocks[ticker]=quantity
        
        
        self.assetValue()
    
    def display_portfolio(self):
        for item in self.stocks:
            print(item,round(yf.Ticker(item).fast_info['last_price']*self.stocks[item],2),self.stocks[item],round(yf.Ticker(item).fast_info['last_price'],2))
        print("Free Cash: "+str(self.balance))
        self.assetValue()
        print("Portfolio Value: "+str(self.stockvalue))
        print("Total portfolio value: "+str(self.balance+self.stockvalue))
        print()
    
    def sell(self,ticker,quantity):

        self.stocks[ticker]-=quantity
        cashflow=round(yf.Ticker(ticker).fast_info["last_price"],2)*quantity 
        self.stockvalue-=cashflow
        self.balance+=cashflow

    


    
kyler = portfolio("Kyler","Kyler0228")
kyler.add_funds(20000)
kyler.add_stock("NVDA",100)
kyler.add_stock("ATYR",690)
kyler.assetValue()
kyler.display_portfolio()
kyler.sell("NVDA",5)
kyler.display_portfolio()


