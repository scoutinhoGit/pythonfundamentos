val_hora = float(input("informe o valor de sua hora      :  "))
qtd_hora = float(input("informe a qtde horas trabalhadas :  "))

sal_bruto = val_hora * qtd_hora

if sal_bruto <= 1900:
    val_desc_ir = 0
elif sal_bruto <= 2800:
    val_desc_ir = sal_bruto * 0.07
elif sal_bruto <= 3700:
    val_desc_ir = sal_bruto * 0.15
elif sal_bruto <= 4600:   
    val_desc_ir = sal_bruto * 0.22
else:
    val_desc_ir = sal_bruto * 0.27

val_fgts = sal_bruto * 0.11
val_desc_sind = sal_bruto * 0.03

print (f'Salario bruto .......... {sal_bruto} ')
print (f'(-) IR ................. {val_desc_ir} ')
print (f'(-) Sindicato .......... {val_desc_sind} ')
print (f'Salario Liquido ........ {sal_bruto - val_desc_ir - val_desc_sind} ')
print (f'Total Descontos ........ {val_desc_ir + val_desc_sind} ')
print (f'FGTS .......... ........ {val_fgts} ')

