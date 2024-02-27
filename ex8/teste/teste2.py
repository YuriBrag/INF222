import matplotlib.pyplot as plt
amostraHomens=[44,41,62,52,41,34,42,52,51,35,30,39,35,47,31,47,37,57,39,53,45,36,62,43,60,46,40,36]
amostraMulheres=[28,63,32,26,31,29,38,54,24,25,60,43,35,34,34,41,36,32,41,33,39,34,26,25,33]

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

plt.boxplot([amostraHomens, amostraMulheres])
plt.title("Comparação amostral das idades dos atores e atrizes ganhadores de oscars")
plt.xticks([1, 2], ['Atores', 'Atrizes'])
plt.show()

