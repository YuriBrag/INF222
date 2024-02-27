import matplotlib.pyplot as plt

medicoesOoklaDownload = [262.03,270.44,264.24,264.45,260.86,265.11,257.08,264.51,262.22,265.90,265.46,274.76,271.28,267.27,260.67]

medicoesMlabDownload = [237.41,233.13,217.63,252.29,232.33,219.56,199.83,242.98,246.02,234.07,230.26,210.45,210.45,243.47,241.00]

medicoesESAQDownload = [239.64,226.17,254.97,231.58,244.51,240.92,258.36,256.54,246.07,234.38,231.99,222.12,221.61,239.75,241.53]

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
plt.ylabel('Velocidade De Download em Mbps', fontsize=15)

plt.boxplot([medicoesOoklaDownload, medicoesMlabDownload, medicoesESAQDownload])
plt.xticks([1, 2, 3], ['Ookla Download', 'Mlab Download', 'ESAQ Download'])
plt.title("Comparações Múltiplas")
plt.show()
