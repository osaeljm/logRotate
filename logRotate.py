import os
import subprocess

### Variables
logPath = '/Users/osaeljm/Documents/log'
listLog = []

os.chdir(logPath)
#logFile.append(os.system(ls))

#type(os.system('find . -type f -mtime +1'))

logFiles = subprocess.run('find . -type f -mtime +1', shell=True, capture_output=True, text=True)
#subprocess.run('ls -la', shell=True)
print(len(logFiles.stdout))
print(logFiles.stdout)

#subprocess.run(['rm', '-fr'], shell=True,input=logFiles.stdout)
#find . -type f -mtime +7

