import matplotlib.pyplot as plt
amostraMedicao=[262.03, 270.44,264.24,264.45,260.86,265.11,257.08,264.51,262.22,265.90,265.46,274.76,271.28,267.27,260.67]
amostraMedUp = [137.67,137.63,137.64,137.54,137.59,137.51,137.44,137.13,137.43,142.61,152.61,144.19,140.13,140.72,136.48]

valContrato = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250]

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
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14", "M15"] ) 
plt.xlabel('Medição', fontsize=15)
plt.ylabel('Velocidade em Mbps', fontsize=15)

plt.plot(amostraMedicao)
plt.plot(amostraMedUp)
plt.plot(valContrato)
plt.title("Medições Pelo Ookla")
plt.show()
