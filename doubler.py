
import random 

def doubler(observation, configuration):
    print(f"Step: {observation.step}, Signs: {configuration.signs}")  # Для проверки
    if observation.step == 0:
        return random.randrange(configuration.signs)
    return (observation.step * 2) % configuration.signs
