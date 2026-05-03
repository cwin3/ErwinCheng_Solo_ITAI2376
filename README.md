# ErwinCheng_Solo_ITAI2376

# 🚗 Smart Car Buying Assistant Agent

## Description
An AI agent that aggregates car listings, analyzes pricing, and recommends the best deals using reasoning and tool-based decision making.

## Project Type
Option A — Single AI Agent

## Problem
Buying a car requires searching across multiple platforms and comparing listings manually. This agent automates that process.

## Architecture
The agent:
1. Takes user input (budget, preferences)
2. Searches listings (Tool 1)
3. Analyzes pricing (Tool 2)
4. Uses reasoning (ReAct)
5. Returns ranked recommendations

## Tools Used
- LangChain
- OpenAI API
- Python

## Features
- Car listing aggregation (simulated)
- Price analysis scoring
- Memory of user preferences
- ReAct reasoning loop

## How to Run
```bash
pip install -r requirements.txt
python main.py
