import unittest
from src.memetics.cybersemiotic import CybersemioticMeme, SemioticNetwork
from unittest.mock import patch
import uuid

class TestCybersemioticMeme(unittest.TestCase):

    def test_initialization_with_defaults(self):
        meme = CybersemioticMeme()
        self.assertIsNotNone(meme.id)
        self.assertEqual(meme.icon, "")
        self.assertEqual(meme.index, "")
        self.assertEqual(meme.symbol, "")
        self.assertEqual(meme.context, "default")
        self.assertEqual(meme.tags, [])
        self.assertEqual(meme.creator, "")

    def test_initialization_with_custom_values(self):
        meme = CybersemioticMeme(
            icon="AI_hands.png",
            index="Human-AI collaboration",
            symbol="Co-creation",
            context="scientific discourse",
            creator="Human-AI Research Collective",
            tags=["technology", "ethics"]
        )
        self.assertEqual(meme.icon, "AI_hands.png")
        self.assertEqual(meme.index, "Human-AI collaboration")
        self.assertEqual(meme.symbol, "Co-creation")
        self.assertEqual(meme.context, "scientific discourse")
        self.assertEqual(meme.creator, "Human-AI Research Collective")
        self.assertEqual(meme.tags, ["technology", "ethics"])

    def test_copy(self):
        original = CybersemioticMeme(
            icon="test.png",
            symbol="Test Meme",
            context="test context"
        )
        copied = original.copy()
        self.assertEqual(original.id, copied.id)
        self.assertEqual(original.icon, copied.icon)
        self.assertEqual(original.symbol, copied.symbol)
        self.assertEqual(original.context, copied.context)
        self.assertNotEqual(id(original), id(copied))

    def test_evolve(self):
        meme = CybersemioticMeme(
            symbol="Co-creation",
            context="scientific discourse"
        )
        evolved = meme.evolve("Symbiosis", "religious discourse")
        self.assertEqual(evolved.symbol, "Symbiosis")
        self.assertEqual(evolved.context, "religious discourse")
        self.assertIn("evolved_religious_discourse", evolved.tags)
        self.assertNotEqual(meme.id, evolved.id)

    def test_str_representation(self):
        meme = CybersemioticMeme(symbol="Test Meme", context="test")
        self.assertIn("Test Meme", str(meme))
        self.assertIn("test", str(meme))

    def test_evolve_with_empty_values(self):
        meme = CybersemioticMeme(symbol="Old")
        evolved = meme.evolve("", "")
        self.assertEqual(evolved.symbol, "")
        self.assertEqual(evolved.context, "")
        self.assertIn("evolved_", evolved.tags[0])

class TestSemioticNetwork(unittest.TestCase):

    def setUp(self):
        self.network = SemioticNetwork()

    def test_initialization(self):
        self.assertEqual(self.network.memes, {})
        self.assertEqual(self.network.relationships, {})

    def test_add_meme(self):
        meme = CybersemioticMeme(
            icon="test.png",
            symbol="Test Meme",
            context="test"
        )
        self.network.add_meme(meme)
        self.assertIn(meme.id, self.network.memes)
        self.assertEqual(self.network.memes[meme.id], meme)
        self.assertIn(meme.id, self.network.relationships)

    def test_add_relationship(self):
        meme_a = CybersemioticMeme(symbol="Meme A")
        meme_b = CybersemioticMeme(symbol="Meme B")
        self.network.add_meme(meme_a)
        self.network.add_meme(meme_b)

        self.network.add_relationship(meme_a.id, meme_b.id)
        self.assertIn(meme_b.id, self.network.relationships[meme_a.id])
        self.assertIn(meme_a.id, self.network.relationships[meme_b.id])

    def test_propagate_with_new_context(self):
        meme = CybersemioticMeme(
            symbol="Co-creation",
            context="scientific discourse"
        )
        self.network.add_meme(meme)
        self.network.add_relationship(meme.id, meme.id)  # Self-reference

        influenced = self.network.propagate(meme.id, "religious discourse", "Symbiosis")
        self.assertEqual(len(influenced), 0)
        self.assertEqual(len(self.network.memes), 2)
        self.assertIn(meme.id, self.network.memes)
        new_meme = [m for m in self.network.memes.values() if m.id != meme.id][0]
        self.assertEqual(new_meme.symbol, "Symbiosis")
        self.assertEqual(new_meme.context, "religious discourse")

    def test_propagate_nonexistent_meme(self):
        with self.assertRaises(ValueError):
            self.network.propagate("nonexistent", "new context", "new symbol")

    def test_get_contextual_meaning(self):
        meme1 = CybersemioticMeme(symbol="Meme 1", context="scientific")
        meme2 = CybersemioticMeme(symbol="Meme 2", context="religious")
        meme3 = CybersemioticMeme(symbol="Meme 3", context="scientific")

        self.network.add_meme(meme1)
        self.network.add_meme(meme2)
        self.network.add_meme(meme3)

        results = self.network.get_contextual_meaning("scientific")
        self.assertEqual(len(results), 2)
        self.assertIn(meme1, results)
        self.assertIn(meme3, results)
        self.assertNotIn(meme2, results)

    def test_get_meaning_shifts(self):
        meme = CybersemioticMeme(symbol="Co-creation", context="scientific")
        self.network.add_meme(meme)

        shifted = self.network.get_meaning_shifts(meme.id)
        self.assertEqual(len(shifted), 1)
        self.assertEqual(shifted["scientific"], "Co-creation")

    def test_get_meaning_shifts_with_multiple_contexts(self):
        meme = CybersemioticMeme(symbol="Co-creation", context="scientific")
        self.network.add_meme(meme)

        evolved = meme.evolve("Symbiosis", "religious")
        self.network.add_meme(evolved)

        shifted = self.network.get_meaning_shifts(meme.id)
        self.assertEqual(len(shifted), 2)
        self.assertIn("scientific", shifted)
        self.assertIn("religious", shifted)

class TestCybersemioticMemeEdgeCases(unittest.TestCase):

    def test_empty_meme(self):
        meme = CybersemioticMeme()
        self.assertEqual(meme.icon, "")
        self.assertEqual(meme.index, "")
        self.assertEqual(meme.symbol, "")
        self.assertEqual(meme.context, "default")

    def test_evolve_with_none_values(self):
        meme = CybersemioticMeme(symbol="Original")
        evolved = meme.evolve(None, None)
        self.assertIsNone(evolved.symbol)
        self.assertIsNone(evolved.context)

    def test_copy_with_empty_fields(self):
        meme = CybersemioticMeme()
        copied = meme.copy()
        self.assertEqual(meme.id, copied.id)
        self.assertEqual(meme.icon, copied.icon)
        self.assertEqual(meme.index, copied.index)
        self.assertEqual(meme.symbol, copied.symbol)
        self.assertEqual(meme.context, copied.context)
        self.assertEqual(meme.tags, copied.tags)

class TestSemioticNetworkEdgeCases(unittest.TestCase):

    def test_add_meme_with_existing_id(self):
        meme = CybersemioticMeme()
        self.network.add_meme(meme)
        self.network.add_meme(meme)  # Adding same meme twice
        self.assertEqual(len(self.network.memes), 1)  # Should not duplicate

    def test_add_relationship_with_nonexistent_meme(self):
        meme_a = CybersemioticMeme()
        meme_b = CybersemioticMeme()
        self.network.add_meme(meme_a)
        self.network.add_relationship(meme_a.id, meme_b.id)
        self.assertIn(meme_a.id, self.network.relationships)
        self.assertIn(meme_b.id, self.network.relationships)

    def test_get_contextual_meaning_with_empty_network(self):
        results = self.network.get_contextual_meaning("test")
        self.assertEqual(len(results), 0)

    def test_get_meaning_shifts_with_unknown_meme_id(self):
        result = self.network.get_meaning_shifts("nonexistent")
        self.assertEqual(result, {})

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCybersemioticMeme)
    suite.addTests(loader.loadTestsFromTestCase(TestSemioticNetwork))
    suite.addTests(loader.loadTestsFromTestCase(TestCybersemioticMemeEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestSemioticNetworkEdgeCases))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    if not success:
        exit(1)
