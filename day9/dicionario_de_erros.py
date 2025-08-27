# Criar um dicionario com informações de erros em python
erros_python = {
    "SyntaxError": "Erro de sintaxe, ocorre quando o código não está escrito corretamente.",
    "TypeError": "Erro de tipo, ocorre quando uma operação ou função é aplicada a um objeto de tipo inadequado.",
    "ValueError": "Erro de valor, ocorre quando uma função recebe um argumento com o tipo correto, mas valor inapropriado.",
    "IndexError": "Erro de índice, ocorre quando se tenta acessar um índice que está fora do intervalo de uma lista ou tupla.",
    "KeyError": "Erro de chave, ocorre quando se tenta acessar uma chave que não existe em um dicionário.",
    "AttributeError": "Erro de atributo, ocorre quando se tenta acessar um atributo que não existe em um objeto.",
    "ImportError": "Erro de importação, ocorre quando um módulo não pode ser importado.",
    "ZeroDivisionError": "Erro de divisão por zero, ocorre quando se tenta dividir um número por zero.",
    "FileNotFoundError": "Erro de arquivo não encontrado, ocorre quando se tenta acessar um arquivo que não existe.",
    "IndentationError": "Erro de indentação, ocorre quando a indentação do código não está correta.",
    "MemoryError": "Erro de memória, ocorre quando o sistema fica sem memória disponível para alocar novos objetos.",
    "OverflowError": "Erro de estouro, ocorre quando o resultado de uma operação aritmética é muito grande para ser representado.",
    "RecursionError": "Erro de recursão, ocorre quando a profundidade máxima de recursão é excedida.",
    "StopIteration": "Exceção que é levantada para indicar o fim de uma iteração.",
    "KeyboardInterrupt": "Exceção que é levantada quando o usuário interrompe a execução do programa, geralmente pressionando Ctrl+C.",
    "SystemExit": "Exceção que é levantada quando o programa está prestes a terminar sua execução.",
    "FloatingPointError": "Erro de ponto flutuante, ocorre quando uma operação de ponto flutuante falha.",
    "AssertionError": "Erro de asserção, ocorre quando uma asserção (declaração assert) falha.",
    "UnicodeError": "Erro de Unicode, ocorre quando há um problema com a codificação ou decodificação de strings Unicode.",
    "DeprecationWarning": "Aviso de descontinuação, indica que uma funcionalidade está obsoleta e pode ser removida em versões futuras.",
    "RuntimeError": "Erro de tempo de execução, ocorre quando um erro é detectado que não se enquadra em nenhuma das outras categorias.",
    "NotImplementedError": "Erro de não implementado, ocorre quando um método ou função que deveria ser implementado em uma subclasse não foi implementado.",
    "EnvironmentError": "Erro de ambiente, ocorre quando há um problema relacionado ao ambiente do sistema, como problemas de I/O.",
    "IOError": "Erro de entrada/saída, ocorre quando uma operação de I/O falha.",
    "OSError": "Erro do sistema operacional, ocorre quando uma operação do sistema operacional falha.",
    "BufferError": "Erro de buffer, ocorre quando uma operação relacionada a buffers falha.",
    "ConnectionError": "Erro de conexão, ocorre quando uma operação de rede falha.",
    "TimeoutError": "Erro de tempo limite, ocorre quando uma operação excede o tempo limite definido.",
    "ModuleNotFoundError": "Erro de módulo não encontrado, ocorre quando um módulo especificado não pode ser encontrado.",
    "ChildProcessError": "Erro de processo filho, ocorre quando há um problema relacionado a processos filhos.",
    "BrokenPipeError": "Erro de pipe quebrado, ocorre quando se tenta escrever em um pipe que não tem mais leitores.",
    "FileExistsError": "Erro de arquivo já existe, ocorre quando se tenta criar um arquivo que já existe.",
    "NameError": "Erro de nome, ocorre quando uma variável ou função não é encontrada no escopo atual.",
    "UnboundLocalError": "Erro de variável local não vinculada, ocorre quando uma variável local é referenciada antes de ser atribuída.",
    "TabError": "Erro de tabulação, ocorre quando há uma mistura inconsistente de tabulações e espaços na indentação do código.",
}

print(erros_python["SyntaxError"])

for coisa in erros_python:
    print(coisa)
    print(erros_python[coisa])

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log["France"][1])

nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        "year": 2023},

    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
        "year": 2020},
}

print(travel_log["Germany"]["cities_visited"][2])

