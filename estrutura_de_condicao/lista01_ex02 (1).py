#Façaumalgoritmoquerecebaovalordosaláriomínimoeovalordosaláriodeumfuncionário,
#calculeemostreaquantidadedesaláriosmínimosqueganhaessefuncionário.

salarioMin=float(input("Informe o valor do salário mín:"))
salarioFun=float(input("Informe o valor do salário do funcionário:"))

qtdSalMin= salarioFun/salarioMin

if(qtdSalMin < 1):
    print("O funcionário ganha menos que um salário mínimo!")
else:
    print("O funcionário recebe {0:.2f}".format(round(qtdSalMin,2))," salários mínimos." )