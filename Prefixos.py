def findCompletePrefixes(names, query):
    # Write your code here
    nPrefix = 0
    prefixos = []
    
    for prefixo in query: #percorre a lista de prefixos
        print ("Inicio do prefixo")
        for nome in names: #percorre a lista de nomes
            print(nome.len())

            if (prefixo.len() < nome.len()):
                print(prefixo)
                print(nome)
                if nome.startswith(prefixo):
                    nPrefix += 1
                else: # se o nome nao comeca com o prefixo
                    pass
            else: #se o prefixo nao e menor que o nome
                pass
        #quando tiver percorrido todos os nomes
        print("Fim do prefixo")
        prefixos.append(nPrefix)
            
    
    return prefixos

findCompletePrefixes(['steve','stevens','danny','steves','dan','john','johnny','joe','alex','alexander'], ['steve','alex','joe','john','dan'])