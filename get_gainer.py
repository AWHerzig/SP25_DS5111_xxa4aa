"""
This module contains the template and main script for the new gainers factory archtecture
"""


import bin.gainers.factory as Factory

# TEMPLATE
class ProcessGainer:
    """
    The teplate class which holds the appropriate methods depending on the gainer type
    """
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
        """
        public method called to fully process the gainer in one command
        """
        self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":
    # Our sample main file would look like this
    import sys

    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
    print(runner.normalizer.normalized.shape)
