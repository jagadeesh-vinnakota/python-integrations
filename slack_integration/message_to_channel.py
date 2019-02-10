import os
from slackclient import SlackClient
sc = SlackClient(os.environ["SLACK_TOKEN"])

sc.api_call(
  "chat.postMessage",
  channel="machine-learning",
  text="Hello from Python! :tada:"
)
