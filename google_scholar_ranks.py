import pandas as pd
import os

file_path=r'C:\Users\Shir\OneDrive - Bar Ilan University\research\google scholar journal ranks'

class GS_ranks:
    journals_dict=dict()
    cats_df=pd.DataFrame()

    def extract_excel_data(self):
        for file in os.listdir(path=file_path):
            print('now creating for {}'.format(file))
            obj_path = os.path.join(file_path, file)
            data=pd.read_excel(obj_path,None, index_col=0)
            for cat,val in data.items():
                if cat=='Subcategories':
                    continue
                val['category']=cat
                self.cats_df=self.cats_df.append(val)
                for idx, journal_data in val.iterrows():
                    journal=journal_data['Publication']
                    h5_index=journal_data['h5-index']
                    h5_median=journal_data['h5-median']
                    if not journal in self.journals_dict:
                        self.journals_dict[journal]=0
                    else:
                        self.journals_dict[journal]+=1



if __name__ == '__main__':
    gs_ranks=GS_ranks()
    data=gs_ranks.extract_excel_data()

    for k,v in gs_ranks.journals_dict.items():
        if v>1:
            print('current journal {} has {} cats'.format(k,v))
    print(len(gs_ranks.journals_dict))
    print('num categories {}'.format(len(gs_ranks.cats_df['category'].unique())))
