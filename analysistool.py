# from mpl_toolkits.mplot3d.axes3d import Axes3D
# from matplotlib import cm
import numpy as np
import math
import matplotlib.pyplot as plt
import logging
import os

# configure Lgging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


class AnalysisTool:
    def __init__(self):
        self.data = []
        self.path = ''

    def prepare_data(self, path):
        self.path = path
        with open(path, 'r') as datafile:
            lines = datafile.readlines()
        self.data = []
        for i in range(0, len(lines)):
            words = lines[i].split()
            self.data.append([])
            for j in range(0, len(words)):
                self.data[i].append(float(words[j]))
        # check the validation of data

        ordered=True
        for i in range(len(self.data)-1):
            if(self.data[i][0]>self.data[i+1][0]):
                ordered=False

        if ordered:
            logging.info("data is well ordered")
        else:
            logging.error("data is not ordered by time.")


    def show_diagram(self):
        seconds_in_oneday = 60 * 24
        x = []
        y = []
        for i in range(0, len(self.data)):
            x.append(self.data[i][0])
            y.append(self.data[i][1])
        for i in range(1, len(x)):
            x[i] = (x[i] - x[0]) * seconds_in_oneday
        if len(x) <= 0:
            return [], []
        x[0] = 0
        return x, y

    def store_img(self, x, y, dst_folder: str):
        plt.close()
        plt.plot(x, y, 'o')
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
        filename = str(os.path.split(self.path)[1].split('.')[0]) + '.png'
        path = os.path.join(dst_folder, os.path.split(os.path.split(self.path)[0])[1])
        savepath = os.path.join(path, filename)
        logging.info("save img to " + savepath)
        if not os.path.exists(path):
            os.makedirs(path)
        fig.savefig(savepath, dpi=100)

    @staticmethod
    def list_dir(folder):
        ana = AnalysisTool()
        for path, dirs, files in os.walk(folder):
            print("path:" + os.path.split(path)[-1])
            print("dirs:" + str(dirs))
            print("files:" + str(files))
            print()
            for file in files:
                ana.prepare_data(os.path.join(path, file))
                ana.show_diagram()

    @staticmethod
    def norm_dist(u, variance, x):
        sd = math.sqrt(variance)  # 标准差δ
        y = np.exp(-(x - u) ** 2 / (2 * sd ** 2)) / (math.sqrt(2 * math.pi) * sd)
        return y

    @staticmethod
    def uniform_dist(u, d, x):
        y=np.linspace(0,0,len(x))
        for i in range(len(x)):
            if(abs(u-x[i])<(d/2)):
                y[i]=1/d
            else:
                y[i]=0
        return y

    def estimate_probability_densecurve_norm(self, start=0, end=10, size=100):
        '''
        正太分布来进行概率密度曲线估计
        '''
        data = self.data
        # computing avg
        sum_value = 0
        for i in range(0, len(data)):
            sum_value += data[i][1]
        avg = sum_value / len(data)

        # computing standard deviation
        variance = 0
        for i in range(0, len(data)):
            variance += (data[i][1] - avg) ** 2 / len(data)

        # Generate Dense Curve
        x = np.linspace(start, end, size)
        y = np.linspace(0, 0, size)
        for i in range(0, len(data)):
            y += self.norm_dist(data[i][1], variance, x)
        y = y / len(data)
        return x, y

    def estimate_probability_densecurve_rectangle(self, start=0, end=10, size=100):
        '''
        方窗进行概率密度曲线估计
        '''
        data = self.data
        # params
        d=0.03
        # Generate Dense Curve
        x = np.linspace(start, end, size)
        y = np.linspace(0, 0, size)
        for i in range(0, len(data)):
            y += self.uniform_dist(data[i][1], d, x)
        y = y / len(data)
        return x, y

    def estimate_probability_densecurve_norm_personnalized_variance(self, start=0, end=10, size=100):
        '''
        使用个性化的方差来计算
        '''
        data = self.data
        # computing avg
        sum_value = 0
        for i in range(0, len(data)):
            sum_value += data[i][1]
        avg = sum_value / len(data)

        # computing standard deviation
        variance = 0
        for i in range(0, len(data)):
            variance += (data[i][1] - avg) ** 2 / len(data)

        # Generate Dense Curve
        x = np.linspace(start, end, size)
        y = np.linspace(0, 0, size)
        for i in range(0, len(data)):
            y += self.norm_dist(data[i][1], (data[i][1] - avg) ** 2, x)
        y = y / len(data)
        return x, y

    def estimate_probability_densecurve_knn(self, start=0, end=10, size=100):
        '''
        kn近邻估计法
        '''
        data = [row[1] for row in self.data]
        datasorted = sorted(data)
        # parameters
        k = 3
        kn = k * math.sqrt(len(data))

        # Generate Dense Curve
        x = np.linspace(start, end, size)
        y = np.linspace(0, 0, size)

        for i in range(len(x)):  # each x
            start = 0
            end = len(x) - 1
            for j in range(len(datasorted)):  # initialize start, end
                if (datasorted[j] < x[i]):
                    start = j
                else:
                    end = j
                    break
            while end - start + 1 < kn:
                if start == 0:
                    end += 1
                elif end == (len(datasorted) - 1):
                    start -= 1
                else:
                    start -= 1
                    end += 1
                    if (datasorted[end] - x[i]) > (x[i] - datasorted[start]):
                        end -= 1
                    else:
                        start += 1
            V = max(datasorted[end]-x[i],x[i]-datasorted[start])*2
            y[i] = kn / len(datasorted) / V
        return x, y

    def avg_curve(self, avg_size):
        data = self.data



        pass

    def histogram_curve(self, start=0, end=10, size=100):
        x = np.linspace(start, end, size)
        y = np.linspace(0, 0, size)
        data = self.data
        for i in range(len(data)):
            j = 0
            for j in range(len(x)):
                if data[i][1] < x[j]:
                    break
            y[j] += 1
        return x, y


if __name__ == '__main__':
    print("I'm analysis tool")
