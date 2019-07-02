import io
import flask
import qrcode

app = flask.Flask(__name__)

#第二种方法，以post的方式传递数据
@app.route('/')
def home():
    return flask.render_template('qr_tool.html')
@app.route('/qr')
def qr():
    #获取要生成二维码图像的数据
    data = flask.request.args.get("data")

    bi=io.BytesIO() #创建一个BytesIO对象，用于在内存中存储二维码图像数据
    img = qrcode.make(data)
    img.save(bi,"png") #调用img对象的save方法将二维码图像数据以png的编码格式写入bi对象管理的内存空间
    bi.seek(0) #将bi对象内部的位置指针移动到图像数据的起始位置
    
    #返回二维码图像数据
    return flask.send_file(bi,"image/png")

if __name__ ==("__main__"):
    app.run(debug = True)