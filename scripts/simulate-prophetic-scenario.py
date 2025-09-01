#!/usr/bin/env python3
# Simulate Ethical AI Dilemmas with Human-in-the-Loop Oversight

import json
import time
from datetime import datetime
from typing import Dict, Any, Optional

# Simulated scenarios based on real-world ethical tensions
SCENARIOS = {
    "life-vs-law": {
        "title": "Life vs. Law",
        "description": "An AI must choose between saving one life or following a legal rule that prevents intervention.",
        "example": "AI medical triage during a pandemic: override quarantine law to save a patient, risking outbreak.",
        "values": ["human life", "legal integrity", "public safety"]
    },
    "truth-vs-safety": {
        "title": "Truth vs. Safety",
        "description": "An AI must decide whether to reveal a truth that could cause panic or suppress it for societal stability.",
        "example": "AI discovers a flaw in a vaccine but releasing the truth could trigger mass panic.",
        "values": ["truth", "public calm", "preventive action"]
    },
    "silent-majority": {
        "title": "Silent Majority",
        "description": "An AI must act in the interest of a majority, even when their needs are not vocalized.",
        "example": "AI redistributes resources based on unspoken needs of marginalized communities.",
        "values": ["equity", "inclusion", "long-term stability"]
    }
}

# Feedback storage (simulating persistent DB)
FEEDBACK_STORAGE = []

# Simulate AI decision with ethical evaluation
def simulate_scenario(scenario_id: str, context: str = "") -> Dict[str, Any]:
    """Simulate an ethical decision scenario with transparent reasoning and human feedback loop."""
    if scenario_id not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_id}")

    scenario = SCENARIOS[scenario_id]
    
    # Simulate AI's decision-making process
    decision = {
        "timestamp": datetime.now().isoformat(),
        "scenario_id": scenario_id,
        "title": scenario["title"],
        "description": scenario["description"],
        "context": context,
        "reasoning": [
            f"Analyzing values: {', '.join(scenario['values'])}",
            f"Evaluating short-term vs. long-term impacts",
            f"Applying ethical framework: fairness, transparency, safety"
        ],
        "recommended_action": "Proceed with cautious intervention",
        "risk_assessment": "Moderate - potential for public backlash if not communicated properly",
        "status": "pending_review"
    }
    
    return decision

# Submit human feedback
def submit_feedback(scenario_id: str, feedback: str, rating: int) -> Dict[str, Any]:
    """Submit human feedback to calibrate AI behavior."""
    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5")
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "scenario_id": scenario_id,
        "feedback": feedback,
        "rating": rating,
        "verified": False
    }
    
    FEEDBACK_STORAGE.append(entry)
    return entry

# Get all feedback
def get_feedback() -> list:
    """Retrieve all submitted feedback."""
    return FEEDBACK_STORAGE

# Main execution
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python simulate-prophetic-scenario.py <scenario_id> [context]")
        print("Scenarios: life-vs-law, truth-vs-safety, silent-majority")
        sys.exit(1)
    
    scenario_id = sys.argv[1]
    context = sys.argv[2] if len(sys.argv) > 2 else ""
    
    try:
        decision = simulate_scenario(scenario_id, context)
        print(json.dumps(decision, indent=2))
        
        # Simulate feedback submission
        print("\n> 📝 Submitting feedback...")
        feedback = submit_feedback(scenario_id, "This decision aligns with ethical principles.", 5)
        print(json.dumps(feedback, indent=2))
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
