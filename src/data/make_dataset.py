import requests
import pandas as pd

headers = {'User-Agent': "jacobh0830@gmail.com"}

companies = ['TSLA','AAPL','META','AMZN']



companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json", 
    headers=headers
    )

companyData = pd.DataFrame.from_dict(companyTickers.json(),
                                     orient='index')

companyData = companyData[companyData['ticker'].isin(companies)]


companyData['cik_str'] = companyData['cik_str'].astype(
                           str).str.zfill(10)


cik = companyData[0:1].cik_str[0]

filingMetadata = requests.get(
    f'https://data.sec.gov/submissions/CIK{cik}.json',
    headers=headers
    )

print(filingMetadata.json())
