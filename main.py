import functions as f

CADASTRO = "cadastro.txt"
VENDAS = "vendas.txt"

f.registryProd("123","lapis","2.0","5")
f.registryProd("312","Bolsa","4.0","5")
f.updateregistry("312","Bolsa","4.0","5")
print(f.sell("12/03","Victor","312","3"))
#print(f.sell("12/03","Victor","312","4"))
#print(f.sell("12/02","Victor","123","1"))
print((f.showRegistry(VENDAS)))
print((f.showRegistry(CADASTRO)))
print(f.mostValuableClient())
