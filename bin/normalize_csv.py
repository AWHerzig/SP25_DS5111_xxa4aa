


"""
This module normalizes the input csv for lab 3
"""


import sys
import re
import pandas as pd

def read_y_gainers(raw_df):
    """
    Input: raw_df - An example of a raw ygainers.csv loaded into pandas

    Output: norm_df - The ygainers table normalized to requirements

    """

    assert {"Symbol", "Price", "Change", "Change %"}.\
	issubset(raw_df.columns), \
	"The loaded csv is labeled as a Y gainers table, but does not have appropriate columns."

    norm_df = raw_df[["Symbol", "Price", "Change", "Change %"]].\
            rename(columns = {"Symbol": "symbol", "Price": "price", \
				"Change": "price_change", "Change %": "price_percent_change"})

    # symbol is good to go
    norm_df["price"] = norm_df.price.apply(lambda element: element.split(' ')[0])
    # price_change is good to go
    norm_df["price_percent_change"] = norm_df.price_percent_change.\
					str.replace('[+%]', '', regex=True)

    assert list(norm_df.columns) == ["symbol", "price", "price_change", "price_percent_change"], \
	"Output columns are not correct, check proper formatting of ygainers table."

    return norm_df

def read_wsj_gainers(raw_df):
    """
    Input: raw_df - An example of a raw ygainers.csv loaded into pandas

    Output: norm_df - The ygainers table normalized to requirements

    """
    assert {"Unnamed: 0", "Last", "Chg", "% Chg"}.issubset(raw_df.columns), \
	"The loaded csv is labeled as a WSJ gainers table, but does not have appropriate columns."

    norm_df = raw_df[["Unnamed: 0", "Last", "Chg", "% Chg"]].\
            rename(columns = {"Unnamed: 0": "symbol", "Last": "price", \
				"Chg": "price_change", "% Chg": "price_percent_change"})

    norm_df["symbol"] = norm_df.symbol.apply(lambda element: element.split('(')[1].split(')')[0])
    # price is good to go
    # price_change is good to go
    # price_percent_change is good to go

    assert list(norm_df.columns) == ["symbol", "price", "price_change", "price_percent_change"], \
	"Output columns are not correct, check proper formatting of wsjgainers table."

    return norm_df

if __name__ == '__main__':
    pathToRawCSV = sys.argv[1]

    assert re.search("(wjs|wsj|y)gainers.csv", pathToRawCSV), \
	f"Expected path to one of the gainers csvs but got {sys.argv[1]}"

    RawDF = pd.read_csv(pathToRawCSV)

    assert len(RawDF) > 0, "Input CSV should not be empty"

    if 'ygainers' in pathToRawCSV:
        NormDF = read_y_gainers(RawDF)
    else:
        NormDF = read_wsj_gainers(RawDF)

    assert NormDF.shape[0] > 0, "Output csv should not be empty"
    assert NormDF.shape[1] == 4, "Output csv should have four columns"

    pathToNormCSV = pathToRawCSV.replace('.csv', '_norm.csv')
    NormDF.to_csv(pathToNormCSV)
