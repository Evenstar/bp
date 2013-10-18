import sys

ind=[]
oud=[]
while True:
    line=sys.stdin.readline().strip()
    if not line:
        break
    try:
        line=line.split()
        ind.append(long(line[1]))
        oud.append(long(line[2]))
    except:
        sys.stderr.write("wrong")
        continue
ind=sorted(ind,reverse=True)
oud=sorted(oud,reverse=True)


inf=open('indegree','w')
for item in ind:
    inf.write(str(item)+'\n')
inf.close()

ouf=open('outdegree','w')
for item in oud:
    ouf.write(str(item)+'\n')
ouf.close()

