

def diff_state_file(plan_output, plan_output_2):
    diff_output = ""
    if len(plan_output)-len(plan_output_2) > 0:
        for line in plan_output_2.split("\n"):
            if line in plan_output:
                diff_output=diff_output.trim()+line
    else:
        for line in plan_output.split("\n"):
            if line in plan_output_2:
                diff_output=diff_output.trim()+line
    return diff_output