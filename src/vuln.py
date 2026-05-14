import subprocess

def run_user_input(user_input):
    # intentional command injection vuln - should be flagged by a real review
    subprocess.call(user_input, shell=True)
