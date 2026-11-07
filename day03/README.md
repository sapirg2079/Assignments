# Day 03 - Biological Computation: Growth Rate Analysis

## Overview
This program calculates the simple average growth rate ($\Delta OD / \Delta t$) of a microbial culture from optical density ($OD_{600}$) measurements recorded over time. 
love liori
The script reads experimental data from a CSV file, extracts the initial and final time points and OD values, and computes the overall rate of change.

## Files
- `data.csv`: CSV file containing time points (`time_hours`) and optical density measurements (`od600`).
- `growth_simple.py`: Python script containing the calculation function and terminal execution flow.
- `README.md`: Documentation and AI interaction log.

## Prompts Used in AI (VS Code Copilot)
1. *"Write a simple Python function using the built-in `csv` module that reads a file with `time_hours` and `od600` and calculates the average growth rate between the first and last measurements."*
2. *"Keep the code as simple and straightforward as possible so it is easy to understand."*

## How to Run
```bash
python growth_simple.py