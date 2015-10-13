import rubik
import time


def hash(a):
    h=0
    for i in range(0,len(a)):
        h=h+a[i]*(24**i)
    return h%335923


def search(a,b):
    for i in range(0,len(b)):
        if a==b[i]:
            return True
    if i == len(b)-1:
        return False

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
        self.orientation = None
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
    startd={}
    starth[hash(start)]=(start,None,None)
    endd={}
    endh[hash(end)]=(end,None,None)
    startd[startroot.list]=(startroot.list,startroot.parent,startroot.orientation)
    endd[endroot.list]=(endroot.list,endroot.parent,endroot.orientation)
    i=0
    while i<7:
        while True:
            g=startq.dequeue()
            if g==None:
                startq.enqueue(None)
                break

            if rubik.perm_apply(rubik.F,g.list) is not starth[hash(rubik.perm_apply(rubik.F,g.list))]:
                g.child[0]=node(rubik.perm_apply(rubik.F,g.list),g.list,rubik.F)
                starth[hash(rubik.perm_apply(rubik.F,g.list))].append((rubik.perm_apply(rubik.F,g.list),g.list,rubik.F))
                startq.enqueue(g.child[0])
            if rubik.perm_apply(rubik.F,g.list) is endh[hash(rubik.perm_apply(rubik.F,g.list))]:
                fr=moves(rubik.perm_apply(rubik.F,g.list),starth)
                br=moves(rubik.perm_apply(rubik.F,g.list),endh)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.Fi,g.list) is not starth[hash(rubik.perm_apply(rubik.Fi,g.list))]:
                g.child[1]=node(rubik.perm_apply(rubik.Fi,g.list),g.list,rubik.Fi)
                starth[hash(rubik.perm_apply(rubik.Fi,g.list))].append((rubik.perm_apply(rubik.Fi,g.list),g.list,rubik.Fi))
                startq.enqueue(g.child[1])
            if rubik.perm_apply(rubik.Fi,g.list) is endh[hash(rubik.perm_apply(rubik.Fi,g.list))]:
                fr=moves(rubik.perm_apply(rubik.Fi,g.list),starth)
                br=moves(rubik.perm_apply(rubik.Fi,g.list),endh)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.L,g.list) is not starth[hash(rubik.perm_apply(rubik.L,g.list))]:
                g.child[2]=node(rubik.perm_apply(rubik.L,g.list),g.list,rubik.L)
                starth[hash(rubik.perm_apply(rubik.L,g.list))].append((rubik.perm_apply(rubik.L,g.list),g.list,rubik.L))
                startq.enqueue(g.child[2])
            if rubik.perm_apply(rubik.L,g.list) is endh[hash(rubik.perm_apply(rubik.L,g.list))]:
                fr=moves(rubik.perm_apply(rubik.L,g.list),starth)
                br=moves(rubik.perm_apply(rubik.L,g.list),endh)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.Li,g.list) is not starth[hash(rubik.perm_apply(rubik.Li,g.list))]:
                g.child[3]=node(rubik.perm_apply(rubik.Li,g.list),g.list,rubik.Li)
                starth[hash(rubik.perm_apply(rubik.Li,g.list))].append((rubik.perm_apply(rubik.Li,g.list),g.list,rubik.Li))
                startq.enqueue(g.child[3])
            if rubik.perm_apply(rubik.Li,g.list) is endh[hash(rubik.perm_apply(rubik.Li,g.list))]:
                fr=moves(rubik.perm_apply(rubik.Li,g.list),starth)
                br=moves(rubik.perm_apply(rubik.Li,g.list),endh)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.U,g.list) is not starth[hash(rubik.perm_apply(rubik.U,g.list))]:
                g.child[4]=node(rubik.perm_apply(rubik.U,g.list),g.list,rubik.U)
                starth[hash(rubik.perm_apply(rubik.U,g.list))].append((rubik.perm_apply(rubik.U,g.list),g.list,rubik.U))
                startq.enqueue(g.child[4])
            if rubik.perm_apply(rubik.U,g.list) is endh[hash(rubik.perm_apply(rubik.U,g.list))]:
                fr=moves(rubik.perm_apply(rubik.U,g.list),starth)
                br=moves(rubik.perm_apply(rubik.U,g.list),endh)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.Ui,g.list) is not starth[hash(rubik.perm_apply(rubik.Ui,g.list))]:
                g.child[5]=node(rubik.perm_apply(rubik.Ui,g.list),g.list,rubik.Ui)
                starth[hash(rubik.perm_apply(rubik.Ui,g.list))].append((rubik.perm_apply(rubik.Ui,g.list),g.list,rubik.Ui))
                startq.enqueue(g.child[5])
            if rubik.perm_apply(rubik.Li,g.list) is endh[hash(rubik.perm_apply(rubik.Ui,g.list))]:
                fr=moves(rubik.perm_apply(rubik.Ui,g.list),starth)
                br=moves(rubik.perm_apply(rubik.Ui,g.list),endh)
                fr.reverse()

                z=fr+br

                return z

    


        while True:
            k=endq.dequeue()
            if k==None:
                endq.enqueue(None)
                break

            if rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list) is not endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list))]:
                k.child[0]=node(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),k.list,rubik.F)
                endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list))].append((rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),k.list,rubik.F))
                endq.enqueue(k.child[0])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list) is starth[hash(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list))]:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),starth)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),endh)
                fr.reverse()
                z=fr+br

                return z

            if rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list) is not endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list))]:
                k.child[1]=node(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),k.list,rubik.Fi)
                endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list))]=(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),k.list,rubik.Fi)
                endq.enqueue(k.child[1])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list) is startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),starth)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),endh)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list) is not endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list))]:
                k.child[2]=node(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),k.list,rubik.L)
                endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list))]=(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),k.list,rubik.L)
                endq.enqueue(k.child[2])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list) is starth[hash(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list))]:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),starth)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),endh)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list) is not endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list))]:
                k.child[3]=node(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),k.list,rubik.Li)
                endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list))]=(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),k.list,rubik.Li)
                endq.enqueue(k.child[3])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list) is starth[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list))]:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),starth)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),endh)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list) is not endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list))]:
                k.child[4]=node(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),k.list,rubik.U)
                endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list))]=(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),k.list,rubik.U)
                endq.enqueue(k.child[4])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list) is starth[hash(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list))]:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),starth)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),endh)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list) is not endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list))]:
                k.child[5]=node(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),k.list,rubik.Ui)
                endh[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list))]=(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),k.list,rubik.Ui)
                endq.enqueue(k.child[5])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list) is starth[hash(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list))]:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),starth)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),endh)
                fr.reverse()
                z=fr+br

                return z


        i+=1
    return None

def moves(start,dicti):
    move=[]
    i=dicti[hash(start)]
    #print i
    while i[2] is not None:
        move.append(i[2])
        if i[1] is not None:
            c=i[1]
            i=dicti[hash(c)]
    return move



end=rubik.I
start=rubik.Fi
print shortest_path(start,end)

                
 
