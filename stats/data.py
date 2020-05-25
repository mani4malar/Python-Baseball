import os
import pandas as pd
import glob

# game_files =glob.glob(os.path.join(r'C:\Users\mani4\git\Python-Baseball','games','*.EVE'))
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()
# print(game_files)

game_frames=[]
for game_file in game_files:
    game_frame =pd.read_csv(game_file,names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6',  'event'])
    game_frames.append(game_frame)

game=pd.concat(game_frames)

game.loc[game.multi5=='NaN', 'multi5'] = ''

identifiers=game['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers=identifiers.fillna(method='ffill')
identifiers.columns=['game_id','year']
# print(type(identifiers))
# print(identifiers.head())
# print(game.columns)

games=pd.concat([game,identifiers],axis=1,sort=False)
# print(type(games.columns))
# print(games.isna().sum())
# print("=================================")
games = games.fillna('')
games['type'] = pd.Categorical(games.type)
# print(games.isna().sum())
# games=pd.Categorical(games.loc[:])

# print(games.describe())
print(games.info())