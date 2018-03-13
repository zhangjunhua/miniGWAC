
def removetstart():
    with open("b") as a:
        lines=a.readlines()
        for line in lines:
            if not line.startswith('t'):
                print(line,end="")

def checkvalidationofsimdata2():
    inEdge=[]
    ouEdge=[]
    with open('simdata2') as inFile:
        lines=inFile.readlines()
        for line in lines:
            line=line.strip()
            toks=line.split()
            ins=toks[3:int(toks[2])+3]
            ous=toks[int(toks[2])+4:int(toks[int(toks[2])+3])+int(toks[2])+4]
            print(line)
            print(ins,end=" ")
            print(ous)
            for i in ins:
                inEdge.append(i+toks[0])
            for o in ous:
                ouEdge.append(toks[0]+o)

    inEdge.sort()
    ouEdge.sort()

    print(inEdge)
    print(ouEdge)

def converttoGramiData():
    inEdge=[]
    ouEdge=[]
    graph=[]
    with open('simdata2') as inFile:
        lines=inFile.readlines()
        for line in lines:
            line=line.strip()
            toks=line.split()
            ins=toks[3:int(toks[2])+3]
            ous=toks[int(toks[2])+4:int(toks[int(toks[2])+3])+int(toks[2])+4]
            v={}
            v['id']=toks[0]
            v['label']=toks[1]
            v['in']=ins
            v['out']=ous
            graph.append(v)

            # print(line)
            # print(ins,end=" ")
            # print(ous)

            # for i in ins:
            #     inEdge.append(i+toks[0])
            # for o in ous:
            #     ouEdge.append(toks[0]+o)

    # inEdge.sort()
    # ouEdge.sort()
    #
    # print(inEdge)
    # print(ouEdge)
    print("# t 1")
    for v in graph:
        print('v %d %d'%(int(v['id'])-1, ord(v['label'])-ord('a')+1))
    for v in graph:
        for e in v['out']:
            print("e %d %d 1"%(int(v['id'])-1,int(e)-1))

def convertGramiOutput():
    with open("grami_result.txt") as file:
        lines=file.readlines()
        for line in lines:
            line=line.strip()
            if line[-1] == ':':
                print("\nt # %d * 2"%(int(line[:-1])+1))
            else:
                if line.startswith("v"):
                    v=line.split()
                    print("v %s %s"%(v[1],chr(int(v[2])+ord("a")-1)))
                else:
                    print(line)

def validatingData():
    with open("D:\Personal\Documents\WeChat Files\zjhwechat\Files\p2p_vertexlabelformat_forgrami.csv") as file:
        lines=file.readlines()
        labelDict={}
        for line in lines:
            if line.startswith("v"):
                toks=line.split()
                if int(toks[2]) in labelDict.keys():
                    labelDict[int(toks[2])]+=1
                else:
                    labelDict[int(toks[2])]=0
        for k,v in sorted(labelDict.items()):
            print(k,v)

if __name__ == '__main__':
    # converttoGramiData()
    # convertGramiOutput()
    validatingData()




# 0.000040 0.093535 0.451127 133.019159 (exceeds,ismin,supp,suppY,suppV)=(47770,1296,1296,778,56)
# t # 778 * 56
# v 0 56
# v 1 69
# e 1 0 0
#
#
#
# ====================enter loopsim======================
#
# ====================leave loopsim======================
# basic/../gSpan/../basic/Worker.h(614) rank#0:loop end
# Communication Time : 0.049528 seconds
# - Serialization Time : 0.013834 seconds
# - Transfer Time : 0.031868 seconds
# Total Computational Time : 133.850799 seconds
# Total gspan time : 0.461400 seconds
# Total #msgs=10831729, Total #vadd=0
# total #supersteps=3999
# Dump Time : 0.160648 seconds
# [giraph@master simmining]$ less output.txt
# [giraph@master simmining]$ cd
# [giraph@master ~]$ ls

