from nbformat import v4 as nbf
import nbformat

# Create a new Jupyter notebook
nb = nbf.new_notebook()

# Introduction cell
intro = nbf.new_markdown_cell("""
# Blood Pressure and Flow in the Human Vasculature

This exercise models blood pressure-related flow in arteries and veins using Poiseuille's law. You will explore pressure changes across different vascular segments and identify physiologically normal and abnormal thresholds.

## Objectives
- Understand pressure distribution across the vascular system
- Apply Poiseuille's law to model blood flow
- Identify physiological thresholds for blood pressure
- Answer descriptive questions based on plots and simulations
""")

# Poiseuille's Law cell
poiseuille_law = nbf.new_code_cell("""
import numpy as np
import matplotlib.pyplot as plt

# Poiseuille's Law: Q = (π * ΔP * r^4) / (8 * η * L)
def poiseuille_flow(delta_p, radius, viscosity, length):
    return (np.pi * delta_p * radius**4) / (8 * viscosity * length)

# Parameters
viscosity = 0.004  # Pa.s (typical blood viscosity)
length = 0.1       # m (segment length)
delta_p = 1333     # Pa (10 mmHg)
radii = np.linspace(0.001, 0.01, 100)  # Radii from 1mm to 10mm

# Calculate flow
flows = poiseuille_flow(delta_p, radii, viscosity, length)

# Plot
plt.figure(figsize=(8,5))
plt.plot(radii*1000, flows)
plt.xlabel('Radius (mm)')
plt.ylabel('Flow Rate (m^3/s)')
plt.title("Poiseuille's Law: Flow vs Vessel Radius")
plt.grid(True)
plt.show()
""")

# Pressure profile cell
pressure_profile = nbf.new_code_cell("""
import matplotlib.pyplot as plt

# Pressure values in mmHg across vascular segments
segments = ['Aorta', 'Arteries', 'Arterioles', 'Capillaries', 'Venules', 'Veins', 'Vena Cava']
pressures = [120, 95, 60, 30, 15, 10, 5]

plt.figure(figsize=(10,5))
plt.plot(segments, pressures, marker='o')
plt.ylabel('Pressure (mmHg)')
plt.title('Blood Pressure Across Vascular Segments')
plt.grid(True)
plt.show()
""")

# Abnormal pressure detection cell
abnormal_detection = nbf.new_code_cell("""
# Define physiological thresholds (min, max) for each segment
thresholds = {
    'Aorta': (90, 130),
    'Arteries': (70, 120),
    'Arterioles': (40, 80),
    'Capillaries': (20, 40),
    'Venules': (10, 20),
    'Veins': (5, 15),
    'Vena Cava': (2, 8)
}

# Detect abnormal pressures
abnormal_segments = []
for segment, pressure in zip(segments, pressures):
    min_thresh, max_thresh = thresholds[segment]
    if pressure < min_thresh or pressure > max_thresh:
        abnormal_segments.append((segment, pressure, min_thresh, max_thresh))

# Display abnormal segments
if abnormal_segments:
    print("Abnormal pressure detected in the following segments:")
    for seg, val, min_t, max_t in abnormal_segments:
        print(f"- {seg}: {val} mmHg (Normal range: {min_t}-{max_t} mmHg)")
else:
    print("All pressures are within physiological thresholds.")

# Plot with color indication
colors = ['red' if (seg, val, _, _) in abnormal_segments else 'green' for seg, val in zip(segments, pressures)]
plt.figure(figsize=(10,5))
plt.bar(segments, pressures, color=colors)
plt.ylabel('Pressure (mmHg)')
plt.title('Blood Pressure Across Vascular Segments with Abnormal Detection')
plt.grid(True)
plt.show()
""")

# Descriptive questions with answers
questions_answers = nbf.new_markdown_cell("""
## Questions and Answers

1. **What is the pressure drop from the aorta to the capillaries?**  
   The pressure drops from 120 mmHg in the aorta to 30 mmHg in the capillaries, resulting in a drop of **90 mmHg**.

2. **Which segment shows the greatest resistance to flow?**  
   Arterioles show the greatest resistance due to their small radius and muscular walls, which regulate blood flow.

3. **How does vessel radius affect flow rate according to Poiseuille's law?**  
   Flow rate is proportional to the **fourth power of the radius**. Small changes in radius lead to large changes in flow.

4. **At what pressure levels would you consider the values physiologically abnormal?**  
   Any pressure outside the defined thresholds for each segment (e.g., aorta < 90 or > 130 mmHg) is considered abnormal.

5. **How does the pressure in the vena cava compare to the aorta?**  
   The pressure in the vena cava (5 mmHg) is significantly lower than in the aorta (120 mmHg), reflecting the drop across the systemic circulation.
""")

# Assemble notebook
nb.cells = [
    intro,
    poiseuille_law,
    pressure_profile,
    abnormal_detection,
    questions_answers,
]

# Save notebook
with open("blood_pressure_exercise_with_answers.ipynb", "w") as f:
    nbformat.write(nb, f)

print("Notebook with embedded answers has been created successfully.")
