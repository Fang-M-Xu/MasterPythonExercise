import math


class StatisticsF:
    def __init__(self, data_list):
        self.data_list = data_list

    def count(self):
        return len(self.data_list)

    def sum(self):
        return sum(self.data_list)

    def min(self):
        lst = list(self.data_list)
        lst.sort()
        return lst[0]

    def max(self):
        lst = list(self.data_list)
        lst.sort(reverse=True)
        return lst[0]

    def range(self):
        lst = list(self.data_list)
        lst.sort()
        return lst[-1] - lst[0]

    def mean(self):
        return sum(self.data_list) / len(self.data_list)

    def mode(self):
        lst = list(self.data_list)
        dict_mode = {}
        for i in lst:
            if dict_mode.get(i) is None:
                dict_mode[i] = 1
            else:
                dict_mode[i] += 1
        rev_dict_mode = sorted(dict_mode.items(), reverse=True, key=lambda x: x[1])
        return rev_dict_mode[0]

    def var(self):
        lst = list(self.data_list)
        mean = sum(lst) / len(lst)
        deviation = [(x - mean) ** 2 for x in lst]
        variance = sum(deviation) / len(lst)
        return variance

    def std(self):
        var = self.var()
        std = math.sqrt(var)
        return std


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = StatisticsF(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
