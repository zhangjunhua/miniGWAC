import numpy as np
import random
import matplotlib.pyplot as plt


def exp1():
    '''http://blog.csdn.net/u010414589/article/details/49622625'''
    dta = [10930, 10318, 10595, 10972, 7706, 6756, 9092, 10551, 9722, 10913, 11151, 8186, 6422,
           6337, 11649, 11652, 10310, 12043, 7937, 6476, 9662, 9570, 9981, 9331, 9449, 6773, 6304, 9355,
           10477, 10148, 10395, 11261, 8713, 7299, 10424, 10795, 11069, 11602, 11427, 9095, 7707, 10767,
           12136, 12812, 12006, 12528, 10329, 7818, 11719, 11683, 12603, 11495, 13670, 11337, 10232,
           13261, 13230, 15535, 16837, 19598, 14823, 11622, 19391, 18177, 19994, 14723, 15694, 13248,
           9543, 12872, 13101, 15053, 12619, 13749, 10228, 9725, 14729, 12518, 14564, 15085, 14722,
           11999, 9390, 13481, 14795, 15845, 15271, 14686, 11054, 10395]
    plt.subplot('411')
    plt.title(u"original sequence")
    plt.plot(range(len(dta)), dta)

    # 一阶差分序列
    # ADF单位根平稳型检验, what's this?
    diff1 = []
    for i in range(len(dta) - 1):
        diff1.append(dta[i + 1] - dta[i])
    plt.subplot('412')
    plt.title(u'first order difference sequence')
    plt.plot(range(len(diff1)), diff1)

    # 自相关图acf
    autocorrs = []
    max_autocorr = 0
    diff1_avg = sum(diff1) / len(diff1)
    # print("diff1_avg:%f"%(diff1_avg))
    for k in range(40):
        sum_corr = 0
        diff1_avg1 = sum(diff1[:len(diff1) - k]) / (len(diff1) - k)
        diff1_avg2 = sum(diff1[k:len((diff1))]) / (len(diff1) - k)
        for i in range(len(diff1) - k):
            sum_corr += (diff1[i] - diff1_avg1) * (diff1[i + k] - diff1_avg2)
        autocorr = sum_corr / (len(diff1) - k)
        max_autocorr = max(max_autocorr, autocorr)
        autocorrs.append(autocorr / max_autocorr)
    # print(autocorrs)
    plt.subplot('413')
    plt.title(u'acf')
    plt.plot(range(len(autocorrs)), autocorrs)
    plt.grid(b='True')

    plt.show()


def randomwalk():
    size = 10000
    curve = []
    curve.append(0)
    # curve.append(0)
    for i in range(size):
        # curve.append(random.gauss(0,1))
        # curve.append(random.random()-0.5)
        curve.append(random.gauss(0, 1)+curve[i])
    plt.plot(range(len(curve)), curve)
    plt.show()


if __name__ == '__main__':
    # exp1()
    randomwalk()
