GeoTracker - IP Geolocation Tracker
A simple Python tool that fetches the geolocation of an IP address and displays it on an interactive map.

 Features
- Get geolocation data (country, city, coordinates) for any IP address
- Auto-detect your current public IP if no IP is provided
- Generate an interactive HTML map with a location marker
- Clean, safe virtual environment setup

Requirements
- Python 3.8+ (pre-installed on Ubuntu/Debian)
- Linux/macOS/WSL (tested on Ubuntu)

Quick Setup (Step-by-Step)
1. Create & Activate Virtual Environment
```bash
# Create virtual env
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```
You’ll see `(.venv)` in your terminal prompt when active.

2. Install Dependencies
```bash
pip install requests folium
```

3. Run the Tool
```bash
python geotracker.py
```

### 4. View the Map
Open `ip_geolocation_map.html` in your web browser to see the location.

3. Save and run

Files Generated
- `geotracker.py` → Main script
- `ip_geolocation_map.html` → Interactive map
- `.venv/` → Virtual environment folder




Can’t open the map
Double-click `ip_geolocation_map.html` to open it in any browser.

 Notes
- Uses the free `ip-api.com` API (no API key needed)
- Safe for personal use
- Works offline after map generation


