import schedule 
import time 

def job(): 
    print("hellow world") 


#schedule.every(1).seconds.do (job) 
#schedule.every().hour.do(job) 
schedule.every().day.at("20:31").do(job) 
#schedule.every().monday.do(job) 
#schedule.every()wednesday.at("13:55").do(job)  
#schedule.every().minute.at(":17").do(job) 

while True: 
    schedule.run_pending() 
    time.sleep(1) 