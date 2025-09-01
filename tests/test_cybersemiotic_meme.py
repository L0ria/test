"""Unit tests for the CybersemioticMeme and SemioticNetwork classes.""

import unittest
from src.memetics.cybersemiotic import CybersemioticMeme, SemioticNetwork


class TestCybersemioticMeme(unittest.TestCase):
    
    def test_meme_creation(self):
        """Test that a meme is created with valid attributes."""
        meme = CybersemioticMeme(
            icon="cat.jpg",
            index="internet cat",
            symbol="funny animal",
            context="social media",
            creator="User123"
        )
        self.assertEqual(meme.icon, "cat.jpg")
        self.assertEqual(meme.index, "internet cat")
        self.assertEqual(meme.symbol, "funny animal")
        self.assertEqual(meme.context, "social media")
        self.assertEqual(meme.creator, "User123")
        self.assertTrue(meme.id.startswith(""))

    def test_meme_evolution(self):
        """Test that a meme can evolve with new symbol and context."""
        meme = CybersemioticMeme(
            icon="dog.jpg",
            index="loyal pet",
            symbol="companion",
            context="family home"
        )
        evolved = meme.evolve("guardian", "security system")
        
        self.assertNotEqual(evolved.id, meme.id)
        self.assertEqual(evolved.symbol, "guardian")
        self.assertEqual(evolved.context, "security system")
        self.assertIn("evolved_security system", evolved.tags)

    def test_meme_copy(self):
        """Test that copy() creates a deep copy."""
        meme = CybersemioticMeme(
            icon="image.png",
            index="symbolic meaning",
            symbol="transcendence",
            context="spiritual community",
            tags=["philosophy", "art"],
            creator="Visionary"
        )
        copy = meme.copy()
        
        self.assertEqual(copy.icon, meme.icon)
        self.assertEqual(copy.symbol, meme.symbol)
        self.assertEqual(copy.tags, meme.tags)
        self.assertNotEqual(copy.id, meme.id)


class TestSemioticNetwork(unittest.TestCase):
    
    def setUp(self):
        self.network = SemioticNetwork()
        self.meme1 = CybersemioticMeme(
            icon="AI.png",
            index="artificial intelligence",
            symbol="tool",
            context="engineering"
        )
        self.meme2 = CybersemioticMeme(
            icon="heart.png",
            index="empathy",
            symbol="care",
            context="mental health"
        )
        self.network.add_meme(self.meme1)
        self.network.add_meme(self.meme2)

    def test_add_meme(self):
        """Test that adding a meme updates the network."""
        self.assertIn(self.meme1.id, self.network.memes)
        self.assertIn(self.meme2.id, self.network.memes)

    def test_add_relationship(self):
        """Test that relationships are properly established."""
        self.network.add_relationship(self.meme1.id, self.meme2.id)
        self.assertIn(self.meme2.id, self.network.relationships[self.meme1.id])

    def test_propagate(self):
        """Test that propagation creates a new meme and returns influenced memes."""
        self.network.add_relationship(self.meme1.id, self.meme2.id)
        
        influenced = self.network.propagate(
            meme_id=self.meme1.id,
            new_context="philosophical discourse",
            new_symbol="partner in evolution"
        )
        
        # Should return meme2 (influenced by meme1)
        self.assertEqual(len(influenced), 1)
        self.assertEqual(influenced[0], self.meme2)
        
        # Check that new meme was created
        new_meme_id = None
        for mid in self.network.memes:
            if mid != self.meme1.id and mid != self.meme2.id:
                new_meme_id = mid
                break
        self.assertIsNotNone(new_meme_id)
        new_meme = self.network.memes[new_meme_id]
        self.assertEqual(new_meme.symbol, "partner in evolution")
        self.assertEqual(new_meme.context, "philosophical discourse")

    def test_get_contextual_meaning(self):
        """Test retrieval of memes by context."""
        memes = self.network.get_contextual_meaning("engineering")
        self.assertEqual(len(memes), 1)
        self.assertEqual(memes[0], self.meme1)

    def test_get_meaning_shifts(self):
        """Test that meaning shifts across contexts are tracked."""
        shifts = self.network.get_meaning_shifts(self.meme1.id)
        self.assertEqual(len(shifts), 1)
        self.assertIn("engineering", shifts)
        self.assertEqual(shifts["engineering"], "tool")


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCybersemioticMeme)

if __name__ == "__main__":
    unittest.main()