import json, os

def create_v2(account_id):

    with open(
        f"outputs/accounts/{account_id}/v1/account_memo.json"
    ) as f:
        memo = json.load(f)

    memo["business_hours"] = {
        "days": "Mon-Fri",
        "start": "8:00",
        "end": "17:00"
    }

    memo["notes"] += " | Updated from onboarding"

    path=f"outputs/accounts/{account_id}/v2"
    os.makedirs(path,exist_ok=True)

    with open(f"{path}/account_memo.json","w") as f:
        json.dump(memo,f,indent=2)

create_v2("bens-electric")