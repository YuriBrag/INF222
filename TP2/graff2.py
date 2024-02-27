import matplotlib.pyplot as plt
amostraMedicao1=[237.41,233.13,217.63,252.29,232.33,219.56,199.83,242.98,246.02,234.07,230.26,210.45,210.45,243.47,241.00]
amostraMedicao2= [11.72,51.02,44.78,38.98,22.03,23.98,18.73,10.95,40.93,17.42,59.52,68.41,15.35,53.47,43.16]

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

plt.xlabel('Medição', fontsize=15)
plt.ylabel('Velocidade em Mbps', fontsize=15)

plt.boxplot([amostraMedicao1, amostraMedicao2])
plt.xticks([1, 2], ['Sem Download do Software em Andamento', 'Com Download do Software em Andamento'])
plt.title("Medições Pelo M-Lab")
plt.show()
