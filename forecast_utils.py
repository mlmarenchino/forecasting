import pandas as pd

def load_csv_timestamp(fname, period=False):
    df = pd.read_csv(fname)
    index = pd.to_datetime(df.iloc[:,0])
    if period:
        index = index.dt.to_period()
    df = df.drop(df.columns[0], axis=1)
    return df.set_index(index)


def load_csv_quarters(fname, period=False):
    df = pd.read_csv(fname)
    index = df.iloc[:,0].str.split().str.join(sep="")
    index = pd.to_datetime(index)
    if period:
        index = index.dt.to_period()
    df = df.drop(df.columns[0], axis=1)
    return df.set_index(index)

