import os

def registryProd(cod, des, pre, qunt):

    if os.path.exists("cadastro.txt"):
        if not(checkIfProdExists(cod)):
            arq = open("cadastro.txt", "a")
            args = [cod, des, pre, qunt]
            arq.write((" ").join(args)+ "\n")
            arq.close()
            return True
        else:
            return False
    else:
        arq = open("cadastro.txt", "a")
        args = [cod, des, pre, qunt]
        arq.write((" ").join(args)+ "\n" )
        arq.close()
        return True

def checkIfProdExists(cod):
    arq = open("cadastro.txt")
    v = []
    for line in arq:
        print(line)
        if line.find(cod) != -1:
            arq.close()
            return False
    arq.close()
    return True

def updateregistry(cod, des, pre, qunt):
    arq = open("cadastro.txt",'r+')
    v = []
    args = [cod, des, pre, qunt]
    for line in arq:
        v.append(line)
    arq.close()

    for i in range(len(v)):
        if v[i].find(cod) != -1:
            v[i] = (" ").join(args) + "\n"
    arq = open("cadastro.txt", 'r+')
    arq.write(("").join(v)
              )
    print(v)



#def sellProd(data, nomeCliente, cod, qunt):
registryProd("123","","","")
registryProd("321","","","")
updateregistry("123","cassetinho","5,0","1")
updateregistry("321","revolver","500,0","1")

