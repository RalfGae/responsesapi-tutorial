# Copilot Coding Agent Instructions for responsesapi-tutorial

## Project Overview
This repository is a series of Python lessons demonstrating AI-powered workflows using OpenAI APIs, Pydantic schemas, and external APIs. Each lesson is a standalone script focused on a specific capability (e.g., chat, image analysis, function calling, web access).

## Architecture & Patterns
- Each lesson (`lesson-*.py`) is a self-contained script. There is no shared package structure.
- Lessons use the OpenAI Python SDK, often with function calling (`tools` parameter) and Pydantic for input validation.
- External APIs (e.g., Open-Meteo for weather) are accessed via `requests`.
- Tool functions are defined in the same file as the lesson, registered in a `tools` list, and invoked based on model responses.
- The main workflow is: build input messages → call OpenAI API → handle function calls → append results to messages → repeat until a final message is received.

## Developer Workflow
- Setup: Run `bash setup.sh` to create a virtual environment and install dependencies from `requirements.txt`.
- Run lessons: Activate the venv (`source venv/bin/activate`) and run any lesson (`python lesson-8.py`).
- Add new dependencies: Update `requirements.txt` with `pip freeze > requirements.txt`.
- Environment variables (API keys) are stored in `.env` (never commit real secrets).

## Project-Specific Conventions
- Use Pydantic models for tool parameter schemas, with `extra="forbid"` for strict validation.
- Function calling tools are described as dicts in a `tools` list, with `"type": "function"`, `"name"`, `"description"`, `"parameters"`, and `"strict": True`.
- Lessons may include an `instructions` parameter to guide model behavior (e.g., "separate the tasks and do them one by one").
- Output handling: Print model responses and tool results to the console.
- **Auto-approval:** All tool/function calls are executed immediately when requested by the model. No manual confirmation is required.

## Integration Points
- OpenAI API: Used for chat, function calling, and structured output.
- External APIs: Used in lessons (e.g., weather data via Open-Meteo).
- Pydantic: Used for input validation in function calling.

## Key Files & Examples
- `lesson-8.py`: Shows advanced function calling with multiple tools and Pydantic schemas.
- `setup.sh`: Automates venv creation and dependency installation.
- `requirements.txt`: Lists all Python dependencies.
- `README.md`: Contains setup, workflow, and lesson overview.

## Example: Tool Registration and Use
```python
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the weather for a given latitude and longitude",
        "parameters": weather_schema,
        "strict": True
    }
]
response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools
)
```

## Notes
- Each lesson is independent; changes in one do not affect others.
- Follow the patterns in lesson-8.py for new function-calling workflows.
- Do not add project-wide structure unless explicitly requested.

---

If any section is unclear or missing important details, please specify so I can refine these instructions.
