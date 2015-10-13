import rubik


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

    startd={}
    startd[start]=(start,None,None)
    endd={}
    endd[end]=(end,None,None)

    i=0
    while i<7:
        while True:
            g=startq.dequeue()
            if g==None:
                startq.enqueue(None)
                break

            if rubik.perm_apply(rubik.F,g.list) not in startd:
                g.child[0]=node(rubik.perm_apply(rubik.F,g.list),g.list,rubik.F)
                startd[rubik.perm_apply(rubik.F,g.list)]=(rubik.perm_apply(rubik.F,g.list),g.list,rubik.F)
                startq.enqueue(g.child[0])
            if rubik.perm_apply(rubik.F,g.list) in endd:
                fr=moves(rubik.perm_apply(rubik.F,g.list),startd)
                br=moves(rubik.perm_apply(rubik.F,g.list),endd)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.Fi,g.list) not in startd:
                g.child[1]=node(rubik.perm_apply(rubik.Fi,g.list),g.list,rubik.Fi)
                startd[rubik.perm_apply(rubik.Fi,g.list)]=(rubik.perm_apply(rubik.Fi,g.list),g.list,rubik.Fi)
                startq.enqueue(g.child[1])
            if rubik.perm_apply(rubik.Fi,g.list) in endd:
                fr=moves(rubik.perm_apply(rubik.Fi,g.list),startd)
                br=moves(rubik.perm_apply(rubik.Fi,g.list),endd)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.L,g.list) not in startd:
                g.child[2]=node(rubik.perm_apply(rubik.L,g.list),g.list,rubik.L)
                startd[rubik.perm_apply(rubik.L,g.list)]=(rubik.perm_apply(rubik.L,g.list),g.list,rubik.L)
                startq.enqueue(g.child[2])
            if rubik.perm_apply(rubik.L,g.list) in endd:
                fr=moves(rubik.perm_apply(rubik.L,g.list),startd)
                br=moves(rubik.perm_apply(rubik.L,g.list),endd)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.Li,g.list) not in startd:
                g.child[3]=node(rubik.perm_apply(rubik.Li,g.list),g.list,rubik.Li)
                startd[rubik.perm_apply(rubik.Li,g.list)]=(rubik.perm_apply(rubik.Li,g.list),g.list,rubik.Li)
                startq.enqueue(g.child[3])
            if rubik.perm_apply(rubik.Li,g.list) in endd:
                fr=moves(rubik.perm_apply(rubik.Li,g.list),startd)
                br=moves(rubik.perm_apply(rubik.Li,g.list),endd)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.U,g.list) not in startd:
                g.child[4]=node(rubik.perm_apply(rubik.U,g.list),g.list,rubik.U)
                startd[rubik.perm_apply(rubik.U,g.list)]=(rubik.perm_apply(rubik.U,g.list),g.list,rubik.U)
                startq.enqueue(g.child[4])
            if rubik.perm_apply(rubik.U,g.list) in endd:
                fr=moves(rubik.perm_apply(rubik.U,g.list),startd)
                br=moves(rubik.perm_apply(rubik.U,g.list),endd)
                fr.reverse()

                z=fr+br

                return z


            if rubik.perm_apply(rubik.Ui,g.list) not in startd:
                g.child[5]=node(rubik.perm_apply(rubik.Ui,g.list),g.list,rubik.Ui)
                startd[rubik.perm_apply(rubik.Ui,g.list)]=(rubik.perm_apply(rubik.Ui,g.list),g.list,rubik.Ui)
                startq.enqueue(g.child[5])
            if rubik.perm_apply(rubik.Li,g.list) in endd:
                fr=moves(rubik.perm_apply(rubik.Ui,g.list),startd)
                br=moves(rubik.perm_apply(rubik.Ui,g.list),endd)
                fr.reverse()

                z=fr+br

                return z

    


        while True:
            k=endq.dequeue()
            if k==None:
                endq.enqueue(None)
                break

            if rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list) not in endd:
                k.child[0]=node(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),k.list,rubik.F)
                endd[rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list)]=(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),k.list,rubik.F)
                endq.enqueue(k.child[0])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list) in startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),startd)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.F),k.list),endd)
                fr.reverse()
                z=fr+br

                return z

            if rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list) not in endd:
                k.child[1]=node(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),k.list,rubik.Fi)
                endd[rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list)]=(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),k.list,rubik.Fi)
                endq.enqueue(k.child[1])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list) in startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),startd)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Fi),k.list),endd)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list) not in endd:
                k.child[2]=node(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),k.list,rubik.L)
                endd[rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list)]=(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),k.list,rubik.L)
                endq.enqueue(k.child[2])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list) in startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),startd)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.L),k.list),endd)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list) not in endd:
                k.child[3]=node(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),k.list,rubik.Li)
                endd[rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list)]=(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),k.list,rubik.Li)
                endq.enqueue(k.child[3])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list) in startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),startd)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Li),k.list),endd)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list) not in endd:
                k.child[4]=node(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),k.list,rubik.U)
                endd[rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list)]=(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),k.list,rubik.U)
                endq.enqueue(k.child[4])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list) in startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),startd)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.U),k.list),endd)
                fr.reverse()
                z=fr+br

                return z


            if rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list) not in endd:
                k.child[5]=node(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),k.list,rubik.Ui)
                endd[rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list)]=(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),k.list,rubik.Ui)
                endq.enqueue(k.child[5])
            if  rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list) in startd:
                fr=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),startd)
                br=moves(rubik.perm_apply(rubik.perm_inverse(rubik.Ui),k.list),endd)
                fr.reverse()
                z=fr+br

                return z


        i+=1
    return None

def moves(start,dicti):
    move=[]
    i=dicti[start]
    #print i
    while i[2] is not None:
        move.append(i[2])
        if i[1] is not None:
            c=i[1]
            i=dicti[c]
    return move






                
 
