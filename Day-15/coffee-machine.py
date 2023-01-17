import os
import machine_data

data = machine_data
resources = data.resources

def get_report():
    output = ""
    for i in resources:
        output += (f"{i}: {resources[i]}\n")
    return output
report = get_report()


