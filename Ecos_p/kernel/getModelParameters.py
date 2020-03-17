# -*- coding: utf-8 -*-
import os2

files = os.listdir(path=os.getcwd())

#TODO: pegar espacos do arquivo spaces.py
def get_espaces(spaces_file = 'spaces.py'):
    try:
        file = open(spaces_file,"r")
        spaces = []
        for linha in file:

            if linha[0:5] == 'class' and linha[-2] == ':':
                spaces.append(linha[6:-9])
        return spaces

    except:
        print('Arquivo de espaços não encontrado')
        return 'ERRO'

#TODO: pegar agentes do arquivo
def get_agents(agents_file = 'agents.py'):
    try:
        file = open(agents_file, 'r')
        agents = []
        for linha in file:
            if linha[0:5] == 'class' and linha[-2] == ':':
                agents.append(linha[6:linha.index('(')])
        return agents

    except:
        print('Arquivo de agentes não encontrado')
        return 'ERRO'

#TODO: pegar agentes do arquivo. Recomendado que todos os actionSets tenham "ActionSet" no nome do módulo
def list_actionSet_files(actionSet_name):
    actionSet_files = []

    for file in files:

        if actionSet_name in file:
            actionSet_files.append(file[:-3])

    if not actionSet_files == []:
        return actionSet_files

    else:
        print('Nenhum arquivo de ação foi encontrado')
        return "ERRO"

#TODO: pegar as ações dentro do actionSet esolhido
def get_actions_from_ActionSet(actionSet_file):
    try:
        file = open(actionSet_file, 'r')
        actions = []
        for linha in file:
            if not '__init__' in linha:
                if 'def' in linha and linha[-2] == ':':
                    actions.append(linha[linha.index('def') + 4:linha.index('(')])

        return actionSet_file, actions

    except:
        print('Arquivo de ação não encontrado')
        return 'ERRO'


"""
WEB - O usuário entra com o nome do arquivo .py que contém os espaços
"""
#TODO: pegar lista de todos os espacos dentro do arquivo de espaços (spaces.py)
space_list = get_espaces()


#TODO: pega cada espaço é vetor com atributos próprios. Inicializa o spaces
spaces = dict()
for space in space_list:
    spaces[space] = [{'ActionSet': []},
                     [],
                     []]

print('Spaces:')
for key, arg in spaces.items():
    print(key, arg)

#TODO: sao exibidos os arquivos '...ActionSet.py'
actionSet_name = 'ActionSet'
actionSet_list = list_actionSet_files(actionSet_name=actionSet_name)

#TODO: (WEB) seleiona um ActionSet dentro de actionSet_list
actionSet_file = actionSet_list[0]

"""
WEB - são exibidos arquivos .py que contenham os conjuntos de ações
"""

#TODO: pegar todas as ações de um ActionSet do modelo (DumbModelActionSet.py)
actionSet = get_actions_from_ActionSet(actionSet_file=actionSet_file)

#TODO: escolhe o actionSet_file para cada space. Neste caso, o actionSet é o mesmo para os dois espacos
spaces['FunnySpace'][0] = {actionSet_file: actionSet}
spaces['BoringSpace'][0] = {actionSet_file: actionSet}

"""
WEB - o usuário escolhe as ações dentro do action set para cada estado
"""
#TODO: armazena em cada estado a lista de ações desejadas. Antes de inserir ações ao estado, é checado se a ação está definida dentro de actionSet
def put_actions_into_space(actions, space, spaces):
    aux = spaces[space][1].copy()

    if space in spaces:
        for action in actions:
            if spaces[space][0][str(spaces[space][0].keys()).lstrip('dict_keys')[3:-3]]:
                aux.append(action)

    spaces[space][1] = aux

"""
WEB: Para cada espaço, o usuário escolha e adiciona uma ação dentro do conjunto de ações do espaço
Por enquanto, só existe um actionSet (dumbModelActionSet). Portanto, estou usando o mesmo actionSet para os dois espaços
"""
print('\nActionSet_file: ', actionSet_file)
put_actions_into_space(actions=['happy_hello', 'formal_hello'], space='FunnySpace', spaces=spaces)
print(spaces)

print('\nActionSet_file: ', actionSet_file)
put_actions_into_space(actions=['simple_hello', 'sim_info'], space='BoringSpace', spaces=spaces)
print(spaces)

"""
AGENTES
"""
print('\nAgents:')
agents_file = 'agents.py'
agents_list = get_agents(agents_file=agents_file)
agents = dict()
for agent in agents_list:
    print(agent)
    agents[agent] = [[],[]]

#TODO: (WEB) adiciona os espaços (previamente selecionados)ao agente
print('\nSelecionando os espaços de cada agente')

print('- Funny_Bug')
for space in spaces:
    if space == 'FunnySpace':
        print('\t'+space + ' SELECIONADO')
agents['Funny_Bug'][0] = ['FunnySpace']

print('\n- Circumspect_Bug')
for space in spaces:
    if space == 'FunnySpace' or 'BoringSpace':
        print('\t'+space + ' SELECIONADO\n')
agents['Circumspect_Bug'][0] = ['FunnySpace', 'BoringSpace']

# So mostra os agentes e suas definicoes
for agent, definition in agents.items():
    print(agent, definition)

