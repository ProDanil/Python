import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit as fAct

def initNetPar():
    inputNodes = 784
    print('Введите число скрытых нейронов: ')
    hiddenNodes = int(input())
    outNodes = 10
    print('Введите коэф. обучения: ')
    learnSpeed = float(input())
    return inputNodes, hiddenNodes, outNodes, learnSpeed

def createNetW(inputNodes, hiddenNodes, outNodes):
    wInHid = np.random.uniform(-0.5, 0.5, (hiddenNodes, inputNodes))
    wHidOut = np.random.uniform(-0.5, 0.5, (outNodes, hiddenNodes))
    return wInHid, wHidOut

def netOut(wInHid, wHidOut, inputSignal, returnHid):
    inputs = np.array(inputSignal, ndmin=2).T
    hidIn = np.dot(wInHid, inputs)
    hidOut = fAct(hidIn)
    finalIn = np.dot(wHidOut, hidOut)
    finalOut = fAct(finalIn)

    if returnHid==0:
        return finalOut
    else:
        return finalOut, hidOut

def netTrain(targetList, inputSignal, wInHid, wHidOut, learnSpeed):
    targets = np.array(targetList, ndmin=2).T
    inputs = np.array(inputSignal, ndmin=2).T
    finalOut, hidOut = netOut(wInHid, wHidOut, inputSignal, 1)

    outErrors = targets - finalOut
    hidErrors = np.dot(wHidOut.T, outErrors)

    wHidOut += learnSpeed*np.dot((outErrors*finalOut*(1-finalOut)), hidOut.T)
    wInHid += learnSpeed*np.dot((hidErrors*hidOut*(1-hidOut)), inputs.T)

    return wInHid, wHidOut

def trainSet(wInHid, wHidOut, learnSpeed):
    dataFile = open("mnist_train.csv",'r')
    trainingList = dataFile.readlines()
    dataFile.close()

    for record in trainingList:
        allValues = record.split(',')
        inputs = (np.asfarray(allValues[1:])/255.0*0.999)+0.001
        targets = np.zeros(10)+0.001
        targets[int(allValues[0])]=1.0
        wInHid, wHidOut = netTrain(targets, inputs, wInHid, wHidOut, learnSpeed)

    return wInHid, wHidOut

def testSet(wInHid, wHidOut):
    dataFile = open("mnist_test.csv",'r')
    testList = dataFile.readlines()
    dataFile.close()

    test=[]
    for record in testList:
        allValues = record.split(',')
        inputs = (np.asfarray(allValues[1:])/255.0*0.999)+0.001
        outSession = netOut(wInHid, wHidOut, inputs, 0)

        if int(allValues[0])==np.argmax(outSession):
            test.append(1)
        else:
            test.append(0)
    test = np.asarray(test)
    print('Эффективность % = ', (test.sum()/test.size)*100)

def plotImage(pixels: np.array):
    plt.imshow(pixels.reshape((28,28)), cmap='gray')
    plt.show()

inputNodes, hidNodes, outNodes, learnSpeed = initNetPar()
wInHid, wHidOut = createNetW(inputNodes, hidNodes, outNodes)
for i in range(5):
    print('Тест № ', i+1)
    wInHid, wHidOut = trainSet(wInHid, wHidOut, learnSpeed)
    testSet(wInHid, wHidOut)

dataFile = open("mnist_test.csv", 'r')
testList = dataFile.readlines()
dataFile.close()
allValues = testList[int(np.random.uniform(0,9999))].split(',')
inputs = (np.asfarray(allValues[1:])/255.0*0.999)+0.001
# wIn = np.random.uniform(0.5, 0.5, (100, 784))
# wOut = np.random.uniform(0.5, 0.5, (10, 100))
# outSession = netOut(wIn, wOut, inputs, 0)
outSession = netOut(wInHid, wHidOut, inputs, 0)
print(np.argmax(outSession))
plotImage(np.asfarray(allValues[1:]))

