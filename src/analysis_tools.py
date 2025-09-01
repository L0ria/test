import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import List, Dict
import networkx as nx
from meme_complex import MemeComplex

# Set style for plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


def plot_meme_complex_network(meme_complex: MemeComplex, title: str = "Meme Complex Network"):
    """Visualize the meme complex as a directed graph."""
    fig, ax = plt.subplots(figsize=(12, 8))

    pos = nx.spring_layout(meme_complex.network, k=2, iterations=50)

    # Draw nodes with fitness-based coloring
    node_colors = [d['fitness'] for n, d in meme_complex.network.nodes(data=True)]
    nodes = nx.draw_networkx_nodes(
        meme_complex.network,
        pos,
        node_color=node_colors,
        cmap="RdYlBu_r",
        node_size=800,
        alpha=0.8,
        ax=ax
    )

    # Draw edges with weight-based thickness
    edge_weights = [d['weight'] for u, v, d in meme_complex.network.edges(data=True)]
    edges = nx.draw_networkx_edges(
        meme_complex.network,
        pos,
        width=edge_weights,
        alpha=0.6,
        edge_color="gray",
        arrows=True,
        arrowsize=15,
        ax=ax
    )

    # Add labels
    nx.draw_networkx_labels(meme_complex.network, pos, font_size=8, font_weight="bold", ax=ax)

    # Colorbar
    plt.colorbar(nodes, label="Fitness")

    plt.title(title, fontsize=16, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def analyze_coevolution_strength(meme_complexes: List[MemeComplex]) -> Dict[str, float]:
    """Compute and compare co-evolutionary interaction strength across meme complexes."""
    results = {}
    for mc in meme_complexes:
        strength = mc.coevolution_strength()
        results[mc.name] = strength
    return results


def generate_coevolution_report(meme_complexes: List[MemeComplex]) -> pd.DataFrame:
    """Generate a structured report on multiple meme complexes."""
    data = []
    for mc in meme_complexes:
        report = mc.report()
        data.append(report)

    return pd.DataFrame(data).sort_values(by="coevolution_strength", ascending=False)


def plot_fitness_evolution(meme_complex: MemeComplex, title: str = "Meme Complex Fitness Over Generations"):
    """Plot the average fitness of the meme complex across generations."""
    fig, ax = plt.subplots(figsize=(10, 6))

    generations = list(range(len(meme_complex.fitness_history)))
    ax.plot(generations, meme_complex.fitness_history, marker='o', linestyle='-', color='b', label='Average Fitness')

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Average Fitness")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


def compare_stability_scores(meme_complexes: List[MemeComplex]) -> pd.DataFrame:
    """Compare stability scores across multiple meme complexes."""
    data = []
    for mc in meme_complexes:
        stability = mc.get_stability_score()
        data.append({"Name": mc.name, "Stability Score": stability})
    return pd.DataFrame(data).sort_values(by="Stability Score", ascending=False)