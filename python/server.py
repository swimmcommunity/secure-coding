import os
import subprocess
from flask import Flask, render_template, escape, request, send_file, abort
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
        abort(404)
    
    base_dir = os.path.join(os.getcwd(), 'python', 'pictures')
    file_path = os.path.join(base_dir, image_name)

    if not os.path.exists(file_path):
        abort(404)
    if not is_safe_path(base_dir, file_path):
        abort(403)
    return send_file(file_path)

@app.route('/link/<user_name>')
def link(user_name):
    return render_template('link.html', user_name=user_name)


if __name__ == '__main__':
    app.run()
