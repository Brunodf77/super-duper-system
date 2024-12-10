pokedex = []
def creationPokemon() :
    pokemon = { 
        "Nom" : input ("Selectionner un nom"),
        "Type" : input ("Selectionner un type"),
        "HP" : input ("Selectionner des HP"),
        "Attaque" : input ("Selectionner une attaque"),
        "Defense" : input ("Selectionner une Defense"),
    }        

def ajouteauPokedex(pokemon) : 
    pokedex.append(pokemon) 