import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global city, day, month

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?): ").lower()
        if city in CITY_DATA:
            print('Valid city inputed')
            break
        else:
            print("please enter a valid city")
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        input_values = ['month', 'day', 'both', 'not at all']
        input_data = input("Would you like to filter the data by month, day, both or not at all?: ").lower()
        if input_data in input_values:
            print('Valid input')
            break
        else:
            print("please enter a valid input")

    while True:
        input_values = ["all", "january", "february", "march", "april", "may", "june", "monday", "tuesday", "wednesday", "thursday",                          "friday", "saturday", "sunday"]
        if input_data == 'month':
            month = input("Which month - All, January, February, March, April, May, or June?: ").lower()
            day = 'all'
            if month in input_values:
                print("valid input")
                break
            else:
                print("invalid input")
        elif input_data == 'day':
            day = input(" Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?: ").lower()
            month = 'all'
            if day in input_values:
                print("valid input")
                break
            else:
                print("invalid input")

        elif input_data == 'both':
            month = input("Which month - January, February, March, April, May, or June?: ").lower()
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?: ").lower()
            if day in input_values and month in input_values:
                print("valid input")
                break
            else:
                print("invalid input")

        else:
            month = 'all'
            day   = 'all'
            print('showing all data from', city)
            break

    print('-'*40)
    print('Filter: ', 'city:', city,'---', 'month:', month,'---', 'day:', day)

    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and week day
    """
    #load city data
    df = pd.read_csv(CITY_DATA[city])
    #converting start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extracting month, day of the week and hour from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        #index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    if month == 'all' and day == 'all':
        num_month = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        index_month = num_month - 1
        common_month = months[index_month]
        print("The Most Common month of travel for {} city is".format(city), common_month)
    # TO DO: display the most common week day of a month
    elif month != 'all' and day == 'all':
        common_week_day = df['day_of_week'].mode()[0]
        common_start_hour = df['hour'].mode()[0]
        print("For The Month Of {}".format(city))
        print("The Most Common hour is - {}".format(common_start_hour))
        print("The Most Common day is - {}".format(common_week_day))


    # To DO: displays the most common hours for a specified weekday for all months
    elif month == 'all' and day != 'all':
        common_start_hour = df['hour'].mode()[0]
        print("The Most Common hours on {}s for {}  city is: ".format(day, city), common_start_hour)

    # TO DO: display the most common start hour
    else:
        common_start_hour = df['hour'].mode()[0]
        print("The Most Common Start hours on {}s in the month of {} is: ".format(day, month), common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The Most commonly used start station - ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The Most commonly used end station - ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combo_station'] = df['Start Station'] + df['End Station']
    common_combo = df['combo_station'].mode()[0]
    print("The Most combination of start and end station is - ", common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time - ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time - ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_count = df['User Type'].value_counts()
    print("\nUser types count -\n", User_count)

    # TO DO: Display counts of gender
    print("\nGender count stat-\n")
    if city != 'washington':
        Gender_count = df['Gender'].value_counts()
        print('\n')
        print("\nGender count -\n", Gender_count)

        # TO DO: Display earliest, most recent, and most common year of birth
        Earlier_year = df['Birth Year'].head(1)
        print("\nEarlier yeah of birth -\n", Earlier_year)
        Most_recent = (df['Birth Year'].tail(1))
        print("\nMost recent year of birth -\n", Most_recent)
        Most_common = df['Birth Year'].mode()[0]
        print("\nMost common year of birth -\n", Most_common)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("\nNo Gender data to display from washington\n")


def data_display(df):
    """"Displays filtered raw data from bikeshare users."""

    print('\nDetailed view?...\n')
    start_time = time.time()
    # TO DO: Display a prompt that ask the user if they want to see 5 lines of raw data
    print("\nDo you wish to see the first 5 lines of raw data?\n")
    input_data = input("\n(Yes/No): \n").casefold()

    index_count = 5
    # TO DO: Display that data if the answer is 'yes',
    while input_data == 'yes':
        print(df.head(index_count))
        # TO DO: Displays the next 5 lines,
        print("\nDo you want to see the next 5 lines?\n")
        more = input("\n(Yes/No): \n").casefold()
        if more == 'yes':
            index_count += 5
            print('showing 5 more lines')
        else:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
