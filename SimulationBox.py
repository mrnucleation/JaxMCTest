



class SimBox:
    def __init__(self, nmax=500, ndimensions=3):
        self.coords = np.zeros(size=(nmax, ndimensions))
        self.nmax = nmax
        self.ndimensions = ndimensions

    def periodic(self, r, L):
        return r - L * np.round(r/L)



