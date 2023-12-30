#!/bin/bash

sudo mv /home/pi/CheckInternet/CheckInternet.service /etc/systemd/system/ && sudo systemctl daemon-reload
chmod +x -R /home/pi/CheckInternet/*
