import bin.gainers.base as Base
import os
from datetime import datetime
import subprocess
import pandas as pd
class GainerDownloadWSJ(Base.GainerDownload):
    def __init__(self):
        pass

    def download(self):
        result = subprocess.run(["make", "wjsgainers.csv"])
        self.raw = pd.read_csv('wjsgainers.csv')
        os.remove('wjsgainers.html')
        os.remove('wjsgainers.csv')
        print("Downloading WSJ gainers")
        
class GainerProcessWSJ(Base.GainerProcess):
    def __init__(self):
        pass

    def normalize(self, raw_df):
        norm_df = raw_df[["Unnamed: 0", "Last", "Chg", "% Chg"]].\
            rename(columns = {"Unnamed: 0": "symbol", "Last": "price", \
				"Chg": "price_change", "% Chg": "price_percent_change"})

        norm_df["symbol"] = norm_df.symbol.apply(lambda element: element.split('(')[1].split(')')[0])
        self.normalized = norm_df
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        path = "sample_data/wjsgainers_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        self.normalized.to_csv(path)
        print("Saving WSJ gainers")
