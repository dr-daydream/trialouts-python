#         time

import time 
# print(time.ctime(0))

# print(time.time())

#print(time.ctime(time.time()))
#time_ob = time.localtime()
#time_ob = time.gmtime()
#print(time_ob)
#hor_reg = time.strftime('%A %B %Y %H:%M:%S', time_ob)
#print(hor_reg)

#time_string = "23 February, 2022"
#time_ob = time.strptime(time_string,"%d %B, %Y")
#print(time_ob)

#    (year, month, day, hours, minutes, secs, #dayoftheweek, #dayoftheyear, #daylight savings time)

#time_tuple = (2022, 4, 20, 4, 20, 0, 3, 54, 0)
#time_string = time.asctime(time_tuple)
#print(time_string)

time_tuple = (1970, 6, 7, 14, 34, 0, 0, 0, 0,)
time_string = time.asctime(time_tuple)
print(time_string)