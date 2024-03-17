from slack_notifications import Slack


def get_slack():
    return Slack(SLACK_TOKEN)


def send_slack_message(channel, username, text):
    slack = get_slack()
    try:
        slack.send_notify(channel=channel, username=username, text=text)
    except Exception as e:
        print("Error in sending slack message: ", e)
        return False
    finally:
        return True

send_slack_message(channel="testdrift", username="testdrift2", text="Test Message sent to check the drift status")


