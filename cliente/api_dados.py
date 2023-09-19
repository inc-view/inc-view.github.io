# O pacote os é usado para chamar comandos de console pelo python
# especificamente usamos cls/clear para limpar a tela e deixar a interface mais ajeitada
import os
# A psutil é o pacote para obter os dados de máquina
import psutil
# A time é usada pela função sleep, para que possamos fazer os registros a cada 1 segundo
import time
# Pacotes MySQL para conectar com o banco
import mysql.connector
import mysql.connector.errorcode
# Pacote matplotlib para exibir o gráfico
import matplotlib.pyplot as plt
# pacotes para enviar os dados para o slack
import requests
import json

# Webhook ligando ao canal #chat_jira do Slack
webbook = "https://hooks.slack.com/services/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"

# Esta variável é só para facilitar a edição de cores, que são usadas como métricas
# Ao invés de ficar colocando o código \033[92m] é so chamar cor['verde'], p.ex.
cor = {
    'verde': "\033[92m",
    'amarelo': "\033[93m",
    'vermelho': "\033[31m",
    'branco': "\033[0m"
}

# A variável conexao cria a conexão ao banco de dados. A comando (criada a partir da 
# conexao.cursor()) é onde efetivamente fazemos as chamadas de insert/select.
conexao = mysql.connector.connect(
    host="localhost",
    user="viss",
    password="urubu100",
    port=3306,
    database="apiViss"
)

comando = conexao.cursor()

# Essa variável é usada junto do while abaixo para que o usuário selecione uma opção
# ela é inicializada com "" para que caiamos dentro do while na primeira passada
opcao = ""

while not opcao in ("1", "2", "3"):
    print("Escolha uma opção:\n1) Registrar dados\n2) Exibir Histórico\n3) Sair")
    opcao = input()

# Opção de exibir histórico
if opcao == "2":

    fig = plt.figure()
    gs = fig.add_gridspec(1,3)
    fig.set_figheight(100)
    fig.set_figwidth(300)
    axs = gs.subplots(sharex=True, sharey=True)
    # recuperamos todas as colunas dos últimos 40 registros (~20 min)
    # Uma possível melhoria seria deixar o usuário escolher o período que quer observar
    comando.execute("SELECT * FROM registro ORDER BY dataRegistro DESC LIMIT 40")
    x = []
    yCpu = []
    yRam = []
    yDisco = []

    # aqui são montados os arrays, para exibir através do matplotlib
    for (id, cpu, ram, disco, dataRegistro) in comando:
        x.append(dataRegistro)
        yCpu.append(cpu)
        yRam.append(ram)
        yDisco.append(disco)

    # Todos usam o mesmo array x, pois todos se referem às mesmas datas e horas.
    axs[0].plot(x, yCpu, 'g')
    axs[0].set_title('Uso de CPU')
    axs[0].tick_params(axis='x', labelrotation = 45)
    axs[0].set_ylabel('Porcentagem de uso (%)')
    
    axs[1].plot(x, yRam, 'b')
    axs[1].set_title('Uso de RAM')
    axs[1].tick_params(axis='x', labelrotation = 45)
    axs[1].set_xlabel('Data e hora do registro')

    axs[2].plot(x, yDisco, 'r')
    axs[2].set_title('Uso de disco')
    axs[2].tick_params(axis='x', labelrotation = 45)
    
    # Setando yticks para que sejam exibidas labels de 10 em 10 % na esquerda
    plt.yticks([0,10,20,30,40,50,60,70,80,90,100])

    # Adicionando margem, para que o título do eixo x não fique cortado
    plt.subplots_adjust(bottom=0.20)
    plt.show()

# Opção de exibição em tempo real, e que salva no banco
elif opcao == "1":

    # A variável cont é usada para salvar no banco intermitentemente
    # A API lê os dados e exibe ao usuário 1 vez por segundo, mas grava no
    # banco a cada 30. A variável cont é incrementada em 1 a cada exibição,
    # e quando ela chega em 30 nós salvamos no banco.
    cont = 0

    # Essas variáveis de histórico não fazem muito sentido mais. Antes elas 
    # estavam sendo usadas porque não tinhamos a conexão com o banco, então 
    # os dados que deveriam ser salvos eram guardados nesses arrays.
    # Como temos a conexão com o banco podemos alterar isso agora, então podemos 
    # mencionar que essas variáveis vem de uma versão anterior da API e que 
    # vamos retirá-las no futuro.
    cpu_historico = []
    ram_historico = []
    disco_historico = []

    # Essas 4 variáveis são usadas para fazer a média para salvar no banco. Nós
    # lemos os dados 1 vez por segundo, durante 30 segundos, e vamos salvando nessas
    # variáveis para depois tirar a média e salvar no BD.
    cpu_soma = 0
    ram_soma = 0
    disco_usado_soma = 0
    disco_total_soma = 0

    while True:
        # Limpar o console
        os.system('cls')

        # IMPORTANTE: Nós já obtemos os dados de CPU e RAM tratados da psutil, em forma
        # de porcentagem de uso. Nós também tratamos o disco para obter a porcentagem de
        # uso, mas fazemos de modo diferente para considerar a possibilidade de diversas
        # partições
        cpu_use = psutil.cpu_percent()
        partitions = psutil.disk_partitions()

        # A variável disk_use_list armazena o uso de disco de todas as partições.
        # cada posição deste array se refere aos dados de 1 partição.
        disk_use_list = []

        # A variável disk_bar é um array de strings, onde vão sendo armazenadas as barras
        # que são exibidas no console. Assim como a disk_use_list, cada posição deste array
        # armazena a barra referente à uma partição.
        disk_bar = []

        # percorremos todas as partições obtidas a partir da psutil. A função enumerate  é do
        # próprio python, e basicamente ela nos "dá" um id para cada item.
        # Seria possível usar o for com uma sintaxe do tipo 
        #   for part in partitions:
        # Porém,  tem o problema que neste caso não temos como saber em qual índice estamos
        # atualmente, sem computações adicionais. A função enumerate simplifica esse processo, 
        # nos dando tanto o item do array quanto seu respectivo índice (representados por part 
        # e k neste for, respectivamente)
        for (k, part) in enumerate(partitions):

            # Usamos a propriedade "device" da partição, para obter o seu uso de disco, e adicionamos
            # no array disk_use_list
            disk_use_list.append(psutil.disk_usage(part.device))

            # Também aproveitamenos para já começar a criação da barra de porcentagem que é exibida
            # no console.
            if (disk_use_list[k].percent <= 70):
                disk_bar.append(cor['verde'] + "|")
            elif (disk_use_list[k].percent <= 90):
                disk_bar.append(cor['amarelo'] + "|")
            else:
                disk_bar.append(cor['vermelho'] + "|")

        # A função virtual_memory retorna todas as estatístcas de uso da RAM, como
        # Total disponível, quanto esta sendo usado, porcentagem usada, etc.
        ram_use = psutil.virtual_memory()
        cpu_bar = ""

        # Assim como no disco acima, criamos o início das barras que serão exibidas no console,
        # com as respectivas métricas.
        if (cpu_use <= 70):
            cpu_bar = cor['verde'] + "|"
        elif (cpu_use <= 90):
            cpu_bar = cor['amarelo'] + "|"
        else:
            cpu_bar = cor['vermelho'] + "|"

        ram_bar = ""
        if (ram_use.percent <= 70):
            ram_bar = cor['verde'] + "|"
        elif (ram_use.percent <= 90):
            ram_bar = cor['amarelo'] + "|"
        else:
            ram_bar = cor['vermelho'] + "|"

        # Este for é onde é construído o "corpo" das barras. o "for i in range(51)"
        # vai percorrer todos os valores de 0 a 50 (inclusive), e comparamos esse número
        # com a porcentagem de uso, preenchendo com "=" ou " " dependendo se o uso está
        # acima ou abaixo do i do for.
        for i in range(51):
            if (cpu_use <= i*2):
                cpu_bar += " "
            else:
                cpu_bar += "="
            
            # no caso do disco, novamente temos que usar um for para percorrer todas as partições.
            for (k, disk_use) in enumerate(disk_use_list):
                if (disk_use.percent <= i*2):
                    disk_bar[k] += " "
                else:
                    disk_bar[k] += "="

            if (ram_use.percent <= i*2):
                ram_bar += " "
            else:
                ram_bar += "=" 


        # Finalizamos as barras, adicionando um "|" e a cor branca.
        # É importante voltar a cor para branco aqui, se não essas cores começam
        # a vazar para o resto do console.
        cpu_bar += "|" + cor['branco']          
        ram_bar += "|" + cor['branco']  

        for (k,disk) in enumerate(disk_use_list):         
            disk_bar[k] += "|" + cor['branco']     


        # exibimos através de prints. Aqui exibimios não só as barras, mas também os dados
        # numéricos
        # CPU: porcentagem de uso (%)
        # RAM: RAM usada / RAM total (GB)
        # Disco: Nome da partição e disco usado / disco total (GB)
        # no caso da RAM e disco dividimos por 1000000000 para converter de byte para GB.
        # também é usado round para exibir só 2 casas decimais, para ficar mais amigável para o usuário
        print('CPU: ' + str(cpu_use) + ' %\n' + cpu_bar)
        print('\nRAM: ' + str(round(ram_use.used / pow(10, 9), 2)) + '/' + str(round(ram_use.total / pow(10, 9),2)) +' GB\n' + ram_bar)
        
        for (k,disk) in enumerate(disk_use_list):         
            print('\n' + partitions[k].device + ': ' +str(round(disk.used / pow(10, 9), 2))+ '/' +str(round(disk.total / pow(10, 9), 2))  + ' GB\n' + disk_bar[k])

        # Somamos nas variáveis que usaremos para gravar no banco depois
        cpu_soma += cpu_use
        ram_soma += ram_use.percent
        for disco in disk_use_list:
            disco_usado_soma += disco.used
            disco_total_soma += disco.total
        cont += 1

        # a cada 30 ciclos, gravamos os dados no banco.
        if (cont >= 30):

            # no caso da CPU e da RAM, como somamos a porcentagem a cada ciclo, nós dividimos por 30
            # para obter a média. 
            # No caso do disco, como obtemos as somas de disco usado e disco total (e não a porcentagem)
            # essa divisão por 30 não é necessária, nós só convertemos em porcentagem
            # Nos 3 casos usamos round para 2 casas decimais
            cpu_historico.append(round(cpu_soma / 30, 2))
            ram_historico.append(round(ram_soma / 30, 2))
            disco_historico.append(round((100 * disco_usado_soma) / (disco_total_soma), 2))

            # Executamos o INSERT
            # Como eu mencionei antes, as variáveis historico são meio desnecessárias, nós poderíamos
            # pegar os cálculos feitos acima e jogá-los direto no INSERT.
            # Mas, não podemos mudar isso agora, então ficamos com esse código legado por enquanto
            comando.execute(
                "INSERT INTO registro (usoCpu, usoRam, usoDisco, dataRegistro) VALUES "
                f"({cpu_historico[-1]},{ram_historico[-1]},{disco_historico[-1]}, now());"
            )
            # aqui tem um macetezinho que eu acho útil de python, que você pode usar índices negativos
            # em arrays. Basicamente eles siginificam que você conta de trás para frente, então o índice
            # -1 te da o último item do array, o -2 dá o penúltimo, e assim por diante.

            # Envio de mensagem ao slack 
            if (ram_historico[-1] <= 90):
                mensagem = { "text": "A RAM está em estado crítico" }
                requests.post(webbook, data=json.dumps(mensagem))

            conexao.commit()

            # Resetando as variáveis para o próximo ciclo.
            cpu_soma = 0
            ram_soma = 0
            disco_usado_soma = 0
            disco_total_soma = 0
            cont = 0

        # De novo, isso aqui é código legado de primeira versão. Está comentado mas vamos tirar no futuro
        #print('\nHistórico: ')
        #print('CPU:\n', cpu_historico)
        #print('RAM:\n', ram_historico)
        #print('Disco:\n', disco_historico)

        # Função sleep, para dar uma pausa de 1 segundo entre os registros.
        time.sleep(1)