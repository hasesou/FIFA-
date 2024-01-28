from flaskr import app
from flask import render_template,request
import pandas as pandas
import numpy as numpy
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import pathlib as pathlib
import io as io
import csv as csv
from wtforms import Form
from wtforms.fields import (
    StringField, IntegerField, SubmitField
)
import seaborn as sns

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads',methods=['GET','POST'])
def graph():
    file = request.files["the_file"]
    if not file:
        return 'ファイルアップロードされてません'
    if file.filename.endswith('.csv'):
    #CSVファイルを読み込む
        df = pandas.read_csv(file,encoding = 'UTF8')
        #列を取得する
        #国別での選手数トップ10を抽出
        #Nationalityで国籍の列を取り出す
        Nationality = df['Nationality']
    #それぞれの要素数をカウントする
        countries = list(Nationality.value_counts(sort=True).to_dict().keys())[:10]
        #国ごとのTOP10が抽出
        numbers = Nationality.value_counts(sort=True).to_list()[:10]

        x = numpy.array(countries)
        y = numpy.array(numbers)

    #国別での選手数トップ10グラフの抽出
    plt.figure(figsize=(10, 10),facecolor = 'lightblue')
    plt.bar(x,y)
    plt.title('Affiliation Players')
    a = plt.show()
    #df.plot()
    return render_template("graph.html",a=a)

@app.route('/uploads2',methods=['GET','POST'])
def graph2():
    file = request.files["the_file"]
    if not file:
        return 'ファイルアップロードされてません'
    if file.filename.endswith('.csv'):
    #CSVファイルを読み込む
        df = pandas.read_csv(file,encoding = 'UTF8')
        #列を取得する
        #21歳以下の若手でポテンシャルが75以上選手をを抱えている国トップ10
        young_players = df.query('Age >= 21 & Potential <= 75')
        #Nationalityで国籍の列を取り出す
        Nationality = young_players['Nationality']
    #それぞれの要素数をカウントする
        countries = list(Nationality.value_counts(sort=True).to_dict().keys())[:10]
        #国ごとのTOP10が抽出
        numbers = Nationality.value_counts(sort=True).to_list()[:10]

        x = numpy.array(countries)
        y = numpy.array(numbers)

    #国別での選手数トップ10グラフの抽出
    plt.figure(figsize=(10, 10),facecolor = 'lightblue')
    plt.bar(x,y)
    plt.title('Young_players')
    b = plt.show()
    #df.plot()
    return render_template("graph2.html",b=b)

@app.route('/uploads3',methods=['GET','POST'])
def eleven():
    file = request.files["the_file"]
    if not file:
        return 'ファイルアップロードされてません'
    if file.filename.endswith('.csv'):
        #CSVファイルを読み込む
        df = pandas.read_csv(file,encoding = 'UTF8').astype(str)
        #GKを選出する
        #入力した内容のデータを取得
        a = 'GK'
        #a2 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven = df[(df['Nationality'] == name) & (df['Position'] == a) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven2 = df[(df['Nationality'] == name) & (df['Position'] == a2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name = Besteleven[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries = list(Name.value_counts(sort=True).to_dict().keys())[:1]
        
        #右サイドバックを選出する
        #入力した内容のデータを取得
        b = 'RB'
        #b2 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven3 = df[(df['Nationality'] == name) & (df['Position'] == b) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven4 = df[(df['Nationality'] == name) & (df['Position'] == b2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name2 = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name2 = Besteleven3[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries2 = list(Name2.value_counts(sort=True).to_dict().keys())[:1]
        
        #右センターバックを選出する
        #入力した内容のデータを取得
        c = 'RCB'
        #c2 ='SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven5 = df[(df['Nationality'] == name) & (df['Position'] == c) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven6 = df[(df['Nationality'] == name) & (df['Position'] == c2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name3 = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name3 = Besteleven5[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries3 = list(Name3.value_counts(sort=True).to_dict().keys())[:1]
        
        #左センターバックを選出する
        #入力した内容のデータを取得
        d = 'LCB'
        #d2 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven7 = df[(df['Nationality'] == name) & (df['Position'] == d) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven8 = df[(df['Nationality'] == name) & (df['Position'] == d2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name4 = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name4 = Besteleven7[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries4 = list(Name4.value_counts(sort=True).to_dict().keys())[:1]
        
        #左サイドバックを選出する
        #入力した内容のデータを取得
        e = 'LB'
        #e2 ='SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven9 = df[(df['Nationality'] == name) & (df['Position'] == e) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven10 = df[(df['Nationality'] == name) & (df['Position'] == e2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name5 = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name5 = Besteleven9[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries5 = list(Name5.value_counts(sort=True).to_dict().keys())[:1]
        
        #右ボランチを選出する
        #入力した内容のデータを取得
        f = 'RCM'
        f2 = 'RDM'
        f3 = 'CDM'
        #f4 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven11 = df[(df['Nationality'] == name) & (df['Position'] == f) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        Besteleven12 = df[(df['Nationality'] == name) & (df['Position'] == f2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        Besteleven13 = df[(df['Nationality'] == name) & (df['Position'] == f3) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven14 = df[(df['Nationality'] == name) & (df['Position'] == f4) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name6 = Besteleven[['Name','Club','Overall','Potential','Age']]
        if file in Besteleven11:
            Name6 = Besteleven11[['Name','Club','Overall','Potential','Age']]
        elif file in Besteleven12:
            Name6 = Besteleven12[['Name','Club','Overall','Potential','Age']]
        else: Name6 = Besteleven13[['Name','Club','Overall','Potential','Age']]
        
        Name6 = Besteleven11[['Name','Club','Overall','Potential','Age']]
        Name6 = Besteleven12[['Name','Club','Overall','Potential','Age']]
        Name6 = Besteleven13[['Name','Club','Overall','Potential','Age']]
        #elif file not in Besteleven13:
            #Name6 = Besteleven14[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries6 = list(Name6.value_counts(sort=True).to_dict().keys())[:1]
        
        #左ボランチを選出する
        #入力した内容のデータを取得
        g = 'LCM'
        g2 ='LDM'
        #g3 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven14 = df[(df['Nationality'] == name) & (df['Position'] == g) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        Besteleven15 = df[(df['Nationality'] == name) & (df['Position'] == g2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven16 = df[(df['Nationality'] == name) & (df['Position'] == g3) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name7 = Besteleven[['Name','Club','Overall','Potential','Age']]
        if file in Besteleven14:
            Name7 = Besteleven14[['Name','Club','Overall','Potential','Age']]
        elif file in Besteleven15:
            Name7 = Besteleven15[['Name','Club','Overall','Potential','Age']]
        
        Name7 = Besteleven14[['Name','Club','Overall','Potential','Age']]
        Name7 = Besteleven15[['Name','Club','Overall','Potential','Age']]
        #elif file not in Besteleven15:
            #Name7 = Besteleven16[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries7 = list(Name7.value_counts(sort=True).to_dict().keys())[:1]
        
        #右サイドを選出する
        #入力した内容のデータを取得
        h = 'RM'
        h2 = 'RW'
        #h3 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven17 = df[(df['Nationality'] == name) & (df['Position'] == h) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        Besteleven18 = df[(df['Nationality'] == name) & (df['Position'] == h2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven19 = df[(df['Nationality'] == name) & (df['Position'] == h3) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name8 = Besteleven[['Name','Club','Overall','Potential','Age']]
        if file in Besteleven17:
            Name8 = Besteleven17[['Name','Club','Overall','Potential','Age']]
        elif file in Besteleven18:
            Name8 = Besteleven18[['Name','Club','Overall','Potential','Age']]
        #elif file not in Besteleven18:
        Name8 = Besteleven17[['Name','Club','Overall','Potential','Age']]
        Name8 = Besteleven18[['Name','Club','Overall','Potential','Age']]
            #Name8 = Besteleven19[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries8 = list(Name8.value_counts(sort=True).to_dict().keys())[:1]
        
        #トップ下を選出する
        #入力した内容のデータを取得
        i = 'CAM'
        #i2 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven20 = df[(df['Nationality'] == name) & (df['Position'] == i) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven21 = df[(df['Nationality'] == name) & (df['Position'] == i2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name9 = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name9 = Besteleven20[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries9 = list(Name9.value_counts(sort=True).to_dict().keys())[:1]
        
        #左サイドを選出する
        #入力した内容のデータを取得
        j = 'LM'
        j2 = 'LW'
        #j3 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven22 = df[(df['Nationality'] == name) & (df['Position'] == j) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        Besteleven23 = df[(df['Nationality'] == name) & (df['Position'] == j2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven24 = df[(df['Nationality'] == name) & (df['Position'] == j3) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name10 = Besteleven[['Name','Club','Overall','Potential','Age']]
        if file in Besteleven22:
            Name10 = Besteleven22[['Name','Club','Overall','Potential','Age']]
        elif file in Besteleven23:
            Name10 = Besteleven23[['Name','Club','Overall','Potential','Age']]
        #elif file not in Besteleven23:
            #Name10 = Besteleven24[['Name','Club','Overall','Potential','Age']]
        #Name10 = Besteleven23[['Name','Club','Overall','Potential','Age']]
        #elif file not in Besteleven23:
        Name10 = Besteleven22[['Name','Club','Overall','Potential','Age']]
        Name10 = Besteleven23[['Name','Club','Overall','Potential','Age']]
        #else: Name10 = Besteleven23[['Name','Club','Overall','Potential','Age','Position']]
        #elif file not in Besteleven23:
            #Name10 = Besteleven24[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries10 = list(Name10.value_counts(sort=True).to_dict().keys())[:1]
        
        #フォワードを選出する
        #入力した内容のデータを取得
        k = 'ST'
        #k2 = 'SUB'
        name = request.form.get('sel')
        name2 = request.form.get('sel2')
        name3 = request.form.get('sel3')
        name4 = request.form.get('sel4')
        name5 = request.form.get('sel5')
        Besteleven25 = df[(df['Nationality'] == name) & (df['Position'] == k) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Besteleven26 = df[(df['Nationality'] == name) & (df['Position'] == k2) & (df['Overall'] >= name2) & (df['Age'] >= name3) & (df['Age'] <= name4) & (df['Potential'] >= name5)]
        #Name11 = Besteleven[['Name','Club','Overall','Potential','Age']]
        Name11 = Besteleven25[['Name','Club','Overall','Potential','Age']]
        #それぞれの要素数をカウントする
        countries11 = list(Name11.value_counts(sort=True).to_dict().keys())[:1]
        
        return render_template('eleven.html',
        countries=countries,
        countries2=countries2,
        countries3=countries3,
        countries4=countries4,
        countries5=countries5,
        countries6=countries6,
        countries7=countries7,
        countries8=countries8,
        countries9=countries9,
        countries10=countries10,
        countries11=countries11) 
        
if __name__ == '__main__':
    app.run(debug=True)