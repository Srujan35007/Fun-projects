'''
Gets the number of redditors who are online at a particular time of the day.
[x] Get online metrics 
[x] Append to a Log file
'''
import time 
import praw # pip3 install praw
from datetime import datetime
print("Imports complete")


reddit = praw.Reddit(
    client_id = 'CLIENT_ID',
    client_secret = 'CLIENT_SECRET',
    username = 'AccountUsername',
    password = 'AccountPassword',
    user_agent = 'ABCD'
)

subreddit = reddit.subreddit('SUBREDDIT_NAME')
get_active_count = lambda : subreddit._fetch_data()['data']['accounts_active']
log_file = "./LogFILE.txt"

start_time = time.time()
run = True
log_count = 0
while run:
    if (time.time() - start_time)/(24*60*60) > 1:
        run = False
    else:
        pass
        
	date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M")
	active_count = get_active_count()
	with open(log_file, 'a') as append_file:
		append_file.write(f"{date_and_time} {active_count}\n")
	log_count += 1
	print(f"Log {log_count}. {date_and_time} => {active_count}")
	time.sleep(5*60)
