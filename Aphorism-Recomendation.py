# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Sariyer Academy Research and Production focused AI Education Examination
#

# The project idea is creating a simple recomendation engine based of user single answer.
#
#
#
#  

# ### Introduction

# * [Preperation of the Data](#Preperations)
#     * [Manipulation and Storing the sentences](#Manipulation-Data)
#     
#          Create list of setences from example and make a category list from all example sentences

# * [Using Algoritms and functions](#Algorithm)
#       Checking the user answer and If the user had answer only a single word then should recomend a random                     sentence from same category. If the user answers a long sentence then we should use the Jaccard Similarity 
# * [Result](#Result) 
#
#
#  

import pandas as pd
import numpy as np
import random
import re

import warnings
warnings.filterwarnings('ignore')

pd.options.display.max_colwidth = 300

# ### Preperations

# We have Five different category of aphorism from Turkish language that "Hayat"(Life), "Sevgi"(Love), "Gayret"(Assiduity), "Umut"(Hope) and "Idare"(Management)

Hayat = """
Olumlu düşünen, bütün olası dünyaların en iyisinde yaşadığımızı söyler ve olumsuz düşünen, bunun gerçek olmasından korkar. James Cabell

Bu dünyaya gelmenin sadece tek bir yolu vardır, terk etmenin ise çok fazla yolu. Donald Harington

Birisinin ‘Hayat zor.’ diye yakındığını duyduğumda, her zaman, ‘Neye kıyasla?’ diye sormayı isterim. Sidney Harris

Mutsuz olmamamız gerekir. Kimsenin hayatla bir kontratı yok. DavidHeath

Hayatını kazanırken yaşamasını bilmeyen bir adam, servetini kazanmadan öncesine göre daha fakirdir. Josiah Holland

Yarının ne olacağını sormaktan vazgeç. Her gün, sana verilen bir hazinedir. Eline geçtikçe değerlendir. Horace

Hayatınızı yaşamanın en iyi yolu, sizden sonra da kalıcı olacak şeyler için harcamaktır. William James

Biz Japonlar, küçük zevklerden hoşlanırız, israftan değil. Daha fazlasını karşılayabilirse de, insanın basit bir yaşam tarzı olması kanısındayım. Massaru Ibuka

Benim sanatım ve mesleğim yaşamaktır. Montaigne

Hayat, çikolata ile dolu bir kutu gibidir. Ne çıkacağını asla bilemezsiniz. Forrest Gump Filmi

Hayat, büyük bir sürprizdir. Ölümün neden daha büyük bir sürpriz olması gerektiğini anlayamıyorum. Vladimir Nabokov
"""

Sevgi = """
Karım,  benim  ‘Seni seviyorum.’  dememi binlerce kez duydu ama, hiçbir zaman ‘Üzgünüm.’ dediğimi duymadı. Bruce Willis

Büyüklerine saygı, küçüklerine şevkat göstermeyenler, bizden değildir. Hz, Muhammed

Sevip de kaybetmek, sevmemiş olmaktan daha iyidir. Seneca

Sevgiyle düşünün, sevgiyle konuşun, sevgiyle davranın. Her ihtiyaç karşılanacaktır. James Ailen

Sevgi, insanı birliğe, bencillik ise yalnızlığa götürür. Schiller

Sevdiği kadını ve sevdiği işi bulan bir erkek, yeryüzünde cenneti bulmuş demektir. Helen Rowland

Kızgınlık, kırgınlık ya da acıya tutunmayın. Enerjinizi çalarlar ve sizi sevmekten alıkoyarlar. Leo Buscaglia

Herkes temel bir şeyi unutuyor; insanlar sizi, siz onları sevmeden sevmeyecekler. Pat Carroll

Sevgi, dünyadaki yaşamın aktığı nehirdir. Henry Beecher

Sevmeden verebilirsiniz ama, vermeden sevemezsiniz. Amy Carmichael

"""

Gayret = """
Dileyin verilecektir; arayın bulacaksınız; kapıyı çalın size açılacaktır.    Hz.İsa (a.s.)

Damlayan su, mermeri, yürüyen de dağları deler. Ovidius

Hazine, eziyet çekene gözükür.    Hz. Mevlâna

Beklenen gün gelecekse, çekilen çile kutsaldır.V. Hugo

Yarınlar yorgun ve bezgin kimseler değil, rahatını terk edebilen gayretli insanlara aittir. Cicero

Emek olmadan, yemek olmaz.    Atasözü

Kötülüğün hakim olmaması için tek şart, iyilerin gayret göstermeleridir. Kelâmı Kibar

İnsan bir şeyi çok ciddi olarak arzu etmeye görsün; hiçbir şey erişilemeyecek kadar yükseklerde değildir. H. Andersen

Ümitsizlik ve korkaklık, çalışma azminden yoksun insanlara göredir.  A. Mourois

Bir çığlık, bir çığ meydana getirir.  Soljenitsin

Kıramıyacağm zinciri, hiç olmazsa kemir. C. Şehabettin

Basit bir insanın elinden geleni yapması; bilgili ve zeki bir insanın tembelliğinden çok daha değerlidir.

Taşı delen, suyun kuvveti değil; dalgaların sürekliliğidir.

Damlayan su, taşı deler. Ovidius
"""

Umut = """
Başlangıçta fazla umut ederiz ama, sonrasında yeteri kadar değil. Joesph Roux

Hayatta umutsuz durumlar yoktur,  sadece umutsuzluk besleyen insanlar vardır. Booth

Şafaktan önce her yer karanlıktır. Katherine Mansfield

Umut, gözle görülemeyeni görür, elle tutulamayanı hisseder ve imkansızı başarır. Anonim

Büyük umutlar, büyük adamlar yaratır. Thomas Fuller

Umut, fakirin ekmeğidir. Thales Miletus

Kazanmayı umut etmeyen, daha baştan kaybetmiştir. Jose Olmedo

Umut etmeyen, hiçbir zaman umutsuzluğa kapılmaz. George Bernard Shaw

Hiçbir kış, sonsuza kadar sürmez. Hal Borland

Umut, şüphe etmek daha kolayken, inanmaya devam etmektir. Anonim

Umut, mutluluktan alınmış bir miktar borçtur. Joseph İoubert
"""

Idare = """
Çok söyleyen değil, çok iş yapan yöneticiye muhtaçsınız. Hz. Ömer (r.a.)

Sevginin kurduğu devleti, adalet devam ettirir. Farabi

Her memleketin hakettiği bir hükümeti vardır. J. Maistere

Hükümetlerin en kötüsü, suçsuzu korkutandır.

Kendinizi yönetirken kafanızı, başkalarını yönetirken kalbinizi kullanın.

Evi ev eden avrat, yurdu şen eden devlet. Atasözü

Mal cimrilerde, silah korkanlarda, idare de zayıflarda olursa, işler bozulur. Hz. Ebubekir

İnsanlar üç sınıftır: İdareciler, din alimleri ve halk. İdareciler bozulunca, geçim; alimler bozulunca, din; halk bozulunca da hak bozulur. Ebu Bekir Verrak

Kendini yönet, dünyayı yönetecek gücü bulabilirsin. Plato

Kötü idarecilerin başarısı, halkın ıstırabıdır.

Bir memlekette ayaklar baş olursa, başlar ayaklar altında mahvolur.

"""

# We need to add all list a single list and create each category names 
categories = [Hayat,Sevgi,Gayret,Umut,Idare]
categories_name = ["Hayat", "Sevgi","Gayret","Umut","Idare"]

# ### Manipulation-Data

# Split each row with new line (\n) 
for i in range(len(categories)):
    categories[i] = categories[i].split("\n")
    

# Create a dataframe
df = []
df = pd.DataFrame(df, columns=['sentence','category'])


# +
# Add each sentence to Dataframe (df) with the category names
for i in range(len(categories_name)):
    for k in range(len(categories[i])):
        df = df.append({'sentence': categories[i][k], 'category': categories_name[i]}, ignore_index=True)
    
    df = df[df['sentence']!=""]
    df.reset_index(drop=True, inplace=True)
    
  

# +
df["cleaned"]=df['sentence'].copy()

for i in range(len(df)):
    df["cleaned"][i] = re.sub('[!@#’‘?.,\'$]', '', df["cleaned"][i])
    df["cleaned"][i] = df["cleaned"][i].lower()
   
# -

# ### Algorithm

# +

def give_a_recomendation():
    result = []
    answer = input("Hi Human, What do you want? ")
    # We need to turn lowercase  user answer for correct proportions
    answer=answer.lower()
  
 
 # One of the main reques is If not a word use Jaccard similarity. 
 # We count user answer words and if it is more than one word and use Jaccard similarity
 
    if len(answer.split())>1:
        # Jaccard Similarity
        for i in range(len(df)):
            # Jaccard similarity
            a = set(df["cleaned"][i].split()) 
            b = set(answer.split())
            c = a.intersection(b)
            result.append(float(len(c)) / (len(a) + len(b) - len(c)))
        # We add all result in a new column that we can find any of result    
        pd.DataFrame(result)   
        df['result'] = result
        # Return as max result row sentence 
        return df[df['result']==df['result'].max()].values[0][0]

#    The second request is If User type a single word and the word is the same the category name 
#   and we will find a random word in the category
    
#    If only one word but not the same any category name then we can choose any random sentence in our data

    else:
        for i in categories_name:
            i=i.lower()
            if(i==answer):
                return df["sentence"][df["category"].str.lower()==answer].sample(n=1).values[0]
        return df["sentence"].sample(n=1).values[0]
        
# -

# ### Result

# Summary of the final dataframe 

df.head()
#
#  

# <p>The project is a small daily challenge project from <a href="https://www.linkedin.com/in/uzay-çetin-b1a9ab100/">Uzay Cetin</a>
# and his team. </p>
# <p>
# The project idea is to recommend an aphorism after Users input with using the Jaccard similarity and also the same category randomisation.
#
# The first step was cleaning and preparing the data for the programme.
# Then the programme checks user input as a sentence or a single word to recommend an aphorism.
# </p>
#
# Stored the same sentences with removing symbols and makes lowercase for increasing similarity between user input and display the original sentence.
#
#
#
#
#  

# <div class="alert alert-success" role="alert">
#   Tell me something
# </div>
#

# +
give_a_recomendation()


# -




