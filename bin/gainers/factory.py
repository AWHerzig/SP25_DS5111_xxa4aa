"""
This module sets up the overall factory for the gainer jobs
"""
from bin.gainers import yahoo
from bin.gainers import wsj

# FACTORY
class GainerFactory:
    """
    This class is the aforementioned factory
    """
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'wjs'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        This method will identify which downloader to use in this job
        
        trigger off url to return correct downloader
        """
        if self.choice == 'yahoo':
            return yahoo.GainerDownloadYahoo()
        else:
            return wsj.GainerDownloadWSJ()

    def get_processor(self):
        """
        This method will identify which processor to use in this job
        
        trigger off url to return correct downloader
        """
        if self.choice == 'yahoo':
            return yahoo.GainerProcessYahoo()
        else':
            return wsj.GainerProcessWSJ()
