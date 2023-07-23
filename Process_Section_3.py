#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing libraries
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import helpers

def convert_to_df(file_name):
    #Read CSV file into dataframe
    data = pd.read_csv(file_name)
    global DATA
    DATA = data
    print('*** PREVIEW ***')
    print(data.head())
    
    
### Display the proportion of number of bedrooms of Airbnb listing using pie chart

def pie_plot():
    data = DATA
    bedrooms = data['bedrooms']

    ## getting the count for each unique amenities

    df_cols = ['bedrooms', 'count']

    df = pd.DataFrame(columns=df_cols)
    df['bedrooms'] = bedrooms
    df['count'] = 0

    ## grouping and sorting data

    df_ = df.groupby(['bedrooms'], as_index=False).count()

    # Filtering out insignificant data
    index_names = df_[ df_['count'] < 100 ].index
    index_price = df_[ df_['count'] < 100 ].count

    #sum rows in index positions
    sum = df_.iloc[index_names].sum()

    #Removing the insignificant rows
    df_.drop(index_names, inplace = True)

    ### Adding new row to the dataframe
    new_row = {'bedrooms':'others', 'count':sum['count']}
    df_ = pd.concat([df_, pd.DataFrame([new_row])], ignore_index=True)
    print('--------------------------------------------------------------------------\n')
    print(df_, end = '\n')

    # Creating plot
    fig = plt.figure(figsize =(10, 7))
    # 
    plt.pie(df_['count'].tolist(), labels= (df_['bedrooms']).tolist(), autopct= '%1.1f%%')
    plt.title("Distribution of 'Number of Rooms' across all Airbnb lettings")
    plt.legend(loc='best',bbox_to_anchor=(1.2,1))

    # show plot
    plt.show()
    inquire_further_visualization()
  

### Display the number of listings for each room type using bar chart

## compile list of room types provided across all location
def bar_plot():
    data = DATA
    df_room_types = data['room_type']

    ## getting the count for each unique amenities

    df_cols = ['room_type', 'count']

    df = pd.DataFrame(columns=df_cols)
    df['room_type'] = df_room_types
    df['count'] = 0

    ## grouping and sorting data

    df_ = df.groupby(['room_type'], as_index=False).count()

    print('--------------------------------------------------------------------------\n')
    print(df_, end = '\n')

    room_type = df_['room_type'].tolist()
    count = df_['count'].tolist()

    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(room_type, count, color ='maroon',
          width = 0.4)

    plt.xlabel("Room types")
    plt.ylabel("No. of listings")
    plt.title("No. of listings for each room type in Air BnB")
    plt.show()
    inquire_further_visualization()


### Display the relationship between accommodates and price using scatter plot

## compile list of property types provided across all location
def scatter_plot():
    data = DATA
    df_accommodates = data['accommodates']
    df_price = data['price']

    ## getting the count for each unique amenities

    accommodates = df_accommodates.tolist()
    price = df_price.tolist()


    # creating the scatter plot
    plt.scatter(accommodates, price, c ="blue")
    plt.xlabel("NO. OF PERSONS ACCOMODATED (y-axis)")
    plt.ylabel("PRICE (x-axis)")
    plt.title("Relationship between the number of people a lisitng accommodates and its price")

    # To show the plot
    plt.show()
    inquire_further_visualization()


### Display Airbnb prices from 2019 - 2022 with line chart using subplots

# Filter data as mean of each month's data

def filter_monthly(d_frame):
    month_mean = []
    for i in range(12):
        filtered_df = d_frame.loc[d_frame['host_since'].dt.month == i+1]
        mean_price = filtered_df['price'].mean()
        month_mean.append(mean_price)
    return month_mean 

# Convert the date to datetime64 
def subplot():
    data = DATA
    data['host_since'] = pd.to_datetime(data['host_since'], format='%d-%m-%y')

    # Filter data yearly 
    filtered_df_2019 = data.loc[(data['host_since'] >= '2019-01-01')
                                & (data['host_since'] < '2020-01-01')]

    filtered_df_2020 = data.loc[(data['host_since'] >= '2020-01-01')
                                & (data['host_since'] < '2021-01-01')]

    filtered_df_2021 = data.loc[(data['host_since'] >= '2021-01-01')
                                & (data['host_since'] < '2022-01-01')]

    filtered_df_2022 = data.loc[(data['host_since'] >= '2022-01-01')
                                & (data['host_since'] < '2023-01-01')]

    monthly_filter_2019 = filter_monthly(filtered_df_2019)
    monthly_filter_2020 = filter_monthly(filtered_df_2020)
    monthly_filter_2021 = filter_monthly(filtered_df_2021)
    monthly_filter_2022 = filter_monthly(filtered_df_2022)

    # making subplots
    months = ['Jan','Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, ax = plt.subplots(2, 2, sharex= False, sharey=True)
    fig.set_size_inches(12,10.5)
    fig.suptitle('PRICE TIME SERIES "2019 to 2022"')

    # set data with subplots and plot
    ax[0, 0].plot(months, monthly_filter_2019, marker= '.', linewidth = 3, mec= 'red')
    ax[0, 1].plot(months, monthly_filter_2020, marker= '.', linewidth = 3, mec= 'red')
    ax[1, 0].plot(months, monthly_filter_2021, marker= '.', linewidth = 3, mec= 'red')
    ax[1, 1].plot(months, monthly_filter_2022, marker= '.', linewidth = 3, mec= 'red')

    ax[0, 0].set_title("2019")
    ax[0, 1].set_title("2020")
    ax[1, 0].set_title("2021")
    ax[1, 1].set_title("2022")

    plt.ylabel('Price (£)')

    fig.tight_layout(pad=2.0)
    plt.show()
    inquire_further_visualization()


### satisfaction of customers across all listilngs

def ratings():
    data = DATA

    one_star_reviews = len(data.query('review_scores_rating<1.5'))
    two_star_reviews = len(data.query('review_scores_rating<2.5 & review_scores_rating>1.4'))
    three_star_reviews = len(data.query('review_scores_rating<3.5 & review_scores_rating>2.4'))
    four_star_reviews = len(data.query('review_scores_rating<4.5 & review_scores_rating>3.4'))
    five_star_reviews = len(data.query('review_scores_rating<5.5 & review_scores_rating>4.4'))


    one_star_experience = len(data.query('review_scores_value<1.5'))
    two_star_experience = len(data.query('review_scores_value<2.5 & review_scores_value>1.4'))
    three_star_experience = len(data.query('review_scores_value<3.5 & review_scores_value>2.4'))
    four_star_experience = len(data.query('review_scores_value<4.5 & review_scores_value>3.4'))
    five_star_experience = len(data.query('review_scores_value<5.5 & review_scores_value>4.4'))


    ratings = [one_star_reviews, two_star_reviews, three_star_reviews, four_star_reviews, five_star_reviews]
    experience = [one_star_experience, two_star_experience, three_star_experience, four_star_experience, five_star_experience]


    n=5
    r = np.arange(n)
    width = 0.25


    plt.bar(r, ratings, color = 'r',
            width = width, edgecolor = 'black',
            label='Review score of rating')
    plt.bar(r + width, experience, color = 'g', 
            width = width, edgecolor = 'black',
            label='Review score of value')

    plt.xlabel("Review ratings / Value score")
    plt.ylabel("Number of ratings")
    plt.title("Ratings across all Airbnb listings based on customer experience and value gotten compared to amount paid")
    plt.xticks(r + width/2,['1 star','2 star','3 star','4 star', '5 star'])
    plt.legend()

    plt.show()
    inquire_further_visualization()


def initialize_visualization():
    print("\nTo display the proportion of number of bedrooms of Airbnb listing using pie chart, type '1'")
    print("To display the number of listings for each room type using bar chart, type '2'")
    print("To display the relationship between accommodates and price using scatter plot, type '3'")
    print("To display Airbnb prices from 2019 - 2022 with line chart using subplots, type '4'")
    print("To display ratings across all Airbnb listings based on customer experience and value gotten, type '5'")

    search_param = int(input("\nPlease input your desired option: "))

    if search_param == 1:
        pie_plot()

    elif search_param == 2:
        bar_plot()

    elif search_param == 3:
        scatter_plot()

    elif search_param == 4:
        subplot()

    elif search_param == 5:
        ratings()

    else:
        print(f"'{search_param}' is an invalid input. Try again!")
        initialize_visualization()

# request further visualization, to come after satisfaction of each question1!!!
def inquire_further_visualization():
    while True:
        try:
            visualize_again = str(input("Would you like to see another visualization? (y/n): "))
            if visualize_again.lower() == 'y':
                initialize_visualization()
            elif visualize_again.lower() == 'n':
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
                print(f'{visualize_again} is an invalid input. Try again!')
                continue
        except Exception as e:
            print(f"Error: {e}")
            continue
            

