import subprocess
from abc import ABC, abstractmethod
# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self):
        self.url = url
        self.raw = None

    @abstractmethod
    def download(self):
        pass
    

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
