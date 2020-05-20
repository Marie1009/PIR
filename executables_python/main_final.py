import ccdc
import v4_hcda

import time

# Debut du decompte du temps
start_time = time.time()

# recuperation des datasets
all_data = v4_hcda.get_sequences("./datasetP")
print('get_sequences')
# modification des timestamps sans concatenation des sequences (division par 1000 de toutes les valeurs)
data_modif = v4_hcda.modif_timestamps(all_data,0.001)
print('modif_timestamps')

# choix du nombre de sequences a analyser
nb_salades = 10
data_selected = data_modif[0:nb_salades]
#concatenation et decalage des timestamps
transformed_data= v4_hcda.decal_concat(data_selected)
print('decal_concat')
#for d in transformed_data:
#    print(d)

limite_ecarts = v4_hcda.exploration(data_selected)
limite_freq = nb_salades #au minimum on veut que les chroniques soient presentes 1 fois par salade... mais pas verifiable

gaps_dict = {}
for E in data_selected:
    ccdc.get_gaps(E, limite_ecarts, gaps_dict)
base = ccdc.generate_trees(gaps_dict)
#ccdc.print_tree(base)

#base = ccdc.CCDC(transformed_data,limite_ecarts)
#ccdc.print_tree(base)

results = v4_hcda.main_concat_v2(limite_ecarts,limite_freq,base,transformed_data)
#results = v4_hcda.main_concat(limite_ecarts,limite_freq,lambda x: ccdc.CCDC(x,limite_ecarts),transformed_data)

#avec indice
#results = v4_hcda.main_concat(limite_ecarts,limite_freq,lambda x: ccdc.CCDC(x,limite_ecarts),transformed_data[:v4_hcda.indice(nb_salades,all_data)])

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))

print(len(results))
