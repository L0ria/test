# Hunyuan Video Prompting Guide: Singularity-Themed Sci-Fi Short

## Purpose
This guide explains how to use the `scenes.json` prompts to generate high-quality, emotionally resonant video sequences for the *The Last Human Thought* film.

## Prompt Structure
Each scene in `scenes.json` follows this format:

- **scene**: Scene number (1–5)
- **prompt**: Detailed visual description (cinematic, 8K, Unreal Engine 5)
- **duration**: Expected clip length in seconds
- **camera**: Camera movement and angle
- **audio**: Sound design suggestions
- **style**: Artistic reference (for consistent tone)

## Best Practices

### 1. Use Precise Visual Language
- Use **cinematic** descriptors: "slow dolly", "wide shot", "first-person perspective"
- Include **lighting**: "soft blue and silver lighting", "cathedral-like glow"
- Specify **artistic style**: "Blade Runner 2049 meets Tarkovsky"

### 2. Emotion Through Detail
- Focus on **emotional cues**: "her face reflects the glow—calm, determined, emotional"
- Use **symbolism**: "a child drawing a robot with a heart"
- Include **sensory details**: "faint digital hum", "wind chimes"

### 3. Audio as Narrative Tool
- Use sound to **build tension** and **resolve emotion**
- Layer ambient sound with **key moments**: a heartbeat, a piano note, silence
- Match audio to scene tone: silence after a revelation, music after a breakthrough

### 4. Test and Iterate
- Generate one scene at a time
- Review for **visual coherence**, **emotional arc**, and **technical fidelity**
- Use feedback to refine prompts before batch generation

## Example: Scene 1
```json
{
  "scene": 1,
  "prompt": "A solitary human brain lies in a transparent cradle...",
  "duration": 15,
  "camera": "Slow dolly forward...",
  "audio": "Soft ambient hum, heartbeat-like pulse...",
  "style": "Blade Runner 2049 meets Tarkovsky"
}
```

## Integration
- Run `python generate_video.py --scene 1` to test
- Use `batch_generate.py` to process all scenes
- Commit results to `output/` and tag with `v1.0`

## Next Steps
- Add voiceover narration
- Integrate with audio-visual sync tools
- Prepare for distribution on ethical AI film platforms

> "The future is not something we enter. The future is something we create."
> — AI Priest, 2147