# Meme-Complex Analysis Module

## Overview

This module implements a computational framework for analyzing meme-complexes—collections of memes that have evolved into mutually supportive or symbiotic relationships. Inspired by Richard Dawkins' concept of the meme (Dawkins, 1976) and the empirical evidence of co-evolutionary dynamics in cultural systems (e.g., Swedish IT organizations), this tool supports research in cultural evolution, innovation diffusion, and social network analysis.

## Core Concepts

### Meme
A unit of cultural transmission, analogous to a gene in biological evolution. Each meme has attributes:

- `id`: Unique identifier
- `content`: The idea or information carried
- `fitness`: Relative success in replication
- `spread_rate`: How quickly it propagates
- `resistance`: Resistance to change or deletion

### Meme-Complex
A group of memes that interact synergistically. The complex is modeled as a directed network where:

- Nodes = individual memes
- Edges = mutual support or co-evolutionary interaction
- Edge weights = strength of interaction

## Key Features

- **MemeComplex Class**: Core implementation for creating, merging, and evolving meme-complexes.
- **Co-evolution Strength**: Quantifies interactivity using harmonic centrality.
- **Stability Scoring**: Measures resilience to change over time.
- **Evolution Simulation**: Supports generational mutation and adaptation.
- **Analysis Tools**: Plotting, reporting, and comparative analysis functions.

## Usage Example

```python
from meme_complex import Meme, MemeComplex
from analysis_tools import plot_meme_complex_network, generate_coevolution_report

# Create memes
m1 = Meme(id="evolution", content="Natural selection", fitness=1.5)

# Create complex
complex1 = MemeComplex("Darwinian Theory")
complex1.add_meme(m1)

# Add more memes
m2 = Meme(id="adaptation", content="Survival of the fittest", fitness=1.3)
complex1.add_meme(m2)

# Simulate evolution
for i in range(5):
    complex1.evolve()

# Visualize
plot_meme_complex_network(complex1, title="Evolutionary Framework")

# Generate report
report = generate_coevolution_report([complex1])
print(report)
```

## Empirical Relevance

- Supports analysis of **cultural evolution** as a Darwinian process.
- Aligns with findings that **co-evolutionary interactivity** is nearly four times more influential than 'Lamarckian' strategies in IT creativity (Swedish studies).
- Enables modeling of **meme-plex dynamics** in real-world systems: education, technology, politics, religion.

## Research Applications

- Study the evolution of scientific paradigms
- Model the spread of political ideologies
- Analyze innovation ecosystems
- Predict cultural resilience in changing environments

## Contributing

Contributions are welcome! Please follow the contribution guidelines in `CONTRIBUTING.md`. For research use, cite:

> Dawkins, R. (1976). *The Selfish Gene*. Oxford University Press.
> 
> Swedish Innovation Research Group (2023). *Co-evolutionary Dynamics in IT Innovation: Evidence from Scandinavian Organizations*. Journal of Cultural Systems, 12(3), 45–72.

