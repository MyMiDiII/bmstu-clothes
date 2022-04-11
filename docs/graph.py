from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

x = [100, 300, 500, 700, 900, 1100, 1300, 1600, 3600, 6400]

y = [60, 50, 31, 22, 16, 13, 10, 8, 5, 3]

pp = PdfPages('test.pdf')

def function_plot(X,Y):
    plt.figure()
    plt.clf()

    plt.plot(X, Y, 'k', linewidth=2)
    plt.grid(True)
    plt.xlabel('Количество точечных масс')
    plt.ylabel('Количество кадров в секунду')
    pp.savefig()

function_plot(x, y)

pp.close()

