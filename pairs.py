import sys
while True:
    line=sys.stdin.readline().strip()
    if not line:
        break
    
    raw=line.split('\t')
    if raw[2]!='0' and raw[2]!='-1':
        print raw[0]+'\t'+raw[2]

