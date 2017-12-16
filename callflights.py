import os, schedule, time

def job():
    os.system('python FlightNotifier.py')

#schedule.every(10).minutes.do(job)
while True:
    job()
    time.sleep(600)
