
def counter_cycler_agent(observation, configuration):
    return (observation.step + 1) % configuration.signs
