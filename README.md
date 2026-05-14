# AI Automation Workflow (Beginner-Friendly)

Welcome 👋 This is a tiny learning project that shows how an AI workflow can run step-by-step.

## Exactly how to run this code

### 1) Open a terminal in this project folder
If you're already in this folder, confirm with:

```bash
pwd
```

You should see a path ending in `UmarFaruq9`.

### 2) Check Python is installed

```bash
python3 --version
```

If you see something like `Python 3.x.x`, you're good.

### 3) Run the program

```bash
python3 vibecode_workflow.py
```

### 4) Type your idea when prompted
Example input:

```text
I want to automate customer support triage
```

### 5) Read the output report
You will see:
- your prompt
- generated plan
- generated tasks

---

## What this project demonstrates

1. Capture an idea
2. Convert it into a simple plan
3. Convert plan milestones into tasks
4. Print a report

---

## If command fails

### Error: `python3: command not found`
Install Python 3, then rerun.

### Error: `can't open file 'vibecode_workflow.py'`
You are in the wrong folder. Run `pwd`, then `cd` into the project directory.

---

## Next beginner steps

- Edit milestone text in `generate_plan`
- Add another step function
- Save results to a JSON file
