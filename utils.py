#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Libraries
import csv
import os
import Process_Section_1 as p_1
import Process_Section_2 as p_2
import Process_Section_3 as p_3

FILENAME_PATH = ''
HEADERS = ['host_id', 'name', 'description', 'host_name', 'host_since', 'host_location', 'host_response_time',
                       'host_response_rate', 'host_acceptance_rate', 'host_is_superhost', 'host_total_listings_count',
                       'host_verifications', 'host_identity_verified', 'property_type', 'room_type', 'accommodates',
                       'bathrooms_text', 'bedrooms', 'beds', 'amenities', 'price', 'minimum_nights', 'maximum_nights',
                       'instant_bookable', 'number_of_reviews', 'first_review', 'last_review', 'review_scores_rating',
                       'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin',
                       'review_scores_communication', 'review_scores_location', 'review_scores_value']

# Read the csv file
def read_file(file_uploaded):
    try:
        with open(file_uploaded, 'r') as file:
            csv_reader = csv.DictReader(file)
            dict_from_csv = dict(list(csv_reader)[0])

            # making a list from the keys of the dict
            list_of_column_names = list(dict_from_csv.keys())

            if (all(x in list_of_column_names for x in HEADERS) == False):
                print(f"You have uploaded the wrong file \n")
                process_file()
            else:
                global FILENAME_PATH
                FILENAME_PATH = file_uploaded
    except Exception as e:
        print(f'Error: {e}')
        print('Please input a valid file path or file name if file is available in the same directory as this script')
        retry_upload()
        process_file()

# Try uploading file again after a failed attempt
def retry_upload():
    while True:
        retry = str(input("Would you like to retry uploading? (y/n): "))
        if retry.lower() == 'y':
            break
        elif retry.lower() == 'n':
            print(f'Bye!')
            os.abort()
        else:
            print("Invalid input! Try again.")
            continue


# input filename or file path is being accessed for originality
def process_file():
    file_name = str(input("Input file name or path: "))
    print('******File is being assessed!*******''\n')
    read_file(file_name)

class Process():
    def __init__(self, file_name):
        self.file_name = file_name
    def process_with_csv(self):
        p_1.extract_file(self.file_name)
        p_1.initialize_search()
        return
    def process_with_pandas(self):
        p_2.convert_to_df(self.file_name)
        p_2.initialize_analysis()
        return
    def process_with_matplotlib(self):
        p_3.convert_to_df(self.file_name)
        p_3.initialize_visualization()
        return
