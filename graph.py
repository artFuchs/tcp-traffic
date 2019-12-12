import matplotlib.pyplot as plt
import sys

argslen = len(sys.argv)
if argslen < 2:
    print("python3 graph.py file1 file2 file3 ...")
    sys.exit(1)

for i in range(1,argslen):
    logFile = open(sys.argv[i],'r')
    lines = logFile.readlines()
    x=[]
    y=[]
    for l in lines:
        data = l.split()
        x.append(data[0])
        y.append(int(data[1]))
    plt.plot(x,y,label = sys.argv[i])

plt.xlabel('x - time')
plt.ylabel('y - bits/s')
plt.title('tcp trafic - bits/s X time')
plt.show()




