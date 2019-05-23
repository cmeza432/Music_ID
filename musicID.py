"""
Name:           Carlos Meza
Description:    Shazamm
 Build database of songs given using glob function, then build signatures for each song and for single test song wanted to be matched using
 spectogram function. Then take five highest values found using the normalization and print out song names. Plot three closest values of their 
 spectogram.
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob

# Populates the signatures of given spectrogram and returns those max freq values
def populateSignatures(f, t, Sxx):
    result = np.zeros(len(t))
    # Loop through each instance and save those high max values from each column
    for k in range(len(t)):
        # Get highest value in column
        maxValue = max(Sxx[:,k])
        # Get equivalent freq value for maxValue
        index = Sxx[:,k].tolist().index(maxValue)
        # Set the empty result array to these frequency values of max value
        result[k] = f[index]

    return result


def classifyMusic() :
    # Create our 64 filenames that fit song-*.wav
    database = glob.glob('song-*.wav')
    # Create matrix array of signatures for each song
    databaseSignatures = np.empty((len(database),0)).tolist()
    # Array to hold vector norm values of each song compared
    similarity = np.empty(len(database))

    
    # Populate database signature array with signatures
    for i in range(len(database)):
        x, fs = sf.read(database[i])
        f, t, Sxx = spectrogram(x, fs=fs, nperseg=fs//2)
        databaseSignatures[i] = populateSignatures(f, t, Sxx)
        
    # Create signature for the corrupted song
    xTest, fs = sf.read('testSong.wav')
    f, t, Sxx = spectrogram(xTest, fs = fs, nperseg = fs // 2)
    testSignature = populateSignatures(f,t,Sxx)
    
    # Create Vector norm values for each song against test song
    for i in range(len(database)):
        similarity[i] = norm(databaseSignatures[i] - testSignature, ord=1)
    
    # Sort the norm values into new array to search highest values
    similaritySort = sorted(similarity)
    
    # Match the name to index of five highest values and print out
    for k in range(5):
        # Store index value of the value in song array and get index for name
        index = similarity.tolist().index(similaritySort[k])
        tempName = database[index]       
        # Save two closest values x value for plotting
        if(k == 0):
            x, fs = sf.read(database[index])
            firstX = x
        elif(k == 1):
            x, fs = sf.read(database[index])
            secondX = x
        print(similaritySort[k], tempName, sep="  ")
    
    # Print spectrogram of test song and two best matches
    # Test song plot
    plt.figure(0)
    plt.title('Test Song')
    plt.specgram(xTest, Fs=fs)
    # First best match plot
    plt.figure(1)
    plt.title('1st Best Match')
    plt.specgram(firstX, Fs=fs)
    # Second best match plot
    plt.figure(2)
    plt.title('2nd Best Match')
    plt.specgram(secondX, Fs=fs)
    plt.show()
    
###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
