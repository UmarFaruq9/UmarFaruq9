"""Simple AI automation workflow runner for vibecoding."""

from dataclasses import dataclass
from typing import Callable, Dict, Any, List


Context = Dict[str, Any]
StepFn = Callable[[Context], Any]


@dataclass
class Step:
    name: str
    run: StepFn


class Workflow:
    def __init__(self, name: str, steps: List[Step]):
        self.name = name
        self.steps = steps

    def execute(self, seed_context: Context | None = None) -> Context:
        context = dict(seed_context or {})
        context.setdefault("results", {})

        print(f"\n🚀 Running workflow: {self.name}")
        for i, step in enumerate(self.steps, start=1):
            print(f"[{i}/{len(self.steps)}] {step.name}...")
            output = step.run(context)
            context["results"][step.name] = output

        print("✅ Workflow complete")
        return context


# --- Example step functions ---

def capture_prompt(context: Context) -> str:
    prompt = context.get("prompt", "Build an AI automation side project")
    return prompt


def generate_plan(context: Context) -> Dict[str, Any]:
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
    milestones = context["results"]["Generate plan"]["milestones"]
    return [f"Task {idx + 1}: {item}" for idx, item in enumerate(milestones)]


def print_report(context: Context) -> str:
    results = context["results"]
    print("\n📋 Report")
    print("- Prompt:", results["Capture prompt"])
    print("- Plan:", results["Generate plan"])
    print("- Tasks:", results["Build tasks"])
    return "report_printed"


if __name__ == "__main__":
    workflow = Workflow(
        name="Vibecode Automation Flow",
        steps=[
            Step("Capture prompt", capture_prompt),
            Step("Generate plan", generate_plan),
            Step("Build tasks", build_tasks),
            Step("Print report", print_report),
        ],
    )

    workflow.execute(
        {
            "prompt": "I want to code about AI automation and workflow",
        }
    )
