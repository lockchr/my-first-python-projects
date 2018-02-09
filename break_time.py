import webbrowser
import time

total_breaks = 3
break_count = 0

print("This Program started on:" ' ' + time.ctime())
while (break_count < total_breaks):
	time.sleep(7200)
	webbrowser.open("https://www.youtube.com/watch?v=NzY831Ubwbg&list=RDMMNzY831Ubwbg")
	break_count = break_count + 1