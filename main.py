#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        if v[i] != " \n":
            j = v[i].split()[0]
            if j == cod:
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
            if len(line.split()) == 4:
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
    else:
        return False

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
            t = line.split()
            if len(t) == 4:
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
        if len(line.split()) == 4:
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
                if len(l) == 4:
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


CADASTRO = "cadastro.txt"
VENDAS = "vendas.txt"


print("Bem vindo ao sistema de registro de produtos e vendas! \n")
welcome = "Digite o número da operação desejada abaixo: \n"+ "1) Registrar produto    2) Atualizar estoque    3)Realizar venda de produto \n"+ "4)Mostrar estoque       5) Vendas do dia        6)Mostrar vendas gerais \n"+ "7) Mostrar itens mais vendidos     8) Mostrar itens menos vendidos 9) Mostrar clientes que mais compram  \n"+"Não digite nada se quiser parar a execução do programa"

n = raw_input(welcome)

while(n != ""):
    print("")
    if n == "1":
        print('\n')
        e = raw_input("Insira os valores do produto no formato <codigo descriçaõ preço quantidade> as informações devem estar separadas por espaço \n")
        p = e.split()
        b = registryProd(p[0],p[1],p[2],p[3])

        if b:
            print("Produto adicionado com sucesso")
        else:
            print("Erro ao cadastrar. Esse código já está sendo usado")
    if n == "2":
        print('\n')
        e = raw_input(
            "Insira o código do produto seguido das novas informações <codigo nova_descriçaõ novo_preço nova_quantidade> as informações devem estar separadas por espaço \n")
        p = e.split()
        b = updateregistry(p[0], p[1], p[2], p[3])
        print("\n")
        if b:
            print("Produto atualizado com sucesso")
        else:
            print("Erro ao atualizar. O produto selecionado não existe")
    if n == "3":
        print('\n')
        e = raw_input(
            "Insira a data e o nome do cliente, seguido do código do produto e a quantidade da venda <data nome_cliente codigo quantidad_ venda> as informações devem estar separadas por espaço \n")
        p = e.split()
        b = sell(p[0], p[1], p[2], p[3])
        if b:
            print("Produto vendido com sucesso")
        else:
            print("Erro ao vender. O produto selecionado não tem estoque ou não existe")
    if n == "4":
        print('\n')
        print("Estoque: \n")
        r = raw_input("Quer imprimir no estoque.txt?(y/n)")
        reg = showRegistry(CADASTRO)
        if reg == None:
            print("Nenhum produto foi encontrado")
        else:
            arq = open("estoque.txt", "w")
            if r == "y":
                arq.write(reg)
            if r == "n":
                print(reg)
            arq.close()
            print("Sucesso")
    if n == "5":
        r = raw_input("Quer imprimir no vendas_dia.txt?(y/n)")
        e = raw_input("Insira a data que você quer checar as vendas")
        print("Vendas: \n")
        b = showSellsByDay(e)
        if not(b):
            print("Não há vendas nesse dia")
        else:
            arq = open("vendas_dia.txt","w")
            for i in b:
                if r == "y":
                    arq.write(i)
                if r == "n":
                    print(i)
            arq.close()
    if n == "6":
        print("Vendas: \n")
        reg = showRegistry(VENDAS)
        r = raw_input("Quer imprimir no vendas.txt?(y/n)")
        if not(reg):
            print("Nenhuma venda foi encontrada")
        else:
            arq = open("vendas.txt", "w")
            if r == "y":
                arq.write(reg)
            if r == "n":
                print(reg)
            arq.close()
            print("Sucesso")
    if n =="7":
        print("Itens mais vendidos \n")
        b = soldProducts(findHigher)
        r = raw_input("Quer imprimir no most_item.txt?(y/n)")
        if not(b):
            print("Nenhum produto encontrado. Alguma venda foi feita?")
        else:
            arq = open("most_item.txt", "w")
            for i in b:
                if r == "y":
                    arq.write(i)
                if r == "n":
                    print(i)
            arq.close()
            print("Sucesso")
    if n == "8":
        print("Itens menos vendidos \n")
        b = soldProducts(findSmaller)
        r = raw_input("Quer imprimir no least_item.txt?(y/n)")
        if not (b):
            print("Nenhum produto encontrado. Alguma venda foi feita?")
        else:
            arq = open("least_item.txt", "w")
            for i in b:
                if r == "y":
                    arq.write(i)
                if r == "n":
                    print(i)
            arq.close()
            print("Sucesso")
    if n == "9":
        print("Os clientes que mais compram são: \n")
        b = mostValuableClient()
        r = raw_input("Quer imprimir no most_client.txt?(y/n)")
        if not(b):
            print("Não há clientes. Alguma venda foi feita?")
        else:
            arq = open("most_client.txt", "w")
            for i in b:
                if r == "y":
                    arq.write(i)
                if r == "n":
                    print(i)
            arq.close()
            print("Sucesso")
    print("")
    n = raw_input(welcome)
