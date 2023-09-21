
from fixieai import agents

BASE_PROMPT = """I am an intelligent agent that does a task."""

FEW_SHOTS = """
Q: Example question here
A: Example of answer here
"""

agent = agents.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)
