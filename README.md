# PowerPoint Generation Agent

An AI-powered system that automatically creates professional PowerPoint presentations from text prompts.

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up environment variables:**
Create a `.env` file in the project root with:
```
TAVILY_API_KEY=your_tavily_api_key_here
```

3. **Get a Tavily API key:**
- Sign up at [Tavily](https://tavily.com)
- Get your API key from the dashboard

## Quick Start

Run the main script with a prompt:

```bash
python powerpoint_agent.py
```

Or use it programmatically:

```python
from powerpoint_agent import create_powerpoint_presentation

# Create a presentation
result = create_powerpoint_presentation(
    prompt="Create a 5-slide presentation about renewable energy trends",
    filename="my_presentation.pptx"
)
```

## How It Works

The system uses multiple AI subagents:
- **Research Agent**: Gathers information on your topic
- **Content Writer**: Creates engaging presentation content
- **PowerPoint Designer**: Designs optimal layouts and visual elements
- **Reviewer**: Ensures quality and effectiveness

## Output

The system generates:
- `enhanced_presentation.pptx` - Your final presentation
- `enhanced_slide_plan.json` - Detailed slide plan
- `research_results.txt` - Research data (if applicable)

## Example Prompts

- "Create a 10-slide presentation about AI in healthcare"
- "Make a 5-slide deck on sustainable business practices"
- "Generate a presentation about digital transformation trends"

## Requirements

- Python 3.8+
- Internet connection (for research)
- Tavily API key
