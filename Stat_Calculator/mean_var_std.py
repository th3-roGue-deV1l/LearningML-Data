import numpy as np

#Check List Size
def check_list_size(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine elements.")
    pass

#Function that calculates the required statistics for a row
def statistics(arr):

    mean, variance, stddev, maxim, minim, sumation = [], [], [], [], [], []
    for row in arr:
        mean.append(np.mean(row))
        variance.append(np.var(row))
        stddev.append(np.std(row))
        maxim.append(np.max(row))
        minim.append(np.min(row))
        sumation.append(np.sum(row))

    return [mean, variance, stddev, maxim, minim, sumation]

#Function that appends respective data to the dictionary
def append_data(dict, stats):
    keys_list = dict.keys()
    # print(keys_list)
    for idx, key in enumerate(keys_list):
        dict[key].append(stats[idx])

#The first-called major calculation function
def calculate(list):

    try:
        check_list_size(list)
    except ValueError as e:
        print('Error', e)

    #Given list into array
    array_3x3 = np.array(list).reshape(3, 3)
    array_3x3 = np.transpose(array_3x3)

    #Initialise dict
    calculations = {
        'mean' : [],
        'variance' : [],
        'standard_deviation' : [],
        'max' : [],
        'min' : [],
        'sum' : [],
    }

    #Axis-1
    list_of_stat = statistics(array_3x3)
    append_data(calculations, list_of_stat)

    #Axis-2
    array_3x3 = np.transpose(array_3x3)
    list_of_stat = statistics(array_3x3)
    append_data(calculations, list_of_stat)

    #Stat
    list_of_stat = [
        np.mean(array_3x3),
        np.var(array_3x3),
        np.std(array_3x3),
        np.max(array_3x3),
        np.min(array_3x3),
        np.sum(array_3x3)
    ]
    append_data(calculations, list_of_stat)

    return calculations