from analysistool import AnalysisTool
import numpy as np
import matplotlib.pyplot as plt

src_folder = 'D:/Personal/Desktop/working2/research/天文大数据/miniGWAC/天文台光变曲线数据'
dst_folder = 'E:/working_folder/GWAC_anomaly_detection'

file10_1114 = src_folder + '/starlist10/1114.txt'

file11_1678 = src_folder + '/starlist11/1678.txt'
file11_2002 = src_folder + '/starlist11/2002.txt'  # bad estimation
file11_2391 = src_folder + '/starlist11/2391.txt'  # good estimation
file11_2520 = src_folder + '/starlist11/2520.txt'  # bad estimation
file11_3348 = src_folder + '/starlist11/3348.txt'

file12_3261 = src_folder + '/starlist12/3261.txt'

file13_1678 = src_folder + '/starlist13/1678.txt'

tool = AnalysisTool()

params = {
    # 'start': 0,
    # 'end': 10,
    'start': 0,
    'end': 10,
    'size': 100,
    'multiply': 1,
    'acc_hstgm': 1,
    'acc_dnscrv': 0.1,
    'filename': file13_1678,
    'amplify_fact': 1.5,
    'dnscrv_version': 1,
    'dnscrv_func': tool.estimate_probability_densecurve_knn,
    'avg_size': 20,
}


def draw_diagram():
    x, y = tool.show_diagram()
    plt.title(params['filename'].split('/')[-2] + "/" + params['filename'].split('/')[-1])
    plt.plot(x, y, "ro", linewidth=1)

    y_avg = np.linspace(0, 0, len(x))
    # draw average curve
    for i in range(len(y_avg)):  # 每一个数据点
        sum_y = 0
        count = 0
        start = x[i] - params['avg_size'] / 2
        end = x[i] + params['avg_size'] / 2

        for j in range(len(x)):
            if x[j] < end and x[j] >= start:
                sum_y += y[j]
                count += 1
        y_avg[i] = sum_y / count
    plt.plot(x, y_avg, 'b-', linewidth=1)


def draw_dense_curve():
    x, y = params['dnscrv_func'](start=params['start'], end=params['end'], size=params['size'])
    params['acc_dnscrv'] = sum(y)
    params['multiply'] = params['acc_hstgm'] / params['acc_dnscrv']
    print(params['multiply'])
    y *= params['multiply']
    # y*=8
    plt.plot(x, y, "r-", linewidth=1)


def draw_histogram():
    (x, y) = tool.histogram_curve(start=params['start'], end=params['end'], size=params['size'])
    params['acc_hstgm'] = sum(y)
    plt.plot(x, y, "g-", linewidth=1)


def exp1():
    tool.prepare_data(params['filename'])
    data = [row[1] for row in tool.data]
    min_v = min(data)
    max_v = max(data)
    params['start'] = min_v - (max_v - min_v) * params['amplify_fact'] / 2
    params['end'] = max_v + (max_v - min_v) * params['amplify_fact'] / 2
    plt.figure(1)
    draw_diagram()
    plt.figure(2)
    draw_histogram()
    draw_dense_curve()
    print(params)
    plt.grid(True)

    plt.show()


def exp2():
    tool.prepare_data(params['filename'])
    data = [row[1] for row in tool.data]
    min_v = min(data)
    max_v = max(data)
    params['start'] = min_v - (max_v - min_v) * params['amplify_fact'] / 2
    params['end'] = max_v + (max_v - min_v) * params['amplify_fact'] / 2
    plt.figure(1)
    draw_diagram()
    # plt.figure(2)
    # draw_histogram()
    # draw_dense_curve()
    # print(params)
    # plt.grid(True)

    plt.show()


if __name__ == '__main__':
    exp2()
