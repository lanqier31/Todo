# -*-coding:utf-8-*-
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g,jsonify
# from app.models.Roles import Role,User
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
    articles = Article.query.all()
    for article in articles:
        htmlparser = HTMLParser.HTMLParser()
        article.body = htmlparser.unescape(article.body)
    categories= Category.query.all()
    return render_template('knowledge/test.html',categories=categories,articles=articles)


@app.route('/addarticle',methods={'POST'})
def addarticle():
    try:
        data = str(request.values)
        # print data
        category = request.form.get('category')
        title = request.form.get('title',"null")
        body = request.form.get('body')
        author = request.form.get('author')
        createtime = request.form.get('createtime')

        article = Article(category,title,body,author,createtime)
        db.session.add(article)
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


