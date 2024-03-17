

def diff_state_file(plan_output, plan_output_2):
    if len(plan_output)-len(plan_output_2) > 0:
        for line in plan_output_2.split("\n"):
            plan_output = plan_output.replace(line, "")
        diff_output = plan_output
    else:
        for line in plan_output.split("\n"):
            plan_output_2 = plan_output_2.replace(line, "")
        diff_output = plan_output_2
    return diff_output