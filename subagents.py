"""
Sub-agents for the PowerPoint Generation Agent

This file contains all the sub-agent definitions used by the main PowerPoint agent.
"""

# Research Sub-Agent
research_sub_agent = {
    "name": "research-agent",
    "description": "Used to research topics thoroughly for presentation content. Provide this agent with specific research topics or questions.",
    "prompt": "research_sub_agent_prompt",  # Will be loaded from prompts.py
    "tools": ["research_topic_tool"]
}

# Content Writer Sub-Agent
content_writer_sub_agent = {
    "name": "content-writer-agent", 
    "description": "Used to create engaging presentation content based on research and requirements. Provide this agent with research results and slide requirements.",
    "prompt": "content_writer_sub_agent_prompt",  # Will be loaded from prompts.py
    "tools": []
}

# PowerPoint Designer Sub-Agent
powerpoint_designer_sub_agent = {
    "name": "powerpoint-designer-agent",
    "description": "AI-powered PowerPoint designer that analyzes content and determines optimal layouts and visual elements for each slide. Uses LLM intelligence to choose the best presentation design.",
    "prompt": "powerpoint_designer_sub_agent_prompt",  # Will be loaded from prompts.py
    "tools": ["save_enhanced_plan_tool"]
}

# Reviewer Sub-Agent
reviewer_sub_agent = {
    "name": "reviewer-agent",
    "description": "Used to review and critique presentations for quality and effectiveness. Provide this agent with the presentation plan and content.",
    "prompt": "reviewer_sub_agent_prompt",  # Will be loaded from prompts.py
    "tools": []
}

# List of all sub-agents
all_subagents = [
    research_sub_agent,
    content_writer_sub_agent,
    powerpoint_designer_sub_agent,
    reviewer_sub_agent
]
