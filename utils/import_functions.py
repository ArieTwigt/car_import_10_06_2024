from typing import List, Dict
import requests


def import_cars_by_brand(brand: str) -> List[Dict]:
    '''
    Import cars from the RDW API based on the brand.

    Input:
    * The brand of the car

    Ouput:
    * List of cars
    
    '''
    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # check for empty results
    if len(data) == 0:
        raise ValueError(f"No cars found for {brand}")

    return data