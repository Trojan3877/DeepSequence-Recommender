import time

events = [
    {"user": 1, "item": 101},
    {"user": 2, "item": 305}
]

for event in events:
    print("Producing event:", event)
    time.sleep(1)
