'''
memetics.py: A computational framework for modeling cultural evolution through memes

This module implements a Darwinian-inspired model of meme propagation and evolution,
inspired by Richard Semon's *mnemisches* and the later development of the meme concept by Richard Dawkins.
It distinguishes between content, form, and *stance*—a key contribution from Shifman (2013).

Licensed under CC-BY 4.0: https://creativecommons.org/licenses/by/4.0/
'''

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Any
from enum import Enum
import random
import json
import csv
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MemeStance(Enum):
    """Enumeration of possible stances an addresser can take toward a meme."""
    SUPPORTIVE = "supportive"
    IRONIC = "ironic"
    SUBVERSIVE = "subversive"
    NEUTRAL = "neutral"
    PARODIC = "parodic"
    REINFORCING = "reinforcing"


@dataclass
class Meme:
    """A unit of cultural transmission, modeled after Dawkins' concept of a meme.

    Attributes:
        id (str): Unique identifier for the meme
        content (str): The textual or symbolic content
        mutation_rate (float): Probability of mutation per generation (0.0 to 1.0)
        initial_fitness (float): Base fitness score (0.0 to 1.0)
        stance (MemeStance): The stance taken by the addresser
        version (int): Version number of the meme (for tracking evolution)
        created_at (datetime): When the meme was first created
    """

    id: str
    content: str
    mutation_rate: float
    initial_fitness: float
    stance: MemeStance
    version: int = 1
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def mutate(self) -> 'Meme':
        """Apply a random mutation to the meme content.

        Returns:
            Meme: A new meme instance with mutated content.
        """
        if random.random() < self.mutation_rate:
            # Simple mutation: replace first word with a synonym
            words = self.content.split()
            if len(words) > 0:
                # Mock synonym replacement
                synonyms = {
                    "world": ["reality", "planet", "universe"],
                    "simulation": ["construct", "fabrication", "dream"],
                    "the": ["this", "that", "our"],
                    "is": ["are", "was", "seems"]
                }
                word = words[0]
                if word.lower() in synonyms:
                    new_word = random.choice(synonyms[word.lower()])
                    words[0] = new_word
                    new_content = " ".join(words)
                    logger.info(f"Meme {self.id} mutated: '{self.content}' -> '{new_content}'")
                    return Meme(
                        id=f"{self.id}-mutated-{random.randint(1000, 9999)}",
                        content=new_content,
                        mutation_rate=self.mutation_rate,
                        initial_fitness=self.initial_fitness,
                        stance=self.stance,
                        version=self.version + 1,
                        created_at=self.created_at
                    )
        return self  # No mutation

    def replicate(self) -> 'Meme':
        """Create a faithful copy of this meme (for propagation).

        Returns:
            Meme: A new meme with same attributes, except a new ID.
        """
        return Meme(
            id=f"{self.id}-copy-{random.randint(1000, 9999)}",
            content=self.content,
            mutation_rate=self.mutation_rate,
            initial_fitness=self.initial_fitness,
            stance=self.stance,
            version=self.version,
            created_at=self.created_at
        )

    def get_fitness(self, engagement: float = 1.0) -> float:
        """Calculate current fitness score based on initial fitness and external factors.

        Args:
            engagement (float): External engagement factor (e.g., likes, shares)

        Returns:
            float: Final fitness score (0.0 to 1.0)
        """
        base = self.initial_fitness
        # Apply stance multiplier
        stance_multiplier = {
            MemeStance.SUPPORTIVE: 1.3,
            MemeStance.IRONIC: 1.1,
            MemeStance.SUBVERSIVE: 1.2,
            MemeStance.PARODIC: 1.5,
            MemeStance.NEUTRAL: 0.9,
            MemeStance.REINFORCING: 1.0
        }.get(self.stance, 1.0)
        return min(1.0, base * stance_multiplier * engagement)

    def to_dict(self) -> Dict[str, Any]:
        """Convert meme to dictionary for serialization.

        Returns:
            Dict: Serialized representation
        """
        return {
            "id": self.id,
            "content": self.content,
            "mutation_rate": self.mutation_rate,
            "initial_fitness": self.initial_fitness,
            "stance": self.stance.value,
            "version": self.version,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Meme':
        """Reconstruct a Meme from dictionary.

        Args:
            data (Dict): Dictionary with meme data

        Returns:
            Meme: Reconstructed meme instance
        """
        return cls(
            id=data["id"],
            content=data["content"],
            mutation_rate=data["mutation_rate"],
            initial_fitness=data["initial_fitness"],
            stance=MemeStance(data["stance"]),
            version=data["version"],
            created_at=datetime.fromisoformat(data["created_at"])
        )


class MemePool:
    """A population of memes that evolve over generations.

    Manages replication, mutation, selection, and fitness tracking.
    """

    def __init__(self):
        self.memes: List[Meme] = []
        self.generation: int = 0

    def add_meme(self, meme: Meme) -> None:
        """Add a meme to the pool.

        Args:
            meme (Meme): The meme to add
        """
        self.memes.append(meme)
        logger.info(f"Added meme {meme.id} to pool")

    def evolve(self, selection_pressure: float = 0.5) -> None:
        """Simulate one generation of evolution.

        Args:
            selection_pressure (float): Proportion of memes to retain (0.0 to 1.0)
        """
        logger.info(f"Starting generation {self.generation + 1}")
        self.generation += 1

        # Sort by fitness (descending)
        ranked = sorted(self.memes, key=lambda m: m.get_fitness(), reverse=True)
        
        # Apply selection pressure
        keep_count = int(len(ranked) * selection_pressure)
        survivors = ranked[:keep_count]
        
        # Generate new offspring from survivors
        offspring = []
        for meme in survivors:
            for _ in range(2):  # Each meme produces 2 offspring
                replicated = meme.replicate()
                mutated = replicated.mutate()
                offspring.append(mutated)

        # Replace current pool
        self.memes = survivors + offspring
        logger.info(f"Generation {self.generation} complete: {len(self.memes)} memes")

    def get_top_meme(self) -> Optional[Meme]:
        """Return the most fit meme in the pool.

        Returns:
            Meme or None: The fittest meme, or None if pool is empty
        """
        if not self.memes:
            return None
        return max(self.memes, key=lambda m: m.get_fitness())

    def save_to_json(self, path: str) -> None:
        """Save current pool state to JSON.

        Args:
            path (str): File path to save
        """
        data = [meme.to_dict() for meme in self.memes]
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        logger.info(f"Pool saved to {path}")

    def load_from_json(self, path: str) -> None:
        """Load pool state from JSON.

        Args:
            path (str): File path to load from
        """
        with open(path, 'r') as f:
            data = json.load(f)
        self.memes = [Meme.from_dict(d) for d in data]
        logger.info(f"Pool loaded from {path}")

    def save_to_csv(self, path: str) -> None:
        """Save meme data to CSV.

        Args:
            path (str): File path to save
        """
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["id", "content", "mutation_rate", "initial_fitness", "stance", "version", "created_at"]
            )
            writer.writeheader()
            for meme in self.memes:
                writer.writerow(meme.to_dict())
        logger.info(f"Pool saved to {path}")


class StanceAnalyzer:
    """Tracks the stance an addresser takes toward a meme instance.

    This implements Shifman’s concept of *stance* as distinct from content or form.
    """

    def __init__(self):
        self.stance_history: Dict[str, List[str]] = {}  # meme_id -> list of stances

    def add_stance(self, meme_id: str, stance: MemeStance) -> None:
        """Record a stance taken toward a specific meme.

        Args:
            meme_id (str): ID of the meme
            stance (MemeStance): The stance taken
        """
        if meme_id not in self.stance_history:
            self.stance_history[meme_id] = []
        self.stance_history[meme_id].append(stance.value)
        logger.info(f"Recorded stance '{stance.value}' for meme {meme_id}")

    def get_stance_distribution(self, meme_id: str) -> Dict[str, int]:
        """Get frequency of stances for a given meme.

        Args:
            meme_id (str): ID of the meme

        Returns:
            Dict[str, int]: Count of each stance
        """
        if meme_id not in self.stance_history:
            return {}
        from collections import Counter
        return dict(Counter(self.stance_history[meme_id]))

    def get_overall_stance_trend(self) -> Dict[str, int]:
        """Get the overall distribution of stances across all memes.

        Returns:
            Dict[str, int]: Count of each stance across all memes
        """
        all_stances = []
        for meme_id in self.stance_history:
            all_stances.extend(self.stance_history[meme_id])
        from collections import Counter
        return dict(Counter(all_stances))

    def export_stance_log(self, path: str) -> None:
        """Export stance history to JSON.

        Args:
            path (str): File path to save
        """
        with open(path, 'w') as f:
            json.dump(self.stance_history, f, indent=2)
        logger.info(f"Stance log exported to {path}")


# Example usage
if __name__ == "__main__":
    # Create a meme with initial traits
    meme = Meme(
        id="meme_001",
        content="The world is a simulation",
        mutation_rate=0.1,
        initial_fitness=0.7,
        stance=MemeStance.IRONIC
    )

    # Simulate evolution in a pool
    pool = MemePool()
    pool.add_meme(meme)

    for generation in range(10):
        pool.evolve()
        print(f"Generation {generation}: {len(pool.memes)} memes")

    # Analyze stance distribution
    analyzer = StanceAnalyzer()
    analyzer.add_stance("meme_001", MemeStance.PARODIC)
    print(analyzer.get_stance_distribution("meme_001"))

    # Export logs
    pool.save_to_json("meme_pool.json")
    analyzer.export_stance_log("stance_log.json")
