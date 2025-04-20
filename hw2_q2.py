from enum import Enum
from collections import namedtuple
from itertools import zip_longest

# Define the possible conditions
Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

# Helper: determines if the agent can attend a meeting
def is_active(agent):
    return agent.category not in {Condition.HEALTHY, Condition.DEAD}

# Helper: applies the cure effect to the agent
def cure_effect(agent):
    if agent.category == Condition.DYING:
        return agent._replace(category=Condition.SICK)
    elif agent.category == Condition.SICK:
        return agent._replace(category=Condition.HEALTHY)
    return agent

# Helper: worsens the agent’s condition
def worsen(agent):
    if agent.category == Condition.SICK:
        return agent._replace(category=Condition.DYING)
    elif agent.category == Condition.DYING:
        return agent._replace(category=Condition.DEAD)
    return agent

# Helper: handles a meeting between two active agents
def process_pair(a1, a2):
    if a1.category == Condition.CURE and a2.category != Condition.CURE:
        return a1, cure_effect(a2)
    elif a2.category == Condition.CURE and a1.category != Condition.CURE:
        return cure_effect(a1), a2
    elif a1.category == Condition.CURE and a2.category == Condition.CURE:
        return a1, a2
    else:
        return worsen(a1), worsen(a2)

# Main function
def meetup(agent_listing: tuple) -> list:
    active_agents = [agent for agent in agent_listing if is_active(agent)]
    inactive_agents = [agent for agent in agent_listing if not is_active(agent)]
    
    result_agents = []

    # Group agents into pairs (a1, a2), handle odd number with zip_longest
    for a1, a2 in zip_longest(*[iter(active_agents)]*2):
        if a2 is None:
            result_agents.append(a1)
        else:
            updated1, updated2 = process_pair(a1, a2)
            result_agents.extend([updated1, updated2])

    return result_agents + inactive_agents

