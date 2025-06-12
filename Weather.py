#!/usr/bin/env python3

import requests
import json
import os

# Use KJXI – Fox Stephens Field directly
station_id = "KSHV"
headers = {"User-Agent": "weather-script-tj/1.0"}

try:
    # Get latest observation
    latest_obs_url = f"https://api.weather.gov/stations/{station_id}/observations/latest"
    response = requests.get(latest_obs_url, headers=headers, timeout=5)
    obs = response.json()
    props = obs.get("properties", {})

    # Extract and format values
    temp_c = props.get("temperature", {}).get("value")
    temp_f = round(temp_c * 9 / 5 + 32, 1) if temp_c is not None else "N/A"

    wind = props.get("windSpeed", {}).get("value")
    wind_mph = round(wind * 2.23694, 1) if wind is not None else "Calm"

    humidity = props.get("relativeHumidity", {}).get("value", "N/A")
    visibility = props.get("visibility", {}).get("value")
    visibility_mi = round(visibility / 1609.34, 1) if visibility is not None else "N/A"
    condition = props.get("textDescription", "Unknown")

    icon = ""  # Optional: map icons based on conditions

    tooltip = (
        f"<b>{condition}</b>\n"
        f"🌡️ Temp: {temp_f}°F\n"
        f"💨 Wind: {wind_mph} mph\n"
        f"💧 Humidity: {humidity}%\n"
        f"👁 Visibility: {visibility_mi} mi"
    )

    out_data = {
        "text": f"{icon}  {temp_f}°F",
        "alt": condition,
        "tooltip": tooltip,
        "class": "noaa"
    }

    print(json.dumps(out_data))

    # Write to local cache
    cache_out = f"{icon} {condition}\n  {temp_f}°F\n  {wind_mph} mph\n  {humidity}%\n  {visibility_mi} mi"
    with open(os.path.expanduser("~/.cache/.weather_cache"), "w") as f:
        f.write(cache_out)

except Exception as e:
    print(json.dumps({
        "text": "",
        "tooltip": f"Error: {str(e)}",
        "class": "error"
    }))
