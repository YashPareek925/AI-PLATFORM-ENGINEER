# AI Platform Engineer Demo Project

## Objective
This project converts natural language prompts into structured application configurations using a multi-stage pipeline.

The goal is to simulate how a compiler-like AI system can generate software architecture from user requirements.

---

# Features

- Multi-stage generation pipeline
- Intent extraction
- System design generation
- Schema generation
- Validation system
- Repair engine
- Runtime simulation
- Evaluation framework

---

# Pipeline

User Prompt
→ Intent Extractor
→ System Designer
→ Schema Generator
→ Validator
→ Repair Engine
→ Runtime Simulation

---

# Tech Stack

- Python
- FastAPI
- Pydantic

---

# How To Run

## Install dependencies

```bash

pip install -r requirements.txt

Run server

uvicorn app.main:app --reload
________________________________________
API Endpoint
POST:

/generate
Example Input:

{
  "prompt": "Build a CRM with login and dashboard"
}
________________________________________
Evaluation
The project includes: - multiple prompts - runtime checks - latency tracking - validation handling
________________________________________
Design Decisions
Why Multi-Stage?
Instead of using one large prompt, the project separates the pipeline into multiple stages.
This improves: - modularity - debugging - reliability - consistency
________________________________________
Validation + Repair
The validator checks: - missing keys - invalid structure - missing endpoints - empty database tables
The repair engine automatically fixes missing sections.
________________________________________
Runtime Simulation
The runtime simulator checks whether the generated configuration is usable for execution.
This demonstrates execution awareness.
________________________________________
Future Improvements
•	real LLM integration
•	automatic frontend generation
•	advanced schema validation
•	database migration generation
•	authentication middleware generation ```
