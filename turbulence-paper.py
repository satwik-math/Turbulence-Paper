import matplotlib.pyplot as plt
import numpy as np
import csv

def read_data(file_name):
    with open(file_name, 'r') as dat_file:
        velo1, velo2, velo3 = [], [], []
        for row in csv.reader(dat_file):
            velo1.append(float(row[0]))
            velo2.append(float(row[1]))
            velo3.append(float(row[2]))
    return velo1, velo2, velo3

def calculate_residuals(a, b, c):
    residuals = np.array(a) - np.mean(a), np.array(b) - np.mean(b), np.array(c) - np.mean(c)
    return residuals

def calculate_quadrants(residuals):
    Q = list(map(lambda x, y: (x, y), residuals[0], residuals[2]))
    Qu1 = [i for i in Q if i[0] > 0 and i[1] > 0]
    Qu2 = [i for i in Q if i[0] < 0 and i[1] > 0]
    Qu3 = [i for i in Q if i[0] < 0 and i[1] < 0]
    Qu4 = [i for i in Q if i[0] > 0 and i[1] < 0]
    return Qu1, Qu2, Qu3, Qu4

def calculate_RSS(Quadrants):
    RSSQ = [i[1] * i[0] for i in Quadrants]
    return - sum(RSSQ)*(1/len(Quadrants))

def turb(I):
    velo1, velo2, velo3 = read_data("m" + str(I) + ".dat")
    residuals = calculate_residuals(velo1, velo2, velo3)
    Qu1, Qu2, Qu3, Qu4 = calculate_quadrants(residuals)
    RSS1 = calculate_RSS(Qu1)
    RSS2 = calculate_RSS(Qu2)
    RSS3 = calculate_RSS(Qu3)
    RSS4 = calculate_RSS(Qu4)
    RSS = calculate_RSS(list(zip(residuals[0], residuals[2])))
    return RSS1, RSS2, RSS3, RSS4, RSS

Range = list(range(100, 144))
L = [turb(k) for k in Range]

RSS1, RSS2, RSS3, RSS4, RSS = zip(*L)

Domain = np.linspace(0, 1, len(Range))

plt.plot(RSS1, Domain, 'o', color='black')
plt.plot(RSS2, Domain, 'o', color='blue')
plt.plot(RSS3, Domain, 'o', color='red')
plt.plot(RSS4, Domain, 'o', color='green')
plt.plot(RSS, Domain, '+', color='black')
plt.title("Reynolds Shear Stress")
plt.ylabel("Open Channel Height")
plt.show()
