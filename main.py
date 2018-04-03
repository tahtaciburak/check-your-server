########################################
#           CHECK YOUR SERVER          #
#                                      #
#   Its a simple tool that pings your  #
#   serves given below and generates   #
#   reports about uptime statuses.     #
#                                      # 
#   Author:  github.com/tahtaciburak   #
########################################

import schedule
import time
import os
import datetime
import json

'''
config = {
	'ping_count': '1',
	'frequency': 10,
	'logfile_path':'logs.log',
        'errorfile_path': 'error.log',
	'hosts': ['github.com']
}
'''

config_file= open('./config.json')
config = json.load(open('config.json'))

hosts = config['hosts']
ping_count = config['ping_count']
freq = config['frequency']
path = config['logfile_path']
errpath = config['errorfile_path']

fp = open(path,"a")
errfp = open(errpath,"a")

def ping_it(hostname):
	response = os.system("ping -c "+ping_count+" "+hostname)
	os.system("clear")
	log_data = ""
	if response == 0:
		time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		log_data = "Host: "+hostname+" "+" Time Stamp: "+time_stamp+" Status: [UP]\n"
		fp.write(log_data)
	else:
		time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		log_data = "Host: "+hostname+" "+" Time Stamp: "+time_stamp+" Status: [DOWN]\n"
		fp.write(log_data)
		errfp.write(log_data)

def PingJob():
	for hostname in hosts:
		ping_it(hostname)

# You can comment out if you need another time period
schedule.every(freq).seconds.do(PingJob)
#schedule.every(freq).minutes.do(PingJob)
#schedule.every(freq).days.do(PingJob)
#For more info check schedule module docs on PyPI

while True:
	schedule.run_pending()
	time.sleep(1)
