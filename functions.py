import os

def sell(data, nome,cod, qunt):
    if os.path.exists("cadastro.txt"):
        product = getProdByCod(cod).split()
        if product is not None and int(qunt) <= int(product[3]):
            arq = open("vendas.txt", "a")
            args = [data, nome, cod, qunt]
            arq.write((" ").join(args)+ " \n")
            arq.close()
            updateregistry(product[0],product[1],product[2],str(int(product[3]) - int(qunt)))
            return True
        else:
            return False



def getProdByCod(cod):
    arq = open("cadastro.txt", 'r+')
    v = []
    for line in arq:
        v.append(line)
    arq.close()

    find = None
    for i in range(len(v)):
        if v[i].find(cod) != -1:
            find = v[i]
    if find == None:
        return None
    else:
        return find#.split(" ")


def registryProd(cod, des, pre, qunt):

    if os.path.exists("cadastro.txt"):
        if not(checkIfProdExists(cod)):
            arq = open("cadastro.txt", "a")
            args = [cod, des, pre, qunt]
            arq.write((" ").join(args)+ " \n")
            arq.close()
            return True
        else:
            return False
    else:
        arq = open("cadastro.txt", "a")
        args = [cod, des, pre, qunt]
        arq.write((" ").join(args) + " \n")
        arq.close()
        return True

def checkIfProdExists(cod):
    arq = open("cadastro.txt")
    v = []
    for line in arq:
        if line.find(cod) != -1:
            arq.close()
            return True
    arq.close()
    return False

def showRegistry(path):
    if os.path.exists(path):
        arq = open(path, "r")
        v = arq.read()
        v.replace("\n"," ")
        arq.close()
        return v

def soldProducts(method):
    if os.path.exists("vendas.txt") and os.path.exists("cadastro.txt"):
        arq = open("cadastro.txt","r")
        products = []
        for line in arq:
            products.append(line.split()[0])
        arq.close()

        arq = open("vendas.txt", "r")
        quantities = []
        for cod in products:
            count = 0
            arq = open("vendas.txt", "r")
            for sell in arq:
                s = sell.split()
                if cod == s[2]:
                    count += int(s[3])
            quantities.append(count)
            arq.close()
        chosen = method(quantities)
        res = []
        for i in chosen:
            res.append(getProdByCod(products[i]))
        return res

def findHigher(v):
    h = -1
    l = []
    for i in range(len(v)):
        if v[i] > h:
            h = v[i]
            l = [i]
        elif i == h:
            l.append(i)
    return l

def findSmaller(v):
    h = 2**1234567
    l = []
    for i in range(len(v)):
        if v[i] < h:
            h = v[i]
            l = [i]
        elif i == h:
            l.append(i)
    return l

def showSellsByDay(string):
    if os.path.exists("vendas.txt"):
        arq = open("vendas.txt","r")
        v = []
        for line in arq:
            t = line.split();
            if string in t[0]:
                v.append(line)
        arq.close()
        if len(v) > 0:
            return v
        else:
            return False
    return False

def findAllClients():
    arq = open("vendas.txt","r")
    c = []
    for line in arq:
        cred = line.split()[1]
        if not(cred in c):
            c.append(cred)
    arq.close()
    return c

def mostValuableClient():
    if os.path.exists("vendas.txt") and os.path.exists("cadastro.txt"):
        allClients = findAllClients()

        res = []
        for c in allClients:
            c_n = 0.0
            arq = open("vendas.txt", "r")
            for line in arq:
                l = line.split()
                if c == l[1]:
                    p = getProdByCod(l[2]).split()
                    c_n += float(p[2]) * float(l[3])
            res.append(c_n)
            arq.close()
        indexes = findHigher(res)
        result = []
        for i in indexes:
            result.append(allClients[i])
        return result
    return False


def updateregistry(cod, des, pre, qunt):
    if os.path.exists("cadastro.txt"):
        arq = open("cadastro.txt",'r+')
        v = []
        args = [cod, des, pre, qunt]
        for line in arq:
            v.append(line)
        arq.close()
        find = False
        for i in range(len(v)):
            if v[i].find(cod) != -1:
                find = True
                v[i] = (" ").join(args)+ " \n"
        arq = open("cadastro.txt", 'r+')
        for j in v:
            arq.write(j)
        arq.close()
        return find
    else:
        return False
