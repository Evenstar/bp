import sys
import cPickle as pickle

D={}
k=0
with open('../../data/userIds') as f:
    for line in f:
        k+=1
        if k % 100000==0:
            sys.stderr.write(str(k)+'\n')
        line=line.strip().split('\t')
        D[line[0]]=int(line[1])
fout=open('folnum.dump','w')
pickle.dump(fout,D)
fout.close()

