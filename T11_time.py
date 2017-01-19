#epoch:1970-01-01 00:00:00 UTC
#function time.time() return UnixTimestamp:the seconds from epoch to now
import time

starttime=time.time()
print"Program starts at %f"%starttime
for i in range(10):
	print i
endtime=time.time()
print"Program end at %f"%endtime
print"Total time is %f"%(endtime - starttime)

#time.sleep(secs)
print"Hold on..."
time.sleep(5)
print"Thank you for waiting!:)"