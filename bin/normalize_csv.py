





import pandas as pd
import sys
import re


def readYgainers(raw_df):
    assert {"Symbol", "Price", "Change", "Change %"}.issubset(raw_df.columns), f"The loaded csv is labeled as a yahoo gainers table, but does not have appropriate column names."

    norm_df = raw_df[["Symbol", "Price", "Change", "Change %"]].\
            rename(columns = {"Symbol": "symbol", "Price": "price", "Change": "price_change", "Change %": "price_percent_change"})

    # symbol is good to go
    norm_df["price"] = norm_df.price.apply(lambda element: element.split(' ')[0])
    # price_change is good to go
    norm_df["price_percent_change"] = norm_df.price_percent_change.str.replace('[+%]', '', regex=True) # Aidan make sure negatives still work
    
    assert list(norm_df.columns) == ["symbol", "price", "price_change", "price_percent_change"], "Output columns are not correct, check proper formatting of ygainers table."

    return norm_df

def readWSJgainers(raw_df):
    assert {"Unnamed: 0", "Last", "Chg", "% Chg"}.issubset(raw_df.columns), f"The loaded csv is labeled as a Wall Street Journal gainers table, but does not have appropriate column names."

    norm_df = raw_df[["Unnamed: 0", "Last", "Chg", "% Chg"]].\
            rename(columns = {"Unnamed: 0": "symbol", "Last": "price", "Chg": "price_change", "% Chg": "price_percent_change"})

    norm_df["symbol"] = norm_df.symbol.apply(lambda element: element.split('(')[1].split(')')[0])
    # price is good to go
    # price_change is good to go
    # price_percent_change is good to go

    assert list(norm_df.columns) == ["symbol", "price", "price_change", "price_percent_change"], "Output columns are not correct, check proper formatting of wsjgainers table."

    return norm_df

if __name__ == '__main__':
    pathToRawCSV = sys.argv[1]

    assert re.search("(wjs|wsj|y)gainers.csv", pathToRawCSV), f"Expected path to one of the gainers csvs but got {sys.argv[1]}" # In the makefile, its listed as wjs which may be a typo but I'll accept both

    RawDF = pd.read_csv(pathToRawCSV)

    assert len(RawDF) > 0, "Input CSV should not be empty"

    if 'ygainers' in pathToRawCSV:
        NormDF = readYgainers(RawDF)
    else:
        NormDF = readWSJgainers(RawDF)
    
    assert NormDF.shape[0] > 0, "Output csv should not be empty"
    assert NormDF.shape[1] == 4, "Output csv should have four columns" # Exact ones have already been checked once at this point so quick spot-check

    pathToNormCSV = pathToRawCSV.replace('.csv', '_norm.csv')
    NormDF.to_csv(pathToNormCSV)

