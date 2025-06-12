# Hyprland-Weather
AI Generated Weather Script and shell script for weather add U for Imperial for Fahrenheit.
choose files $User/home/.config/hypr/UserScripts/
Use Thonny to Change Station ID to your Cloest Area just Bing "How to Find NOAA Weather Station ID Near Me, Or Ask Copilot by Microsoft."

```station_id = "KSHV"```

CHange KSHV Shreveport to another Location.

Note the line in Python Bash Shell Script as follows

``` data=($(curl -s https://en.wttr.in/"$city"$1\?0qnTu 2>&1)) ```
At the End U is added for Imperial Units
Celsius was changed to Fahrenheit for you.
Metric = Celsius
Imperial = Fahrenheit
