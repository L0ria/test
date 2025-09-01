from typing import Dict, List, Set, Tuple, Optional
import networkx as nx
import numpy as np
from dataclasses import dataclass

@dataclass
class Meme:
    """Represents a single meme with its attributes."""
    id: str
    content: str
    fitness: float = 1.0
    spread_rate: float = 1.0
    resistance: float = 0.5

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Meme) and self.id == other.id

class MemeComplex:
    """A collection of memes that have evolved into a mutually supportive or symbiotic relationship."

    def __init__(self, name: str):
        self.name = name
        self.memes: Set[Meme] = set()
        self.network = nx.DiGraph()
        self.fitness_history: List[float] = []
        self.generation = 0

    def add_meme(self, meme: Meme) -> bool:
        """Add a meme to the complex, updating the network structure."""
        if meme in self.memes:
            return False

        self.memes.add(meme)
        self.network.add_node(meme.id, content=meme.content, fitness=meme.fitness)
        self.fitness_history.append(meme.fitness)
        return True

    def merge(self, other: 'MemeComplex') -> 'MemeComplex':
        """Merge another meme complex into this one, preserving mutual support."""
        merged = MemeComplex(f"{self.name}_merged_{other.name}")
        merged.memes = self.memes | other.memes

        # Copy nodes and edges
        merged.network = nx.DiGraph()
        merged.network.add_nodes_from(self.network.nodes(data=True))
        merged.network.add_nodes_from(other.network.nodes(data=True))
        merged.network.add_edges_from(self.network.edges())
        merged.network.add_edges_from(other.network.edges())

        # Add inter-complex connections based on fitness correlation
        self_fitnesses = {n: d['fitness'] for n, d in self.network.nodes(data=True)}
        other_fitnesses = {n: d['fitness'] for n, d in other.network.nodes(data=True)}

        # Connect memes with similar fitness values
        for m1 in self.memes:
            for m2 in other.memes:
                corr = np.corrcoef(
                    [self_fitnesses[m1.id], other_fitnesses.get(m2.id, 0.5)],
                    [other_fitnesses.get(m2.id, 0.5), self_fitnesses[m1.id]]
                )[0][1]
                if corr > 0.6:  # Strong positive correlation
                    merged.network.add_edge(m1.id, m2.id, weight=corr)
                    merged.network.add_edge(m2.id, m1.id, weight=corr)

        merged.generation = max(self.generation, other.generation) + 1
        return merged

    def coevolution_strength(self) -> float:
        """Compute co-evolutionary interactivity strength using network centrality measures."
        if len(self.memes) < 2:
            return 0.0

        # Use harmonic centrality to measure interaction strength
        try:
            centrality = nx.harmonic_centrality(self.network)
            avg_centrality = np.mean(list(centrality.values()))
            return float(avg_centrality)
        except:
            return 0.0

    def evolve(self, mutation_rate: float = 0.1) -> None:
        """Simulate one generation of evolution with mutation and fitness adaptation."""
        new_meme_set = set()
        for meme in self.memes:
            # Mutate fitness and spread rate
            new_fitness = max(0.1, min(2.0, meme.fitness + np.random.normal(0, mutation_rate)))
            new_spread_rate = max(0.1, min(3.0, meme.spread_rate + np.random.normal(0, mutation_rate)))
            new_meme = Meme(
                id=f"{meme.id}_mutated_{self.generation}",
                content=meme.content,
                fitness=new_fitness,
                spread_rate=new_spread_rate,
                resistance=meme.resistance
            )
            new_meme_set.add(new_meme)

        # Update network with new memes
        self.memes = new_meme_set
        self.network.clear()
        self.network.add_nodes_from([(m.id, {'content': m.content, 'fitness': m.fitness}) for m in self.memes])
        self.generation += 1

    def get_stability_score(self) -> float:
        """Evaluate the stability of the meme-complex over time."""
        if len(self.fitness_history) < 2:
            return 1.0

        changes = np.diff(self.fitness_history)
        volatility = np.std(changes)
        return max(0.0, 1.0 - volatility / 1.0)  # Normalize against max expected volatility

    def report(self) -> Dict:
        """Generate a comprehensive report on the meme complex."""
        return {
            "name": self.name,
            "memes_count": len(self.memes),
            "coevolution_strength": self.coevolution_strength(),
            "stability_score": self.get_stability_score(),
            "generation": self.generation,
            "avg_fitness": np.mean([m.fitness for m in self.memes]) if self.memes else 0.0
        }