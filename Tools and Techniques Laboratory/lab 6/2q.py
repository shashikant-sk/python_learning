# 2.) Using class in python add two times and display the result.
  
#    ex :- Enter Time 1: 2:30:45
#          Enter time 3:45:22
#          -------------------
#          total time is 6:15:07
 


class Time: 
    def __init__(self, hours=0, minutes=0, seconds=0): # __init is used to initialize the attributes of the class
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def add(self, other):
        total_seconds = self.seconds + other.seconds # self.seconds and other.seconds are the attributes of the class # use of self is to access the attributes of the class
        carry_minutes, new_seconds = divmod(total_seconds, 60)
        
        total_minutes = self.minutes + other.minutes + carry_minutes
        carry_hours, new_minutes = divmod(total_minutes, 60)
        
        total_hours = self.hours + other.hours + carry_hours
        
        return Time(total_hours, new_minutes, new_seconds)
    
    def __str__(self):
        return f"{self.hours}:{self.minutes:02}:{self.seconds:02}"

# Prompt user for input
time1_str = input("Enter Time 1 (hh:mm:ss): ")
time2_str = input("Enter Time 2 (hh:mm:ss): ")

# Parse input strings into Time objects
time1 = Time(*map(int, time1_str.split(":")))
time2 = Time(*map(int, time2_str.split(":")))

# Add the two times
total_time = time1.add(time2)

# Display the result
print(f"Total time is {total_time}")

    

 


