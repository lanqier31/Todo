# -*-coding:utf-8-*-
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
from app.models.User import User
from app.models.Category import Category,Article
from app.models.Todo import Todo
import os ,json,sys
from app import app,db
from BeautifulSoup import BeautifulSoup
import HTMLParser
from datetime import date,timedelta
from sqlalchemy import extract
reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')


@app.route('/test')
def test():
    treeData = menuTree()
    articles = Article.query.all()
    users = User.query.all()
    for article in articles:
        htmlparser = HTMLParser.HTMLParser()
        article.body = htmlparser.unescape(article.body)
    categories= Category.query.all()
    return render_template('knowledge/test.html',treeData=treeData,articles=articles,users = users)


@app.route('/addarticle',methods={'POST'})
def addarticle():
    try:
        data = str(request.values)
        # print data
        parent_title = request.form.get('parent_title')
        level = request.form.get('level')
        title = request.form.get('title',"null")
        body = request.form.get('body')
        author = request.form.get('author')
        createtime = request.form.get('createtime')

        article = Article(title,body,author,createtime,level,parent_title)
        category = Category(name =title,level =level)
        db.session.add(article)
        db.session.add(category)
        db.session.commit()
        flash('New article was successfully posted')
        return redirect(url_for('test'))
    except IOError:
        print IOError


@app.route('/delete_article',methods={'POST'})
def delete_article():
    try:
        article_id = request.form.get('id')
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()

        return 'success'
    except IOError:
        return 'error'


@app.route('/edit_article',methods={'POST'})
def edit_article():
    try:
        article_id = request.form.get('pk')
        article = Article.query.get(article_id)
        print article
        return article
    except IOError:
        return 'error'

@app.route('/menuTree', methods=['GET', 'POST'])
def menuTree():
    data = []
    chs= []
    parents= Article.query.filter_by(level=1).all()   #查询所有的菜单项
    #列出每个菜单项对应的子功能
    for p in parents:
        da = {"text": p.title,"id": p.id,"href": '#'+str(p.id)}
        children = p.get_child(p.title)

        if children:
            for child in children:
                chs.append({"text": child['cname'],"id":child['cid'],"href": '#'+str(child['cid'])})
                da['nodes']=chs
            chs = []
        data.append(da)
        # print data
    return jsonify(data)

