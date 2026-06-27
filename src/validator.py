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

    def accuracy(self, theoretical, measured):
        """
        Calculate recovery rate (%) at each concentration level.

        Parameters
        ----------
        theoretical : list — theoretical concentrations
        measured    : list — experimentally measured concentrations
        """
        theoretical = np.array(theoretical)
        measured = np.array(measured)

        recovery = (measured / theoretical) * 100
        mean_recovery = np.mean(recovery)

        print("\n=== ACCURACY (Recovery) ===")
        for i in range(len(theoretical)):
            status = "✅" if 98 <= recovery[i] <= 102 else "❌"
            print(f"Level {i + 1}: {recovery[i]:.2f}% {status}")

        print(f"Mean Recovery : {mean_recovery:.2f}%")

        if 98 <= mean_recovery <= 102:
            print("Status        : ✅ PASS (98–102%)")
        else:
            print("Status        : ❌ FAIL")

        return recovery, mean_recovery

    def precision(self, replicates):
        """
        Calculate repeatability (RSD%) from replicate measurements.

        Parameters
        ----------
        replicates : list — repeated measurements at same concentration
        """
        replicates = np.array(replicates)

        mean = np.mean(replicates)
        std = np.std(replicates, ddof=1)
        rsd = (std / mean) * 100

        print("\n=== PRECISION (Repeatability) ===")
        print(f"Mean : {mean:.4f}")
        print(f"SD   : {std:.4f}")
        print(f"RSD  : {rsd:.2f}%")

        if rsd <= 2.0:
            print("Status : ✅ PASS (RSD ≤ 2%)")
        else:
            print("Status : ❌ FAIL (RSD > 2%)")

        return mean, std, rsd