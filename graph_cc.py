import sys
import copy

def walk(G, s, S=set()):
    '''Traverse the graph starting from s'''
    P,Q=dict(),set()
    P[s]=None
    Q.add(s)
    while Q:
        u=Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v]=u
    return P

def components(G):
    '''Compute the connected components in G, treated as an undirected graph'''
    comp=[]
    seen=set()
    for u in G:
        if u in seen: continue
        C=walk(G,u)
        comp.append(C)
        seen.update(C)
    return comp

def build( fname ):
    '''Build the graph from edge list, treated as an undirected graph'''
    G={}
    with open(fname) as f:
        for line in f:
            u,v=line.strip().split('\t')
            if not G.has_key(u):
                G[u]=set()
            if not G.has_key(v):
                G[v]=set()
            G[u].add(v)
            G[v].add(u)
    return G

def skeleton( G, L=1):
    Gs=copy.deepcopy(G)
    leaf=set()
    for u in G.keys():
        if len(G[u])==1:
            leaf.add(u)
            del(Gs[u])
    for u in Gs.keys():
        Gs[u]=Gs[u].difference(leaf)
    return Gs

if __name__=='__main__':
    fname=sys.argv[1]
    G=build(fname)
    comp=components(G)
    compsize=[]
    for i in xrange(len(comp)):
        compsize.append(len(comp[i]))
    compsize=sorted(compsize)
    deg=[]
    Gs=skeleton(G)
    for i in Gs.keys():
        deg.append(len(Gs[i]))
    deg=sorted(deg)
    print compsize
    print deg




