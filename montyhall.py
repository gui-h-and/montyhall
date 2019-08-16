#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ------------------
# MONTY HALL PROBLEM
# Link: https://pt.wikipedia.org/wiki/Problema_de_Monty_Hall
# O jogo: Monty Hall, o apresentador, apresentava três portas aos concorrentes. Atrás de uma delas estava um prêmio (um carro) e, atrás das outras duas, dois bodes.
# Na 1.ª etapa o concorrente escolhe uma das três portas (que ainda não é aberta);
# Na 2.ª etapa, Monty abre uma das outras duas portas que o concorrente não escolheu, revelando que o carro não se encontra nessa porta e revelando um dos bodes;
# Na 3.ª etapa Monty pergunta ao concorrente se quer decidir permanecer com a porta que escolheu no início do jogo ou se ele pretende mudar para a outra porta que ainda está fechada para então a abrir. Agora, com duas portas apenas para escolher — pois uma delas já se viu, na 2.ª etapa, que não tinha o prêmio — e sabendo que o carro está atrás de uma das restantes duas, o concorrente tem que tomar a decisão.
# Qual é a estratégia mais lógica? Ficar com a porta escolhida inicialmente ou mudar de porta?
# ------------------

# ALGORITHM
# ------------------
# GET randomly user's chosen door
# SET values for the 3 doors (one of them has the prize)
# ELIMINATE one of the two remained doors (the goat one)
# ITERATE both choices (change door or keep it)
# SAVE results

# IMPORTS
# ------------------
# STANDART LIBRARY
import random

#THIRT PARTY
import numpy as np

#LOCAL APPLICATION


# VARIABLES
# ------------------
changed_door_ratio = 0
result_without_change = 0
result_with_change = 0
unchanged_door_ratio = 0


def play_dice(min, max):
    """Randomize between min & max
    """
    return random.randint(min, max)


def set_door_prizes(doors):
    """Set values ​​for each door, in a way that only one door has a car prize
    """

    doors[0] = play_dice(0,1)
    while doors[0]+doors[1]+doors[2]!=1:
        if doors[0] == 0:
            doors[1] = play_dice(0,1)
            if doors[1] == 0:
                doors[2] = play_dice(0,1)
            
        
    
    return doors


def elim_door(user_choice, doors):
    """After the guest chooses, the show host eliminates one of the two remaining doors
    """

    if user_choice == 0:
        if doors[1]+doors[2] == 0:
            changed_door = random.choice([1, 2])
        
        elif doors[1] == 1:
            changed_door = 1

        elif doors[2] == 1:
            changed_door = 2

    elif user_choice == 1:
        if doors[0]+doors[2] == 0:
            changed_door = random.choice([0, 2])
        
        elif doors[0] == 1:
            changed_door = 0
        
        elif doors[2] == 1:
            changed_door = 2
        
    elif user_choice == 2:
        if doors[0]+doors[1] == 0:
            changed_door = random.choice([0, 1])
        
        elif doors[0] == 1:
            changed_door = 0
        
        elif doors[1] == 1:
            changed_door = 1

    
    return changed_door


def run_simulation(num_iterations):

    num_executions = num_iterations
    result_with_change = 0
    result_without_change = 0

    while (num_executions > 0):

        doors = set_door_prizes(np.array([0, 0, 0]))
        #print("\nPortas: %s" % (doors))

        user_choice = play_dice(0, 2)
        #print("Escolha inicial: %s" % (user_choice))

        changed_door = elim_door(user_choice,doors)
        #print("Porta restante:  %s" % (changed_door))

        if doors[user_choice] == 1:
            result_without_change = result_without_change + 1

        if doors[changed_door] == 1:
            result_with_change = result_with_change + 1


        num_executions = num_executions - 1


    unchanged_door_ratio = float(result_without_change)*100/num_iterations
    changed_door_ratio = float(result_with_change)*100/num_iterations

    print("\n-------- MONTY HALL PROBLEM --------")
    print("\n Amont of iterations: %d" % (num_iterations))
    print("\n Keeping initial choice:\n %d cars (%.2f%%)" % (result_without_change, unchanged_door_ratio))
    print("\n Changing choice:\n %d cars (%.2f%%)\n" % (result_with_change, changed_door_ratio))


run_simulation(10)
run_simulation(100)
run_simulation(1000)
run_simulation(10000)