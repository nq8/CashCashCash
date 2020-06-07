import pandas as pd
import csv
import portfolioManager


#url_world = 'https://www.ishares.com/de/privatanleger/de/produkte/251882/ishares-msci-world-ucits-etf-acc-fund/1478358465952.ajax?fileType=csv&fileName=EUNL_holdings&dataType=fund'
#url_em = "https://www.ishares.com/de/privatanleger/de/produkte/264659/ishares-msci-emerging-markets-imi-ucits-etf/1478358465952.ajax?fileType=csv&fileName=IS3N_holdings&dataType=fund"
#url_mf = "https://www.ishares.com/de/professionelle-anleger/de/produkte/277246/ishares-factorselect-msci-world-ucits-etf/1478358465952.ajax?fileType=csv&fileName=IBCZ_holdings&dataType=fund"

class IshareManager:
    def get_breakdown(self):
        url_world = 'https://www.ishares.com/de/privatanleger/de/produkte/251882/ishares-msci-world-ucits-etf-acc-fund/1478358465952.ajax?fileType=csv&fileName=EUNL_holdings&dataType=fund'
        url_em = "https://www.ishares.com/de/privatanleger/de/produkte/264659/ishares-msci-emerging-markets-imi-ucits-etf/1478358465952.ajax?fileType=csv&fileName=IS3N_holdings&dataType=fund"
        url_mf = "https://www.ishares.com/de/professionelle-anleger/de/produkte/277246/ishares-factorselect-msci-world-ucits-etf/1478358465952.ajax?fileType=csv&fileName=IBCZ_holdings&dataType=fund"

        world_isin = "IE00B4L5Y983"
        em_isin = "IE00BKM4GZ66"
        mf_isin = "IE00BZ0PKT83"

        df_breakdown = pd.read_csv(url_world, skiprows=2, decimal=',')[0:0]

        # TODO Factor needs to incorporate current stock price
        if world_isin in self.df_portfolio["isin"].values:
            df_world = pd.read_csv(url_world, skiprows=2, decimal=',')
            factor = self.df_portfolio[self.df_portfolio["isin"] == world_isin].iloc[0].share
            #print(index)
            df_world["Gewichtung (%)"] = df_world["Gewichtung (%)"] * factor
            df_breakdown = df_breakdown.append(df_world)
            print(df_breakdown.head())
        if em_isin in self.df_portfolio["isin"].values:
            df_em = pd.read_csv(url_em, skiprows=2, decimal=',')
            factor = self.df_portfolio[self.df_portfolio["isin"] == em_isin].iloc[0].share
            #print(index)
            df_em["Gewichtung (%)"] = df_em["Gewichtung (%)"] * factor
            df_breakdown = df_breakdown.append(df_em)
            print(df_breakdown.head())
        if mf_isin in self.df_portfolio["isin"].values:
            df_mf = pd.read_csv(url_mf, skiprows=2, decimal=',')
            factor = self.df_portfolio[self.df_portfolio["isin"] == mf_isin].iloc[0].share
            #print(index)
            df_mf["Gewichtung (%)"] = df_mf["Gewichtung (%)"] * factor
            df_breakdown = df_breakdown.append(df_mf)
            print(df_breakdown.head())
        df_breakdown["Gewichtung (%)"] = df_breakdown["Gewichtung (%)"] * 1/df_breakdown["Gewichtung (%)"].sum()
        print(df_breakdown.head())
        self.df_breakdown = df_breakdown

    def __init__(self, df_portfolio):
        self.df_portfolio = df_portfolio
        self.get_breakdown()

if __name__ == '__main__':
    test = portfolioManager.PortfolioManager()
    a = IshareManager(test.get_df())