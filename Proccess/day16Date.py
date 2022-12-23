from datetime import datetime

'''

    Get the current day, month, year, hour, minute and timestamp from datetime module
    Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
    Today is 5 December, 2019. Change this time string to time.
    Calculate the time difference between now and new year.
    Calculate the time difference between 1 January 1970 and now.
    Think, what can you use the datetime module for? Examples:
        Time series analysis
        To get a timestamp of any activities in an application
        Adding posts on a blog
'''
now_date = datetime.now()
print("current date:{},{},{},{},{},{}".format(now_date.day,now_date.month,now_date.year,now_date.hour,now_date.minute,now_date.timestamp()))
time_format = now_date.strftime("%m/%d/%Y, %H:%M:%S")
print(time_format)

today = "5 December, 2019"
today_object = datetime.strptime(today,"%d %B, %Y")
print(today_object)

now = datetime(year = now_date.year, month = now_date.month, day = now_date.day, hour = now_date.hour, minute = now_date.minute, second = now_date.second)
new_year = datetime(year = 2023, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = new_year - now
print(diff)

spe_time = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff2 = now - spe_time
print(diff2)

'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
'''

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic,es,ru = names
print(nordic,es,ru)















