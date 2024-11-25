# different func for some backend logic
from datetime import datetime, timedelta

def stop_work(query,localtime):

    
    
    stop_time = localtime
    
    all_time = query.start_date
    
    
    
    split_list = [int(i) for i in query.work_time if i.isdigit()]
    time_dict = {'days': split_list[0],
                 'hours': split_list[1],
                 'minutes': split_list[2],
                 }
    db_time = timedelta(days=time_dict['days'], hours=time_dict['hours'], minutes=time_dict['minutes'])
    
    
    work = abs((stop_time - all_time)) + db_time
    
    second = work.total_seconds()
    answer = {'days' : int(second // 86400), 
                'hours' : int(second // 3600 % 24),
                'minutes': int(second // 60 % 60),
                }
   
    return f"{answer['days']} дней {answer['hours']} часов {answer['minutes']} минут"
    
    