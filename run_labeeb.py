from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/current/dialogue', interpreter=nlu_interpreter, action_endpoint=action_endpoint)

input_channel = SlackInput('SLACK KEY STAETING WITH xoxb')  # TODO Replace with your own SLACK KEY,
# TODO this needs to to be enhanced to use environment variables

# print("Your bot is ready to talk! Type your messages here or send 'stop'")
agent.handle_channels([input_channel], 5005, serve_forever=True)
