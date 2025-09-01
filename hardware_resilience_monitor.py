import numpy as np
import random
from typing import Dict, Tuple

class SEPAnalyzer:
    """A lightweight implementation of the soft error probability (SEP) estimation framework 
    from arXiv:2508.12345, adapted for cloud-scale deployment.

    This class models the combined impact of process variation (PV) and aging on soft error probability.
    """

    def __init__(
        self,
        process_variation: float = 0.1,
        aging_factor: float = 1.0,
        threshold_voltage: float = 0.8,
        nominal_voltage: float = 1.0,
        base_error_rate: float = 1e-6
    ):
        """Initialize the SEP analyzer.

        Args:
            process_variation (float): Fractional variation in transistor threshold (e.g., 0.15 = 15%)
            aging_factor (float): Aging degradation multiplier (1.0 = no aging, >1.0 = degraded)
            threshold_voltage (float): Minimum voltage to prevent soft error
            nominal_voltage (float): Nominal operating voltage
            base_error_rate (float): Base soft error rate in pristine conditions
        """
        self.process_variation = process_variation
        self.aging_factor = aging_factor
        self.threshold_voltage = threshold_voltage
        self.nominal_voltage = nominal_voltage
        self.base_error_rate = base_error_rate

    def estimate_probability(self) -> float:
        """Estimate soft error probability under current conditions.

        Returns:
            float: Estimated soft error probability (0.0 to 1.0)
        """
        # Apply aging and process variation to effective voltage
        effective_voltage = self.nominal_voltage * (1.0 - self.process_variation) / self.aging_factor

        # Calculate soft error likelihood based on voltage margin
        voltage_margin = max(0.0, effective_voltage - self.threshold_voltage)
        voltage_ratio = voltage_margin / self.threshold_voltage

        # Nonlinear degradation model (inspired by paper's statistical approach)
        if voltage_ratio <= 0.1:
            return self.base_error_rate * (1.0 + 0.5 * self.aging_factor)
        elif voltage_ratio <= 0.5:
            return self.base_error_rate * (1.0 + 1.2 * self.aging_factor * voltage_ratio)
        else:
            return self.base_error_rate * (1.0 + 2.0 * self.aging_factor * np.log(1 + voltage_ratio))

    def get_diagnostics(self) -> Dict[str, float]:
        """Return diagnostic metrics for monitoring.

        Returns:
            Dict[str, float]: Key metrics for telemetry
        """
        return {
            "effective_voltage": self.nominal_voltage * (1.0 - self.process_variation) / self.aging_factor,
            "voltage_margin": max(0.0, self.nominal_voltage * (1.0 - self.process_variation) / self.aging_factor - self.threshold_voltage),
            "aging_factor": self.aging_factor,
            "process_variation": self.process_variation,
            "estimated_error_rate": self.estimate_probability()
        }

    def set_conditions(self, process_variation: float, aging_factor: float):
        """Update system conditions dynamically.

        Args:
            process_variation (float): Updated process variation
            aging_factor (float): Updated aging factor
        """
        self.process_variation = process_variation
        self.aging_factor = aging_factor


def main():
    # Example usage
    analyzer = SEPAnalyzer(process_variation=0.15, aging_factor=1.05)
    error_rate = analyzer.estimate_probability()
    print(f"Estimated soft error probability: {error_rate:.8f}")
    diagnostics = analyzer.get_diagnostics()
    for k, v in diagnostics.items():
        print(f"{k}: {v:.4f}")


if __name__ == "__main__":
    main()