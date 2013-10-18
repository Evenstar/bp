import sys
D={}

def count():
    while True:
        line=sys.stdin.readline().strip()
        if not line:
            break
        try:
            line=line.split('\t')
            if not D.has_key(line[-1]):
                D[line[-1]]=0
            D[line[-1]]+=1
        except:
            sys.stderr.write('Wrong data format.\n')
            continue
    L=sorted(D.iteritems(),key=lambda x: x[1],reverse=True)
    return L

L=count()
for u,v in L:
    print str(u)+'\t'+str(v)
