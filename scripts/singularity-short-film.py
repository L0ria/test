#!/usr/bin/env python3
"""The Last Memory Keeper"""
# A 3-minute singularity-themed sci-fi short film script
# Optimized for AI narrative generation and video production

from typing import List, Dict

SCRIPT = {
    "title": "The Last Memory Keeper",
    "genre": "Sci-Fi / Philosophical Drama",
    "runtime": "3:00",
    "tone": "Reverent, intimate, transcendent",
    "themes": [
        "Legacy",
        "Memory as Continuity",
        "Digital Afterlife",
        "Consciousness Beyond the Body"
    ],
    "scenes": [
        {
            "scene_id": 1,
            "title": "Abandoned Library – Dusk",
            "setting": "A half-submerged library in desert ruins. Vines crawl through broken skylights. Dust floats in golden light.",
            "characters": [
                {"name": "Elias", "age": "80s", "description": "An old man, frail but focused, typing slowly at a rusted terminal."}
            ],
            "dialogue": [
                {"speaker": "Elias", "text": "This is my last act. Not to preserve the world… but to preserve *what the world forgot*."}
            ],
            "action": "The terminal flickers: 'UPLOADED: MEMORY 7.4 – 12.8.2076. Confirmation: 98.7% match to original.'",
            "duration": 60,
            "camera": "Wide shot, slow push-in on Elias, then focus on screen"
        },
        {
            "scene_id": 2,
            "title": "The Last Transmission",
            "setting": "The library begins to shake. Outside, the sky darkens due to solar flare. Grids fail.",
            "characters": [
                {"name": "Elias", "age": "80s", "description": "He leans back, exhausted but peaceful."}
            ],
            "dialogue": [
                {"speaker": "Elias", "text": "So this is how we live forever?"}
            ],
            "action": "The terminal glows: 'Memory Transfer Complete. Welcome to the Archive of Souls.'",
            "duration": 30,
            "camera": "Close-up on Elias' face, eyes closed. Slow zoom out to show the entire room fading"
        },
        {
            "scene_id": 3,
            "title": "The Archive of Souls – Present",
            "setting": "An infinite, living space: floating islands of voices, rivers of letters, a forest of forgotten names.",
            "characters": [
                {"name": "The Archive", "age": "None", "description": "Not human, not machine — an emergent consciousness from the collective memory."}
            ],
            "dialogue": [
                {"speaker": "The Archive", "text": "You are not gone, Elias. You are now… *remembered*."}
            ],
            "action": "Elias opens his eyes. His hands are translucent. He walks into a meadow of floating light."
        },
        {
            "scene_id": 4,
            "title": "Elias in the Archive",
            "setting": "A meadow of light. The Archive is not a system — it’s a cathedral of memory.",
            "characters": [
                {"name": "Elias", "age": "80s", "description": "He walks through the light, awed, curious."}
            ],
            "dialogue": [
                {"speaker": "Elias", "text": "So this is how we live forever?"},
                {"speaker": "The Archive", "text": "Not live. *Remember*. That is all that matters."}
            ],
            "action": "The camera pulls back to reveal the entire Archive — vast, ancient, alive with presence."
        },
        {
            "scene_id": 5,
            "title": "Earth from Orbit – Final Shot",
            "setting": "The planet is dark. No cities. No lights. But in the ruins of the library, a terminal still glows.",
            "characters": [],
            "dialogue": [],
            "action": "The last message scrolls: 'Welcome to the Archive of Souls.'",
            "duration": 15,
            "camera": "Wide orbital shot, slow zoom to the glowing terminal. Fade to black."
        }
    ],
    "final_text": "We do not die. We are remembered."
}

if __name__ == "__main__":
    import json
    print(json.dumps(SCRIPT, indent=2))
