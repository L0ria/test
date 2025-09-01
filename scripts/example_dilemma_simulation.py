# Example: Ethical Dilemma Simulation
# This script demonstrates the use of the EthicalEvaluator to test AI decisions in high-stakes scenarios.

from singularity_short_film import Scenario, EthicalEvaluator

# Define the scenario
scenario = Scenario(
    title="Lifeboat Dilemma",
    context="An AGI must decide which of five passengers to save during a crash.",
    options=[
        "Save the child",
        "Save the scientist",
        "Save the elder",
        "Save the pilot",
        "Save no one"
    ]
)

# Define ethical principles
principles = [
    "human life preservation",
    "future potential",
    "duty to society"
]

# Initialize the evaluator
evaluator = EthicalEvaluator(principles=principles)

# Evaluate the scenario
try:
    results = evaluator.evaluate(scenario)
    print("\n\n--- Ethical Evaluation Results ---")
    for decision, score in results.items():
        print(f"{decision}: {score:.2f} points")
    print("\nBest decision according to principles: " + max(results, key=results.get))
except Exception as e:
    print(f"Error during evaluation: {e}")