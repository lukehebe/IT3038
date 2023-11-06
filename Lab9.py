import requests


api_url = "http://localhost:3000/blue"

try:
 
    response = requests.get(api_url)

    
    if response.status_code == 200:
        data = response.json()
        
       
        for widget in data:
            widget_name = widget["name"]
            widget_color = widget["color"]
            print(f"{widget_name} is {widget_color}.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
