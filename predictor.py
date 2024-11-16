
import random

pattern_history = {}

def predictor(observation, configuration):
    global pattern_history
    if observation.step == 0:
        pattern_history = {}
        return random.randrange(configuration.signs)
    
    last_move = observation.lastOpponentAction
    if last_move in pattern_history:
        pattern_history[last_move] += 1
    else:
        pattern_history[last_move] = 1

    # Предсказываем следующий ход противника
    predicted_move = max(pattern_history, key=pattern_history.get)
    return (predicted_move + 1) % configuration.signs
