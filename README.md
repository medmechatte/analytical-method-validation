# 🧪 Analytical Method Validation Toolkit

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Domain](https://img.shields.io/badge/Domain-Analytical%20Chemistry-orange.svg)
![Guidelines](https://img.shields.io/badge/Guidelines-ICH%20Q2(R1)-red.svg)

A Python toolkit for **analytical method validation** following
**ICH Q2(R1)** and **ISO** guidelines.
Designed for analytical chemists and researchers working with
HPLC, UV-Vis, and other quantitative analytical methods.

---

## 📋 Features

- ✅ **Linearity** — calibration curve, R², slope, intercept
- ✅ **LOD & LOQ** — signal-to-noise and regression methods
- ✅ **Accuracy** — recovery rate (%) at multiple concentration levels
- ✅ **Precision** — repeatability and intermediate precision
- ✅ **Automated plots** — publication-ready figures
- ✅ **PDF Report** — auto-generated validation report

---

## 🗂️ Project Structure

analytical-method-validation/
├── data/                  # Input data (CSV format)
├── notebooks/             # Jupyter notebooks with examples
├── src/
│   ├── validator.py       # Core validation functions
│   ├── plots.py           # Visualization functions
│   └── report.py          # PDF report generator
├── results/               # Generated figures and reports
├── tests/                 # Unit tests
├── requirements.txt       # Python dependencies
└── README.md

---

## 🚀 Quick Start

from src.validator import MethodValidator

validator = MethodValidator(
    concentrations=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
    responses=[1523, 7614, 15230, 30180, 75640, 151200]
)

results = validator.run_all()
print(results.summary())

---

## 📊 Example Output

| Parameter | Value | Acceptance Criteria | Status |
|-----------|-------|-------------------|--------|
| R²        | 0.9998 | ≥ 0.999          | ✅ Pass |
| LOD       | 0.03 µg/mL | —             | ✅      |
| LOQ       | 0.10 µg/mL | —             | ✅      |
| Recovery  | 99.8 % | 98–102 %         | ✅ Pass |
| RSD       | 0.8 %  | ≤ 2 %            | ✅ Pass |

---

## 🛠️ Installation

git clone https://github.com/medmechatte/analytical-method-validation.git
cd analytical-method-validation
pip install -r requirements.txt

---

## 📚 References

- ICH Q2(R1) — Validation of Analytical Procedures (2005)
- ISO 8466-1 — Calibration and evaluation of analytical methods

---

## 👨‍🔬 Author

**Mohamed Amine Mechatte**
PhD Researcher — Chemometrics & Analytical Chemistry
Sidi Mohamed Ben Abdellah University, Fez, Morocco