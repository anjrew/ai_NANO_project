
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

# CUSTOMER VARIABLES
qsWorkerMistakePercent = 5

# AI VARIABLES
aiMistakesPercentage = 50
difficulty = 1
# difficultyAmplification = 0.8
dataNodesNeeded = 12000
reasons = 6000 # The amount of classifications of reason
# https://www.researchgate.net/post/What_is_the_minimum_sample_size_required_to_train_a_Deep_Learning_model-CNN
samplesNeededPerReason = 1000 # Most people saying 1000 per class for the most complex cases

# OTHER VARIABLES
amountModulesPeryear = 6000
years = 10

mistakesWorker = []
mistakesAi = []
sampleAmount = 0
i = 0
while i < years:
    
    x = 0
    while x < amountModulesPeryear:
        sampleAmount = sampleAmount + 1
        if sampleAmount % samplesNeededPerReason == 0:
            aiMistakesPercentage = aiMistakesPercentage - difficulty
            # difficulty = difficulty * difficultyAmplification

        x = x + 1

    mistakesAi.append(aiMistakesPercentage)
    mistakesWorker.append(qsWorkerMistakePercent) 
    i = i+1

# PLOTTING
fig, ax = plt.subplots()
theRange = range(0, years)
print(theRange)
ax.plot( range(0, years), mistakesAi, range(0, years), mistakesWorker )

# LEGEND
ax.set(xlabel='Time', ylabel='Cost', title='Payback period')
ax.legend(['AI', 'Worker'])
ax.grid()

# SAVING PNG AND RENDERING
fig.savefig("test.png")
plt.show()

exit()