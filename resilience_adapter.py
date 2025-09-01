from typing import Callable, Dict
import logging
from datetime import datetime

class ResilienceAdapter:
    """Adapts hardware-level soft error probabilities into cloud-level resilience actions.

    This component monitors SEP estimates and triggers appropriate responses based on thresholds.
    """

    def __init__(
        self,
        threshold: float = 0.01,
        alert_callback: Callable[[str, Dict], None] = None,
        auto_repair: bool = False
    ):
        """Initialize the resilience adapter.

        Args:
            threshold (float): Error probability threshold for triggering alerts
            alert_callback (Callable): Function to call when alert is triggered
            auto_repair (bool): Whether to enable automated recovery actions
        """
        self.threshold = threshold
        self.alert_callback = alert_callback or self._default_alert_handler
        self.auto_repair = auto_repair
        self.last_alert_time = None
        self.alert_count = 0

        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _default_alert_handler(self, message: str, details: Dict):
        """Default alert handler that logs the event.

        Args:
            message (str): Alert message
            details (Dict): Additional diagnostic info
        """
        self.logger.warning(f"[RESILIENCE ALERT] {message} | Details: {details}")

    def trigger_alert(self, error_probability: float, context: Dict = None):
        """Trigger an alert if error probability exceeds threshold.

        Args:
            error_probability (float): Current estimated error probability
            context (Dict): Additional context (e.g., system ID, location)
        """
        if error_probability > self.threshold:
            self.alert_count += 1
            self.last_alert_time = datetime.utcnow().isoformat()

            # Prepare alert message
            message = f"Soft error probability exceeded threshold: {error_probability:.6f} > {self.threshold}" 
            if context:
                message += f" | Context: {context}"

            # Call the callback
            self.alert_callback(message, {
                "error_probability": error_probability,
                "threshold": self.threshold,
                "alert_count": self.alert_count,
                "last_alert": self.last_alert_time,
                "context": context
            })

            # Optional: auto-repair
            if self.auto_repair:
                self._auto_repair()

    def _auto_repair(self):
        """Simulate an automated recovery action (e.g., reroute, restart).

        In real systems, this could trigger Kubernetes pod rescheduling, instance replacement, etc.
        """
        self.logger.info("[AUTO-REPAIR] Initiating recovery sequence...")
        # Placeholder for actual repair logic

    def reset_alert_counter(self):
        """Reset the alert counter.

        Useful for periodic maintenance or after recovery.
        """
        self.alert_count = 0


def main():
    # Example usage
    adapter = ResilienceAdapter(threshold=0.01, auto_repair=True)
    
    # Simulate monitoring
    for i in range(5):
        error_rate = 0.008 + 0.001 * i
        context = {"system_id": "prod-001", "region": "us-east-1"}
        adapter.trigger_alert(error_rate, context)


if __name__ == "__main__":
    main()