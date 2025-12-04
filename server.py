import os
import bottle
from bottle import route, run, template
import markdown

# 1. 正确读取环境变量，为Azure部署做好准备
# Azure应用服务会通过环境变量 PORT 提供端口号
host = os.getenv('HOST', '0.0.0.0')  # 监听所有网络接口
port = int(os.getenv('PORT', 8000))  # 默认使用8000端口

app = bottle.Bottle()

@app.route('/')
def home():
    try:
        # 2. 使用正确的变量名，并添加异常处理
        with open('README.md', 'r', encoding='utf-8') as fp:
            md_content = fp.read()
        html_content = markdown.markdown(md_content)
        return html_content
    except FileNotFoundError:
        return "<h1>README.md 文件未找到</h1>"
    except Exception as e:
        return f"<h1>读取文件时出错</h1><p>{str(e)}</p>"

# 3. 在生产环境中，不应使用 bottle 自带的开发服务器
# 此处为测试，我们启动它
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)