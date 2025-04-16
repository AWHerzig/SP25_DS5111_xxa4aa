"""
This module contains the specifc methods for getting yahoo gainers
"""

import os
from datetime import datetime
import subprocess
import pandas as pd
import bin.gainers.base as Base

class GainerDownloadYahoo(Base.GainerDownload):
    """
    This Class contains the downloading method for getting yahoo gainers
    """
    def __init__(self):
        pass


    def download(self):
        """
        This method downloads the ygainer info and loads it into the python enviornment
        
        Currently runs the makefile because it activates the venv and
        I don't know how to in python but I'm hoping to figure that out still
        """
        #subprocess.run([".", "env/bin/activate"], check=True, text = True)
        #result = subprocess.run(["sudo", "google-chrome-stable", "--headless", "--disable-gpu",
        #"--dump-dom", "--no-sandbox", "--timeout=5000",
        #"'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'"],
        # check=True, text=True, capture_output=True)
        #print(result)
        subprocess.run(["make", "ygainers.csv"], check=True)
        self.raw = pd.read_csv('ygainers.csv')
        os.remove('ygainers.html')
        os.remove('ygainers.csv')

class GainerProcessYahoo(Base.GainerProcess):
    """
    This Class contains the processing methods for getting yahoo gainers
    Normalizing and Saving
    """
    def __init__(self):
        pass

    def normalize(self, raw_df):
        """
        This method normalizes the ygainer info
        """
        norm_df = raw_df[["Symbol", "Price", "Change", "Change %"]].\
            rename(columns = {"Symbol": "symbol", "Price": "price", \
                "Change": "price_change", "Change %": "price_percent_change"})
        norm_df["price"] = norm_df.price.apply(lambda element: element.split(' ')[0])
        norm_df["price_percent_change"] = norm_df.price_percent_change.\
                     str.replace('[+%]', '', regex=True)
        self.normalized = norm_df

        print("Normalizing yahoo gainers")

    def save_with_timestamp(self):
        """
        This method saves the ygainer info with a standard timestamp
        """
        path = "sample_data/ygainers_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        self.normalized.to_csv(path)
        print("Saving Yahoo gainers")
