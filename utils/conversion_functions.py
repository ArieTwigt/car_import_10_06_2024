import pandas as pd
from typing import List

def convert_list_to_df(object_list: List) -> pd.DataFrame:
    '''
    This function converts a list to a pandas DataFrame

    Input:
    * List 

    Output:
    * DataFrame
    
    '''

    # convert the list to a DataFrame
    df = pd.DataFrame(object_list)

    return df