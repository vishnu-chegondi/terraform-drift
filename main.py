import subprocess
from parse_state_diff import diff_state_file


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
    
