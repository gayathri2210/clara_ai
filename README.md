Clara Automation Pipeline
Submitted By Gayathri Dhanasekaran
This project implements a zero-cost automation pipeline that converts demo and onboarding call transcripts into Retell voice agent configurations.

The system automatically:

1)Processes demo call transcripts

2)Generates a structured Account Memo JSON

3)Creates a Retell Agent Draft Specification (v1)

4)Applies onboarding updates to produce Agent v2

5)Tracks changes and stores outputs with versioning

Provides a simple dashboard and diff viewer

Architecture Overview:
flowchart LR

A[Demo Call Recordings / Transcripts] --> B[Ingestion & Normalization]
B --> C[Assign Account ID]

C --> D[Extraction Engine<br/>Rule-based Parser]
D --> E[Account Memo JSON]

E --> F[Prompt Generator]
F --> G[Retell Agent Draft Spec v1]

G --> H[Store Outputs<br/>outputs/accounts/<account_id>/v1]

I[Onboarding Call Recordings / Transcripts] --> J[Onboarding Extraction]
J --> K[Patch / Update Existing Account Memo]

K --> L[Regenerate Agent Spec v2]
L --> M[Store Outputs<br/>outputs/accounts/<account_id>/v2]

H --> N[Diff Engine]
M --> N

N --> O[Dashboard UI]
O --> P[Metrics + Change Viewer]

subgraph Automation Layer
Q[n8n Workflow]
end

Q --> B
Q --> D
Q --> F
Q --> L






Automated call testing and validation
