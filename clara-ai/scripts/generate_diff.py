import difflib
import os

def create_diff(account):
    v1 = open(f"outputs/accounts/{account}/v1/account_memo.json").read().splitlines()
    v2 = open(f"outputs/accounts/{account}/v2/account_memo.json").read().splitlines()

    html = difflib.HtmlDiff().make_file(v1, v2)

    os.makedirs("dashboard/diffs", exist_ok=True)

    with open(f"dashboard/diffs/{account}.html", "w") as f:
        f.write(html)

    print(f"Diff generated for {account}")


accounts = os.listdir("outputs/accounts")

for acc in accounts:
    create_diff(acc)