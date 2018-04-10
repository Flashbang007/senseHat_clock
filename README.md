# senseHat_clock
A clock, that shows sensor data for the raspberry pi sense hat

# Install

Just copy `clock.py` to any folder and make it executable

# Usage 

Just execute
You may start it as dameon, by creating an systemD service.
```
[Service]
ExecStart=/PATH/TO/SCRIPT/clock_neu.py
Restart=on-abort
SuccessExitStatus=9 15 SIGKILL SIGTERM
[Install]
WantedBy=multi-user.target
```
