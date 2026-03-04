Clara Automation Pipeline

Submitted by: Gayathri Dhanasekaran

This project implements a zero-cost automation pipeline that converts demo and onboarding call transcripts into Retell voice agent configurations.

The system automatically:

Processes demo call transcripts

Generates a structured Account Memo JSON

Creates a Retell Agent Draft Specification (v1)

Applies onboarding updates to produce Agent v2

Tracks changes and stores outputs with versioning

Provides a simple dashboard and diff viewer

Architecture Overview
<img width="1690" height="610" alt="architecture1" src="https://github.com/user-attachments/assets/2a3d88ac-9675-449c-8681-652ebdb070a5" /> <img width="1582" height="446" alt="architecture2" src="https://github.com/user-attachments/assets/8b1510cb-a6c2-4d4e-82c7-9b5627d2ab6f" />
Data Flow

The system processes data in two phases.

Pipeline A – Demo Call Processing

Demo call transcript is ingested

Account ID is assigned

Structured business information is extracted

Account Memo JSON is generated

Retell agent specification v1 is created

Outputs are stored

Pipeline B – Onboarding Updates

Onboarding call transcript is ingested

Additional information is extracted

Existing account memo is updated

Agent specification v2 is generated

Differences between v1 and v2 are tracked

1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/clara-automation-pipeline.git

cd clara-automation-pipeline

How to Run Locally
1. Install Dependencies

Ensure the following are installed:

Python 3.10+

Docker

n8n

2. Start the API Server

Run the pipeline API:

python scripts/api_runner.py

Server runs at:

http://127.0.0.1:5000

3. Start n8n

Run n8n with Docker:

docker compose up

Open the n8n editor:

http://localhost:5678

4. Run the Dashboard

Serve the dashboard locally:

python -m http.server 8000

Open the dashboard:

http://localhost:8000/dashboard/index.html

The dashboard allows:

Viewing processed accounts

Comparing v1 vs v2

Viewing summary metrics

Dataset Usage

The system processes the provided:

Demo call transcripts

Onboarding call transcripts

Each dataset file is processed to generate outputs per account_id.

Example account:

bens-electric
Generated Outputs

For each account the system produces:

Account Memo

Structured business data extracted from conversations.

Example:

{
  "business_name": "Ben's Electrical Solutions",
  "service_call_fee": "$115",
  "hourly_rate": "$98",
  "business_hours": "Monday - Friday 8:30 AM - 5 PM"
}
Retell Agent Specification

Defines the voice agent behaviour, including:

Greeting

Call routing

Business hours handling

Emergency call routing

Fallback logic

Two versions are generated:

v1 → generated from demo call

v2 → updated from onboarding call

Dashboard Features

The dashboard provides a simple UI for:

1.Account Explorer

2.View processed accounts.

3.Diff Viewer

Highlights configuration changes between:

v1 → v2

Metrics

Displays pipeline statistics:

1.Number of processed accounts

2.Number of versions generated

3.Number of configuration changes

LLM Usage

The assignment requires zero-cost execution, so this implementation uses:

Rule-based extraction + templating

instead of paid LLM APIs.

This ensures:

Deterministic outputs

No hallucination

Zero runtime cost

Missing information is flagged under:

questions_or_unknowns
Retell Setup

The system generates a Retell Agent Draft Spec JSON.

If API access is unavailable on the free tier:

Create a Retell account

Open the Retell Agent Builder

Paste the generated agent_spec.json

Configure the voice agent manually

This ensures compatibility with the expected Retell configuration format.

Known Limitations

1.Extraction uses rule-based parsing instead of a semantic model

2.Complex conversation structures may require additional rules

3.Dashboard is minimal and intended for demonstration

4.Real deployments would require secure data storage and authentication

Production Improvements

With production access, the system could be extended with:

1. LLM-Based Semantic Extraction

Improves understanding of conversational context.

2. Automatic Speech Transcription

Directly process call recordings without transcripts.

3. CRM Integration

Create tickets in systems such as:

Asana

HubSpot

Salesforce

4. Agent Simulation

Automatically test generated voice agents.

5. Deployment Pipeline

Push generated agents directly to Retell via API.
