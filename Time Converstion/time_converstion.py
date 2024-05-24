# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.




# Explanation of the Code:
# Extract AM/PM:

# period = s[-2:]: Extracts the last two characters of the string s to determine if it is AM or PM.
# Extract Time Components:

# hour = int(s[:2]): Converts the first two characters to an integer to get the hour.
# minute = s[3:5]: Extracts the minute part as a string.
# second = s[6:8]: Extracts the second part as a string.
# Convert Hour Based on AM/PM:

# If the period is "AM":
# If the hour is 12, it is midnight, so set the hour to 0.
# Otherwise, leave the hour unchanged.
# If the period is "PM":
# If the hour is 12, it is noon, so leave the hour unchanged.
# Otherwise, add 12 to the hour to convert it to 24-hour format.
# Format Hour:

# hour = f"{hour:02}": Ensures that the hour is formatted as a two-digit string.
# Construct the 24-hour Time String:

# return f"{hour}:{minute}:{second}": Combines the hour, minute, and second into the final 24-hour format string.
#=====================================================================================================================
import math
import os
import random
import re
import sys


# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.


def timeConversion(s):
    # Extracting the AM/PM part
    period = s[-2:]
    
    # Extracting the hour, minute, and second parts
    hour   = int(s[:2])
    minute = s[3:5]
    second = s[6:8]
    
    # Converting the hour part based on AM/PM
    if period    == "AM":
        if hour  == 12:
            hour = 0  
    else:  
        if hour  != 12:
            hour += 12  
    
    
    hour = f"{hour:02}"
    return f"{hour}:{minute}:{second}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = timeConversion(s)
    
    fptr.write(result + '\n')
    
    fptr.close()
