import pandas as pd
import numpy as np
import difflib as dl

tune_list = []


df = pd.read_csv('irish_fiddle.csv')

tunes = df['Track Name']

for tune in tunes:
    if '/' in tune:
        first_split = tune.split("/")
        x = first_split[0]
        y = first_split[1]
        tune_list.append(x)

        if '/' in y:
            z = y.split('/')
            tune_list.append(z)
        else:
            tune_list.append(y)

    else:
        if ',' in tune:
            first_split = tune.split(",")
            a = first_split[0]
            b = first_split[1]
            tune_list.append(a)

            if ',' in b:
                c = b.split(',')
                tune_list.append(c)
            else:
                tune_list.append(b)


tune_array = np.asarray(tune_list)

np.sort(tune_array)

for tune in tune_array:
    for tune2 in tune_array:
        if dl.SequenceMatcher(None, tune, tune2) < 1.0:
            array.remove(tune2)


tune_df = pd.DataFrame(tune_array)

tune_df.sort_values(by=[0], inplace=True)
tune_df_str = tune_df[0].str.strip()

# print(tune_df_str)
tune_df_str.drop_duplicates(keep='first', inplace=True)


tune_df_str.to_csv('irish_fiddle_split.csv', header=None, index=None)




