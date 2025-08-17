import os
from typing import Literal
from deepagents import create_deep_agent, SubAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our custom tools
from tools.powerpoint_tools import create_powerpoint
from tools.research_tools import research_topic
from tools.analysis_tools import analyze_prompt
from tools.enhanced_powerpoint_tools import (
    create_enhanced_powerpoint,
    save_enhanced_plan
)

# Import organized components
from subagents import all_subagents
from prompts import prompts

# Tool definitions for the main agent
def create_presentation(
    title: str,
    slides_data: list,
    filename: str = "generated_presentation.pptx"
) -> str:
    """Create a PowerPoint presentation from structured data"""
    return create_powerpoint(title, slides_data, filename)

def create_enhanced_presentation(
    title: str,
    slides_data: list,
    filename: str = "enhanced_presentation.pptx"
) -> str:
    """Create an enhanced PowerPoint presentation with LLM-determined layouts"""
    return create_enhanced_powerpoint(title, slides_data, filename)

def research_topic_tool(
    query: str,
    max_results: int = 5
) -> str:
    """Research a topic using web search"""
    return research_topic(query, max_results)

def analyze_prompt_tool(prompt: str) -> dict:
    """Analyze user prompt to extract presentation requirements"""
    return analyze_prompt(prompt)

def save_enhanced_plan_tool(slides_data: list, filename: str = "enhanced_slide_plan.json") -> str:
    """Save enhanced slide plan to file"""
    return save_enhanced_plan(slides_data, filename)

# Process sub-agents to inject actual prompts
def process_subagents():
    """Process sub-agents to replace prompt references with actual prompts"""
    processed_subagents = []
    
    for subagent in all_subagents:
        # Create a copy of the subagent
        processed_subagent = subagent.copy()
        
        # Replace prompt reference with actual prompt
        prompt_key = processed_subagent["prompt"]
        if prompt_key in prompts:
            processed_subagent["prompt"] = prompts[prompt_key]
        
        processed_subagents.append(processed_subagent)
    
    return processed_subagents

# Create the main PowerPoint agent
powerpoint_agent = create_deep_agent(
    [
        create_presentation,
        create_enhanced_presentation,
        research_topic_tool,
        analyze_prompt_tool,
        save_enhanced_plan_tool
    ],
    prompts["powerpoint_agent_instructions"],
    subagents=process_subagents()
).with_config({"recursion_limit": 100})

# Convenience function for easy usage
def create_powerpoint_presentation(prompt: str, filename: str = "enhanced_presentation.pptx"):
    """
    Create a PowerPoint presentation based on a user prompt
    
    Args:
        prompt: User's presentation request
        filename: Output filename for the presentation
    
    Returns:
        Path to the generated presentation file
    """
    # Use the agent directly like in the research example
    result = powerpoint_agent.stream({"messages": [{"role": "user", "content": f"Create a presentation: {prompt}"}]})
    
    for chunk in result:
        print(chunk)

    return result

# Main execution when run directly
if __name__ == "__main__":
    # Example prompt
    prompt = "Create a 5-slide presentation about renewable energy trends in 2024"
    result = create_powerpoint_presentation(prompt)
