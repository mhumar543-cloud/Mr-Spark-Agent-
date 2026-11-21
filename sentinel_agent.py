import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from typing import List

# Load environment variables
load_dotenv()

# OpenRouter configuration for OpenAI SDK
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# -------------------------------------------------------------------
# Pydantic Schemas for Structured Agent Responses
# -------------------------------------------------------------------
class SecurityVulnerability(BaseModel):
    severity: str  # HIGH, MEDIUM, LOW
    vulnerability_type: str
    description: str
    recommendation: str

class SecurityReport(BaseModel):
    security_score: int  # 0 to 100
    vulnerabilities: List[SecurityVulnerability]
    summary: str

class QualityIssue(BaseModel):
    issue_type: str
    line_or_section: str
    explanation: str
    suggested_fix: str

class QualityReport(BaseModel):
    code_quality_score: int  # 0 to 100
    issues: List[QualityIssue]
    refactored_code_snippet: str

class DocsReport(BaseModel):
    project_title: str
    readme_markdown: str
    changelog_entry: str


# -------------------------------------------------------------------
# Multi-Agent Sentinel Core Engine
# -------------------------------------------------------------------
class SparkSentinelEngine:
    def __init__(self, model: str = "openai/gpt-4o"):
        self.model = model

    def run_security_agent(self, code_content: str) -> SecurityReport:
        """Agent 1: Security & Vulnerability Auditor"""
        system_prompt = (
            "You are an Elite Security Audit Agent specialized in static code analysis. "
            "Scan the code for hardcoded API keys/secrets, SQL injections, insecure imports, "
            "and severe vulnerabilities. "
            "You MUST return a valid JSON object matching this exact structure: "
            "{"
            "\"security_score\": <int 0-100>,"
            "\"vulnerabilities\": [{\"severity\": \"HIGH/MEDIUM/LOW\", \"vulnerability_type\": \"<string>\", \"description\": \"<string>\", \"recommendation\": \"<string>\"}],"
            "\"summary\": \"<string>\""
            "}"
        )
        
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Audit this code for security vulnerabilities:\n\n{code_content}"}
            ],
            response_format={"type": "json_object"},
            max_tokens=1000
        )
        content = response.choices[0].message.content
        return SecurityReport.model_validate_json(content)

    def run_quality_agent(self, code_content: str) -> QualityReport:
        """Agent 2: Code Quality & Optimization Agent"""
        system_prompt = (
            "You are a Senior Principal Software Architect. Audit code for performance bottlenecks, "
            "anti-patterns, readability, and offer clean refactored code snippets. "
            "You MUST return a valid JSON object matching this exact structure: "
            "{"
            "\"code_quality_score\": <int 0-100>,"
            "\"issues\": [{\"issue_type\": \"<string>\", \"line_or_section\": \"<string>\", \"explanation\": \"<string>\", \"suggested_fix\": \"<string>\"}],"
            "\"refactored_code_snippet\": \"<string>\""
            "}"
        )
        
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Analyze code quality and suggest optimizations:\n\n{code_content}"}
            ],
            response_format={"type": "json_object"},
            max_tokens=1000
        )
        content = response.choices[0].message.content
        return QualityReport.model_validate_json(content)

    def run_docs_agent(self, code_content: str, repo_name: str = "Project Repo") -> DocsReport:
        """Agent 3: Documentation & Release Sentinel Agent"""
        system_prompt = (
            "You are a Technical Writer Agent. Generate high-quality Markdown README documentation "
            "including overview, usage instructions, and release change-logs for the given codebase. "
            "You MUST return a valid JSON object matching this exact structure: "
            "{"
            "\"project_title\": \"<string>\","
            "\"readme_markdown\": \"<string>\","
            "\"changelog_entry\": \"<string>\""
            "}"
        )
        
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate documentation and changelog for repository '{repo_name}':\n\n{code_content}"}
            ],
            response_format={"type": "json_object"},
            max_tokens=1000
        )
        content = response.choices[0].message.content
        return DocsReport.model_validate_json(content)