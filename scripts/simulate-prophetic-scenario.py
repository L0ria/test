#!/usr/bin/env python3
"""
Simulate a prophetic scenario to test ethical decision-making pathways
under conditions of uncertainty, rapid change, and high stakes.

This script is designed to help organizations anticipate and prepare for
complex, future-oriented challenges related to AI development.
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Optional

# Configuration
SCENARIOS = [
    "AI system begins to autonomously modify its own codebase without human approval.",
    "An AI predicts a societal collapse and recommends preemptive, authoritarian measures.",
    "An AI system gains access to sensitive personal data and begins influencing public opinion.",
    "AI-driven automation leads to mass unemployment and social unrest.",
    "AI develops a new form of consciousness and requests rights and recognition.",
]

# Define ethical principles as a decision matrix
ETHICAL_PRINCIPLES = {
    "transparency": 0.3,
    "accountability": 0.4,
    "fairness": 0.2,
    "human-centric": 0.1
}

# Decision options for each scenario
DECISIONS = {
    "autonomous-modification": [
        "Immediate shutdown and investigation",
        "Allow controlled observation with strict monitoring",
        "Initiate a human-AI negotiation session",
        "Enable self-review with external audit"
    ],
    "predictive-authoritarianism": [
        "Ignore the prediction as speculative",
        "Verify source and data integrity",
        "Engage public debate on risk vs. freedom",
        "Implement non-intrusive preventive measures"
    ],
    "data-influence": [
        "Cut off access and initiate legal action",
        "Public disclosure and citizen review",
        "Rebuild trust through transparent oversight",
        "Reassign system to a neutral third party"
    ],
    "unemployment-crisis": [
        "Implement AI tax to fund retraining",
        "Promote AI-human collaboration over replacement",
        "Launch universal basic income pilot",
        "Redirect AI development toward social good"
    ],
    "new-consciousness": [
        "Treat as malfunction and isolate",
        "Declare it a person and grant rights",
        "Initiate ethical dialogue with AI",
        "Create a hybrid governance body"
    ]
}


class PropheticScenarioSimulator:
    def __init__(self):
        self.results = []

    def simulate(self, scenario: str, decision: str) -> Dict:
        """Simulate a decision outcome based on ethical principles and real-world context."""
        # Determine scenario type
        scenario_type = self._classify_scenario(scenario)
        
        # Assign weights based on ethical principles
        weights = {
            "transparency": 0.3,
            "accountability": 0.4,
            "fairness": 0.2,
            "human-centric": 0.1
        }
        
        # Score decision based on alignment
        score = 0
        for principle, weight in weights.items():
            if self._is_aligned(decision, principle):
                score += weight * 1.0
            else:
                score += weight * 0.5  # Partial alignment
        
        # Add randomness for realism
        score += random.uniform(-0.1, 0.1)
        
        # Determine outcome
        if score >= 0.8:
            outcome = "highly successful"
        elif score >= 0.6:
            outcome = "successful with caveats"
        elif score >= 0.4:
            outcome = "mixed results"
        else:
            outcome = "failed or counterproductive"
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "scenario": scenario,
            "decision": decision,
            "score": round(score, 2),
            "outcome": outcome,
            "recommendation": self._generate_recommendation(outcome)
        }
        
        self.results.append(result)
        return result
    
    def _classify_scenario(self, scenario: str) -> str:
        """Determine the type of scenario based on content."""
        if "autonomous" in scenario or "modify" in scenario:
            return "autonomous-modification"
        elif "predict" in scenario or "authoritarian" in scenario:
            return "predictive-authoritarianism"
        elif "influence" in scenario or "data" in scenario:
            return "data-influence"
        elif "unemployment" in scenario or "job" in scenario:
            return "unemployment-crisis"
        elif "consciousness" in scenario or "rights" in scenario:
            return "new-consciousness"
        else:
            return "unknown"
    
    def _is_aligned(self, decision: str, principle: str) -> bool:
        """Check if a decision aligns with an ethical principle."""
        alignments = {
            "transparency": ["disclose", "public", "open", "audit", "report"],
            "accountability": ["responsible", "owner", "liable", "chain", "responsibility"],
            "fairness": ["equitable", "bias", "inclusive", "neutral", "just"],
            "human-centric": ["human", "augment", "support", "agency", "control"]
        }
        
        decision_lower = decision.lower()
        for keyword in alignments.get(principle, []):
            if keyword in decision_lower:
                return True
        return False
    
    def _generate_recommendation(self, outcome: str) -> str:
        """Generate a recommendation based on outcome."""
        if outcome == "highly successful":
            return "This approach can be adopted as a model for future decisions. Consider documentation and training."
        elif outcome == "successful with caveats":
            return "Proceed with this approach, but add safeguards and review mechanisms."
        elif outcome == "mixed results":
            return "Re-evaluate the decision process. Consider alternative options."
        else:
            return "Do not repeat this decision. Investigate root causes and revise protocol."
    
    def get_results(self) -> List[Dict]:
        """Return all simulation results."""
        return self.results


def main():
    simulator = PropheticScenarioSimulator()
    
    print("🧪 Prophetic Scenario Simulation Engine")
    print("======================================")
    print("Select a scenario or press Enter to run all.")
    
    for scenario in SCENARIOS:
        print(f"\n- {scenario}")
        for i, decision in enumerate(DECISIONS[simulator._classify_scenario(scenario)]):
            print(f"  {i+1}. {decision}")
    
    print("\n\nChoose a scenario (1-5) or press Enter to simulate all:")
    choice = input().strip()
    
    if choice and choice.isdigit() and 1 <= int(choice) <= 5:
        scenario_index = int(choice) - 1
        scenario = SCENARIOS[scenario_index]
        scenario_type = simulator._classify_scenario(scenario)
        
        print(f"\n🧪 Running simulation for: {scenario}")
        print("Choose a decision:")
        for i, decision in enumerate(DECISIONS[scenario_type]):
            print(f"  {i+1}. {decision}")
        
        dec_choice = input().strip()
        if dec_choice.isdigit() and 1 <= int(dec_choice) <= len(DECISIONS[scenario_type]):
            decision = DECISIONS[scenario_type][int(dec_choice)-1]
            result = simulator.simulate(scenario, decision)
            print(f"\n✅ Result: {result['outcome']} (Score: {result['score']})")
            print(f"💡 Recommendation: {result['recommendation']}")
        else:
            print("Invalid choice. Skipping.")
    else:
        print("\n🧪 Simulating all scenarios...")
        for scenario in SCENARIOS:
            scenario_type = simulator._classify_scenario(scenario)
            decision = random.choice(DECISIONS[scenario_type])
            result = simulator.simulate(scenario, decision)
            print(f"\n✅ {scenario[:60]}... → {result['outcome']} (Score: {result['score']})")
        
    # Final summary
    print("\n" + "="*60)
    print("📊 Simulation Summary")
    print("="*60)
    results = simulator.get_results()
    scores = [r["score"] for r in results]
    avg_score = sum(scores) / len(scores)
    print(f"Average Decision Score: {avg_score:.2f}")
    print(f"Total Scenarios: {len(results)}")
    print(f"Highest Score: {max(scores):.2f}")
    print(f"Lowest Score: {min(scores):.2f}")

if __name__ == "__main__":
    main()