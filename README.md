# AI Automation Workflow (Beginner-Friendly)

Welcome 👋 — this project is a **very simple** way to learn how AI workflows are structured.

If you're new, don't worry. You only need to run one command to see it work.

## 1) What is this?

This project shows a tiny pipeline with 4 steps:

1. Capture your idea
2. Turn it into a project plan
3. Turn milestones into tasks
4. Print everything as a report

Think of it like a mini assembly line for ideas.

## 2) How to run it

From this folder, run:

```bash
python3 vibecode_workflow.py
```

You'll be asked to type your project idea.

## 3) What to edit first

Open `vibecode_workflow.py` and look at:

- `capture_prompt` → reads your idea
- `generate_plan` → creates a simple plan dictionary
- `build_tasks` → creates task strings
- `print_report` → prints results

## 4) Beginner exercises

Try these one by one:

- Change the default milestones in `generate_plan`
- Add a new step called `Estimate timeline`
- Save `context["results"]` to a JSON file

## 5) What this is NOT (yet)

This starter does **not** call real AI APIs yet.
It is a learning scaffold so you can understand flow first.
