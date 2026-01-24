import time
import winsound

minutes = int(input("Enter minutes for the countdown: "))

while minutes > 0:
    print("Time left: {} minutes".format(minutes))
    minutes -= 1
    time.sleep(60)  # Wait for 60 seconds

print("Time's up!")
winsound.Beep(1000, 2000)  # Beep at 1000 Hz for 2 seconds
