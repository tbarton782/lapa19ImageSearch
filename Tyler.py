import pickle

from popsift import computeKp
from popsift import compare


def findMatch(self):
    userdes = computeKp(str(self))
    f = open('monuments.pkl', 'rb')
    tup = pickle.load(f)

    maxp = -1
    while (tup):
        print(tup[1])
        c = compare(userdes, tup[0], 0)

        if c > 0:
            if maxp < c:
                maxp = c
                self = tup[1]

        try:
            tup = pickle.load(f)
        except:
            if maxp != -1:
                print("and the winner is...", self)
                ind = self.rfind("/")
                ind2 = -1
                for i in ['1', '2', '3', '4', '5']:
                    ind2 = max(self.find(i), ind2)
                self.label_2.setText(
                    "The image is of : " + self[ind + 1:ind2])
            else:
                self.label_2.setText("Sorry !No matches found")
            break

# findMatch('QuerryImg_Dragon.jpg')
