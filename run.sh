#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "Running beginner AI workflow demo..."
python3 vibecode_workflow.py
