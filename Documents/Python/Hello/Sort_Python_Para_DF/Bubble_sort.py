# Códgo para ordenação de um DF por bubble sort(Não é rapido definitivamente, não use, so em últimmo caso)
# for i in range(df.shape[0]):
#     for j in range(df.shape[0]-i-1):
#         if(df.loc[j,'coluna que vai sofrer o sort'] > df.loc[j+1,'coluna que vai sofrer o sort']):
#             aux = df.iloc[j]
#             df.iloc[j] = df.iloc[j+1]
#             df.iloc[j+1] = aux