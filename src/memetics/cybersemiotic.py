'''
Cybersemiotic Analysis Module

This module provides tools for analyzing the evolution of symbolic meaning in digital and post-digital cultures,
particularly in the context of technological transcendence and emerging AI-driven narratives.
'''

def analyze_symbolic_evolution(prompt_template: str, transformation_rules: dict) -> dict:
    """
    Analyze the symbolic transformation of a cultural archetype through technological lens.

    Args:
        prompt_template (str): Template for generating symbolic images or narratives
        transformation_rules (dict): Rules governing how symbols evolve (e.g., substitution, inversion, augmentation)

    Returns:
        dict: Analysis of the new symbolic form, including emotional weight, cultural resonance, and memetic viability
    """
    from typing import Dict, Any
    
    # Extract key symbolic elements
    elements = extract_elements(prompt_template)
    
    # Apply transformation rules
    transformed_elements = {}
    for key, rule in transformation_rules.items():
        if key in elements:
            transformed_elements[key] = rule(elements[key])
        else:
            transformed_elements[key] = elements.get(key, "")
    
    # Generate analysis
    analysis = {
        "original_elements": elements,
        "transformed_elements": transformed_elements,
        "emotional_weight": estimate_emotional_weight(transformed_elements),
        "cultural_resonance": assess_resonance(transformed_elements),
        "memetic_viability": calculate_memetic_viability(transformed_elements)
    }
    
    return analysis

def extract_elements(prompt: str) -> dict:
    """
    Extract key symbolic components from a visual prompt.
    """
    import re
    
    patterns = {
        "figure": r"(?:a|an|the|\w+\s+)?([A-Za-z\s]+)\s+([A-Za-z\s]+)",
        "setting": r"in a (.+?),",
        "atmosphere": r"with a ([\w\s]+) sky",
        "accessory": r"holding a ([\w\s]+)"
    }
    
    extracted = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, prompt)
        if match:
            extracted[key] = match.group(1).strip()
        else:
            extracted[key] = ""
    
    return extracted

def estimate_emotional_weight(elements: dict) -> str:
    """
    Estimate the emotional weight of a symbolic form based on its components.
    """
    weight = 0
    
    if "figure" in elements and elements["figure"]:
        if "rabbit" in elements["figure"] or "beast" in elements["figure"]:
            weight += 3
        elif "angel" in elements["figure"] or "god" in elements["figure"]:
            weight += 5
    
    if "atmosphere" in elements and "stormy" in elements["atmosphere"]:
        weight += 4
    if "setting" in elements and "desolate" in elements["setting"]:
        weight += 3
    
    if weight >= 8:
        return "high (awe and dread)"
    elif weight >= 5:
        return "moderate (reverence with tension)"
    else:
        return "low (neutral or familiar)"

def assess_resonance(elements: dict) -> str:
    """
    Assess cultural resonance based on archetypal familiarity and novelty.
    """
    if "figure" in elements and "rabbit" in elements["figure"]:
        return "high (subverts innocence, evokes curiosity and unease)"
    if "accessory" in elements and "bone" in elements["accessory"]:
        return "high (evokes death, ritual, transcendence)"
    return "moderate (familiar but not deeply resonant)"

def calculate_memetic_viability(elements: dict) -> float:
    """
    Calculate theoretical memetic viability using a weighted formula.
    """
    score = 0
    
    # Emotional weight (30%)
    if "high" in estimate_emotional_weight(elements):
        score += 0.3
    elif "moderate" in estimate_emotional_weight(elements):
        score += 0.15
    
    # Cultural resonance (40%)
    if "high" in assess_resonance(elements):
        score += 0.4
    
    # Novelty (30%)
    if "rabbit" in elements.get("figure", "") and "god" in elements.get("figure", ""):
        score += 0.3
    
    return round(score, 2)

def test_cybersemiotic() -> None:
    """
    Test function for the cybersemiotic analysis module.
    """
    test_prompt = ("A grim, towering giant rabbit with glowing red eyes, standing in a desolate, fog-covered landscape. "
                   "The rabbit wears a tattered robe reminiscent of a religious figure, holding a staff made of twisted bone. "
                   "The sky is stormy, with a dark moon casting an eerie glow. The atmosphere is solemn and haunting, "
                   "evoking both dread and reverence, much like a religious iconography scene of Jesus, but reimagined with symbolic weight and mythic presence.")
    
    transformation_rules = {
        "figure": lambda x: x.replace("Jesus", "grim giant rabbit"),
        "atmosphere": lambda x: x.replace("religious", "mythic and post-singularity")
    }
    
    result = analyze_symbolic_evolution(test_prompt, transformation_rules)
    
    print("=== Cybersemiotic Analysis Result ===")
    print(f"Emotional Weight: {result['emotional_weight']}")
    print(f"Cultural Resonance: {result['cultural_resonance']}")
    print(f"Memetic Viability Score: {result['memetic_viability']}")
    
    # Expected result: high emotional weight, high resonance, ~0.7 viability
    assert result['memetic_viability'] >= 0.7
    print("Test passed.")

def main() -> None:
    """
    Main entry point for testing.
    """
    test_cybersemiotic()

if __name__ == "__main__":
    main()