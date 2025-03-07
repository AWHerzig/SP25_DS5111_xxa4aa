"""
This module sets up the base classes for downloaders and processors
"""
from abc import ABC, abstractmethod
# DOWNLOADER
class GainerDownload(ABC):
    """
    This class is the base Class for the Downloader
    """
    def __init__(self):
        self.raw = None

    @abstractmethod
    def download(self):
        """
        The download method will be specified in the specific classes.
        """
        pass


class GainerProcess(ABC):
    """
    This class is the base Class for the Processors
    """
    def __init__(self):
        self.normalized = None

    @abstractmethod
    def normalize(self, raw_df):
        """
        The normalize method will be specified in the specific classes.
        """
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """
        The saving method will be specified in the specific classes.
        """
        pass
