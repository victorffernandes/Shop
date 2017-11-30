import os

def sell(data, nome,cod, qunt):
    if os.path.exists("cadastro.txt"):
        product = getProdByCod(cod)
        if product is not None and qunt <= product[3]:
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
        return find.split(" ")


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

def showRegistry():
    if os.path.exists("cadastro.txt"):
        arq = open("cadastro.txt", "r")
        v = arq.read()
        v.replace("\n"," ")
        print("Registry: "+ v)
        arq.close()

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
        arq.write((" ").join(v))
        return find
    else:
        return False



#def sellProd(data, nomeCliente, cod, qunt):
#print(updateregistry("123","cassetinho","5,0","1"))
showRegistry()
sell("Hoje","Victor", "456", "1")
showRegistry()
registryProd("321","revolver","300","1")
registryProd("456","espingarda","300","1")
sell("Hoje","Victor", "321", "1")
