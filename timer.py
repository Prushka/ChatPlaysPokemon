import datetime
from file_handler import write_to_file

start_time = datetime.datetime.strptime('Dec 1 2019  3:00AM',
                                        '%b %d %Y %I:%M%p')


def refresh_timer():
    now = datetime.datetime.now()
    diff = now - start_time
    days, seconds = diff.days, diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    write_to_file("obs_timer.txt", f"第二个存档已开始 {days}天{hours}时{minutes}分")
