from src.validator import MethodValidator

# Données de calibration HPLC simulées (réalistes)
concentrations = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]  # µg/mL
responses      = [1523, 7614, 15230, 30180, 75640, 151200]  # Aires HPLC

# Créer l'objet validateur
validator = MethodValidator(concentrations, responses)

# Tester la linéarité
validator.linearity()

# Tester LOD et LOQ
validator.lod_loq()