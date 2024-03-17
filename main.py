import subprocess
from parse_state_diff import parse_state_diff


def run_terraform_plan():
    plan_process = subprocess.run("terraform plan", shell=True, check=True, capture_output=True)
    return plan_process.stdout.decode("utf-8")

if __name__ == "__main__":
    plan_output = run_terraform_plan()
    plan_output_2 = run_terraform_plan()
    diff_output = parse_state_diff(plan_output, plan_output_2)
    
