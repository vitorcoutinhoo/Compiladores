# Analisador Léxico

Analisador léxico criado na matéria de Compiladores para reconhecer <br> os tokens da linguagem cic_2024.1.

## Organização das Pastas

_automaton_: 
- Contém o dicionario dos estados (automaton.txt), que serve para a <br> montagem da tabela de trasições.
- Contém a tabela de trasições (df.txt), serve para vizualizar as <br> transições e seus estados resultantes.

_input_: Pasta reservada a colocar todos os códigos a passar pelo <br>analisador léxico. O arquivo tem que ter o formato referente a linguagem apresentada: "*.cic*".

_logs_: Pasta reservada aos outputs dos códigos. O arquivo será formatado: "*nomedoarquivodeentrada.log*"

_codes_:
- _reader_pointer.py_: Classe responsável por ler o arquivo de entrada.
- _reserved_words_and_automaton.py_: Contém funções relacionadas a criação do automato, <br> guardar as palavras reservadas e os estados finais.
- _tokens.py_: Função responsável por identificar os tokens
- _tables.py_: Classe responsável pela criação das tabelas
- _error.py_: Classe responsável por identificar os tipos de erros e mostrar-los no código.

_main.py_: Arquivo principal

