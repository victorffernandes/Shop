import functions as f

CADASTRO = "cadastro.txt"
VENDAS = "vendas.txt"

f.registryProd("123","Bolsa","2.0","5")
f.registryProd("312","Bolsa","2.0","5")
f.updateregistry("123","Davidson","2.0","9")
print((f.showRegistry(CADASTRO)))

