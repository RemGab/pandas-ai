"""Example of using PandasAI with am Excel file."""

import os

from pandasai import Agent

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "$2a$10$yv13u18eyh4o4pt32aB1puDceJI1kmVfI3vowSgq7uovkvPPkubRC"

agent = Agent("data/AMZN.csv")
response = agent.chat("donne moi les derniers prix de amazon")
print(response)
# Output: 247 loans have been paid off by men.
