import bin.gainers.base as Base
import os
from datetime import datetime
import subprocess
import pandas as pd

class GainerDownloadYahoo(Base.GainerDownload):
    def __init__(self):
        pass
        

    def download(self):
        #sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'
        #subprocess.run([".", "env/bin/activate"], check=True, text = True)
        #result = subprocess.run(["sudo", "google-chrome-stable", "--headless", "--disable-gpu", "--dump-dom", "--no-sandbox", "--timeout=5000", "'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'"], check=True, text=True, capture_output=True)
        #print(result)
        result = subprocess.run(["make", "ygainers.csv"])
        self.raw = pd.read_csv('ygainers.csv')
        os.remove('ygainers.html')
        os.remove('ygainers.csv')

class GainerProcessYahoo(Base.GainerProcess):
    def __init__(self):
        pass

    def normalize(self, raw_df):
        norm_df = raw_df[["Symbol", "Price", "Change", "Change %"]].\
            rename(columns = {"Symbol": "symbol", "Price": "price", \
				"Change": "price_change", "Change %": "price_percent_change"})
        norm_df["price"] = norm_df.price.apply(lambda element: element.split(' ')[0])
        norm_df["price_percent_change"] = norm_df.price_percent_change.\
					str.replace('[+%]', '', regex=True)
        self.normalized = norm_df

        print("Normalizing yahoo gainers")

    def save_with_timestamp(self):
        path = "sample_data/ygainers_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        self.normalized.to_csv(path)
        print("Saving Yahoo gainers")
# ITS OWN SEPARATE FILE





