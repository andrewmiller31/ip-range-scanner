'''
By Andrew Miller
1/7/2019

Use this script to ping a range of IPs and find how many receive a response. 

Declare the range be declaring the start and end number between 0 and 255 for W.X.Y.Z
'''
import os
import datetime
import subprocess
import datetime

start = datetime.datetime.now()

ips = []
commands = []

a1 = input('Start range for W (W.X.Y.Z)\n')
b1 = input('End range for W (W.X.Y.Z)\n')
a2 = input('Start range for X (W.X.Y.Z)\n')
b2 = input('End range for X (W.X.Y.Z)\n')
a3 = input('Start range for Y (W.X.Y.Z)\n')
b3 = input('End range for Y (W.X.Y.Z)\n')
a4 = input('Start range for Z (W.X.Y.Z)\n')
b4 = input('End range for Z (W.X.Y.Z)\n')
 

for w in range(int(a1),int(b1)+1):
  for x in range(int(a2),int(b2)+1):
    for y in range(int(a3),int(b3)+1):
      for z in range(int(a4),int(b4)+1):
	ip = str(w) + '.' + str(x) + '.' + str(y) + '.' + str(z)
	ips.append(ip)

for ip in ips:
  commands.append(["ping","-c","1","-w","1",ip])

def openProcess():
  if len(commands) > 0:
    try:
      p = subprocess.Popen(commands[-1])
    except OSError:
      p.terminate()
      return None,False
    return p,True
  else:
    return None,False

def pings():
  onL = 0
  offL = 0
  
  while(0 < len(commands)):
    processes = []
    count = 0
    while count < 10000:
      p,s = openProcess()
      if s == True:
        del commands[-1]
        processes.append(p)
      count += 1
    for p in processes:
      p.wait()
      if p.returncode == 0:
        onL += 1
      else:
        offL += 1

  return onL,offL

online = 0
offline = 0

start = datetime.datetime.now()

online,offline = pings()

on = 0
off = 0

end = datetime.datetime.now()

print("Start time:")
print(start)
print("End time:")
print(end)
print("Offline:",offline)
print("Online:",online)

