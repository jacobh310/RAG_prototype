from sec_edgar_downloader import Downloader
import yaml

with open("../../configs/data.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

path_to_save = '../../data/raw'
EMAIL = cfg['email']
TICKERS = cfg['tickers']
AMOUNT = cfg['amount'] 

dl = Downloader("RAG", EMAIL, path_to_save,)

for ticker in TICKERS:
    dl.get("10-K", ticker, limit= AMOUNT)

print("Finish Downloading")