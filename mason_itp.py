#coding:utf-8
#Date :Oct 11,2013
#Date :Oct 14,2013
#Description: Fixed a bug that the parent id can't be correctly displayed.
import sys
import re
import cPickle as pickle

rep=re.compile(r'\@(\S+)\s')

def load( fname ):
    ''' Load the name-id  dictonary.'''
    sys.stderr.write('Loading name-id dictionary.\n')
    D={}
    f=open(fname)
    try:
        D=pickle.load(f)
    except:
        sys.stderr.write('Error while loading.\n')
        quit()
    else:
        sys.stderr.write('Loading finished.\n')
    return D

def proc( line,D):
    '''Process a single line'''
    S=line[0]+'\t'+line[1]+'\t'
    if line[3]=='0':
        S+='0'+'\t'+line[5]
        return S
    match=rep.search(line[2])
    if match==None:
        S+=line[3]+'\t'+line[5]
        return S
    uname=match.group(1)
    if D.has_key(uname):
        S+=D[uname]+'\t'+line[5]
        return S
    else:
        S+='-1'+'\t'+line[5]
        return S

def run():
    #    D={}
#    fname=sys.argv[1]
    k=0
    D=load('../tools/idname.dump')
    while True:
        line=sys.stdin.readline()
        if not line:
            break
        k+=1
        if k%100000==0:
            sys.stderr.write(str(k)+'\n')
        try:
            line=line.decode('utf-8')
            line=line.split('\t')
            S=proc(line,D)
        except:
            sys.stderr.write('Wrong line.\n')
            continue
        else:
            print S.encode('utf-8'),

if __name__=='__main__':
    run()

