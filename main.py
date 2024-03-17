import subprocess
import os
from slack_notifications import Slack


def get_slack():
    slack_token = os.getenv("SLACK_TOKEN")
    return Slack(slack_token)

def send_slack_message(channel, username, text):
    slack = get_slack()
    try:
        slack.send_notify(channel=channel, username=username, text=text)
    except Exception as e:
        print("Error in sending slack message: ", e)
        return False
    finally:
        return True

def diff_state_file(plan_output, plan_output_2):
    diff_output = ""
    if len(plan_output)-len(plan_output_2) > 0:
        for line in plan_output_2.split("\n"):
            if line in plan_output:
                diff_output=diff_output+"\n"+line
    else:
        for line in plan_output.split("\n"):
            if line in plan_output_2:
                diff_output=diff_output+"\n"+line
    return diff_output.strip()


def run_terraform_plan():
    plan_process = subprocess.run("terraform plan", shell=True, check=True, capture_output=True)
    return plan_process.stdout.decode("utf-8")

if __name__ == "__main__":
    plan_output = run_terraform_plan()
    subprocess.run("git checkout -b prev_branch HEAD~1", shell=True, check=True)
    plan_output_2 = run_terraform_plan()
    subprocess.run("git checkout main", shell=True, check=True)
    subprocess.run("git branch -D prev_branch", shell=True, check=True)
    diff_output = diff_state_file(plan_output, plan_output_2)
    print(diff_output)
    # send_slack_message("testdrift2", "testdrift2", diff_output)
    
