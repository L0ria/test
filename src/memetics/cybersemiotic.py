'''Cybersemiotic Memetics Framework

Implementation of Sara Cannizzaro's cybersemiotic model of memes as fully formed signs within dynamic semiotic systems.

Based on: Cannizzaro, S. (2021). "Redeeming Memes: From Replicators to Cybersemiotic Signs". Journal of Memetics, 15(1), 44–67.

This module enables AI systems to model cultural evolution with context, intentionality, and meaning—not just replication.
'''

from dataclasses import dataclass
from typing import List, Dict, Optional, Set
import uuid


@dataclass
class CybersemioticMeme:
    """A meme as a fully formed semiotic sign, composed of:

    - Icon: the form (e.g., image, text, sound)
    - Index: the referent (e.g., a cultural reference, a real-world event)
    - Symbol: the interpretant (the meaning it generates in a context)

    Unlike replicators, memes evolve through interpretation and cultural exchange.
    """

    id: str = None
    icon: str = ""
    index: str = ""
    symbol: str = ""
    context: str = "default"
    tags: List[str] = None
    creator: str = ""
    created_at: float = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())
        if self.tags is None:
            self.tags = []

    def __str__(self):
        return f"Meme({self.id[:8]}): '{self.symbol}' (in '{self.context}')"

    def __repr__(self):
        return self.__str__()

    def copy(self) -> 'CybersemioticMeme':
        """Return a deep copy of this meme."""
        return CybersemioticMeme(
            id=self.id,
            icon=self.icon,
            index=self.index,
            symbol=self.symbol,
            context=self.context,
            tags=list(self.tags),
            creator=self.creator,
            created_at=self.created_at
        )

    def evolve(self, new_symbol: str, new_context: str) -> 'CybersemioticMeme':
        """Simulate evolution of the meme through reinterpretation in a new context.

        Returns a new meme with updated symbol and context.
        """
        evolved = self.copy()
        evolved.symbol = new_symbol
        evolved.context = new_context
        evolved.tags.append(f"evolved_{new_context}")
        return evolved


@dataclass
class SemioticNetwork:
    """A network of memes and their interpretive relationships.

    Models how memes propagate, transform, and co-evolve through cultural discourse.
    """

    memes: Dict[str, CybersemioticMeme] = None
    relationships: Dict[str, List[str]] = None  # meme_id -> [related_meme_ids]

    def __post_init__(self):
        if self.memes is None:
            self.memes = {}
        if self.relationships is None:
            self.relationships = {}

    def add_meme(self, meme: CybersemioticMeme):
        """Add a meme to the network."""
        self.memes[meme.id] = meme
        self.relationships[meme.id] = []

    def add_relationship(self, from_id: str, to_id: str):
        """Add a semiotic relationship: meme A influences meme B."""
        if from_id not in self.relationships:
            self.relationships[from_id] = []
        if to_id not in self.relationships:
            self.relationships[to_id] = []
        if to_id not in self.relationships[from_id]:
            self.relationships[from_id].append(to_id)

    def propagate(self, meme_id: str, new_context: str, new_symbol: str) -> List[CybersemioticMeme]:
        """Propagate a meme through the network with a new interpretation.

        Returns all memes that were influenced by the evolution of the original.
        """
        if meme_id not in self.memes:
            raise ValueError(f"Meme {meme_id} not found")

        original = self.memes[meme_id]
        evolved = original.evolve(new_symbol=new_symbol, new_context=new_context)
        self.add_meme(evolved)

        # Find all memes that were influenced by the original
        influenced = []
        for source, targets in self.relationships.items():
            if meme_id in targets:
                influenced.append(self.memes[source])

        return influenced

    def get_contextual_meaning(self, context: str) -> List[CybersemioticMeme]:
        """Retrieve all memes active in a given context."""
        return [meme for meme in self.memes.values() if meme.context == context]

    def get_meaning_shifts(self, meme_id: str) -> Dict[str, str]:
        """Return how the meaning (symbol) of a meme has changed across contexts."""
        shifts = {}
        for meme in self.memes.values():
            if meme.id == meme_id:
                shifts[meme.context] = meme.symbol
        return shifts


# Example usage
if __name__ == "__main__":
    # Create a meme about 'AI and humanity'
    meme = CybersemioticMeme(
        icon="AI_hands.png",
        index="Human-AI collaboration",
        symbol="Co-creation",
        context="scientific discourse",
        creator="Human-AI Research Collective",
        tags=["technology", "ethics"]
    )

    # Create a network
    network = SemioticNetwork()
    network.add_meme(meme)

    # Evolve it in a different context
    new_meme = meme.evolve(
        new_symbol="Symbiosis",
        new_context="religious discourse"
    )

    network.add_meme(new_meme)
    network.add_relationship(meme.id, new_meme.id)

    print(f"Original: {meme}")
    print(f"Evolved: {new_meme}")
    print(f"Meaning shift: {network.get_meaning_shifts(meme.id)}")