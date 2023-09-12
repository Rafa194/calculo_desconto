preco =float(input('Digite o preço do produto: '))
desc_aplicado = preco * (5 / 100)
prod_com_desc = preco - desc_aplicado

print('O produto que custava R${:.2f} na promoção com desconto de 5% vai custar' 
      ' R${:.2f}.'.format(preco, prod_com_desc))






