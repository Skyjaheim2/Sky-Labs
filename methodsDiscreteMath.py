
def solveDiscreteMath(topicAndExtensions, userInput):
    topic = topicAndExtensions.split('→')[0]
    extension = topicAndExtensions.split('→')[1]

    if topic == 'Set Theory':
        solution = setTheory(extension, userInput)


def setTheory(extension, setsString):
    if extension == 'Difference':
        Sets = setsString.split('-')
        print("Set Difference")
