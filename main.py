import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def add_limiter(var,limit,change):
	if(var + change > limit):
		return 1
	else:
		var += change
		return 0

num = 0
print (bcolors.HEADER, "green is prime red is not")
while True:
  if num > 1:   
    for i in range(2, num):   
        if (num % i) == 0:
            
            num+=1
            
            break
            
    else: 
        print(bcolors.OKGREEN,num)
        num+=1
    
  else: 
    
    num+=1
    
  #time.sleep(1)