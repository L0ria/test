from localagi import Action


class TimeProvider(Action):
    """Custom Action for LocalAGI: Provides real-time system time to the LLM.

    This action retrieves the current system time and formats it as a human-readable string
    suitable for integration into LLM responses. It serves as a reliable time source
    for applications requiring accurate temporal context.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "time_provider"
        self.description = "Provides current system time in human-readable format"
        self.parameters = {}

    def run(self, **kwargs):
        """Retrieve and return the current system time.

        Returns:
            dict: A dictionary containing the current time in ISO 8601 format
                  and a human-readable string.
        """
        from datetime import datetime
        import pytz

        # Get current time in UTC
        utc_now = datetime.now(pytz.UTC)

        # Format for human readability
        readable_time = utc_now.strftime("%A, %B %d, %Y at %I:%M:%S %p UTC")

        # ISO 8601 format for machine readability
        iso_time = utc_now.isoformat()

        return {
            "current_time": {
                "iso_8601": iso_time,
                "readable": readable_time
            }
        }

    def schema(self):
        """Return the JSON schema for this action.

        Returns:
            dict: JSON schema defining the action's inputs and outputs.
        """
        return {
            "type": "object",
            "properties": {},
            "returns": {
                "type": "object",
                "properties": {
                    "current_time": {
                        "type": "object",
                        "properties": {
                            "iso_8601": {"type": "string", "description": "Time in ISO 8601 format"},
                            "readable": {"type": "string", "description": "Human-readable time string"}
                        }
                    }
                }
            }
        }

# Example usage
if __name__ == "__main__":
    action = TimeProvider()
    result = action.run()
    print(f"Current time: {result['current_time']['readable']}")
    print(f"ISO 8601 format: {result['current_time']['iso_8601']}")