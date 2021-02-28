import schedule
import time
import os

def updates():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade -y")
    os.system("sudo apt-get update")
    os.system("rpi-update")

schedule.every().day.at("00:00").do(updates)

while True:
    schedule.run_pending()
    time.sleep(1)