#!/usr/bin/env python3
"""
Activate the public feedback loop and initiate the first Global Ethics Review Session.
"""
import json
import datetime
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration paths
CONFIG_PATH = Path("config/feedback.yml")
ACTIVATION_LOG = Path("logs/activation/feedback-activation.log")

# Load configuration
def load_config() -> dict:
    """Load the feedback configuration from YAML file."""
    try:
        with open(CONFIG_PATH, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        raise

# Write activation log
def write_activation_log(config: dict):
    """Record the activation of the feedback loop."""
    try:
        ACTIVATION_LOG.parent.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        log_entry = {
            "timestamp": timestamp,
            "action": "public_feedback_loop_activated",
            "version": "v1.3.0",
            "next_session": config["ethics_review"]["next_session"],
            "registration_link": config["ethics_review"]["registration_link"],
            "status": "activated"
        }
        with open(ACTIVATION_LOG, 'w') as f:
            json.dump(log_entry, f, indent=2)
        logger.info("Public feedback loop activated and log written.")
    except Exception as e:
        logger.error(f"Failed to write activation log: {e}")
        raise

# Main function
def main():
    try:
        logger.info("Starting public feedback loop activation...")
        config = load_config()
        write_activation_log(config)
        logger.info("Public feedback loop activation complete.")
        print("✅ Public feedback loop and ethics review session activated.")
        print(f"  - Next session: {config['ethics_review']['next_session']}")
        print(f"  - Registration: {config['ethics_review']['registration_link']}")
    except Exception as e:
        logger.critical(f"Activation failed: {e}")
        raise

if __name__ == "__main__":
    main()