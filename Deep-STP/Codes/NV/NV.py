# coding=UTF-8
# linDing group
# Hasan Zulfiqar

import numpy as np
import sys
import re


def obtainExternalParameters():
    if  sys.argv[1] == "-i" and sys.argv[3] == "-o":
        in_file = sys.argv[2]
        out_file = sys.argv[4]

        return in_file, out_file
    else:
        print("""\n\n\nUsage: 

	python NV.py -i inputFilename -o outputFilename

    parameter description:

	-i: The input filename. (required)

	-o: The output filename. (required)\n\n\n""")
        assert 0

def NV(sequence):
    StrOfResult = ''
    amino_acid = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    for each in amino_acid:
        W = []
        for i in sequence:
            if i == each:
                W.append(1)
            else:
                W.append(0)
        N = sequence.count(each)
        I = []
        for i in range(1, len(sequence) + 1):
            I.append(i)
        S0 = np.multiply(np.array(W), np.array(I))
        s = list(S0)
        S1 = []
        for i in s:
            if i == 0:
                pass
            else:
                S1.append(i)
        S = np.array(S1)
        T = np.sum(S)
        if N == 0:
            U = 0
        else:
            U = T / N
        if N == 0:
            D = 0
        else:
            D = np.sum((S - U) * (S - U)) / (N * len(sequence))
        StrOfResult +=  ',%.6f' % N
        StrOfResult += ',%.6f' % U
        StrOfResult += ',%.6f' % D
    return StrOfResult + '\n'

def NoteLine(): #生成表头
    amino_acid = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    noteLine = 'class'
    for each in amino_acid:
        noteLine += ",n%s,u%s,D2%s" % (each,each,each)
    return  noteLine + '\n'

def generateCsvFormatLine(in_file, out_file): #生成.csv文件
    g = open(out_file, 'w')
    g.write(NoteLine())
    g.close()

    f = open(in_file)
    lines = f.readlines()
    num_lines = len(lines)
    for i in range(num_lines):
        if lines[i][0] == '>':
            sampleType = '1'
            sequence = lines[i + 1].strip()
            featureValueStr = NV(sequence)
            g = open(out_file, 'a')
            g.write("%s%s" % (sampleType, featureValueStr))
            g.close()
            i += 1

if __name__ == '__main__':
    [in_file, out_file] = obtainExternalParameters()
    generateCsvFormatLine(in_file, out_file)
    #print("------Finished!------")