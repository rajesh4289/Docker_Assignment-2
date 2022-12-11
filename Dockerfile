# Author: ISHA SHARMA
# SAP ID: 500082723
# ROLL NO: R214220530
# Batch: 5
# Course: Container Orchestration and Infrastructure Automation
# Program: BTECH CSE & Spl. CC&VT


# syntax=docker/dockerfile:1
FROM python:latest

WORKDIR /app

COPY . .

CMD [ "python", "server/server.py" ]
