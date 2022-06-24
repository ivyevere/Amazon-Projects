import requests
import json

# message = '@Present test'

def chimeAlert(message):
    webhook_url = 'https://hooks.chime.aws/incomingwebhooks/95756985-ecd6-45d3-a1f9-7f65cb40855e?token=WW12MTVheGJ8MXxyN0JMOU1kV0twV2MzMnRLRHYxSzhpUThyMGxZOGJDSG85eXJtdEUzcXVB'
    r = requests.post(
    url = webhook_url,
    json = {'Content': message}
    )

# print(r)