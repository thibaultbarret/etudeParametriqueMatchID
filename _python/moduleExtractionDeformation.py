import os, subprocess, time 
import subprocess 

def verificationExistenceDossier(dossier) :
    if not os.path.exists(dossier) :
        print('creation dossier :')
        os.makedirs(dossier)
    return dossier


matchIDscriptPart1 = """MatchID.ResetData()
////**************** Units  *******************
MatchID.AddUnitConversion("[mm]","[inch]",0.0393700787)
MatchID.AddUnitConversion("[inch]","[mm]",25.4)
MatchID.AddUnitConversion("[ ]","[%]",100)
MatchID.AddUnitConversion("[%]","[ ]",0.01)
MatchID.AddUnitConversion("[ ]","[um/m]",1000000)
MatchID.AddUnitConversion("[um/m]","[ ]",1E-06)
MatchID.AddUnitConversion("[um/m]","[%]",0.0001)
MatchID.AddUnitConversion("[%]","[um/m]",10000)
////**************** Datasets  *******************
"""

matchIDscriptPart2 = """Strain_Henky_Q4_sw = DIC_Data.CalculateStrain(sw, 50, StrainConvention.Henky, Interpolation.Q4, "", False, False)"""

def extractionDeformation(nomFichierInstructionsMatchID, strainWindow) : 
    """
    Fonction pour calculer les deformations a partir de resultats de correlation MatchID stereo 

    Parameters
    ----------
    nomFichierInstructionsMatchID : str 

    strainWindow : int or list 
    
    """

    matchIDscript = open('extractionScriptDeformation.mico', "w")
    matchIDscript.write(matchIDscriptPart1 + '\n')

    # Ajouter la partie relative au nom de la configuration de parametres : 
    matchIDscript.write(r"DIC_Data = MatchID.LoadData({" + '"' +  nomFichierInstructionsMatchID + '"' + r"})" + "\n")
    
    # Ecrire la commande pour le calul des deformation : 
    # -> Boucle pour faire le calcul pour les deux valeurs de deformations : 
    for sw in strainWindow : 
        # Creation dossier pour les resultats :
        dossierExport = os.path.join(os.getcwd(), '%s-%i' %(nomFichierInstructionsMatchID.replace('.m3inp', ''), sw))
        # print(dossierExport)
        # os.makedirs(dossierExport)
        # Calcul des deformations : 
        matchIDscript.write(matchIDscriptPart2.replace('sw', "%i" %sw) + '\n')
        
        # Extraction : 
        matchIDscript.write("Strain_Henky_Q4_%i.Export(ExportType.CSV," %sw + r'"' + dossierExport + r'"' + r""", {"exx"; "eyy"; "exy"; "evm"}, {}, {"<Delimiter>=<,>";"<NumericalFormat>=<>";"<CsvHeaderStyle>=<Short>"})""" + '\n' )

    matchIDscript.close()

    # Lancement de l'extraction : 
    process = subprocess.Popen(["LibGenRes.exe", "extractionScript.mico"])
    while not os.path.exists(dossierExport + r"\Image_6760_0.tiff")  : 

        time.sleep(5)
    time.sleep(2)
    process.terminate()


