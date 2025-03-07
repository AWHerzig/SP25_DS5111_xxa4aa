import bin.gainers.yahoo as yahoo
import bin.gainers.wsj as wsj

# FACTORY
class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'wjs'], f"Unrecognized gainer type {choice}"
        self.choice = choice 

    def get_downloader(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return yahoo.GainerDownloadYahoo()
        elif self.choice in ['wsj', 'wjs']:
            return wsj.GainerDownloadWSJ()

    def get_processor(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return yahoo.GainerProcessYahoo()
        elif self.choice == 'wsj':
            return wsj.GainerProcessWSJ()
