#calcula o salario bruto
def calc_salario(hora,t_trabalho, faltas = 0):

    s_bruto = hora * t_trabalho

    v_dia = s_bruto/30
    s_bruto = s_bruto - (v_dia * faltas)

    return s_bruto


# printa o menu de escolha
def print_menu():
    print("\n\nDigite 1 Para saber o salario bruto")
    print("Digite 2 Para saber o desconto imposto de renda ")
    print("Digite 3 Para saber o desconto sindicato")
    print("Digite 4 Para saber o desconto INSS")
    print("Digite 5 Para saber o salario liquido")
    print("Digite 6 Para saber o décimo terceiro")
    print("Digite 7 para cancelar\n\n")


# Mostra o menu para o usuario perguntando se ele deseja parar ou continuar
def menu_segue_ou_para():
    print("\n\nDigite 1 finalizar")
    print("Digite 2 para continuar\n\n")

    digito = int(input("Digite um número:"))

    if digito == 1:
        return 0
    elif digito == 2:
        pass
    else:
        print("\nNúmero inválido Digitado \n\n")
        return 0


# Mostra o desconto do INSS
def desc_inss(salario):

    if salario <= 1412.00:
        desconto = salario * 0.075
    elif 1412.00 < salario <= 2666.68:
        desconto = salario * 0.09
    elif 2666.68 <  salario <= 4000.03:
        desconto = salario * 0.12
    elif 4000.03 <  salario:
        desconto = salario * 0.14
    return desconto


# mostra o desconto do imposto de renda
def desc_impR(salario):

    inss = desc_inss(salario)

    salario = salario - inss

    if salario <= 2259.20:
        pass
    elif  2259.20 < salario <= 2826.65:
        desconto = salario * 0.075
    elif  2826.65 <  salario <= 3751.05:
        desconto = salario * 0.15
    elif  3751.05 <  salario <= 4664.68:
        desconto = salario * 0.225    
    elif  4664.68 <  salario :
        desconto = salario * 0.275
    return desconto


# Mostra o desconto Sindical
def desc_sindical(salario,hora,t_trabalho):
    v_dia = (hora * t_trabalho)/30
    return v_dia


#  Calcula o Salario liquido
def sal_liquido(salario,hora,t_trabalhado):
    inss = desc_inss(salario)
    impR = desc_impR(salario)
    sindical = desc_sindical(salario, hora, t_trabalhado)

    salario_liquido = salario - (inss + impR + sindical)
    return salario_liquido



# Calcula o 13º
def dec_terceiro(salario,hora,t_trabalhado):
    liq = sal_liquido(salario, hora, t_trabalhado)
    dec13 = liq + salario
    return dec13




# PROGRAMA PRINCIPAL
def main():

    hora = float(input("quanto voce ganha por hora?:"))
    hora_mes = float(input("quantas hora trabalhadas no mes?:"))
    faltas = float(input("quantas faltas o funcionario teve ao longo do mês?:"))

    total_mes = calc_salario(hora, hora_mes)

    while True:

        print_menu()

        digito = int(input("Digite um número:"))



        if digito == 1:
            print(f"\nseu salario mensal é de: {total_mes}")
            valor = menu_segue_ou_para()
            if valor == 0:
                break



        elif digito == 2:
            des_imp = desc_impR(total_mes)
            print(f"\nDesconto do Imposto de Renda: {des_imp}")
            valor = menu_segue_ou_para()
            if valor == 0:
                break



        elif digito == 3:
            sind = desc_sindical(total_mes, hora, hora_mes)
            print(f"\ndesconto sindicato: {sind}")
            valor = menu_segue_ou_para()
            if valor == 0:
                break



        elif digito == 4:
            des_inss = desc_inss(total_mes)
            print(f"\ndesconto INSS: {des_inss}")
            valor = menu_segue_ou_para()
            if valor == 0:
                break



        elif digito == 5:
            liq = sal_liquido(total_mes, hora, hora_mes)
            print(f"\n Salario liquidor: {liq}")
            valor = menu_segue_ou_para()
            if valor == 0:
                break





        elif digito == 6:
            dec13 = dec_terceiro(total_mes, hora, hora_mes)
            print(f"\n Décimo terceiro: {dec13}")
            valor = menu_segue_ou_para()
            if valor == 0:
                break



        elif digito == 7 :
            break




        else:
            print("\nNúmero inválido Digitado \n\n")
            break

if __name__ == "__main__":
    main()