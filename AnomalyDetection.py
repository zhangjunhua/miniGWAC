import math
import numpy as np
import analysistool
import Experiments
from matplotlib import pyplot as plt


class AnomalyDetection:
    def __init__(self):
        self.window_size = 400
        self.window_weight = np.linspace(0, 2 / self.window_size, self.window_size)
        self.stream_data = []
        self.anomaly = []
        self.threshold = 0.00000000001
        self.sum_square = 0
        self.avg = 0

    def detect(self, time, value) -> bool:
        '''
        detect为暴露出来的程序接口，每次有新的数据进来时，返回这个数据的异常值

        首先数据来了，需要保存所有的数据。计算数据的均值和方差

        构建窗口，窗口构建采用大小为delf.window_size的窗口，
        窗口内的概率密度曲线权重取直线权重：
        如size为100，则权重为sum(np.linspace(0,0.02,100))


        阈值，如何设定阈值？如0.01，是概率还是似然值？

        '''

        # calculate the anomaly score(likelihood)
        likelihood = 0
        if len(self.stream_data) >= self.window_size:
            # np.exp(-(x - u) ** 2 / (2 * sd ** 2)) / (math.sqrt(2 * math.pi) * sd)
            # 计算似然值
            for i in range(len(self.stream_data) - self.window_size, len(self.stream_data)):
                likelihood += math.exp(-(value - self.stream_data[i][1]) ** 2 / 2 / (self.variance ** 2)) / math.pow(
                    2 * math.pi * self.variance, 0.5) * self.window_weight[i + self.window_size - len(self.stream_data)]
        else:
            likelihood = 1
        # update the avg and variance
        self.stream_data.append([time, value])
        self.avg = self.avg * (len(self.stream_data) - 1) / len(self.stream_data) + self.stream_data[-1][1] / len(
            self.stream_data)
        self.sum_square += math.pow(self.stream_data[-1][1], 2)
        self.variance = self.sum_square / len(self.stream_data) - math.pow(self.avg, 2)

        if likelihood < self.threshold:
            return True
        else:
            return False

    def detect2(self, time, value) -> bool:
        '''
        2017年12月28日更新：
        基于detect（）方法，将检测到的异常点剔除
        '''

        # calculate the anomaly score(likelihood)
        likelihood = 0
        if len(self.stream_data) >= self.window_size:
            # np.exp(-(x - u) ** 2 / (2 * sd ** 2)) / (math.sqrt(2 * math.pi) * sd)
            # 计算极大似然值
            for i in range(len(self.stream_data) - self.window_size, len(self.stream_data)):
                if not self.anomaly[i]:
                    likelihood += math.exp(
                        -(value - self.stream_data[i][1]) ** 2 / 2 / (self.variance ** 2)) / math.pow(
                        2 * math.pi * self.variance, 0.5) * self.window_weight[
                                      i + self.window_size - len(self.stream_data)]
        else:
            likelihood = 1
        # update the avg and variance
        if likelihood>=self.threshold:
            self.stream_data.append([time, value])
            self.anomaly.append(True)
            self.avg = self.avg * (len(self.stream_data) - 1) / len(self.stream_data) + self.stream_data[-1][1] / len(
                self.stream_data)
            self.sum_square += math.pow(self.stream_data[-1][1], 2)
            self.variance = self.sum_square / len(self.stream_data) - math.pow(self.avg, 2)

        if likelihood < self.threshold:
            self.anomaly[-1] = True
            return True
        else:
            self.anomaly[-1] = False
            return False

    def __str__(self):
        return str(self.sum_square)

    def __mul__(self, other):
        print('mul')


if __name__ == '__main__':
    detector = AnomalyDetection()
    Experiments.tool.prepare_data(Experiments.file13_1678)
    x, y = Experiments.tool.show_diagram()
    anomaly = [False for row in x]
    for i, time, value in zip(range(len(x)), x, y):
        anomaly[i] = detector.detect2(time, value)
    print(anomaly)

    x_n = []
    y_n = []
    x_ab = []
    y_ab = []
    for i, an in enumerate(anomaly):
        if an:
            x_ab.append(x[i])
            y_ab.append(y[i])
        else:
            x_n.append(x[i])
            y_n.append(y[i])
    plt.title('file13_1678')
    plt.plot(x_ab, y_ab, 'ro')
    plt.plot(x_n, y_n, 'go')
    plt.show()
