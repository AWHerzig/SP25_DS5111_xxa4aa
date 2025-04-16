"""
Test the LAB6 factory design pattern python classes
"""

import sys
import os
sys.path.append('.')
from bin.gainers import factory as Factory
from get_gainer import ProcessGainer
#sys.path.append('.')
# YAHOO
def test_factory_output_shape_yahoo():
    """
    to test the process for yahoo and verify the output has data
    """
    choice = 'yahoo'
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.downloader.download()
    runner.normalizer.normalize(runner.downloader.raw)
    output_shape = runner.normalizer.normalized.shape
    assert output_shape[0] > 0 and output_shape[1] == 4

def test_factory_output_names_yahoo():
    """
    to test the process for yahoo and verify the output has correct names
    """
    choice = 'yahoo'
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.downloader.download()
    runner.normalizer.normalize(runner.downloader.raw)
    correct_columns = ["symbol", "price", "price_change", "price_percent_change"]
    assert list(runner.normalizer.normalized.columns) == correct_columns

def test_factory_no_leftover_files_yahoo():
    """
    make sure ygainers.csv and ygainers.html don't get leftover
    """
    choice = 'yahoo'
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.downloader.download()
    runner.normalizer.normalize(runner.downloader.raw)
    assert not os.path.exists('ygainers.csv')
    assert not os.path.exists('ygainers.html')

# WJS
def test_factory_output_shape_wsj():
    """
    to test the process for wsj and verify the output has data
    """
    choice = 'wsj'
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.downloader.download()
    runner.normalizer.normalize(runner.downloader.raw)
    output_shape = runner.normalizer.normalized.shape
    assert output_shape[0] > 0 and output_shape[1] == 4

def test_factory_output_names_wsj():
    """
    to test the process for wsj and verify the output has correct names
    """
    choice = 'wsj'
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.downloader.download()
    runner.normalizer.normalize(runner.downloader.raw)
    correct_columns = ["symbol", "price", "price_change", "price_percent_change"]
    assert list(runner.normalizer.normalized.columns) == correct_columns

def test_factory_no_leftover_files_wsj():
    """
    make sure wjsgainers.csv and wjsgainers.html don't get leftover
    """
    choice = 'wsj'
    factory = Factory.GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.downloader.download()
    runner.normalizer.normalize(runner.downloader.raw)
    assert not os.path.exists('wjsgainers.csv')
    assert not os.path.exists('wjsgainers.html')
