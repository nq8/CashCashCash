import pandas as pd
import csv

class PortfolioManager:
    def addItem(self, name, isin, symbol, share, category):
        with open('portfolio.csv', 'a', newline='') as f:
            newFileWriter = csv.writer(f)
            newFileWriter.writerow([name, isin, symbol, share, category])
        self.readLocalCSV()
        print(self.df.head())

    def readLocalCSV(self):
        try:
            self.df = pd.read_csv("portfolio.csv")
        except FileNotFoundError:
            with open('portfolio.csv', 'w') as newFile:
                newFileWriter = csv.writer(newFile)
                newFileWriter.writerow(['name', 'isin', 'symbol', 'share', 'category'])
            self.df = pd.read_csv("portfolio.csv")

    def __init__(self):
        self.readLocalCSV()
        #read current share file if available


if __name__ == '__main__':
    a = PortfolioManager()
    a.addItem("Lufthansa", "DE0008232125", "LHA.FRK", "10", "stock")
    a.addItem("Airbus", "NL0000235190", "AIR.FRK", "15", "stock")