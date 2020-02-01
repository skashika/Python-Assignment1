# I have started walking to home at 7:30 AM for the first mile at slow step (8 min:15 sec
# per mile), then 3 miles at speed (7 min:12 sec per mile), what time do I get home for
# breakfast? (format output in hh: min)

m1 = 8 + 15/60
print('Time in Minutes for First Mile ', m1)
m2 = 3 * 7 + 12/60
print('Time in Minutes for Remaining Miles ', m2)
ttw = m1 + m2
print('Total Time taken for the journey in Minutes ', ttw)
time_left_home_hrs = 7
time_left_home_mins = 30
time_min = time_left_home_mins + ttw
if time_min > 60:
    time_left_home_hrs = time_left_home_hrs + 1
    time_min = time_min - 60
print('Time to Home for Breakfast: ', time_left_home_hrs, ':', int(time_min), 'AM')
