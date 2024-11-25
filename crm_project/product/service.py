# different func for some backend logic
from datetime import datetime, timedelta

def stop_work(query,localtime):
    stop_time = localtime
    all_time = query.start_date
    work = (stop_time - all_time) + timedelta(hours=query.work_time.hour, minutes=query.work_time.minute, seconds=query.work_time.second)
   
    return str(work)
    
    