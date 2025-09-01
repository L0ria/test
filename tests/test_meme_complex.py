import unittest
from meme_complex import Meme, MemeComplex


class TestMemeComplex(unittest.TestCase):

    def setUp(self):
        self.meme1 = Meme(id="m1", content="Evolution", fitness=1.2, spread_rate=1.0)
        self.meme2 = Meme(id="m2", content="Selection", fitness=1.5, spread_rate=0.8)
        self.meme3 = Meme(id="m3", content="Mutation", fitness=0.9, spread_rate=1.3)

        self.complex1 = MemeComplex("Complex1")
        self.complex2 = MemeComplex("Complex2")

        # Add memes
        self.complex1.add_meme(self.meme1)
        self.complex1.add_meme(self.meme2)
        self.complex2.add_meme(self.meme3)

    def test_add_meme(self):
        # Test adding new meme
        new_meme = Meme(id="m4", content="Adaptation", fitness=1.1)
        result = self.complex1.add_meme(new_meme)
        self.assertTrue(result)
        self.assertIn(new_meme, self.complex1.memes)

        # Test adding duplicate meme
        result = self.complex1.add_meme(new_meme)
        self.assertFalse(result)

    def test_merge(self):
        merged = self.complex1.merge(self.complex2)
        self.assertEqual(len(merged.memes), 3)
        self.assertIn(self.meme1, merged.memes)
        self.assertIn(self.meme2, merged.memes)
        self.assertIn(self.meme3, merged.memes)
        self.assertEqual(merged.generation, 1)

    def test_coevolution_strength(self):
        # Should be non-zero if more than one meme
        self.assertGreater(self.complex1.coevolution_strength(), 0.0)
        self.assertEqual(self.complex2.coevolution_strength(), 0.0)  # Single meme

    def test_evolve(self):
        self.complex1.evolve()
        self.assertEqual(self.complex1.generation, 1)
        self.assertEqual(len(self.complex1.memes), 2)  # Should still have 2 memes

    def test_report(self):
        report = self.complex1.report()
        self.assertIn("name", report)
        self.assertIn("memes_count", report)
        self.assertIn("coevolution_strength", report)
        self.assertIn("stability_score", report)
        self.assertIn("generation", report)
        self.assertIn("avg_fitness", report)

    def test_get_stability_score(self):
        self.complex1.evolve()
        self.complex1.evolve()
        score = self.complex1.get_stability_score()
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)


def suite():
    return unittest.TestSuite(
        [unittest.makeSuite(TestMemeComplex)]
    )

if __name__ == "__main__":
    unittest.main()