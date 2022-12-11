# Name: RAJESH KUMAR YADAV
# Sap id: 500084908
# Roll no: R2142201739
# Batch: 2(H)
# Course: Container Orchestration and Infrastructure Automation
# Program: BTECH CSE & Spl. CC&VT


# syntax=docker/dockerfile:1
FROM python:latest

WORKDIR /app

COPY . .

CMD [ "python", "server/server.py" ]
