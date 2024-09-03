#UMA LITA, SENDO COLOCADA TDOS OS DIAS DA SEMANA (COM LETRA INICIAIS MAIÚSCULAS)
dias_da_semana = ["Domingo", "domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]

#O USUÁRIO ESCOLHENDO ALGUM DIA DA SEMANA
escolha_dia = input("Escolha algum dia da semana: ")

#SE O DIA ESTIVER NA LISTA, VAI FALAR QUE ESTÁ NA LISTA. SE O DIA NÃO ESTIVER NA LISTA, VAI FALAR QUE NÃO ESTÁ NA LISTA
if escolha_dia in dias_da_semana:
    print(f"O dia {escolha_dia} está na lista")
else:
    print(f"O dia {escolha_dia} não está na lista")