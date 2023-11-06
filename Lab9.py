import requests

# Define the URL of your Node.js API
api_url = "http://your-node-api-url-here"

try:
    # Send a GET request to the Node.js API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Iterate through the list of widgets and print their names and colors
        for widget in data:
            widget_name = widget["name"]
            widget_color = widget["color"]
            print(f"{widget_name} is {widget_color}.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
