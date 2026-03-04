import os, json

accounts = os.listdir("outputs/accounts")

metrics = {
    "total_accounts": len(accounts),
    "accounts": accounts
}

with open("dashboard/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("Metrics generated")