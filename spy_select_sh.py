import sys
import threading
import os
filename=('xaa','xab','xac','xad','xae','xaf','xag','xah','xai','xaj','xak')

def select(mid, fname):
    prefix='../output/itp/'
    command='grep '+mid+' '+prefix+fname+' > '+fname+'.out'
    os.system(command)

def run( mid ):
    thread_list=[]
    for i in range(0,11):
        t=threading.Thread(target=select, args=(mid,filename[i],))
        thread_list.append(t)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    sys.stderr.write('Done')

def combine( mid ):
    fout=open(mid+'.out','w')
    for fname in filename:
        with open(fname+'.out') as f:
            for line in f:
                line=line.strip().split('\t')
                if line[-1]==mid and line[2]!= '-1': 
                    fout.write(line[1]+'\t'+line[0]+'\t'+line[2]+'\n')
    fout.close()
                
mid=sys.argv[1]
run(mid)
combine(mid)

