import uuid
from typing import Dict, List, Set, Any

class CybersemioticMeme:
    """A meme with context, symbol, and evolutionary history."""

    def __init__(self, icon: str = "", index: str = "", symbol: str = "", context: str = "default", creator: str = "", tags: List[str] = None):
        self.id = str(uuid.uuid4())
        self.icon = icon
        self.index = index
        self.symbol = symbol
        self.context = context
        self.creator = creator
        self.tags = tags if tags is not None else []
        
    def copy(self):
        """Return a deep copy of this meme."""
        return CybersemioticMeme(
            icon=self.icon,
            index=self.index,
            symbol=self.symbol,
            context=self.context,
            creator=self.creator,
            tags=self.tags.copy()
        )
    
    def evolve(self, new_symbol: str = None, new_context: str = None):
        """Create a new meme that evolved from this one."""
        new_symbol = new_symbol or self.symbol
        new_context = new_context or self.context
        
        # Create a new meme with evolved properties
        evolved = CybersemioticMeme(
            icon=self.icon,
            index=self.index,
            symbol=new_symbol,
            context=new_context,
            creator=self.creator,
            tags=self.tags.copy()
        )
        
        # Add a tag indicating the evolution
        if new_context:
            evolved.tags.append(f"evolved_{new_context.replace(' ', '_')}")
        
        return evolved
    
    def __str__(self):
        return f"Meme(id={self.id}, symbol='{self.symbol}', context='{self.context}')"
class SemioticNetwork:
    """A network of memes and their relationships."""

    def __init__(self):
        self.memes: Dict[str, CybersemioticMeme] = {}
        self.relationships: Dict[str, Set[str]] = {}

    def add_meme(self, meme: CybersemioticMeme):
        """Add a meme to the network. If it already exists, do nothing."""
        if meme.id not in self.memes:
            self.memes[meme.id] = meme
            self.relationships[meme.id] = set()

    def add_relationship(self, meme_id_a: str, meme_id_b: str):
        """Add a bidirectional relationship between two memes."""
        if meme_id_a not in self.relationships:
            self.relationships[meme_id_a] = set()
        if meme_id_b not in self.relationships:
            self.relationships[meme_id_b] = set()
        
        self.relationships[meme_id_a].add(meme_id_b)
        self.relationships[meme_id_b].add(meme_id_a)

    def propagate(self, meme_id: str, new_context: str, new_symbol: str = None):
        """Create a new meme by evolving the given one and add it to the network. Returns the new meme."""
        if meme_id not in self.memes:
            raise ValueError(f"Meme with id '{meme_id}' not found in the network.")
        
        original_meme = self.memes[meme_id]
        new_symbol = new_symbol or original_meme.symbol
        new_meme = original_meme.evolve(new_symbol, new_context)
        
        # Add the new meme to the network
        self.add_meme(new_meme)
        
        # Create a relationship between the original and the new meme
        self.add_relationship(meme_id, new_meme.id)
        
        return new_meme
    
    def get_contextual_meaning(self, context: str) -> List[CybersemioticMeme]:
        """Return a list of memes with the specified context."""
        return [meme for meme in self.memes.values() if meme.context == context]
    
    def get_meaning_shifts(self, meme_id: str) -> Dict[str, str]:
        """Return a dictionary of all contexts and symbols this meme has had."""
        shifts = {}
        # This is a simple implementation. In a more complex system, you might track history.
        if meme_id in self.memes:
            shifts[self.memes[meme_id].context] = self.memes[meme_id].symbol
        return shifts
