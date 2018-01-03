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
    'avg_size': 10,
}


def draw_diagram():
    x, y = tool.show_diagram()
    plt.title(params['filename'].split('/')[-2] + "/" + params['filename'].split('/')[-1])
    plt.plot(x, y, "ro", linewidth=1)

    y_avg = np.linspace(0, 0, len(x))

    # draw average curve

    # how average curve derived?

    # first, there is a avg_size in params, which indicates the number of data points used in calculating the average,
    # second, the data points used to calculate the avg in the given time is those data points nearest to the given time,
    # for example, for time t and size avg_size, the data point in [t-avg_size/2*gap_time,t+avg_size/2*gap_time] is used
    # to derive the average

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


def draw_diff():
    '''
    use the data points around a given time
    '''
    x, y = tool.show_diagram()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    plt.sca(ax1)
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
            if start <= x[j] < end:
                sum_y += y[j]
                count += 1
        y_avg[i] = sum_y / count

    plt.plot(x, y_avg, 'b-', linewidth=1)

    plt.sca(ax2)
    plt.plot(x, y - y_avg, 'ro')


def draw_diff2():
    '''
    use the data points before a given time
    :return:
    '''
    x, y = tool.show_diagram()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    plt.sca(ax1)
    plt.title(params['filename'].split('/')[-2] + "/" + params['filename'].split('/')[-1])
    plt.plot(x, y, "ro", linewidth=1)

    y_avg = np.linspace(0, 0, len(x))

    # draw average curve
    for i in range(len(y_avg)):  # 每一个数据点
        sum_y = 0
        count = 0
        start = x[i] - params['avg_size']
        end = x[i]

        for j in range(len(x)):
            if x[j] <= end and x[j] > start:
                sum_y += y[j]
                count += 1
        y_avg[i] = sum_y / count

    plt.plot(x, y_avg, 'b-', linewidth=1)

    plt.sca(ax2)
    plt.plot(x, y - y_avg, 'ro')


def draw_diff3():
    '''
    use the data points before a given time, and more importantly, the average is a weighted average
    :return:
    '''
    x, y = tool.show_diagram()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    plt.sca(ax1)
    plt.title(params['filename'].split('/')[-2] + "/" + params['filename'].split('/')[-1])
    plt.plot(x, y, "ro", linewidth=1)

    y_avg = np.linspace(0, 0, len(x))

    # draw average curve
    for i in range(len(y_avg)):  # 每一个数据点
        sum_y = 0
        count = 0
        start = x[i] - params['avg_size']
        end = x[i]

        data_points = []
        data_points.append(0)
        for j in range(len(x)):
            if x[j] <= end and x[j] > start:
                data_points.append(y[j])
        weight = np.linspace(2 / len(data_points), 0, len(data_points))[::-1]

        y_avg[i] = sum(weight * data_points)

    plt.plot(x, y_avg, 'b-', linewidth=1)

    plt.sca(ax2)
    plt.plot(x, y - y_avg, 'ro')

    pass


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


def exp3():
    tool.prepare_data(params['filename'])
    data = [row[1] for row in tool.data]
    min_v = min(data)
    max_v = max(data)
    params['start'] = min_v - (max_v - min_v) * params['amplify_fact'] / 2
    params['end'] = max_v + (max_v - min_v) * params['amplify_fact'] / 2
    plt.figure(1)
    draw_diff3()
    # plt.figure(2)
    # draw_histogram()
    # draw_dense_curve()
    # print(params)
    # plt.grid(True)

    plt.show()


if __name__ == '__main__':
    exp3()
