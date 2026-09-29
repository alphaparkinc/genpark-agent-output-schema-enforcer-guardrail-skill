# genpark-agent-output-schema-enforcer-guardrail-skill

Agent Skill implementing **Structured JSON Output Repair & Schema Enforcement Guardrail** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Raw["Raw Model Output Stream"] --> MarkdownStrip["Markdown Fenced Code Block Stripper"]
    MarkdownStrip --> Parser{"Standard JSON Parse"}
    Parser -->|Success| CheckFields["Check Required Field Keys"]
    Parser -->|Truncated / Incomplete| Repair["Bracket Balance Auto-Healer"]
    Repair --> CheckFields
    CheckFields --> FillMissing["Null-Fill Missing Schema Keys"]
    FillMissing --> SafeJSON["Strict Validated JSON Object"]
```
