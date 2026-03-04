import json

def create_v1(account_id, company):
    memo = {
        "account_id": account_id,
        "company_name": company,
        "business_hours": {},
        "services_supported": [],
        "questions_or_unknowns": [
            "Business hours not confirmed in demo"
        ],
        "notes": "Generated from demo call"
    }

    path = f"outputs/accounts/{account_id}/v1"
    
    import os
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/account_memo.json","w") as f:
        json.dump(memo,f,indent=2)

create_v1("bens-electric","Ben's Electric")