import pandas as pd
import csv

class PortfolioManager:
    def add_item(self, name, isin, symbol, num_shares, category):
        with open('portfolio.csv', 'a', newline='') as f:
            newFileWriter = csv.writer(f)
            newFileWriter.writerow([name, isin, symbol, num_shares, category])
        self.read_local_csv()
        print(self.df.head())

    def read_local_csv(self):
        try:
            self.df = pd.read_csv("portfolio.csv")
        except FileNotFoundError:
            with open('portfolio.csv', 'w') as newFile:
                newFileWriter = csv.writer(newFile)
                newFileWriter.writerow(['name', 'isin', 'symbol', 'share', 'category'])
            self.df = pd.read_csv("portfolio.csv")


    def get_df(self):
        return self.df

    def __init__(self):
        self.read_local_csv()
        #read current share file if available


if __name__ == '__main__':
    a = PortfolioManager()
    a.add_item("Lufthansa", "DE0008232125", "LHA.FRK", "10", "stock")
    a.add_item("Airbus", "NL0000235190", "AIR.FRK", "15", "stock")
    a.add_item("iShares World", "IE00B4L5Y983", "EUNL.FRK", "100", "ETF")
    a.add_item("iShares EM", "IE00BKM4GZ66", "???", "1000", "ETF")