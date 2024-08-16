def quitterProgramme(message = None) : 
    """
    Fonction pour afficher un/des message(s) avant de quitter le programme
    Parameters
    ----------
    message : str / list
    
    """

        

    if isinstance(message, str) : 
        print(message)

    if isinstance(message, list) :
        for mess in message : 
            print(mess)

    print('Fin du programme')
    quit()
