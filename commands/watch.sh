rm src/logs/input_log.csv
touch src/logs/input_log.csv
echo 'Watching actions...'
echo 'Press ESC + mouse click to stop'
py src/watch.py
echo 'Automation stored successfully'