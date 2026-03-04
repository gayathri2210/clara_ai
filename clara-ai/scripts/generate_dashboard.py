import os, json

accounts_dir = "outputs/accounts"

accounts = os.listdir(accounts_dir)

with open("dashboard/accounts.json", "w") as f:
    json.dump(accounts, f, indent=2)

print("Dashboard data generated")