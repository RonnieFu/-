# encoding=gbk
import pandas as pd
from snownlp import SnowNLP

def sentiment_analysis(output_filename):
    df_1 = pd.read_csv(output_filename, header=None, usecols=[1, 2, 3, 4, 5])
    df_1.columns = ['uname', 'comment', 'star', 'title', 'support']
    # ���ֵ
    df_1['comment'].fillna(" ",inplace=True)
    df_1['star'] = df_1['star'].astype(str)
    df_1['star'] = df_1['star'].str.replace("allstar", "")
    df_1['star'] = df_1['star'].str.replace("0", "")
    df_1['star'] = df_1['star'].apply(lambda x: 3 if len(x) > 1 else x)
    # df_1['star']=df_1['star'].str.replace("33","3")
    df_1['star'].fillna(3, inplace=True)
    # ��ץȡ��csv�ļ��������ڵ����У����Ϊ2
    df = pd.read_csv(output_filename, header=None, usecols=[2])

    # ��dataframeת��ΪList
    contents = df.values.tolist()
    # ���ݳ���

    # ������б�洢��з�ֵ
    score = []
    for content in contents:
        try:
            s = SnowNLP(content[0])
            # print(s.summary())
            score.append(s.sentiments)
        except:
            #TODO ������Ҫ�������һ�����
            #print("")
            #�Զ��Ϊ
            score.append(0.5)
    data2 = pd.DataFrame(score)
    # data2.to_csv('sentiment.csv',header=False,index=False,mode='a+')

    # �����������
    df_1['sentiment_score'] = data2

    df_1.to_csv(output_filename, index=False)
