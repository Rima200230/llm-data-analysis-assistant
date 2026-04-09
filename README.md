# llm-data-analysis-assistant
A lightweight agent-like system for analyzing structured telemetry data using natural language queries with LLMs and Python tools.

## Features
-Natural language interaction with structured CSV-based data
-LLM-based anamoly detection and data-grounded analysis
-Rule-based routing between analytical inference and visualization
-Data visualization using Python, pandas and matplotlib

## Tech Stack
-Python
-pandas
-matplotlib
-Gemini API

## Example Queries 
-" Is there any anomaly in the data?"
-" Plot battery temperature"
-" What is unusual in the data?"

## Project Structure
- ' main.py' (main application logic)
- 'data.csv' (example dataset that we are working on)
- 'requirements.txt' (dependencies)

## How it works
the system takes a natural language query and routes it:
-visualisation --> python tools (matplotlib)
-analysis --> LLM(Gemini API)

## Notes
This project demonstrates basic agent-like workflows, prompt engineering, and integration of LLMs with structured data analysis.
