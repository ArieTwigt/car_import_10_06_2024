import pandas as pd
import os
from utils import DATA_FOLDER


def export_df_to_csv(df: pd.DataFrame,
                     brand: str):
    '''
    Exports a DataFrame to csv

    Input:
    * Pandas DataFrame

    Output:
    * csv-file
    
    '''
    # compose the path for brand folder
    brand_folder = f"{DATA_FOLDER}/{brand}"

    # check if the folder already exists
    if not os.path.exists(brand_folder):
        # create the folder
        os.mkdir(brand_folder)

    # compose the filepath
    file_path = f"{brand_folder}/{brand}.csv"

    # export the DataFrame
    df.to_csv(file_path, index=False, sep=";")