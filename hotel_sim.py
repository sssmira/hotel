import sys
import json
from argparse import ArgumentParser
import seaborn as sns
import pandas as pd

"""Hotel Transylvania themed hotel booking simulator. Or otherwise known as our
'Boo-king Program'. This program takes in a JSON file and CSV file to find
the best vacation spot and best vacation activities for the user based on their
preferences.
"""
class Hotel:
    """Class docstring do later
    """
   
    def __init__(self, json_data, csv_data):
        
        # call user_prefs from init 
        # decide to call other methods from init or main
        # place json file here?
        self.hotels_dict = {}
        self.hotels_dict["hotel name"] = json_data["places"]["place name"]
        self.hotels_dict["location"] = json_data["places"]["location"]
        self.hotels_dict["prices"] = json_data["places"]["prices"]
        self.hotels_dict["date"] = json_data["places"]["dates"]
        
        self.csv_data = csv_data
    
    def user_prefs(self):
        """_summary_
        """
        user_data = {}
        name = input("Enter your name: ")
        guests = input("Enter the number of guests (1-3): ")
        nights_staying = input("Enter how many nights you will be staying: ")
        budget = input("Enter the max you are willing to spend for the entire trip: ")
        location = input("Enter your preferred (ROM, SVK, USA, or OCEAN)): ")
        date = input("Enter the month of your visit: ")
        
        user_data['name'] = name
        user_data['guests'] = guests
        user_data["nights_staying"] = nights_staying
        user_data['budget'] = budget
        user_data['location'] = location
        user_data['date'] = date
        
        
    def check_location(self, preferred_location, max_distance):
        # idek what to do abt this
        
        # Define the coordinates of the preferred location
        self.preferred_coords = (preferred_location['latitude'], preferred_location['longitude'])

        nearby_hotels = []
        for hotel in hotels_data:
            hotel_coords = (float(hotel[1]), float(hotel[2]))
            # Assuming latitude is in index 1, and longitude in index 2
            distance = (preferred_coords, hotel_coords).miles

            if distance <= max_distance:
                nearby_hotels.append({'name': hotel[0], 'distance': distance})

        return nearby_hotels

    def check_budget(self):
        """Jeni's method
        checks if user's budget is withing range of possible hotel options.
        
        Args:
            user_budget (float): The user's inputted budget amount
            file_dict (dict): Dictionary of all hotels and their details from an external file.
            
        Returns:
            list: A list of hotels that are within the user's specified budget.
        """
        # potential list comprehension lines 66-74
        budget_hotels = []
        
        for hotel_name, details in file_dict.items():
            hotel_price = details.get("price", 0)
            if hotel_price <= user_budget:
                if budget_hotels.append(hotel_name):
                    # idk if part of got lost or if it never got implemented
                    # but come back and fix
                    pass
        
        if budget_hotels:
            print(f"Hotels within budget: {', '.join(budget_hotels)}")
        else:
            print("No hotels within inputted budget price")
            
        return budget_hotels
        

    def check_date(self, file_dict):
        """Kassia's method. Checks if user's preferred date is within range 
        of possible hotel options.
        
        Args:
            file_dict (dict): Dictionary of all hotels and their details from
            an external file.
            
            
        Side Effects:
        Prints list with matching hotel name's and dates.
        """
        user_date = input('Enter your preferred date:')
       
        
        chosen_date = [f"{name} {details[1]}" for name, details
                       in file_dict.items() if user_date == details[1]]
        print(chosen_date)
        
        if len(chosen_date) == 0:
             print ('No avaiable dates. Try again.') 
    
    def find_intersection(self, user_data, file_dict):
        """Samira's method. Takes a dictionary made from the user's preferences
        dictionary made earlier and a dictionary from the json file. Finds
        the best hotel that matches the user's specified preferences from 
        earlier.
        
        Args:
            user_dict (dict): Dictionary of all the user's answers for each
            question asked earlier, has their preference in hotels.
            file_dict (dict): Dictionary of all hotels and their details from
            an external file.
        
        Returns:
            best_hotel (dict key): Name of the best hotel found from 
            intersection
        """
        best_hotel = None
        num_intersections = 0
        
        # convert dictionary to set
        # get container of keys in the dictionary 
        for hotel_name, hotel_details in file_dict.items():
            intersection = user_data.intersection(hotel_details)
            if len(intersection) > num_intersections:
                num_intersections = len(intersection)
                best_hotel = hotel_name
        return best_hotel

def read_file(filename):
    """Sathya's function
    Load hotel data from a JSON file and return a list of hotel objects or dictionaries.

    Parameters:
    filename (str): The path to the JSON file containing hotel data.

    Returns:
    list: A list of hotel objects or dictionaries with the hotel data.
    """
    try:
        with open(filename, 'r') as file:
            hotel_data = json.load(file)
            hotels = []
            for hotel in hotel_data:
                hotel_dict = {
                    'name': hotel['name'],
                    'location': hotel['location'],
                    'rating': hotel['rating'],
                    'price': hotel['price'],
                }
                hotels.append(hotel_dict)
            return hotels
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filename}.")
        return []
    # don't catch random exceptions
    except Exception as e:
        print(f"An error occurred: {e}")
        # why are you returning an empty list???? 
        return []

def main(json_filepath, csv_filepath):
    """Finds the the hotel that matches the user preferences based on 
    the user's input using the data from the specificed file.
    """
    
    # come back and fix
    json_data = read_file(json_filepath)
    csv_data = pd.read_csv(csv_filepath)
    
    my_trip = Hotel(json_data, csv_data)


def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect one mandatory argument:
        - filepath: a path to a file with list of hotel objects 
        or dictionaries.
       
       
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    

    parser = ArgumentParser()
    parser.add_argument("filename", help="JSON file with hotel data")
    return parser.parse_args(arglist)
  
if __name__ == '__main__':
    main()
