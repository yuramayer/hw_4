
def limited_cycler(observation, configuration):
    return (observation.step * 2) % configuration.signs
