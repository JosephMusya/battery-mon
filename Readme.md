# Battery monitoring script/service for HP

# How to run

1. Clone the repository

```
git clone https://www.github.com/josephmusya/battery-mon
```

2. Create a service file under `/etc/systemd/system/battery_monitor.service`

```jsx
Description=Battery Monitoring Service
After=network.target

[Service]
ExecStart=python3 /home/mucia/Desktop/MyCode/batteryMon/main.py
Restart=always
User=mucia
RestartSec=5

[Install]
WantedBy=multi-user.target
```

3. Restart the daemon

```
sudo systemctl daemon-reload
```

4. Start the battery_monitor.service

```
sudo systemctl start battery_monitor.service
```

5. Check the status of the service

```
sudo systemctl status battery_monitor.service
```