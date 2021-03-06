import rubik


def hash(a):
    h=0
    for i in range(0,len(a)):
        h=h+a[i]*(2**i)
    return h%335923


def search(a,b):
    if b==[]:
        return None
    i=0
    while i< len(b):
        if a==b[i][0]:
            return i
        i+=1
    return None


class queue():
    def __init__(self,a=None):
        self.l=a
    def enqueue(self,a):
        self.l.append(a)
    def isempty(self):
        if len(self.l)==0:
            return False
        else:
            return True
    def dequeue(self):
        if self.isempty():
            b=self.l[0]
            del(self.l[0])
            return b
        else:
            #print "Queue is empty"
            return None


class node():
    def __init__(self,li,parent= None,orientation = None):
        self.list = li
        self.parent = parent
        self.orientation = orientation
        self.child=[]
        for i in range(0,6):
            self.child.append(None)
	


def shortest_path(start, end):

    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if start==end:
        return []
    startroot=node(start)
    endroot=node(end)
    startq=queue([startroot,None])
    endq=queue([endroot,None])
    starth=[]
    endh=[]
    for i in range(0,335923):
        starth.append([])
        endh.append([])
    starth[hash(start)].append((start,None,None))
    endh[hash(end)].append((end,None,None))
    #startd[startroot.list]=(startroot.list,startroot.parent,startroot.orientation)
    #endd[endroot.list]=(endroot.list,endroot.parent,endroot.orientation)
    move=[rubik.F,rubik.Fi,rubik.L,rubik.Li,rubik.U,rubik.Ui]
    i=0
    while i<7:
        while True:
            g=startq.dequeue()
            if g is None:
                startq.enqueue(None)
                break
            j=0
            for k in move:
                m=rubik.perm_apply(k,g.list)
                if search(m,starth[hash(m)]) is None:
                    g.child[j]=node(m,g,k)
                    starth[hash(m)].append((m,g,k))
                    startq.enqueue(g.child[j])
                if search(m,endh[hash(m)]) is not None:
                    fr=path(m,starth[hash(m)])
                    br=path(m,endh[hash(m)])

                    fr.reverse()
                    return fr + br
                j+=1

        while True:
            g=endq.dequeue()
            if g is None:
                endq.enqueue(None)
                break
            j=0
            for k in move:
                m=rubik.perm_apply(rubik.perm_inverse(k),g.list)
                if search(m,endh[hash(m)]) is None:
                    g.child[j]=node(m,g,k)
                    endh[hash(m)].append((m,g,k))
                    endq.enqueue(g.child[j])

                if search(m,starth[hash(m)]) is not None:
                    fr=path(m,starth[hash(m)])
                    br=path(m,endh[hash(m)])
                    fr.reverse()

                    return fr + br

                j+=1
        i+=1
        #print i
    return None




def path(a,b):
    i=search(a,b)
    j=b[i]
    path=[]
    c=j[1]
    d=j[2]
    while d is not None:
        path.append(d)
        if c is not None:    
            d=c.orientation
            c=c.parent
    return path



'''start=rubik.F
end=rubik.I
start = rubik.I
middle = rubik.perm_apply(rubik.F, start)
end = rubik.perm_apply(rubik.L, middle)
start = rubik.I
middle1 = rubik.perm_apply(rubik.F, start)
middle2 = rubik.perm_apply(rubik.F, middle1)
end = rubik.perm_apply(rubik.Li, middle2)
start = rubik.I
middle1 = rubik.perm_apply(rubik.F, start)
middle2 = rubik.perm_apply(rubik.L, middle1)
middle3 = rubik.perm_apply(rubik.F, middle2)
end = rubik.perm_apply(rubik.L, middle3)
start = (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
end = rubik.I
start = (7, 8, 6, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
end = rubik.I
start = rubik.I
middle1 = rubik.perm_apply(rubik.F, start)
middle2 = rubik.perm_apply(rubik.L, middle1)
middle3 = rubik.perm_apply(rubik.F, middle2)
end = rubik.perm_apply(rubik.L, middle3)
print shortest_path(start,end)'''