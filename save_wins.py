
import random 

action_history = []

def save_wins(observation, configuration):
    global action_history

    def determine_result(my_move, opponent_move):
        if my_move == opponent_move:
            return 0  # Ничья
        elif (my_move - opponent_move) % configuration.signs == 1:
            return 1  # Победа
        else:
            return -1  # Поражение

    if observation.step == 0:
        next_action = random.randrange(configuration.signs)
    else:
        last_result = determine_result(action_history[-1], observation.lastOpponentAction)
        if last_result == 1:
            next_action = action_history[-1]  # Повторяем предыдущий успешный ход
        else:
            next_action = random.randrange(configuration.signs)  # Выбираем случайный ход
    action_history.append(next_action)
    return next_action
