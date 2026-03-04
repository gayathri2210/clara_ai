Clara Automation Pipeline
Submitted By Gayathri Dhanasekaran
This project implements a zero-cost automation pipeline that converts demo and onboarding call transcripts into Retell voice agent configurations.

The system automatically:

Processes demo call transcripts

Generates a structured Account Memo JSON

Creates a Retell Agent Draft Specification (v1)

Applies onboarding updates to produce Agent v2

Tracks changes and stores outputs with versioning

Provides a simple dashboard and diff viewer

Architecture Overview

The pipeline follows this flow:

Demo Call Transcript
        ↓
Extraction Script
        ↓
Account Memo (v1 JSON)
        ↓
Agent Prompt Generator
        ↓
Retell Agent Draft (v1)
        ↓
Onboarding Transcript
        ↓
Patch + Update
        ↓
Account Memo (v2)
        ↓
Retell Agent Draft (v2)

Automation is orchestrated using n8n.

The workflow triggers a Python API service which runs the pipeline scripts.

n8n Manual Trigger
        ↓
HTTP Request
        ↓
api_runner.py
        ↓
run_pipeline.py
        ↓
Outputs generated
Project Structure
clara-ai/
│
├── workflows/
│   └── n8n_pipeline.json
│
├── dataset/
│   ├── demo_calls/
│   └── onboarding_calls/
│
├── scripts/
│   ├── run_pipeline.py
│   ├── generate_agent_v2.py
│   ├── api_runner.py
│   ├── generate_dashboard.py
│   ├── generate_diff.py
│   └── summary_metrics.py
│
├── outputs/
│   └── accounts/
│       └── <account_id>/
│           ├── v1/
│           └── v2/
│
├── dashboard/
│   ├── index.html
│   ├── metrics.json
│   └── diffs/
│
└── README.md
Running the Project Locally
1 Install Python Dependencies
pip install flask
2 Start the Pipeline API
python scripts/api_runner.py

This launches a local API server that executes the pipeline.

3 Run the Dashboard

Start a local web server:

python -m http.server 8000

Open:

http://localhost:8000/dashboard/index.html

The dashboard shows:

processed accounts

batch metrics

version differences

4 Run Automation via n8n

Start n8n using Docker:

docker compose up

Open:

http://localhost:5678

Import the workflow:

workflows/n8n_pipeline.json

Execute the workflow to run the pipeline.

Dataset Usage

Place transcripts in the dataset folders.

dataset/demo_calls/<account_id>.txt
dataset/onboarding_calls/<account_id>.txt

Example:

dataset/demo_calls/bens-electric.txt
dataset/onboarding_calls/bens-electric.txt

The pipeline automatically detects accounts based on filenames.

Output Structure

Outputs are generated per account with versioning.

outputs/accounts/<account_id>/v1/
outputs/accounts/<account_id>/v2/

Example:

outputs/accounts/bens-electric/v1/account_memo.json
outputs/accounts/bens-electric/v1/agent_spec.json

outputs/accounts/bens-electric/v2/account_memo.json
outputs/accounts/bens-electric/v2/agent_spec.json
Dashboard Features

The project includes a lightweight UI dashboard.

Features:

Clara AI pipeline metrics

list of processed accounts

clickable v1 → v2 diff viewer

Open:

dashboard/index.html
Diff Viewer

Version differences are generated automatically.

Run:

python scripts/generate_diff.py

Example output:

dashboard/diffs/bens-electric.html

This visually highlights changes between v1 and v2 configurations.

Batch Processing and Metrics

Batch metrics are generated with:

python scripts/summary_metrics.py

Example:

dashboard/metrics.json

This displays the total number of processed accounts in the dashboard.

Retell Agent Setup

A Retell Agent Specification JSON is generated for each account.

Example:

outputs/accounts/bens-electric/v2/agent_spec.json

Because Retell API access may require paid usage, the assignment outputs a configuration spec instead of directly creating agents.

To recreate the agent in Retell:

Create a Conversation Flow Agent

Set execution mode to Flex Mode

Paste the generated system_prompt

Configure transfer logic and business hours

LLM Usage

The project follows the zero-cost constraint.

No paid APIs are used.

Extraction and prompt generation are performed using:

rule-based parsing

structured templates

deterministic logic

This ensures the pipeline remains fully reproducible.

Known Limitations

Transcript parsing is rule-based and may miss unusual phrasing

Diff viewer currently compares only account memo JSON

Dashboard is a lightweight local visualization rather than a production UI

Retell agents are generated as specifications rather than automatically deployed

Future Improvements (With Production Access)

If production resources were available, improvements would include:

LLM-powered semantic extraction for better transcript understanding

Direct Retell API integration for automatic agent deployment

Database storage instead of filesystem outputs

Real-time dashboard and monitoring

Automated call testing and validation
