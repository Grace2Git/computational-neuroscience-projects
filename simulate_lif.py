import matplotlib.pyplot as plt
from lif_model import LIFNeuron

# Create neuron
neuron = LIFNeuron()

# Input current
I = 15

# Run simulation
time, V, spikes = neuron.simulate(I)

# Plot membrane potential
plt.figure(figsize=(8,4))
plt.plot(time, V)
plt.title("LIF Neuron Simulation")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.show()

print("Spike times:", spikes)