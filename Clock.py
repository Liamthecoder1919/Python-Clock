import time

while True:
    current_time = time.strftime("%H:%M:%S")
    print("\r" + current_time, end="")
    time.sleep(1)
