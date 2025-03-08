"""
This module contains the specifc methods for getting wsj gainers
"""
import os
from datetime import datetime
import subprocess
import pandas as pd
import bin.gainers.base as Base
class GainerDownloadWSJ(Base.GainerDownload):
    """
    This Class contains the downloading method for getting wsj gainers
    """
    def __init__(self):
        pass

    def download(self):
        """
        This method downloads the wsjgainer info and loads it into the python enviornment
        
        Currently runs the makefile because it activates the venv and
        I don't know how to in python but I'm hoping to figure that out still
        """
        subprocess.run(["make", "wjsgainers.csv"], check = True)
        self.raw = pd.read_csv('wjsgainers.csv')
        os.remove('wjsgainers.html')
        os.remove('wjsgainers.csv')
        print("Downloading WSJ gainers")

class GainerProcessWSJ(Base.GainerProcess):
    """
    This Class contains the processing methods for getting wsj gainers
    Normalizing and Saving
    """
    def __init__(self):
        pass

    def normalize(self, raw_df):
        """
        This method normalizes the wsjgainer info
        """
        norm_df = raw_df[["Unnamed: 0", "Last", "Chg", "% Chg"]].\
            rename(columns = {"Unnamed: 0": "symbol", "Last": "price", \
                 "Chg": "price_change", "% Chg": "price_percent_change"})

        norm_df["symbol"] = norm_df.symbol.apply(lambda element:element.split('(')[1].split(')')[0])
        self.normalized = norm_df
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        """
        This method saves the wsjgainer info with a standard timestamp
        """
        path = "sample_data/wjsgainers_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
        self.normalized.to_csv(path)
        print("Saving WSJ gainers")
