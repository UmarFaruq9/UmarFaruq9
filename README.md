# Vibecode: AI Automation Workflow Starter

This tiny starter project is for experimenting with AI automation ideas quickly.

## What it does

- Defines a simple workflow engine with named steps.
- Lets each step use an LLM-powered function (or any Python callable).
- Passes a shared context dictionary across all steps.
- Produces a final report with step outputs.

## Quick start

```bash
python3 vibecode_workflow.py
```

## Workflow ideas to try

1. **Idea to spec**: prompt -> technical spec -> task checklist.
2. **Code review bot**: summarize a diff -> detect risks -> suggest fixes.
3. **Content pipeline**: draft -> rewrite -> SEO tags -> publish JSON.
4. **Ops helper**: parse logs -> classify issues -> remediation plan.

## Next upgrades

- Add async execution for parallelizable steps.
- Persist run history to SQLite.
- Add retries/backoff and failure policies.
- Connect to real model APIs (OpenAI, etc.).
