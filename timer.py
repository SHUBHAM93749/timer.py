import time
seconds = input("enter the time in number of seconds")
def countdown(seconds):
    while seconds > 0:
        min = int(seconds/60)
        sec = int(seconds%60)
        timer  = f'{min}:{sec}'
        print(timer,end = '\r')
        time.sleep(1)
        seconds-=1
    print("Time is up")
countdown(int(seconds))