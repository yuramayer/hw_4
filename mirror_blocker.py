
import random 

def mirror_blocker(observation, configuration):
    print(f"Step: {observation.step}, Signs: {configuration.signs}")  # Для проверки
    if observation.step == 0:
        return random.randrange(0,3)
    return (observation.lastOpponentAction + 1) % configuration.signs
