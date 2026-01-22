'''
Docstring for countDownTImer
TODO:
1. Import the time module using import time 
2. Get user to countdown duration (in seconds)
3. Convert input into integer
4. Define a funtion, countdown(t) to perform the countdown
5. Use a while loop to run the countdown until t reaches 0
6. Inside the loop:
    a. Use divmod(t, 60) to convert to min and secs
    b. format the time string using '{:02d}:{:02d}'.format(mins, secs)
    c. Print the time on the same line using end='\r' to overwrite the previous output
    d. Pause the loop for 1 second using time.sleep(1)
    e. Decrease t by 1 each iteration
7. After the loop finishes, print "Fire in the hole!!" to indicate the timer has ended
'''

# Import the time function
import time

#  Get user input for time duration
userInput = int(input("Enter the countdown duration(in seconds): "))

if userInput < 1:
    print("Enter a positive number!!")
    userInput = int(input("Enter the countdown duration(in seconds): "))

# Countdown time function
def countdownTime(t):
    while t:
        mins, secs = divmod(t, 60)

        timer = '{:02d}:{:02d}'.format(mins, secs)

        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Fire in the hole!!!")

countdownTime(userInput)
