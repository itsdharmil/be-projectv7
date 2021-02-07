
import pandas as pd
import numpy as np
import pulp
import sys

sys.path.append('..')
COLS_POS = ['ls', 'st', 'rs', 
            'lw', 'lf', 'cf', 'rf', 'rw', 
            'lam', 'cam', 'ram', 
            'lm', 'lcm', 'cm', 'rcm', 'rm', 
            'lwb', 'ldm', 'cdm', 'rdm', 'rwb',
            'lb', 'lcb', 'cb', 'rcb', 'rb',
            'gk']

FORMATION_4_4_2 = ['gk','rb', 'rcb', 'lcb', 'lb','rm', 'rcm', 'lcm', 'lm','rs', 'ls']

FORMATION_5_3_2 = ['gk','rcb', 'cb', 'lcb','rwb', 'lwb','rcm', 'lcm','cam','rs', 'ls']
FORMATION_4_1_2_1_2=['gk','rb','rcb','lcb','lb','cdm','rcm','lcm','cam','rs','ls']

FORMATION_4_2_4 = ['gk','rb','rcb','lcb','lb','rw','rcm','lcm','lw','rs','ls']

FORMATION_4_3_2_1=['gk','rb','rcb','lcb','lb','rw','rcm','lcm','lw','cam','st']

FORMATION_3_5_2=['gk','rcb','cb','lcb','rm','rcm','cm','lcm','lm','rs','ls']


df=pd.read_csv('file3.csv')
def allplayer():
    return df['id'].tolist()
    
def create_temp(formation):
    
    TEMP = df[df['position'].isin(formation)]
    TEMP = TEMP[['id', 'position', 'value', 'overall']]
    return TEMP


def compute_best_lineup(df, formation, budget):

    # problem definition
    prob = pulp.LpProblem('BestLineup', pulp.LpMaximize)

    # get unique identifiers
    ids = df['id'].tolist()
    
    # parameters
    overalls = pd.Series(df['overall'].values, index=ids).to_dict()
    values = pd.Series(df['value'].values, index=ids).to_dict()

    ## dynamic paramters: selected positions
    ### convert position-strings into binary variables
    for pos in formation:
        df[f'is_{pos}'] = np.where(df['position'] == pos, 1, 0)
    
    ### extract positional parameters
    positions = {}
    for pos in formation:
        positions[pos] = pd.Series(df[f'is_{pos}'].values, index=ids).to_dict()

    # define the decision variable
    players = pulp.LpVariable.dicts("Player", ids, cat='Binary')

    # set objective
    prob += pulp.lpSum([overalls[i] * players[i] for i in ids]), "Total Rating of Lineup"

    # set constraints
    prob += pulp.lpSum([players[i] for i in ids]) == 11, "Pick_11_Players"
    prob += pulp.lpSum([values[i] * players[i] for i in ids]) <= budget, "Total_Value_Under_Budget"
    ## check if required position is picked
    for pos in formation:
        prob += pulp.lpSum([positions[pos][i] * players[i] for i in ids]) == 1, f"Pick_{pos.upper()}"

    result = prob.solve()

    picked_player_ids = [int(i.name.split('_')[1]) for i in prob.variables() if i.varValue > 0]
    
    return formation, picked_player_ids

def process_photo_links(text):
    start = 'https://cdn.sofifa.com/players'
    end = '19_60.png'
    id_str = str(text.split('/')[-1].split('.')[0]).zfill(6)
    return str(f'{start}/{id_str[:3]}/{id_str[3:]}/{end}')

def player_details(ids):
    rslt_df = df[df['id'].isin(ids)]
    rslt_df.set_index("id", drop=True, inplace=True)
    r=rslt_df[['name',  'nationality', 'age', 'club', 'overall', 'value','photo']]
    dictionary = r.T.to_dict('list')
    return dictionary

