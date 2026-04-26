print('Todo por desarrollar')\n\ndf['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto'])
