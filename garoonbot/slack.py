import json

import requests

def send(settings, head, detail=None):
    """
    Send message to Slack

    Args:
        head (str): Headline
        detail (Optional[str]): Detail message ```%s```
    """
    message = '%s\n```%s```' % (head, detail) if detail else head
    requests.post(
        settings['slack']['url'],
        data=json.dumps({
            'username': settings['slack']['username'],
            'icon_emoji': ':%s:' % settings['slack']['emoji'].strip(':'),
            'text': message,
            'channel': settings['slack']['channel']}),
        timeout=10)
