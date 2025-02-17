"""
Test the normalize_csv python script
"""


import sys
import pandas as pd
import bin.normalize_csv
sys.path.append('.')

def test_read_wjsgainers_correct_names():
    """
    to test the reading of wjsgainers.csv
    make sure column names are correct
    """
    raw_wjsgainers = pd.read_csv('sample_data/wjsgainers.csv')
    normalized_wjsgainers = bin.normalize_csv.read_wsj_gainers(raw_wjsgainers)

    correct_columns = ["symbol", "price", "price_change", "price_percent_change"]
    assert list(normalized_wjsgainers.columns) == correct_columns

def test_read_wjsgainers_correct_shape():
    """
    to test the reading of wjsgainers.csv
    make sure the shape is appropriate
    """
    raw_wjsgainers = pd.read_csv('sample_data/wjsgainers.csv')
    normalized_wjsgainers = bin.normalize_csv.read_wsj_gainers(raw_wjsgainers)

    output_shape = normalized_wjsgainers.shape
    assert output_shape[0] > 0 and output_shape[1] == 4

def test_read_ygainers_correct_names():
    """
    to test the reading of ygainers.csv 
    make sure column names are correct
    """
    raw_ygainers = pd.read_csv('sample_data/ygainers.csv')
    normalized_ygainers = bin.normalize_csv.read_y_gainers(raw_ygainers)

    correct_columns = ["symbol", "price", "price_change", "price_percent_change"]
    assert list(normalized_ygainers.columns) == correct_columns

def test_read_ygainers_correct_shape():
    """
    to test the reading of ygainers.csv
    make sure the shape is appropriate
    """
    raw_ygainers = pd.read_csv('sample_data/ygainers.csv')
    normalized_ygainers = bin.normalize_csv.read_y_gainers(raw_ygainers)

    output_shape = normalized_ygainers.shape
    assert output_shape[0] > 0 and output_shape[1] == 4
