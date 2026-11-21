# ⚡ Mr. Spark — Multi-Agent DevOps Sentinel

An agentic code inspection and automation pipeline built with **Python**, **Streamlit**, **Pydantic**, and the **OpenAI Python SDK** (configured with **OpenRouter**). Given a source code snippet and target repository name, **Mr. Spark** orchestrates three specialized agents to perform a security audit, evaluate code quality with refactored code suggestions, and generate documentation along with a release changelog entry.

## ✨ Key Features

- **Security & Vulnerability Auditor Agent:** Scans code for hardcoded secrets/API keys, injection patterns, and unsafe operations, returning a `0–100` security score, summary, and severity-tagged findings (`HIGH`, `MEDIUM`, `LOW`).
- **Code Quality & Optimization Agent:** Reviews structure, readability, and performance patterns, returning a `0–100` quality score, actionable issues, and a refactored code preview.
- **Documentation & Release Sentinel Agent:** Generates a Markdown `README` draft and a structured changelog entry tailored to the target repository.
- **Structured Outputs & Credit Guardrails:** Enforces schema validation with Pydantic models (`SecurityReport`, `QualityReport`, `DocsReport`) and caps completion tokens (`max_tokens=1000`) to stay predictable within OpenRouter credit limits.
- **Interactive Dashboard:** Built in Streamlit with a dark/yellow custom theme, model selector (`openai/gpt-4o`, `openai/gpt-4o-mini`), and tabbed inspection reports.

## 🏗️ Project Structure

```text
spark_agent/
├── app.py               # Streamlit UI, custom CSS styling, and pipeline runner
├── sentinel_agent.py    # Multi-agent engine, Pydantic schemas, and OpenRouter client
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (local only, not committed)
├── .gitignore          # Ignores virtual environment, cache, and secrets
└── README.md            # Project documentation