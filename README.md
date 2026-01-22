# ⏳ Countdown Timer (Python)

A simple **command-line countdown timer** built with Python.  
The program allows a user to enter a time duration in seconds and then counts down to zero, displaying the remaining time in **MM:SS** format.


## 📌 Features
- Takes user input for countdown duration (in seconds)
- Converts seconds into **minutes and seconds**
- Updates the timer in real-time on the same line
- Displays a message when the countdown ends


## 🛠️ Requirements
- Python 3.x  
- No external libraries required (uses Python’s built-in `time` module)


## 🚀 How It Works
1. The user enters a countdown duration in seconds.
2. The input is converted to an integer.
3. A function runs a loop that:
   - Converts seconds into minutes and seconds using `divmod`
   - Displays the time in `MM:SS` format
   - Pauses for one second between updates
4. When the countdown reaches zero, a message is displayed.

# Example Output
Enter the countdown duration(in seconds): 10 \
00:10 \
00:09 \
00:08 \
... \
Fire in the hole!!!
