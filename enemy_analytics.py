
from collections import Counter
import random 

opponent_moves = []

def enemy_analytics(observation, configuration):
    global opponent_moves
    if observation.step == 0:
        opponent_moves = []
        return random.randrange(configuration.signs)
    
    opponent_moves.append(observation.lastOpponentAction)
    move_counts = Counter(opponent_moves)
    most_common_move = move_counts.most_common(1)[0][0]
    return (most_common_move + 1) % configuration.signs
