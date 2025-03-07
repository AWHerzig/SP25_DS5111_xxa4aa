import subprocess
from abc import ABC, abstractmethod
import pandas as pd
import os
from datetime import datetime
# FACTORY
class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice 

    def get_downloader(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self):
        self.url = url
        self.raw = None

    @abstractmethod
    def download(self):
        pass

class GainerDownloadYahoo(GainerDownload):
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

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        pass

    def download(self):
        result = subprocess.run(["make", "wjsgainers.csv"])
        self.raw = pd.read_csv('wjsgainers.csv')
        os.remove('wjsgainers.html')
        os.remove('wjsgainers.csv')
        print("Downloading WSJ gainers")




# PROCESSORS 
class GainerProcess(ABC):
    def __init__(self):
        self.normalized = None

    @abstractmethod
    def normalize(self, raw_df):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass

class GainerProcessYahoo(GainerProcess):
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
class GainerProcessWSJ(GainerProcess):
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

# TEMPLATE
class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize(self.downloader.raw)

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):
        self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":
    # Our sample main file would look like this
    import sys
   
    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
    print(runner.normalizer.normalized.shape)



