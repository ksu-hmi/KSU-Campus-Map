import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import requests
from geopy.geocoders import Nominatim
import webbrowser
import folium
import cv2
import os
import time  # Added for splash screen timing

# Create a function for the splash screen
def show_splash_screen():
    splash_window = tk.Toplevel(screen)
    splash_window.title("KSU Campus Map")
    splash_window.geometry("400x300")
    
    # Customize your splash screen content here (e.g., add a label or image)
    splash_label = tk.Label(splash_window, text="Loading...", font=("Helvetica", 24))
    splash_label.pack(pady=50)
    
    # Simulate some initialization work (replace with your actual initialization code)
    time.sleep(3)  # Display the splash screen for 3 seconds
    
    # Close the splash screen after initialization
    splash_window.destroy()

# Function to handle the search button click
def search():
    area_to_search = entry_box.get()
    if area_to_search:
        # Use the HERE Geocoding API to obtain the coordinates of the entered area
        coordinates = get_coordinates(area_to_search)

        if coordinates:
            # Get the user's current location (you can customize this part)
            user_location = geolocator.geocode("User's Location")

            if user_location:
                # Create a folium map centered on the user's location
                m = folium.Map(location=[user_location.latitude, user_location.longitude], zoom_start=15)

                # Add a marker for the area's coordinates
                folium.Marker(location=coordinates, popup=area_to_search).add_to(m)

                # Save the map to an HTML file
                map_filename = "map.html"
                m.save(map_filename)

                # Specify the web browser to use (chrome)
                browser = webbrowser.get('chrome')
                browser.open(map_filename)
                print("Opening the map with chrome browser")
                print("Map opened")
            else:
                print("User's location not found")
        else:
            print("Area not found")

# Function to open KSU map URL in a web browser
def open_ksu_map():
    ksu_map_url = "https://www.google.com/maps/d/u/0/edit?mid=1GIuyaNsI8wOg-snB8uRltgF3vvZcNIM&ll=34.04018570303751%2C-84.58284579999999&z=17"
    webbrowser.open(ksu_map_url)

# Function to use the HERE Geocoding API
def get_coordinates(area_name):
    response = requests.get(f"{base_url}?q={area_name}&apiKey={api_key}")
    data = response.json()
    items = data.get('items', [])
    if items:
        position = items[0].get('position')
        if position:
            return [position['lat'], position['lng']]
    return None

# Initialize geolocator and HERE API key
geolocator = Nominatim(user_agent="myGeocoder")
api_key = 'HH952QCVVYRXnw4BleCry3gJQlJ2RmKPPj9WgRAlioU' # HERE API key
base_url = 'https://geocode.search.hereapi.com/v1/geocode'



# Create the Tkinter window
screen = tk.Tk()
screen.title("Kennesaw State Campus")
screen.geometry("930x610")

# Call the splash screen function before creating the GUI elements
show_splash_screen()

# Create the GUI elements (after the splash screen)
title_question = tk.Label(screen, text="Areas to Search:")
title_question.pack(side=TOP)

entry_box = tk.Entry(screen)
entry_box.pack(side=TOP)

search_button = tk.Button(screen, text="Search", bg="Yellow", command=search)
search_button.place(x=550, y=20)

# Create the "KSU Map" button
ksu_map_button = tk.Button(screen, text="KSU Map", bg="goldenrod", command=open_ksu_map)
ksu_map_button.place(x=650, y=20)  # Adjust the position as needed

# Load and display the map image
map_image_path = 'Campus.png'
if os.path.exists(map_image_path):
    map_image = cv2.imread(map_image_path)
    img = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(map_image, cv2.COLOR_BGR2RGB)))
    panel = tk.Label(screen, image=img)
    panel.image = img
    panel.pack(side=BOTTOM)

# Start the Tkinter main loop
screen.mainloop()
