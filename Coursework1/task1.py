import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tag import pos_tag

corpus_root = "./corpusA/"
newcorpus = PlaintextCorpusReader(corpus_root, ".*", encoding='latin-1')
# print(newcorpus.words())
pos_tags = pos_tag(newcorpus.words())

# print(pos_tags)

# calculations: by comparing P(NN) * P(VB)
c_NN = 0
c_VB = 0
c_DT = 0
c_race_NN = 0
c_race_VB = 0
c_NN_DT = 0
c_IN_NN = 0
c_VB_DT = 0
c_IN_VB = 0
for i in range(len(pos_tags)):
    if pos_tags[i][1] == "NN":
        c_NN += 1
        if i+1 < len(pos_tags):
            if pos_tags[i+1][1] == "IN":
                c_IN_NN += 1
    elif pos_tags[i][1] == "VB":
        c_VB += 1
        if i+1 < len(pos_tags):
            if pos_tags[i+1][1] == "IN":
                c_IN_VB += 1
    elif pos_tags[i][1] == "DT":
        c_DT += 1
        if i+1 < len(pos_tags):
            if pos_tags[i+1][1] == "NN":
                c_NN_DT += 1
            elif pos_tags[i+1][1] == "VB":
                c_VB_DT += 1

    if pos_tags[i][0] == "race":
        # print(pos_tags[i][0])
        # print(pos_tags[i][1])
        if pos_tags[i][1] == "NN":
            c_race_NN += 1
        if pos_tags[i][1] == "VB":
            c_race_VB += 1
# P(race|NN) = C(race, NN) / C(NN)
P_race_NN = c_race_NN / c_NN
# P(NN|DT) = C(NN, DT) / C(DT)
P_NN_DT = c_NN_DT / c_DT
# P(IN|NN) = C(IN, NN) / C(NN)
P_IN_NN = c_IN_NN / c_NN
# P(NN) = P(race|NN) * P(NN|DT) * P(IN|NN)
P_NN = P_race_NN * P_NN_DT * P_IN_NN
# P(race|VB) = C(race, VB) / C(VB)
P_race_VB = c_race_VB / c_VB
# P(VB|DT) = C(VB, DT) / C(DT)
P_VB_DT = c_VB_DT / c_DT
# P(IN|VB) = C(IN, VB) / C(VB)
P_IN_VB = c_IN_VB / c_VB
# P(VB) = P(race|VB) * P(VB|DT) * P(IN|VB)
P_VB = P_race_VB * P_VB_DT * P_IN_VB

print("count NN: " + str(c_NN))
print("count VB: " + str(c_VB))
print("count DT: " + str(c_DT))
print("count race|NN: " + str(c_race_NN))
print("count race|VB: " + str(c_race_VB))
print("count NN|DT: " + str(c_NN_DT))
print("count VB|DT: " + str(c_VB_DT))
print("count IN|NN: " + str(c_IN_NN))
print("count IN|VB: " + str(c_IN_VB))

print("Word Likelihood P(race|NN): " + str(P_race_NN))
print("Word Likelihood P(race|VB): " + str(P_race_VB))
print("Tag Transition P(NN|DT): " + str(P_NN_DT))
print("Tag Transition P(IN|NN): " + str(P_IN_NN))
print("Tag Transition P(VB|DT): " + str(P_VB_DT))
print("Tag Transition P(IN|VB): " + str(P_IN_VB))

print("Likelihood for NN: " + str(P_NN))
print("Likelihood for VB: " + str(P_VB))
