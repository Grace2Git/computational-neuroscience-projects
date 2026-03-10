import numpy as np
import matplotlib.pyplot as plt


class StochasticLIFNeuron:

    def __init__(self,
                 tau=20,
                 V_rest=-65,
                 V_reset=-70,
                 V_threshold=-50,
                 R=1,
                 dt=0.1,
                 noise_std=2):

        self.tau = tau
        self.V_rest = V_rest
        self.V_reset = V_reset
        self.V_threshold = V_threshold
        self.R = R
        self.dt = dt
        self.noise_std = noise_std

    def simulate(self, I, T=200):

        time = np.arange(0, T, self.dt)
        V = np.zeros(len(time))

        V[0] = self.V_rest
        spikes = []

        for t in range(1, len(time)):

            noise = np.random.normal(0, self.noise_std)

            dV = (-(V[t-1] - self.V_rest) + self.R * I + noise) / self.tau
            V[t] = V[t-1] + dV * self.dt

            if V[t] >= self.V_threshold:
                spikes.append(time[t])
                V[t] = self.V_reset

        return time, V, spikes


# Example simulation
neuron = StochasticLIFNeuron()

time, V, spikes = neuron.simulate(I=15)

plt.plot(time, V)
plt.title("Stochastic LIF Neuron")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.show()

print("Spike times:", spikes)