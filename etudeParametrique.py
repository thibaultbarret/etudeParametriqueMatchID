import os, sys 
sys.path.append('./_python/')
import numpy as np 

incr_subsetSize = 2
incr_stepSize= 1

subsetSize = np.arange(29, 37 + incr_subsetSize, incr_subsetSize, dtype = int)
stepSize = np.arange(4, 9 + incr_stepSize, incr_stepSize, dtype = int)
subsetFonctions = {'affine'    : 1,
                   'quadratic' : 3, }


# Module pour generer le fichier d'entree : 

from moduleGenerationFichierInput import generationFichierInput
from moduleLancementCorrelation   import lancementCorrelation  
from moduleExtractionDeformation  import extractionDeformation
# from modulePostTraitement         import postTraitement

# outputFile = generationFichierInput('./templateInputFileMatchID.m3inp', 35, 4, 'affine', subsetFonctions)

for subset in subsetSize : 
    for step in stepSize : 
        for key in subsetFonctions.keys() : 

            # Generation du fichier d'entree : 
            outputFile = generationFichierInput('./templateInputFileMatchID.m3inp',
                                                subset,
                                                step,
                                                key,
                                                subsetFonctions)

            lancementCorrelation(outputFile,
                                 "MatchIDStereo.exe")

            extractionDeformation(outputFile, [5, 7, 9])

            os.rmdir(outputFile)

            quit()
            # print('analyseEnchoche-%i-%i-%s\n' %(subset, step, key))
