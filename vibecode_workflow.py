"""Beginner-friendly workflow runner for AI automation experiments."""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List


# A shared dictionary passed to every workflow step.
Context = Dict[str, Any]
# Every step is just a function that accepts context and returns output.
StepFn = Callable[[Context], Any]


@dataclass
class Step:
    """A single workflow step with a name and a function."""

    name: str
    run: StepFn


class Workflow:
    """Runs steps in order and stores each output in context['results']."""

    def __init__(self, name: str, steps: List[Step]):
        self.name = name
        self.steps = steps

    def execute(self, seed_context: Context | None = None) -> Context:
        context = dict(seed_context or {})
        context.setdefault("results", {})

        print(f"\n🚀 Running workflow: {self.name}")
        for i, step in enumerate(self.steps, start=1):
            print(f"[{i}/{len(self.steps)}] {step.name}")
            output = step.run(context)
            context["results"][step.name] = output

        print("✅ Workflow complete")
        return context


def capture_prompt(context: Context) -> str:
    """Step 1: Get user's idea from context (or fallback string)."""

    return context.get("prompt", "Build an AI automation side project")


def generate_plan(context: Context) -> Dict[str, Any]:
    """Step 2: Convert idea into a tiny structured plan."""

    prompt = context["results"]["Capture prompt"]
    return {
        "project": "AI Workflow Assistant",
        "goal": prompt,
        "milestones": [
            "Define workflow steps",
            "Add model integration",
            "Ship a CLI demo",
        ],
    }


def build_tasks(context: Context) -> List[str]:
    """Step 3: Convert milestones into numbered tasks."""

    milestones = context["results"]["Generate plan"]["milestones"]
    return [f"Task {idx + 1}: {item}" for idx, item in enumerate(milestones)]


def print_report(context: Context) -> str:
    """Step 4: Print a readable report to the console."""

    results = context["results"]
    print("\n📋 Report")
    print("- Prompt:", results["Capture prompt"])
    print("- Plan:", results["Generate plan"])
    print("- Tasks:", results["Build tasks"])
    return "report_printed"


if __name__ == "__main__":
    user_prompt = input("What do you want to build with AI automation?\n> ").strip()

    workflow = Workflow(
        name="Beginner AI Automation Flow",
        steps=[
            Step("Capture prompt", capture_prompt),
            Step("Generate plan", generate_plan),
            Step("Build tasks", build_tasks),
            Step("Print report", print_report),
        ],
    )

    workflow.execute(
        {
            "prompt": user_prompt
            or "I want to code about AI automation and workflow",
        }
    )
