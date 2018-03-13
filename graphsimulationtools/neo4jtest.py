from neo4j.v1 import GraphDatabase

class tran:
    def __init__(self):
        self.id=-1
        self.v=[]
        self.e=[]

    def addV(self, line):
        v=line.split()
        self.v.append((v[1], v[2].upper()))

    def addE(self, line):
        e=line.split()
        self.e.append((e[1],e[2],e[3]))

class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    def insertT(self, transDB):
        for t in transDB:
            query="CREATE "
            for v in t.v:
                query=query+'(v%s:%s {name:"%s",vid:%d,tid:%d}),'%(v[0],v[1],v[1],int(v[0]),t.id)
            for e in t.e:
                query=query+'(v%s)-[: follow]->(v%s),'%(e[0],e[1])
            query=query[:-1]
            print(query)
            with self._driver.session() as session:
                session.write_transaction(self._insert_trans, query)

    # CREATE
    # (js: Person {name: "Johan",from: "Sweden", learn: "surfing"}),
    # (ir:Person {name: "Ian", from: "England", title: "author"}),
    # (rvb:Person {name: "Rik", from: "Belgium", pet: "Orval"}),
    # (ally:Person {name: "Allison", from: "California", hobby: "surfing"}),
    # (ee) - [: KNOWS{since: 2001}]->(js),
    # (ee) - [: KNOWS{rating: 5}]->(ir),
    # (js) - [: KNOWS]->(ir),
    # (js) - [: KNOWS]->(rvb),
    # (ir) - [: KNOWS]->(js),
    # (ir) - [: KNOWS]->(ally),
    # (rvb) - [: KNOWS]->(ally)
    @staticmethod
    def _insert_trans(tx,query):
        result = tx.run(query)

def loadTrans(transpath):
    with open(transpath) as file:
        lines=file.readlines()
        lines=[line.strip() for line in lines]
        transDB=[]
        trans=tran()
        for line in lines:
            if line.startswith('t'):
                if trans.id>-1:
                    transDB.append(trans)
                    trans=tran()
                    trans.id=int(line.split()[2])
                else:
                    trans=tran()
                    trans.id=int(line.split()[2])

            elif line.startswith('v'):
                trans.addV(line)

            elif line.startswith('e'):
                trans.addE(line)
        transDB.append(trans)
    return transDB

def insertTrans(transDB):
    neo=HelloWorldExample(uri="bolt://127.0.0.1:7687",user="neo4j",password="zjhvision")
    # neo.print_greeting("hello")
    neo.insertT(transDB)
    neo.close()

    pass

def testNeo4j():
    neo=HelloWorldExample(uri="bolt://127.0.0.1:7687",user="neo4j",password="zjhvision")
    neo.print_greeting("hello")
    neo.close()

def insertPatternsToNeo4j():
    # transDB=loadTrans("simresult.txt")
    # transDB = loadTrans("isoresult.txt")
    transDB = loadTrans("testdata")
    insertTrans(transDB)

def insertSimdata4ToNeo4j():
    with open("simdata4") as simdata4:
        lines=[line.strip() for line in simdata4.readlines()]
        g=tran()
        g.id=1
        for line in lines:
            toks=line.split()
            g.addV("v %s %s"%(toks[0],toks[1]))
            for i in range(int(toks[2])):
                g.addE("e %s %s 1"%(toks[3+i],toks[0]))

    transDB=[]
    transDB.append(g)
    insertTrans(transDB)





if __name__ == '__main__':
    insertSimdata4ToNeo4j()






#neo4j query

# MATCH (ee) where ee.tid<5 RETURN ee;