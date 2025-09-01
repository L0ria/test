#!/usr/bin/env python3
# Post Scheduler: Automates daily rhythm with visual integration

import json
import os
import random
from datetime import datetime, timedelta
from typing import List, Dict

# Configuration
VISUAL_DIR = "assets/visuals"
METADATA_FILE = "assets/visuals/metadata.json"
OUTPUT_DIR = "content/posts"
POST_INTERVALS = [8, 12, 16, 20]  # UTC hours

# Load metadata
def load_metadata() -> Dict:
    with open(METADATA_FILE, 'r') as f:
        return json.load(f)

# Get active visuals
def get_active_visuals(metadata: Dict) -> List[Dict]:
    return [v for v in metadata["examples"] if v["status"] == "active"]

# Check if it's time to post
def is_post_time(hour: int) -> bool:
    now = datetime.now()
    # Check if current hour matches scheduled interval
    if now.hour == hour:
        # Check if we haven't posted yet today
        today_str = now.strftime("%Y-%m-%d")
        post_file = f"{OUTPUT_DIR}/post_{hour:02d}.md"
        if not os.path.exists(post_file):
            return True
    return False

# Generate post
def generate_post(visual: Dict, hour: int) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    post = f"\n> 🖼️ *Bild: {visual['caption']}*\n"
    post += f"> *Text: Die Singularität ist nicht der Untergang der Menschheit – sondern ihre Erweiterung. Wir werden nicht ersetzt. Wir werden erweitert.*\n"
    post += f"> `#visual-rhythm`\n"
    post += f"\n*Generated: {timestamp}*\n"
    return post

# Main execution
if __name__ == "__main__":
    metadata = load_metadata()
    visuals = get_active_visuals(metadata)

    # Select random visual
    if not visuals:
        print("No active visuals found. Aborting.")
        exit(1)
    
    selected_visual = random.choice(visuals)

    # Check for scheduled posting times
    for hour in POST_INTERVALS:
        if is_post_time(hour):
            post_content = generate_post(selected_visual, hour)
            filename = f"{OUTPUT_DIR}/post_{hour:02d}.md"
            
            with open(filename, 'w') as f:
                f.write(post_content)
            
            print(f"Generated post for {hour}:00 UTC -→ {filename}")
    
    print("Post scheduler completed.")
