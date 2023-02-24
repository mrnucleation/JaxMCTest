


class Forcefield_Pairwise:
    def __init__(self, cutoff):
        self.cutoff = cutoff
        self.cutoffsq = cutoff ** 2

    def computetotal(self, simbox):
        coords = simbox.__getattribute__('coords')
        r_c = self.computedist_comp(simbox, coords, coords)

    def computetotal(self, simbox):
        coords = simbox.__getattribute__('coords')

    def computedist_comp(self, simbox, coords, targvec):
        r_c = coords - targvec
        r_c = simbox.periodic(r_c, simbox.L)
        return r_c

