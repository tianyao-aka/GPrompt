import time
import random
import warnings
warnings.filterwarnings("ignore")



if __name__ == '__main__':
    # Calculate total seconds for 10 days
    total_seconds = 14 * 24 * 60 * 60
    end_time = time.time() + total_seconds
    while time.time() < end_time:
        print(random.randint(1, 100))  # Print a random integer between 1 and 100
        time.sleep(600)  # Wait for 60 seconds