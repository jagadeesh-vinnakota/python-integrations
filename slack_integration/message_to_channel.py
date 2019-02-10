import os
from slackclient import SlackClient
'''
  Post messages to slack channel. For this we need a slack token which we can get during the installation
  of slack app in the slack workspace.
'''
sc = SlackClient(os.environ["SLACK_TOKEN"])

# Posting a message to machine-learning slack channel.
sc.api_call(
  "chat.postMessage",
  channel="machine-learning",
  text="Hello from Python! :tada:"
)
