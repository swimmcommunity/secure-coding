import os
import subprocess
from flask import Flask, render_template, escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Swimm!'


@app.route("/hello/<name>")
def hello():
    name = request.args.get('name')
    return f'Hello {escape(name)}'


@app.route('/user/<name>')
def hello_name_template(name):
    return render_template('hello_user.html', title='Welcome', username=name)


def is_safe_path(basedir, path):
  return os.path.abspath(path).startswith(basedir)


@app.route('/ping/<server>')
def ping(server):
    args = ['ping', '-n', '1', server]
    return subprocess.check_output(args, shell=False)


@app.route('/picture')
def get_picture():
    image_name = request.args.get('image_name')
    if not image_name:
        return 404
    if not is_safe_path(os.getcwd(), path):
        return 401
    return send_file(os.path.join(os.getcwd(), image_name))

@app.route('/link/<url>')
def link(url):
    return render_template('link.html', url=url)


if __name__ == '__main__':
    app.run()
