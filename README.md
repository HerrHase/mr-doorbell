# Mr. Doorbell

```bash
sudo nano /lib/systemd/system/mrdoorbell.service
```

```bash
[Unit]
Description=Doorbell Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 <path-to-script>/mrdoorbell.py
User=pi

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable mrdoorbell.service
sudo systemctl start mrdoorbell.service
```
