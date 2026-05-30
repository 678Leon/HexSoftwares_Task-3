import requests
import folium

def get_ip_geolocation(ip_address=None):
    url = f"http://ip-api.com/json/{ip_address if ip_address else ''}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'fail':
            raise Exception(f"API Error: {data['message']}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def display_map(geolocation_data):
    if not geolocation_data:
        print("No geolocation data available.")
        return
    lat = geolocation_data['lat']
    lon = geolocation_data['lon']
    city = geolocation_data['city']
    country = geolocation_data['country']
    ip = geolocation_data['query']
    map_obj = folium.Map(location=[lat, lon], zoom_start=10)
    popup_text = f"IP: {ip}<br>Location: {city}, {country}<br>Coordinates: {lat}, {lon}"
    folium.Marker(location=[lat, lon], popup=folium.Popup(popup_text, max_width=300),
                    icon=folium.Icon(color="red", icon="location-dot")).add_to(map_obj)
    map_file = "ip_geolocation_map.html"
    map_obj.save(map_file)
    print(f"Map saved to {map_file}")

if __name__ == "__main__":
    target_ip = None
    geo_data = get_ip_geolocation(target_ip)
    if geo_data:
        print(f"IP: {geo_data['query']}")
        print(f"Location: {geo_data['city']}, {geo_data['country']}")
        print(f"Coordinates: {geo_data['lat']}, {geo_data['lon']}")
        display_map(geo_data)
