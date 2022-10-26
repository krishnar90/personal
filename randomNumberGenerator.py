# program to continuously output random numbers to visualize on grafana
import random
import time
i=10
while i > 0:
    print (random.randint(0,100))
    time.sleep(10)
