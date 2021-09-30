# coding=UTF-8
# linDing group
# Hasan Zulfiqar

def obtainExternalParameters():
    if sys.argv[1] == "-g" and sys.argv[3] == "-i" and sys.argv[5] == "-o":
        g_num = int(sys.argv[2])
        in_file = sys.argv[4]
        out_file = sys.argv[6]

        return g_num, in_file, out_file
    else:
        print("""\n\n\n\n\nUsage: 

python g-gap.py -g g_num -i inputFilename -o outputFilename

parameter description:

-r: It represents the counted rank (or tier) of the correlation along a protein sequence. It must be non-Negative integer and smaller than L-1. 

-i: The input filename. (required)

-o: The output filename. (required)\n\n\n""")
        assert 0    

def ListOfPeipeptide():
    aminoAcid = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    content = []
    for i in aminoAcid:
        for j in aminoAcid:
            peipeptide = i + j
            content.append(peipeptide)
    return content

def ListOfSeq_peipeptide(sequence):
    g_num = g_num = int(sys.argv[2])
    Seq_peipeptide = []
    for i in range(len(sequence) - g_num -1):
        Seq_peipeptide.append(sequence[i] + sequence[i + g_num + 1])
    return Seq_peipeptide

def DictOfEach_seqAndCounts():
    content = ListOfPeipeptide()
    each_seq = {}
    each_seq = each_seq.fromkeys(content, 0)
    counts = {}
    counts = counts.fromkeys(content, 0)
    return each_seq,counts

def CalculateOccurenceFrequencyOfPeipeptide(sequence):
    each_seq = DictOfEach_seqAndCounts()[0]
    counts = DictOfEach_seqAndCounts()[1]
    content = ListOfPeipeptide()
    Seq_peipeptide = ListOfSeq_peipeptide(sequence)

    for each_peipeptide in content:
        each_seq[each_peipeptide] += Seq_peipeptide.count(each_peipeptide)
        counts[each_peipeptide] += Seq_peipeptide.count(each_peipeptide)

    occurfrequency = dict()
    summ = sum(counts.values())
    featureValueStr = ''
    for each_key in counts.keys():
        num = counts[each_key]

        if num == 0:
            occurfrequency[each_key] = float('%.6f' % 0)
            featureValueStr += ',%.6f' % (occurfrequency[each_key])
        else:
            occurfrequency[each_key] = float('%.6f' % (num / summ))
            featureValueStr += ',%.6f' % (occurfrequency[each_key])
    return featureValueStr+'\n'

def generateCsvFormatNoteLine():
    noteLine = 'class'
    peptide = ListOfPeipeptide()
    for eachAA in peptide:
        noteLine += ",%s_freq"%(eachAA)
    return noteLine+'\n'

def generateCsvFormatLine(in_file, out_file):
    g = open(out_file, 'w')
    g.write(generateCsvFormatNoteLine())
    g.close()

    f = open(in_file)
    lines = f.readlines()
    num_lines = len(lines)
    for i in range(num_lines):
        if lines[i][0] == '>':
            sampleType = '1'
            sequence = lines[i+1].strip()
            featureValueStr = CalculateOccurenceFrequencyOfPeipeptide(sequence)
            g = open(out_file, 'a')
            g.write("%s%s" % (sampleType, featureValueStr))
            g.close()
            i += 1

import re
import sys


if __name__ == '__main__':
    [g_num, in_file, out_file] = obtainExternalParameters()
    generateCsvFormatLine(in_file, out_file)
    #print("------Finished!------")



