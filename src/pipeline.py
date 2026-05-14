import subprocess

def process(record):
    # pipeline processor
    subprocess.call(f"process_record {record['id']}", shell=True)
