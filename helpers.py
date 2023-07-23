import utils

def make_selection():
    init_file = utils.Process(str(utils.FILENAME_PATH))
    print("\nMAIN MENU")
    print("\nTo make queries with available filters, type '1'\n")
    print("To view available data analysis on data, type '2'\n")
    print("To visualize available graphical representation of data, type '3'\n")
    selection = int(input("What will you like to do with your uploaded file?: "))

    if selection == 1:
        init_file.process_with_csv()
    elif selection == 2:
        init_file.process_with_pandas()
    elif selection == 3:
        init_file.process_with_matplotlib()
    else:
        print('Invalid input. Try again!')
        make_selection(process_instance)