import matplotlib.pyplot as plt
import numpy as np


def plot_calibration_curve(concentrations, responses, slope, intercept, r_squared):
    """
    Plot calibration curve with regression line.
    """
    concentrations = np.array(concentrations)
    responses = np.array(responses)

    # Ligne de régression
    x_line = np.linspace(min(concentrations), max(concentrations), 100)
    y_line = slope * x_line + intercept

    # Graphique
    plt.figure(figsize=(8, 6))
    plt.scatter(concentrations, responses, color='blue', zorder=5, label='Experimental points')
    plt.plot(x_line, y_line, color='red', label=f'y = {slope:.2f}x + {intercept:.2f}')

    plt.title('Calibration Curve', fontsize=14)
    plt.xlabel('Concentration (µg/mL)', fontsize=12)
    plt.ylabel('Response (Peak Area)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Afficher R²
    plt.text(0.05, 0.95, f'R² = {r_squared:.6f}',
             transform=plt.gca().transAxes,
             fontsize=12, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig('results/calibration_curve.png', dpi=300)
    plt.show()
    print("\n✅ Graphique sauvegardé dans results/calibration_curve.png")


def plot_recovery(theoretical, recovery):
    """
    Plot recovery rates at each concentration level.
    """
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(theoretical)+1), recovery, color='green', alpha=0.7)
    plt.axhline(y=98, color='red', linestyle='--', label='Lower limit (98%)')
    plt.axhline(y=102, color='red', linestyle='--', label='Upper limit (102%)')
    plt.axhline(y=100, color='blue', linestyle='-', alpha=0.3, label='100%')

    plt.title('Accuracy — Recovery Rate (%)', fontsize=14)
    plt.xlabel('Concentration Level', fontsize=12)
    plt.ylabel('Recovery (%)', fontsize=12)
    plt.ylim(95, 105)
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('results/recovery_plot.png', dpi=300)
    plt.show()
    print("✅ Graphique sauvegardé dans results/recovery_plot.png")