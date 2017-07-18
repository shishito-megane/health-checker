# -*- coding:utf-8 -*-
# 健康かどうか判定するモジュール

def judge(sex,sum_hosu):
    """
    健康かどうか判定し，結果画像と結果文字列のソースを出力します．
    """
    lev = 0
    if(sex is "man"):
        if(sum_hosu < 8202):
            lev = 1
        elif(sum_hosu < 9200):
            lev = 2
        else:
            lev = 3
    elif(sex is "woman"):
        if(sum_hosu < 7282):
            lev = 1
        elif(sum_hosu < 8300):
            lev = 2
        else:
            lev = 3

    if(lev==1):
        lev_img = '<img src="/img/level3.jpg" width="300" alt="もう少し頑張ろう。"></img>'
        lev_msg = '<p><Center>もう少し頑張りましょう(T_T)</Center></p>'
    elif(lev==2):
        lev_img = '<img src="/img/level2.jpg" width="300" alt="まぁまぁだね〜"></img>'
        lev_msg = '<p><Center>まあまあですね(・_・)</Center></p>'
    else:
        lev_img = '<img src="/img/level1.jpg" width="300" alt="頑張りました！"></img>'
        lev_msg = '<p><Center>あなたは健康です!(^^)!</Center></p>'

    return lev, lev_img, lev_msg
