import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv',url=FREMONT_URL, force_download=False):
    """Download and cache fremont data

    Parameters
    ----------
    filename : String (optional)
        location to save data
    url : String (optional)
        web location of data
    force_download  : boolean (optional)
        if True, redownload the data

    Returns
    -------
        df : pandas.DataFrame
            DataFrame of the fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL,filename)
    df=pd.read_csv(filename,parse_dates=True,index_col='Date')
    df.columns=['East','West']
    df['Total']=df.East+df.West
    return df