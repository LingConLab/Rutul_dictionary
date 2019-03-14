import json


def process_dict():
    """
    Creates a json file from rutul_data.csv. 
    rutul_data.csv is a csv version of the excel rutul dictionary
    with first 15 columns (from index to pos). Separator is semicolon.
    """
    
    f = open('rutul_data.csv', 'r', encoding='utf-8')
    data = f.readlines()
    del data[0] # delete headings
    # print(len(data))

    res = dict()
    res['data'] = list()

    adds = dict() # additional forms
    toDel = list()

    for indx, line in enumerate(data):
        data[indx] = line.split(';')
        
    for i, new in enumerate(data[1:]):
        # print(data[i])
        # print(new)
        if new[1] == data[i][1]:
            adds[data[i][2]] = new[2] + ' (' + new[10].split('_')[1] + ')'
            toDel.append(i+1)
            # print(i+1)

    for ind, els in enumerate(data):
        # els = line.split(';')
        if ind not in toDel and els[2]:
            row = dict()
            row['id'] = els[1] # no 
            row['transcription'] = els[2] # record
            row['pos'] = els[14].strip() # pos
            if els[3]:
                row['pos'] = row['pos'] + ', ' + els[3] + ' class' # CL
            row['audio'] = "<audio controls preload=\"none\"><source src=\"audio/index.wav\" type=\"audio/wav\"></audio>".replace('index', els[1])
            row['translation'] = els[10].split('_')[0] # eng
            row['rustranslation'] = els[8].split('_')[0] # rus
            if els[2] in adds:
                row['add'] = adds[els[2]]
                row['add_audio'] = ''
            res['data'].append(row)
            
    with open('data.json', 'w', encoding='utf-8') as fw2:
        json.dump(res, fp=fw2, ensure_ascii=False, indent=1)
        
    print('Done.')
    
    
process_dict()
