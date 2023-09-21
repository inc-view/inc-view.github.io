# O pacote pywin32 possui uma série de módulos que podem ser utilizados
# para obter informações da api Win32. Neste protótipo usamos o win32api
# Instalação: pip install pywin32
# Documentação: https://mhammond.github.io/pywin32/
# Funções específicas da win32api estão em Python Objects -> Modules -> win32api
import win32api
import time
import os

# Ainda não estamos salvando no banco, só mantendo um array como histórico
historico = []

# Contém o estado de cada tecla a cada momento, será explicado melhor abaixo
keyState = []
# Contém os "ids" de cada tecla, para uso com a função GetKeyState()
keyboard = []

# Estas duas acumulam os usos do teclado e mouse, para serem salvas no banco quando a
# variável count tiver valor igual à interval.
keyCount = 0
mouseCount = 0

count = 0
interval = 3000

# A variável now foi só utilizada para fazer um teste, e ver quanto tempo
# levava para executar o loop 1000 vezes, e ver se a time.sleep(0.001) era necessária
now = time.time()

# Esse for serve para inicializar os arrays keyState e keyboard, para que eles tenham
# o tamanho apropriado. A função GetKeyboardState() retorna o estado de todo o teclado 
# de uma vez, porém de um jeito que é um pouco difícil de usar, então usamos ela só
# para verificar quantas teclas temos, e montar os dois arrays.
for k, key in enumerate(win32api.GetKeyboardState()):
    keyState.append(0)
    keyboard.append(k)

while True:

    # Para cada tecla no teclado
    for k, key in enumerate(keyboard):

        # Pegamos o estado atual da tecla. Este pode ter 4 valroes:
        # 0 ou 1: tecla não esta pressionada atualmente
        # -127 ou -128: tecla está pressionada.
        # O retorno da função (se é 0 ou 1, ou -127 ou -128) alterna conforme 
        # o usuário pressiona e solta as teclas, p.ex.:
        # Início         Pressiona              Solta               Pressiona       Solta
        # 0 -> 0 -> 0 -> -127 -> -127 -> -127 -> 1 -> 1 -> 1 -> 1 -> -128 -> -128 -> 0 -> 0 -> etc
        curState = win32api.GetKeyState(key)

        # Assim, nós verificamos o array keyState e comparamos com o estado atual
        # se o keyState estava em 0/1, e o estado atual está em -127 e -128, a tecla
        # estava solta, e agora está sendo pressionada, então aumentamos a respectiva
        # contagem. Também setamos o keyState para ser igual ao estado atual, para que
        # não contemos uma única pressionada várias vezes
        if keyState[k] in (0, 1) and curState in (-127, -128):
            keyState[k] = curState

            # Essa comparação com k <= 2 é para verificar se é um clique de mouse ou teclado
            # As teclas com id 1 e 2 se referem aos botões de mouse esquerdo e direito do 
            # mouse, por isso esse if
            if k <= 2:
                mouseCount += 1
            else:
                keyCount += 1
        
        # Também verificamos se o keyState é igual a -127/-128 enquanto o curState é 0/1
        # Ou seja, se a tecla estava pressionada e agora não está mais. Em caso positivo,
        # resetamos o keyState para que uma nova pressionada de tecla possa ser registrada
        # futuramente
        elif keyState[k] in (-127, -128) and curState in (0, 1):
            keyState[k] = curState

    # Então incrementamos a count e comparamos ela com a interval, para salvar no banco só de vez em quando.
    count += 1

    if count >= interval:
        historico.append((mouseCount, keyCount))

        # Resetando as variáveis e printando o histórico
        keyCount = 0
        mouseCount = 0
        count = 0
        os.system('cls')
        print(historico)

        # Conforme mencionado antes, essa parte do time.time() e now foi mais para testar
        # a eficiência, e se a time.sleep(0.001) era necessária ou não
        print(time.time() - now, "s")
        now = time.time()
    
    #time.sleep(0.001)

# Caso queira saber qual id refere a qual tecla, para uso na GetKeyState(), 
# refira à tabela na seguinte página:
# https://learn.microsoft.com/pt-br/windows/win32/inputdev/virtual-key-codes


# Divagação aleatória de possível melhoria, pode ignorar se quiser:
# Uma possível ideia para fazer isso de um jeito mais eficiente seria não ficar
# checando constantemente, tentando pegar os valores -127/-128 da GetKeyState(), 
# mas só verificar quando a tecla muda de estado 0 para 1 ou vice versa. Nesse
# caso até daria para tentar fazer através da GetKeyboardState() ao inves de 
# GetKeyState(); O principal motivo de não usarmos a função do teclado inteiro 
# é pq ela não tem essa distinção de -127 e -128, o retorno dela é so 0s e 1s. 
#
# Fazendo desse jeito daria para checar bem menos, um intervalo de 0.1s a cada 
# medida provavelmente já seria suficiente.
#
# Um jeito que poderia ser bem eficiente é fazer uma operação XOR entre o estado
# atual e o estado antigo, e contar quantas teclas ficaram em 1 (ou seja, quantas
# mudaram de estado). Você imaginaria que fazer isso com um tipo "bytes" (que é o 
# que a GetKeyboardState() retorna) seria bem fácil, mas não sei se tem como em 
# python sem fazer gambiarra.