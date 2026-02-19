import shutil, sys, random, time

width = shutil.get_terminal_size()[0]  # fetch terminal window width
cols = [0] * width
try:
    while True:  # infinite rows for infinite scrolling
        for i in range(width):
            if (random.random() < 0.02):  # for only <2% of chances
                cols[i] = random.randint(4,14)  # size of 1s & 0s stream is between 4 & 14
            if cols[i] == 0:
                print(" ", end='')
            else:
                print(random.choice([0,1]), end='')
                cols[i] -= 1
        print()
        time.sleep(0.1)  # delay 0.1s for slow,visible print flow
    
except KeyboardInterrupt:  # capture key pressing as stop signal
    sys.exit()