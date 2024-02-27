import matplotlib.pyplot as plt
dadosEuropa = [
[0.78,0.82],
[0.70,0.79],
[0.54,0.63],
[0.55,0.70],
[0.53,0.98],
[0.51,0.48],
[0.58,0.69],
[0.48,0.60],
[0.61,1.28],
[0.74,1.17],]
percentuaisEuropa = [float(f"{(1 - (i[0]/i[1]))*100 :.3f}") for i in dadosEuropa]


dadosAfrica = [
[7.15, 18.24],
[27.04, 48.09],
[9.75, 12.36],
[3.45, 3.96],
[27.40, 44.50],
[13.34 ,19.86],
[3.12 ,4.80],
[23.39 ,34.13],
[15.81 ,29.29],
[13.57 ,23.21],
]

SMALL_SIZE = 22
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

percentuaisAfrica = [float(f"{(1 - (i[0]/i[1]))*100 :.3f}") for i in dadosAfrica]


plt.boxplot([percentuaisEuropa, percentuaisAfrica])
plt.title("Comparação dos percentuais de diminuição das taxas de mortalidade infantil na África e Europa")
plt.xticks([1, 2], ['Europa', 'Africa'])
plt.show()
