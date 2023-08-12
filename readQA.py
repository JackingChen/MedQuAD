#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 09:58:30 2023

@author: jack
"""
import xml.etree.ElementTree as ET
import glob
import pandas as pd
files=glob.glob("./*/*.xml")
defaultCols=["Question","Answer"]
def RetreiveQAPair(xml_file_path):
    # 从文件中读取XML数据
    # xml_file_path = './10_MPlus_ADAM_QA/0003402.xml'
    with open(xml_file_path, "r", encoding="utf-8") as xml_file:
        xml_data = xml_file.read()
    
    # 解析XML数据
    root = ET.fromstring(xml_data)
    
    # 提取文档的属性信息
    document_id = root.get("id")
    document_source = root.get("source")
    document_url = root.get("url")
    
    print("Document ID:", document_id)
    print("Document Source:", document_source)
    print("Document URL:", document_url)

    
    # 提取问题和答案对(QAPairs)
    qapairs = root.findall("QAPairs/QAPair")
    
    df_data=pd.DataFrame(columns=defaultCols)
    for i,qapair in enumerate(qapairs):
        question = qapair.find("Question").text
        answer = qapair.find("Answer").text
        df_data.loc[i]=[question,answer]
    return df_data

df=pd.DataFrame([],columns=defaultCols)
for file in files:
    QestionType, Qidx=file[-2:]
    QAindex=f"{QestionType}__{Qidx}"
    df_data=RetreiveQAPair(file)
    df_data['QAindex']=QAindex
    df=pd.concat([df,df_data],ignore_index=True)

# df=
#                                                 Question  ... QAindex
# 0             What is (are) Injury - kidney and ureter ?  ...    m__l
# 1               What causes Injury - kidney and ureter ?  ...    m__l
# 2      What are the symptoms of Injury - kidney and u...  ...    m__l
# 3           How to diagnose Injury - kidney and ureter ?  ...    m__l
# 4      What are the treatments for Injury - kidney an...  ...    m__l
#                                                  ...  ...     ...
# 47436               What is (are) Diabetic Retinopathy ?  ...    m__l
# 47437  What are the treatments for Diabetic Retinopat...  ...    m__l
# 47438  what research (or clinical trials) is being do...  ...    m__l
# 47439              What to do for Diabetic Retinopathy ?  ...    m__l
# 47440               What is (are) Diabetic Retinopathy ?  ...    m__l

# [47441 rows x 3 columns]