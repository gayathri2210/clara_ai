import os
import subprocess

DEMO_FOLDER = "dataset/democalls"
ACCOUNTS = []

# detect accounts automatically
for file in os.listdir(DEMO_FOLDER):
    if file.endswith(".txt"):
        ACCOUNTS.append(file.replace(".txt", ""))

print("Accounts found:", ACCOUNTS)


for account in ACCOUNTS:

    print(f"\nProcessing {account}")

    subprocess.run(
        ["python", "scripts/extract_demo.py", account]
    )

    subprocess.run(
        ["python", "scripts/generate_agent.py", account]
    )

    subprocess.run(
        ["python", "scripts/apply_onboarding_patch.py", account]
    )

    subprocess.run(
        ["python", "scripts/generate_agent_v2.py", account]
    )

print("Pipeline completed for all accounts")