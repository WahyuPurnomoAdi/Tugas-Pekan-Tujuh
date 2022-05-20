import pandas as pd 
pizza = {'Nama' : ['Kipli', 'bima', 'agung', 'dimas', 'ucok', 'tatang', 'candra', 'junaedi', 'fahrul', 'riscky'],
'Tinggi Badan': [181, 171, 164, 173, 169, 178, 163, 180, 165, 181],
'Berat Badan': [71, 54, 53, 58, 62, 68, 59, 67, 59 ,71]
}
pizza_df = pd.DataFrame(pizza)
pizza_df
print(pizza_df)