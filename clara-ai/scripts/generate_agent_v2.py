import json
import os

ACCOUNT_ID = "bens-electric"

def generate_v2_agent(account_id):

    memo_path = f"outputs/accounts/{account_id}/v2/account_memo.json"

    with open(memo_path, "r") as f:
        memo = json.load(f)

    agent = {
        "agent_name": f"{memo['company_name']} Clara Agent",
        "version": "v2",
        "voice_style": "Professional, concise",

        "system_prompt": f"""
You are an AI receptionist for {memo['company_name']}.

BUSINESS HOURS:
{memo.get("business_hours", "UNKNOWN")}

OFFICE HOURS FLOW:
- Greet caller
- Ask purpose
- Collect name and phone number
- Collect service details
- Offer scheduling preference
- Transfer if requested
- Ask if anything else is needed
- Close call politely

AFTER HOURS FLOW:
- Confirm if emergency
- If authorized emergency → transfer immediately
- Otherwise collect details
- Promise follow-up next business day

Never mention internal systems or tools.
""",

        "variables": {
            "business_hours": memo["business_hours"]
        },

        "call_transfer_protocol":
    memo.get(
        "call_transfer_rules",
        {
            "transfer_allowed": True,
            "fallback": "Notify owner"
        }
    ),

        "fallback_protocol": {
            "transfer_failure":
            "Apologize and assure caller the team will follow up shortly."
        }
    }

    output_path = f"outputs/accounts/{account_id}/v2"
    os.makedirs(output_path, exist_ok=True)

    with open(f"{output_path}/agent_spec.json", "w") as f:
        json.dump(agent, f, indent=2)

    print("v2 agent created")

generate_v2_agent(ACCOUNT_ID)