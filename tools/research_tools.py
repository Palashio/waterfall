import os
from typing import List, Dict, Optional
from tavily import TavilyClient
import json
from dotenv import load_dotenv

# Load environment variables from .env file in project root
load_dotenv()

# Initialize Tavily client for web search
tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

def research_topic(
    query: str,
    max_results: int = 5,
    topic: str = "general",
    include_raw_content: bool = True
) -> str:
    """
    Research a topic using web search
    
    Args:
        query: Search query
        max_results: Maximum number of results
        topic: Search topic category
        include_raw_content: Whether to include raw content
    
    Returns:
        Research results as formatted string
    """
    try:
        search_results = tavily_client.search(
            query,
            max_results=max_results,
            include_raw_content=include_raw_content,
            topic=topic
        )
        
        # Format results
        formatted_results = f"Research Results for: {query}\n\n"
        
        for i, result in enumerate(search_results, 1):
            formatted_results += f"{i}. {result.get('title', 'No title')}\n"
            formatted_results += f"   URL: {result.get('url', 'No URL')}\n"
            formatted_results += f"   Content: {result.get('content', 'No content')[:200]}...\n\n"
        
        return formatted_results
        
    except Exception as e:
        return f"Research failed: {str(e)}"

def save_research_results(
    topic: str,
    results: str,
    filename: str = "research_results.txt"
) -> str:
    """
    Save research results to a file
    
    Args:
        topic: Research topic
        results: Research results
        filename: Output filename
    
    Returns:
        Path to saved file
    """
    filepath = os.path.join(os.getcwd(), filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Research Topic: {topic}\n")
        f.write("=" * 50 + "\n\n")
        f.write(results)
    
    return filepath

def load_research_results(
    filename: str = "research_results.txt"
) -> str:
    """
    Load research results from file
    
    Args:
        filename: Results filename
    
    Returns:
        Loaded research results
    """
    filepath = os.path.join(os.getcwd(), filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "No research results found."

def extract_key_points(
    research_text: str,
    max_points: int = 10
) -> List[str]:
    """
    Extract key points from research text
    
    Args:
        research_text: Research content
        max_points: Maximum number of key points
    
    Returns:
        List of key points
    """
    # This is a simplified version - in practice, this would use an LLM
    # to extract key points from the research
    
    lines = research_text.split('\n')
    key_points = []
    
    for line in lines:
        if line.strip() and len(key_points) < max_points:
            # Simple heuristic: lines that start with numbers or bullets
            if (line.strip().startswith(('•', '-', '*', '1.', '2.', '3.')) or
                any(word in line.lower() for word in ['important', 'key', 'main', 'primary'])):
                key_points.append(line.strip())
    
    return key_points[:max_points]

def save_key_points(
    key_points: List[str],
    filename: str = "key_points.json"
) -> str:
    """
    Save key points to a file
    
    Args:
        key_points: List of key points
        filename: Output filename
    
    Returns:
        Path to saved file
    """
    filepath = os.path.join(os.getcwd(), filename)
    
    with open(filepath, 'w') as f:
        json.dump(key_points, f, indent=2)
    
    return filepath
