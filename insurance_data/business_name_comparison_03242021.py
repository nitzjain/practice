#get unique ins_broker_name
#make a list of common words(full country)
#use string matching(fuzzy) : token_set_ratio
#use that to link to original file and then sort.
#blue cross blue shield/BCBS/ blue shielf of california/blue cross of california
#total broker fees + commissions



import pandas as pd
from collections import Counter
from fuzzywuzzy import fuzz

pd.set_option('display.max_columns', 1000)
df = pd.read_csv('/Users/niteshjain/Desktop/Insurance_Project/F_SCH_A_PART1_mod.txt',sep = '|')
#print(df.columns)
#print(df['SPONS_DFE_MAIL_US_STATE'].value_counts().head(50))
#print(df.head())

all_names = df['INS_BROKER_NAME'][df['INS_BROKER_US_STATE']=='TX'].unique()
all_names = all_names.astype(str)

#names_freq = Counter()
#for name in all_names:
 #   names_freq.update(str(name).split(" "))
#key_words = [word for (word,_) in names_freq.most_common(30)]
#print(key_words)
key_words =['INC', 'INC.', 'INSURANCE', '&', 'LLC', 'AND', 'SERVICES', 'GROUP', 'INS', 'BENEFITS', 'AGENCY', 'OF', 'BENEFIT', 'FINANCIAL', 'ASSOCIATES', 'THE',  'AGENTS', 'INS.', 'COMPANY', 'SERVICES,', '-', 'SVCS', 'VARIOUS', 'GROUP,', 'CO', 'AGENCY', 'ASSOCIATES,', 'ASSOC', 'SOLUTIONS', 'CONSULTING', 'SERVICE', 'CORP', 'OTHER', 'ADVISORS', 'PENSION', 'CO.', 'MANAGEMENT', 'LTD', 'PARTNERS', 'AGCY', 'SECURITIES', 'CORPORATE', 'HUB', 'GRP', 'INTERNATIONAL', 'ASSOC.', 'CORPORATION', 'NFP','FL','MA','AR','PA','TX','DC','MI','WI','TN','NY','CA','NC','LA','OR','WV','MN','OH','WA','IL','ME','nan','DE','NJ','VA','CO','IN','NE','AL','AZ','NH','SC','MP','KS','CT','MD','GA','AK','IA','ID','NM','MO','HI','SD','MS','KY','NV','OK','MT','PW','UT','ND','PR','RI','WY','VT','VI','AA','FM','GU','MH']


all_names.sort()
all_main_name = pd.DataFrame(columns=['sort_gp','names','alias','score'])
all_main_name['names'] = all_names
all_main_name['sort_gp'] = all_main_name['names'].apply(lambda x: x[0])
#print(all_main_name)



all_sort_gp = all_main_name['sort_gp'].unique()


def no_key_word(name):
    """check if the name contain the keywords in company"""
    output = True
    for key in key_words:
        if key in name:
            output = False
    return output


for sortgp in all_sort_gp:
    this_gp = all_main_name.groupby(['sort_gp']).get_group(sortgp)
    gp_start = this_gp.index.min()
    gp_end = this_gp.index.max()
    for i in range(gp_start, gp_end + 1):

        # if self has not got alias, asign to be alias of itself
        if pd.isna(all_main_name['alias'].iloc[i]):
            all_main_name['alias'].iloc[i] = all_main_name['names'].iloc[i]
            all_main_name['score'].iloc[i] = 100

        # if the following has not got alias and fuzzy match, asign to be alias of this one
        for j in range(i + 1, gp_end + 1):
            if pd.isna(all_main_name['alias'].iloc[j]):
                fuzz_socre = fuzz.token_sort_ratio(all_main_name['names'].iloc[i], all_main_name['names'].iloc[j])
                if not no_key_word(all_main_name['names'].iloc[j]):
                    fuzz_socre -= 10
                if (fuzz_socre > 85):
                    all_main_name['alias'].iloc[j] = all_main_name['alias'].iloc[i]
                    all_main_name['score'].iloc[j] = fuzz_socre

        if i % (len(all_names) // 10) == 0:
            print("progress: %.2f" % (100 * i / len(all_names)) + "%")

all_main_name.to_csv('/Users/niteshjain/Desktop/Insurance_Project/F_SCH_A_PART1_mod_sorted_TX_032421.txt')
