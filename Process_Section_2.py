#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Libraries
import pandas as pd
import os
import helpers

def convert_to_df(file_name):
    #Read CSV file into dataframe
    data = pd.read_csv(file_name)
    global DATA
    DATA = data
    print('*** PREVIEW ***')
    print(data.head())

def identify_amenities():
    data = DATA
    ## compile list of amenities provided across all location
    amenities_list = data['amenities'].tolist()

    amenities = []
    for i in amenities_list:
        new_format = i.strip("]['").split(', ')
        result = [n.strip('"') for n in new_format]
        amenities += result

    ## getting the count for each unique amenities

    df_cols = ['amenity', 'count']

    df_attr = pd.DataFrame(columns=df_cols)
    df_attr['amenity'] = amenities
    df_attr['count'] = 0

    ## grouping and sorting data
    df = df_attr.groupby(['amenity'], as_index=False).count().sort_values(['count'], ascending=False)
    
    print('--------------------------------------------------------------------------\n')
    print("The ten most popular features or facilities provided by air BnB hosts are: \n")
    print(df[:10].to_string(index=False))
    inquire_further_analysis()
    

def find_average_by_location():
    data = DATA
    location = str(input('Please input your desired location: '))

    location_data = data.loc[data['host_location'] == location.capitalize()]
    if location_data.empty:
        print(f'\nThere are no data for {location}')
    else:
        while True:
            try:
                print("\n For average review, type 'review'. \n For average price, type 'price'\n")
                search = str(input('Please input your desired search option: '))

                if search.lower() == 'review':
                    mean_review = location_data["review_scores_rating"].mean()
                    rounded_number = format(mean_review, ".2f")
                    print('--------------------------------------------------------------------------')
                    print(f'\nThe mean review scores rating in {location} is approximately {rounded_number}\n')
                    break
                elif search.lower() == 'price':
                    mean_price = location_data["price"].mean()
                    rounded_number = format(mean_price, ".2f")
                    print('--------------------------------------------------------------------------')
                    print(f'\nThe mean price in {location} is approximately {rounded_number}\n')
                    break
                else:
                    print('\nInappropriate search option! Try again\n')
                    continue
            except Exception as e:
                print(f"Error: {e}")
                continue
    inquire_further_analysis()
      

def review_ppts():
    data = DATA

    ## compile list of property types provided across all location

    property_list = data['property_type']

    ## getting the count for each unique amenities

    df_cols = ['property_list', 'count']

    df_ppts = pd.DataFrame(columns=df_cols)
    df_ppts['property_list'] = property_list
    df_ppts['count'] = 0

    ## grouping and sorting data

    df = df_ppts.groupby(['property_list'], as_index=False).count().sort_values(['count'], ascending=False)
    
    print('--------------------------------------------------------------------------\n')
    print("The ten most popular PROPERTY TYPES available to AirBnB hosts are: \n")
    print(df[:10].to_string(index=False))
    
    print('--------------------------------------------------------------------------\n')
    print('The ten least popular PROPERTY TYPES available to AirBnB hosts are: \n')
    print(df[-10:].to_string(index=False))
    inquire_further_analysis()

def initialize_analysis():
    print("\nTo see the top 10 most popular amenities or features that Airbnb hosts provide to customers, type '1'")
    print("To see the average 'price of stay' or 'review scores rating' in specified location, type '2'")
    print("To see the 10 most listed and the 10 least listed property types available in Air BnB, type '3'")


    search_param = int(input("\nPlease input your desired option: "))

    if search_param == 1:
        identify_amenities()

    elif search_param == 2:
        find_average_by_location()

    elif search_param == 3:
        review_ppts()

    else:
        print(f"'{search_param}' is an invalid input. Try again!")
        initialize_analysis()

# request further analysis, to come after satisfaction of each question1!!!
def inquire_further_analysis():
    while True:
        try:
            analyse_again = str(input("\nWould you like to make another analysis? (y/n): "))
            if analyse_again.lower() == 'y':
                initialize_analysis()
            elif analyse_again.lower() == 'n':
                print(f'\nThank you!\n')
                while True:
                    try:
                        main_menu = str(input("Would you like to return to main menu? (y/n): "))
                        if main_menu.lower() == 'y':
                            helpers.make_selection()
                        elif main_menu.lower() == 'n':
                            print(f'\nThank you!\n')
                            os._exit(0)
                        else:
                            print(f'{main_menu} is an invalid input. Try again!')
                            continue
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
            else:
                print(f'{analyse_again} is an invalid input. Try again!')
                continue
        except Exception as e:
            print(f"Error: {e}")
            continue

