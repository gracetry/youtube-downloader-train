# from 引入檔名 import 函式名

# 使用 flask 框架
from flask import Flask, render_template, request, redirect, url_for
# 使用 pytube 套件
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    filename = request.args.get('filename')
    # url_for('static', filename='style.css')
    return render_template('index.html', filename=filename)

@app.route('/many')
def index_many():
    filename = request.args.get('filename')
    return render_template('index_many.html', filename=filename)

@app.route('/submit', methods=['POST'])
def post_submit():
    print('post_submit')
    url = request.form.get('url')
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution().download('./')
    filename = yt.title
    print(yt)
    print(yt.title)
    return redirect(url_for('index', filename=filename))

@app.route('/many_submit', methods=['POST'])
def post_many_submit():
    print('post_many_submit')
    filename_dict = dict()
    filename = dict()
    i = 0
    # request.form 是用字典 (key:value) 的方式取得資料
    urls = request.form.getlist('url[]')

    for key in urls :
        yt = YouTube(key)
        video = yt.streams.get_highest_resolution().download('./')
        filename_dict[i] = yt.title
        i += 1

    '''
    想要 {
            'title': {0: 'https://www.youtube.com/watch?v=m405naLWNuQ', 
                    1: 'https://www.youtube.com/watch?v=QuoEeSO22vU'}
        }
    
    通常會怎麼去處理比較好
    '''
    filename['title'] = filename_dict

    # for key in filename['title'] :
    #     print(filename['title'][key])
    return redirect(url_for('index', filename=filename))
    # return 'ok'

if __name__ == '__main__':
    app.run(debug=True)