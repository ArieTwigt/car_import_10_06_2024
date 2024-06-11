from utils.import_functions import import_cars_by_brand
from utils.conversion_functions import convert_list_to_df
from utils.export_functions import export_df_to_csv
from tqdm import tqdm

# get the brand from the input
selected_brands = input("Insert the brand:\n")

# split the string to a list
selected_brand_list = selected_brands.split(" ")

# iterate over the brands list
for selected_brand in tqdm(selected_brand_list):
    try:
        # use the brand for the function
        cars_list = import_cars_by_brand(selected_brand)

        # convert the list to a DataFrame
        cars_df = convert_list_to_df(cars_list)

        # export the pandas DataFrame to a csv
        export_df_to_csv(cars_df, selected_brand)
    except ValueError:
        print(f"Error for {selected_brand}")

