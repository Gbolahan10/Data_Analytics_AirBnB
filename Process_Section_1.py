#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Libraries
import csv
import os
import helpers

HEADERS = ['host_id', 'name', 'description', 'host_name', 'host_since', 'host_location', 'host_response_time',
                       'host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_total_listings_count',
                       'host_verifications', 'host_identity_verified', 'property_type', 'room_type', 'accommodates',
                       'bathrooms_text', 'bedrooms', 'beds', 'amenities', 'price', 'minimum_nights', 'maximum_nights',
                       'instant_bookable', 'number_of_reviews', 'first_review', 'last_review', 'review_scores_rating',
                       'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin',
                       'review_scores_communication', 'review_scores_location', 'review_scores_value']

def extract_file(file):
    rows = []
    with open(file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rows.append(row)
            global UPLOADED_FILE
            UPLOADED_FILE = rows
            

def search_by_hostID():
    rows = UPLOADED_FILE
    while True:
        try:
            host_id = int(input("Please input the host ID: "))
            break
        except:
            print("Ensure your input is an integer! \n")
            continue
    #finding the data by the specified host_id
    data = next((item for item in rows if item["host_id"] == str(host_id)), None)
    
    if not data:
        print(f"\nNo listing found with 'host_id': {host_id}")
    #returning the required data
    else:
        response = {}
        required_fields = ["name", "host_name", "description", "host_location", "host_since"]

        for i in required_fields:
            response[i]= data[i]
        
        print('--------------------------------------------------------------------------\n')
        print(response, end='\n')
    inquire_further_search()

def search_by_location():
    response = {}
    while True:
        try:
            input_location = str(input("Please input your desired location: "))
            break
        except Exception as e:
            print(f"Error: {e}")

    #finding the data with the specified location
    all_data = []

    for item in UPLOADED_FILE:
        if str(item["host_location"]) == input_location.capitalize():
            all_data.append(item)

    if len(all_data) > 0:
        #returning the required data

        while True:
            choose_to_specify = str(input("\nDo you have specific fields you would like to return?(y/n): "))
            if choose_to_specify.lower() == 'y':
                specify_fields = str(input("\nInput specific fields (seperate by space only): "))
                mod_specify_fields = [x.lower() for x in specify_fields.split()]
                if (all(x in HEADERS for x in mod_specify_fields) == False):
                    print(f"\nWrong input. Available fields are: {', '.join(HEADERS)} \n")
                    continue
                else:
                    required_fields = mod_specify_fields
                    break
            else:
                required_fields = ["host_name", "property_type", "price", "minimum_nights", "maximum_nights"]
                break
        if len(all_data) > 10:
            print('--------------------------------------------------------------------------\n')
            for data in all_data[:10]:
                for i in required_fields:
                    response[i] = data[i]
                print(response)
            print(f'... no. of responses = {len(all_data)}\n')
        else:
            print('--------------------------------------------------------------------------\n')
            for data in all_data:
                for i in required_fields:
                    response[i] = data[i]
                print(response)
        inquire_further_search()
    
    else:

        all_locations = [ sub['host_location'] for sub in UPLOADED_FILE ]
        locations = set(all_locations)

        print(f"\nOops! No listing found for {input_location} \n")
        print(f"The available locations are: {str(locations)} \n")

        while True:
            try_again = str(input("\nWould you like to try another location? (y/n): "))
            if try_again.lower() == 'y':
                search_by_location()
            elif try_again.lower() == 'n':
                print("Thank you! \n")
                break
            else:
                print("Invalid input! \n")
                continue
        
    inquire_further_search()


# search by property type
def search_by_property_type():
    while True:
        try:
            input_property_type = str(input("\nPlease input your desired property type: "))
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

    #finding the data with the specified location
    all_data = []
    for item in UPLOADED_FILE:
        if str(item["property_type"]).lower() == input_property_type.lower():
            all_data.append(item)

    if len(all_data) > 0:
        #returning the required data
        response = {}
        print('--------------------------------------------------------------------------\n')

        for data in all_data:
            required_fields = ["room_type", "accommodates", "bathrooms_text", "bedrooms", "beds"]
            for i in required_fields:
                response[i] = data[i]
            print(response, end="\n")
        inquire_further_search()
    else:
        all_property_types = [ sub['property_type'] for sub in UPLOADED_FILE ]
        property_types = set(all_property_types)

        print(f"\nOops! No listing found for {input_property_type} \n")
        print(f"The available property types are: {str(property_types)} \n")

        try_again = str(input("\nWould you like to try another property type? (y/n): "))
        while True:
            if try_again.lower() == 'y':
                search_by_property_type()
            elif try_again.lower() == 'n':
                print("\nThank you! \n")
                break
            else:
                print("\nInvalid input! \n")
                continue

        inquire_further_search()

# Giving the user options to select from
def initialize_search():
    print("\nTo search by 'host_id', type '1'")
    print("To search by 'location', type '2'")
    print("To search by 'property type', type '3'\n")

    search_param = int(input("Please input your desired search option: "))

    if search_param == 1:
        search_by_hostID()

    elif search_param == 2:
        search_by_location()

    elif search_param == 3:
        search_by_property_type()

    else:
        print("\nInvalid input! Try again\n")
        initialize_search()

# request further search, to come after satisfaction of each question1!!!
def inquire_further_search():
    while True:
        try:
            search_again = str(input("\nWould you like to make another search? (y/n): "))
            if search_again.lower() == 'y':
                initialize_search()
            elif search_again.lower() == 'n':
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
                print(f'{search_again} is an invalid input. Try again!')
                continue
        except Exception as e:
            print(f"Error: {e}")
            continue

