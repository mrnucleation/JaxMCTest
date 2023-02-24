# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
#import jax.numpy as np


def main():
    boxLow = 0.0
    boxHigh = 12.0
    natoms = 300
    testcoords = np.random.uniform(boxLow, boxHigh, size=(natoms, 3))
    print(np.linalg.norm(testcoords[0] - testcoords[1]))
    print(testcoords)
    disttest = np.linalg.norm(testcoords[:, None, :] - testcoords[None, :, :], axis=-1)
    print(disttest)
    ljeng = lj(disttest)
    etotal = 0.5*np.sum(ljeng)
    print(ljeng)
    beta = 0.5
    dxmax = 0.2
    for iloop in range(10000):
        nmove = np.random.randint(0, natoms)
        dr = np.random.uniform(-dxmax, dxmax, size=(3))
        rnew = testcoords[nmove] + dr
        if np.any(np.where(rnew > boxHigh)) or np.any(np.where(rnew < boxLow)):
            continue
        rold = testcoords[nmove]
        distnew_1 = np.linalg.norm(rnew - testcoords[:nmove], axis=-1)
        distold_1 = np.linalg.norm(rold - testcoords[:nmove], axis=-1)
        enew = np.sum(lj(distnew_1))
        eold = np.sum(lj(distold_1))
        if nmove < natoms-1:
            distnew_2 = np.linalg.norm(rnew - testcoords[nmove+1:], axis=-1)
            distold_2 = np.linalg.norm(rold - testcoords[nmove+1:], axis=-1)
            enew += np.sum(lj(distnew_2))
            eold += np.sum(lj(distold_2))
        ediff = enew - eold
        if -beta * ediff > np.log(np.random.uniform(0.0, 1.0)):
           testcoords[nmove] += dr
           etotal += enew - eold
        print("loop: ", iloop, "etotal: ", etotal)
    disttest = np.linalg.norm(testcoords[:, None, :] - testcoords[None, :, :], axis=-1)
    print(disttest)
    ljeng = lj(disttest)
    efinal = 0.5*np.sum(ljeng)
    print(etotal, efinal)







def lj(distmatrx):
    lj = np.nan_to_num(np.power(distmatrx, -6.0), nan=0.0, posinf=0.0, neginf=0.0)
    lj = 4 * lj * (lj - 1)
    return lj


if __name__ == "__main__":
    main()
