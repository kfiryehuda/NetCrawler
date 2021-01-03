import requests
import lxml.html
import random
import main
import time


def init_dic(listOfPairs):
    """
    initiates the dictionary.
    :param listOfPairs: list of list. each list has source url and destination url.
    :return: returns initialized dic.
    """
    dic = {}
    # builds dic
    for pair in listOfPairs:
        if pair[0] not in dic:
            dic[pair[0]] = []
        if pair[1] not in dic:
            dic[pair[1]] = []
    n = len(dic)

    # initiates prev and current rank
    for key in dic:
        dic[key].append(1 / n)
        dic[key].append(1 / n)

    # find all i such as i->j, count outbound links
    for key in dic:
        dic[key].append(0)
        dic[key].append([])
        for pair in listOfPairs:
            # i->j
            if key == pair[1]:
                dic[key][3].append(pair[0])
            # outbound links
            if key == pair[0]:
                dic[key][2] += 1
    return dic


def find_dead_ends(dic, listOfPairs):
    """
    making a list of all the urls that are dead ends in our case.
    :param dic: dic with url as a key and the url's info as value
    :param listOfPairs: list of list. each list has source url and destination url.
    :return: returns a list of dead end urls
    """
    dead_ends = []
    source = [x[0] for x in listOfPairs]
    destination = [x[1] for x in listOfPairs]
    for key in dic:
        if key in destination and key not in source:
            dead_ends.append(key)
    return dead_ends


def tennisRank(listOfPairs, numIters):
    """
    finds the rank of each url according to the formula given in the exercise
    :param listOfPairs: list of list. each list has source url and destination url.
    :param numIters: number of iterations
    :return:returns dic with url as key and rank as a value.
    """
    # [0]:prev, [1]:current, [2]: number of outbound links, [3]: connections
    dic = init_dic(listOfPairs)
    n = len(dic)
    dead_ends = find_dead_ends(dic, listOfPairs)
    for iteration in range(numIters):
        for key in dic:
            dic[key][1] = 0.8 * sum([(dic[x][0] / dic[x][2]) for x in dic[key][3]]) + 0.2 * (1 / n) + 0.8 * sum(
                [(dic[x][0] / n) for x in dead_ends])
        # update prev
        for key in dic:
            dic[key][0] = dic[key][1]

    final_dic = {}
    for key in dic:
        final_dic[key] = dic[key][1]

    return final_dic
