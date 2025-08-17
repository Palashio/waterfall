import os
import json
import re
from typing import Dict, List, Optional

def analyze_prompt(
    prompt: str
) -> Dict:
    """
    Analyze a user prompt to extract presentation requirements
    
    Args:
        prompt: User's presentation request
    
    Returns:
        Dictionary with extracted requirements
    """
    analysis = {
        "topic": "",
        "estimated_slides": 5,
        "slide_types": [],
        "target_audience": "general",
        "style": "professional",
        "key_requirements": [],
        "complexity": "medium"
    }
    
    # Extract topic (usually the main subject)
    topic_patterns = [
        r"about\s+(.+)",
        r"on\s+(.+)",
        r"regarding\s+(.+)",
        r"presentation\s+(?:about|on|regarding)\s+(.+)"
    ]
    
    for pattern in topic_patterns:
        match = re.search(pattern, prompt.lower())
        if match:
            analysis["topic"] = match.group(1).strip()
            break
    
    # Extract slide count
    slide_patterns = [
        r"(\d+)\s*slide",
        r"(\d+)\s*page",
        r"(\d+)\s*section"
    ]
    
    for pattern in slide_patterns:
        match = re.search(pattern, prompt.lower())
        if match:
            analysis["estimated_slides"] = int(match.group(1))
            break
    
    # Determine target audience
    audience_keywords = {
        "executive": ["executive", "management", "board", "ceo", "c-level"],
        "technical": ["technical", "developer", "engineer", "programmer", "technical team"],
        "academic": ["academic", "research", "study", "university", "college"],
        "general": ["general", "public", "audience", "stakeholder"]
    }
    
    for audience, keywords in audience_keywords.items():
        if any(keyword in prompt.lower() for keyword in keywords):
            analysis["target_audience"] = audience
            break
    
    # Determine style
    style_keywords = {
        "professional": ["professional", "business", "corporate", "formal"],
        "creative": ["creative", "design", "visual", "artistic"],
        "educational": ["educational", "teaching", "learning", "tutorial"],
        "casual": ["casual", "informal", "friendly", "relaxed"]
    }
    
    for style, keywords in style_keywords.items():
        if any(keyword in prompt.lower() for keyword in keywords):
            analysis["style"] = style
            break
    
    # Extract key requirements
    requirement_patterns = [
        r"include\s+(.+)",
        r"cover\s+(.+)",
        r"focus\s+on\s+(.+)",
        r"highlight\s+(.+)"
    ]
    
    for pattern in requirement_patterns:
        matches = re.findall(pattern, prompt.lower())
        analysis["key_requirements"].extend(matches)
    
    # Determine complexity
    complexity_indicators = {
        "simple": ["simple", "basic", "overview", "introduction"],
        "complex": ["detailed", "comprehensive", "in-depth", "advanced", "technical"],
        "medium": ["balanced", "moderate", "standard"]
    }
    
    for complexity, indicators in complexity_indicators.items():
        if any(indicator in prompt.lower() for indicator in indicators):
            analysis["complexity"] = complexity
            break
    
    return analysis

def generate_slide_structure(
    analysis: Dict
) -> List[Dict]:
    """
    Generate slide structure based on analysis
    
    Args:
        analysis: Prompt analysis results
    
    Returns:
        List of slide structures
    """
    slides = []
    
    # Title slide
    slides.append({
        "type": "title",
        "title": analysis["topic"].title() if analysis["topic"] else "Presentation Title",
        "content": f"Generated for {analysis['target_audience']} audience"
    })
    
    # Determine content slides based on complexity and slide count
    remaining_slides = analysis["estimated_slides"] - 1  # Subtract title slide
    
    if analysis["complexity"] == "simple":
        # Simple structure: overview, key points, summary
        if remaining_slides >= 3:
            slides.append({
                "type": "content",
                "title": "Overview",
                "content": "Key points about the topic"
            })
            slides.append({
                "type": "content", 
                "title": "Key Points",
                "content": "Main takeaways and important information"
            })
            slides.append({
                "type": "content",
                "title": "Summary",
                "content": "Recap and conclusion"
            })
    elif analysis["complexity"] == "complex":
        # Complex structure: introduction, background, details, analysis, conclusion
        if remaining_slides >= 5:
            slides.append({
                "type": "content",
                "title": "Introduction",
                "content": "Background and context"
            })
            slides.append({
                "type": "content",
                "title": "Background",
                "content": "Historical context and foundation"
            })
            slides.append({
                "type": "content",
                "title": "Detailed Analysis",
                "content": "In-depth examination of the topic"
            })
            slides.append({
                "type": "content",
                "title": "Key Findings",
                "content": "Important discoveries and insights"
            })
            slides.append({
                "type": "content",
                "title": "Conclusion",
                "content": "Summary and next steps"
            })
    else:
        # Medium complexity: balanced approach
        if remaining_slides >= 4:
            slides.append({
                "type": "content",
                "title": "Introduction",
                "content": "Overview and context"
            })
            slides.append({
                "type": "content",
                "title": "Main Content",
                "content": "Key information and details"
            })
            slides.append({
                "type": "content",
                "title": "Analysis",
                "content": "Insights and implications"
            })
            slides.append({
                "type": "content",
                "title": "Conclusion",
                "content": "Summary and takeaways"
            })
    
    return slides

def save_analysis(
    analysis: Dict,
    filename: str = "prompt_analysis.json"
) -> str:
    """
    Save prompt analysis to file
    
    Args:
        analysis: Analysis results
        filename: Output filename
    
    Returns:
        Path to saved file
    """
    filepath = os.path.join(os.getcwd(), filename)
    
    with open(filepath, 'w') as f:
        json.dump(analysis, f, indent=2)
    
    return filepath

def load_analysis(
    filename: str = "prompt_analysis.json"
) -> Dict:
    """
    Load prompt analysis from file
    
    Args:
        filename: Analysis filename
    
    Returns:
        Loaded analysis
    """
    filepath = os.path.join(os.getcwd(), filename)
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def validate_presentation_plan(
    slides: List[Dict]
) -> Dict:
    """
    Validate a presentation plan
    
    Args:
        slides: List of slide structures
    
    Returns:
        Validation results
    """
    validation = {
        "valid": True,
        "issues": [],
        "recommendations": []
    }
    
    if not slides:
        validation["valid"] = False
        validation["issues"].append("No slides defined")
        return validation
    
    # Check for title slide
    has_title = any(slide.get("type") == "title" for slide in slides)
    if not has_title:
        validation["recommendations"].append("Consider adding a title slide")
    
    # Check slide count
    if len(slides) < 2:
        validation["recommendations"].append("Consider adding more content slides")
    
    if len(slides) > 20:
        validation["recommendations"].append("Consider reducing slide count for better engagement")
    
    # Check for content slides
    content_slides = [slide for slide in slides if slide.get("type") == "content"]
    if len(content_slides) == 0:
        validation["issues"].append("No content slides found")
        validation["valid"] = False
    
    return validation
