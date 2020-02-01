# Write a Python code to calculate the speed for running a 10-kilometer race in 1 hours 5
# minutes 42 seconds. What is the average pace (time per mile in minutes and seconds)?
# What is the average speed in miles per hour?

distance = 10 * 0.62137
print('Distance in Miles: ', distance)
time1 = 1 * 60 + 5 + (42/60)
print('TIme taken in Minutes: ', time1)
time2 = 1 * 60 * 60 + 5 * 60 + 42
print('Time taken in Seconds: ', time2)
time3 = time1 / 60
print('Time taken in Hours: ', time3)
s1 = distance/time1
print('Speed in Miles/Minute: ', s1)
s2 = distance/time2
print('Speed in Miles/Seconds: ', s2)
s3 = distance/time3
print('Speed in Miles/hours: ', s3)
