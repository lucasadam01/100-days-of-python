print("Bem-vindo à calculadora de gorjetas!\n")

conta = float(input("Qual foi o total da conta? R$"))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? "))
num_pessoas = int(input("Quantas pessoas para dividir a conta? "))

valor_gorjeta = conta * (gorjeta / 100)        
total_final = conta + valor_gorjeta 
valor_por_pessoa = round(total_final / num_pessoas, 2)

print(f"\n10Cada pessoa deverá pagar : R${valor_por_pessoa}")


