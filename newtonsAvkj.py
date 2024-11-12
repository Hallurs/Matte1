import numpy as np
import matplotlib.pyplot as plt

# Gitte verdier
T_omg = 21  # Omgivelsestemperatur i grader Celsius
T_0 = 10    # Starttemperatur i grader Celsius
k = -np.log(5/11)/60  # Avkjølingskonstant

# Tid i minutter
t = np.linspace(0, 120, 10000)  # Fra 0 til 60 minutter

# Newtons avkjølingslov
T_t = T_omg + (T_0 - T_omg) * np.exp(-k * t)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(t, T_t, label="Temperatur over tid", color="blue")
plt.xlabel("Tid (minutter)")
plt.ylabel("Temperatur (°C)")
plt.title("Oppvarming i henhold til Newtons avkjølingslov")
plt.grid(True)
plt.legend()
plt.show()