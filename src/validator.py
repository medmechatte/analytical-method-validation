import numpy as np
from scipy import stats


class MethodValidator:
    """
    Analytical Method Validation following ICH Q2(R1) guidelines.
    """

    def __init__(self, concentrations, responses):
        """
        Parameters
        ----------
        concentrations : list — known concentrations (µg/mL)
        responses      : list — instrument responses (peak areas)
        """
        self.concentrations = np.array(concentrations)
        self.responses = np.array(responses)
        self.slope = None
        self.intercept = None
        self.r_squared = None

    def linearity(self):
        """
        Calculate calibration curve parameters.
        Returns slope, intercept, R²
        """
        self.slope, self.intercept, r, p, se = stats.linregress(
            self.concentrations, self.responses
        )
        self.r_squared = r ** 2

        print("=== LINEARITY ===")
        print(f"Slope     : {self.slope:.4f}")
        print(f"Intercept : {self.intercept:.4f}")
        print(f"R²        : {self.r_squared:.6f}")

        if self.r_squared >= 0.999:
            print("Status    : ✅ PASS (R² ≥ 0.999)")
        else:
            print("Status    : ❌ FAIL (R² < 0.999)")

        return self.slope, self.intercept, self.r_squared

    def lod_loq(self):
        """
        Calculate LOD and LOQ using regression method (ICH Q2R1).
        LOD = 3.3 * (std_residuals / slope)
        LOQ = 10  * (std_residuals / slope)
        """
        if self.slope is None:
            self.linearity()

        # Calculate residuals
        predicted = self.slope * self.concentrations + self.intercept
        residuals = self.responses - predicted
        std_residuals = np.std(residuals, ddof=2)

        lod = 3.3 * (std_residuals / self.slope)
        loq = 10.0 * (std_residuals / self.slope)

        print("\n=== LOD & LOQ ===")
        print(f"LOD : {lod:.4f} µg/mL")
        print(f"LOQ : {loq:.4f} µg/mL")

        return lod, loq