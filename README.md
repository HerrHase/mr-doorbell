# Mr. Doorbell

```bash
sudo nano /lib/systemd/system/mrdoorbell.service
```

```bash
[Unit]
Description=Dummy Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/bin/mrdoorbell.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable mrdoorbell.service
sudo systemctl start mrdoorbell.service
```
