import json

def generate_agent(account_id):

    memo_path = f"outputs/accounts/{account_id}/v1/account_memo.json"

    with open(memo_path) as f:
        memo = json.load(f)

    agent = {
        "agent_name": f"{memo['company_name']} Clara",
        "version": "v1",
        "voice_style": "professional friendly",
        "system_prompt": "Handle calls, collect name and phone number and route appropriately."
    }

    with open(
        f"outputs/accounts/{account_id}/v1/agent_spec.json","w"
    ) as f:
        json.dump(agent,f,indent=2)

generate_agent("bens-electric")