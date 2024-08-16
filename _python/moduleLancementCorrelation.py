import os, subprocess

def lancementCorrelation(inputFile, matchIDsteroCommand) : 
    """
    Fonction pour lancer la correlation

    Parameters
    ----------
    inputFile : str  

    matchIDsteroCommand : str 

    """

    subprocess.run([matchIDsteroCommand, inputFile])
