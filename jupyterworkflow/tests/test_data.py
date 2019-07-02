# python -m pytest jupyterworkflow

from jupyterworkflow.data import get_fremont_data
import pandas as pd
import numpy as np

def test_fremont_data():
    df=get_fremont_data()
    assert all(df.columns==['East', 'West', 'Total'])
    assert isinstance(df.index,pd.DatetimeIndex)
    assert len(np.unique(df.index.time))==24