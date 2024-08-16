import os 
from moduleQuitterProgramme import quitterProgramme

def generationFichierInput(nomFichierTemplate, subsetSize, stepSize, subsetFonction, dictSubsetFonction) : 

    """
    Fonction pour generer le fichier d'instructions MatchID

    Parameters
    ----------
    nomFichierTemplate : str 
        
    subsetSize : int 

    stepSize : int

    subsetFonction : str 

    dictSubsetFonction : dict
    
    Returns
    -------
     
    """

    # 1. Open nomFichierTemplate : 
    if not os.path.exists(nomFichierTemplate) : 
        quitterProgramme("Le fichier %s n'existe pas" %nomFichierTemplate)

    with open(nomFichierTemplate, 'r') as fichierTemplate :
        lignesFichierTemplate = fichierTemplate.readlines()
    

    outputFile = "analyse-%i-%i-%s.m3inp" %(subsetSize, stepSize, subsetFonction)
    with open(outputFile, "w") as fileToWrite :
        for line in lignesFichierTemplate : 
            cond = True 

            if "<Subset$size>=" in line : 
                fileToWrite.write("<Subset$size>=<%i>\n" %subsetSize)
                cond = False

            if "<Step$size>=" in line : 
                fileToWrite.write("<Step$size>=<%i>\n" %stepSize)
                cond = False
            
            if "<Transformation>=" in line : 
                fileToWrite.write("<Transformation>=<%i>\n" %dictSubsetFonction[subsetFonction])
                cond = False
        
            if "<Output$path>=" in line : 
                fileToWrite.write("<Output$path>=<%s>\n" %(os.path.join(os.getcwd(), 'etudeParametrique', 'Analyse-%i-%i-%s' %(subsetSize, stepSize, subsetFonction))))
                cond = False

            if cond is True : 
                fileToWrite.write(line)


    return outputFile
