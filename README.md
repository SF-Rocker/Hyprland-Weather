# Hyprland-Weather
AI Generated Weather Script and shell script for weather add U for Imperial for Fahrenheit.
choose files $User/home/.config/hypr/UserScripts/
Use Thonny to Change Station ID to your Cloest Area just Bing "How to Find NOAA Weather Station ID Near Me, Or Ask Copilot by Microsoft."

```station_id = "KSHV"```

Change KSHV Shreveport to another Location.

Note the line in Python Bash Shell Script or Python3.sh in the UserScripts folder as follows

``` data=($(curl -s https://en.wttr.in/"$city"$1\?0qnTu 2>&1)) ```
At the End U is added for Imperial Units
Celsius was changed to Fahrenheit for you.
Metric = Celsius &
Imperial = Fahrenheit

# Other Note put these two files in the .config/hypr/UserScripts folder and overide existing data.
# Regular Hyprland Weather Script is a auto generated prediction based on your ISP's IP address, that could be 60 miles away from you.
