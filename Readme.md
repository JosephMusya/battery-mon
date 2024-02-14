# Battery monitoring script/service for PC

# How to run

1. Clone the repository

```
git clone https://github.com/JosephMusya/battery-mon.git
```

2. Create a service file under `/etc/systemd/system/battery_monitor.service`

```jsx
Description=Battery Monitoring Service
After=network.target

[Service]
ExecStart=python3 /path/to/main/py/file
Restart=always
User=YOUR_COMPUTER_USER
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
