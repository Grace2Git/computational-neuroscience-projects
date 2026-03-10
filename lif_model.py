import numpy as np

class LIFNeuron:
    def __init__(self,
                 tau=20,
                 V_rest=-65,
                 V_reset=-70,
                 V_threshold=-50,
                 R=1,
                 dt=0.1,
                 refractory_period=5):

        self.tau = tau
        self.V_rest = V_rest
        self.V_reset = V_reset
        self.V_threshold = V_threshold
        self.R = R
        self.dt = dt
        self.refractory_period = refractory_period

    def simulate(self, I, T=200):

        time = np.arange(0, T, self.dt)
        V = np.zeros(len(time))

        V[0] = self.V_rest
        refractory_timer = 0

        spikes = []

        for t in range(1, len(time)):

            if refractory_timer > 0:
                V[t] = self.V_reset
                refractory_timer -= self.dt
                continue

            dV = (-(V[t-1] - self.V_rest) + self.R * I) / self.tau
            V[t] = V[t-1] + dV * self.dt

            if V[t] >= self.V_threshold:
                spikes.append(time[t])
                V[t] = self.V_reset
                refractory_timer = self.refractory_period

        return time, V, spikes