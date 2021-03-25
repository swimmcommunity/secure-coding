import os
import subprocess
import platform
from urllib.parse import urlparse, urljoin
from flask import Flask, render_template, escape, request, send_file, abort, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Swimm!'


@app.route("/hello")
def hello():
    name = request.args.get('name')
    return f'Hello {escape(name)}'


@app.route('/user/<name>')
def hello_name_template(name):
    return render_template('hello_user.html', title='Welcome', username=name)


def is_safe_path(basedir, path):
  return os.path.abspath(path).startswith(basedir)


def get_ping_number_of_attempts_flag():
    if platform.system() == 'Windows':
        return '-n'
    return '-c'


@app.route('/ping/<server>')
def ping(server):
    number_of_attempts_flag = get_ping_number_of_attempts_flag()
    args = ['ping', number_of_attempts_flag, '1', server]
    return subprocess.check_output(args, shell=False)


@app.route('/picture')
def get_picture():
    image_name = request.args.get('image_name')
    if not image_name:
        abort(404)
    
    base_dir = os.path.join(os.getcwd(), 'python', 'pictures')
    file_path = os.path.join(base_dir, image_name)

    if not is_safe_path(base_dir, file_path):
        abort(403)

    if not os.path.exists(file_path):
        abort(404)

    return send_file(file_path)

@app.route('/secure_link/<user_name>')
def secure_link(user_name):
    return render_template('secure_link.html', user_name=user_name)


@app.route('/link/<url>')
def link(url):
    return render_template('link.html', url=url)


@app.route('/redirect_me')
def redirect_me():
    url =  request.args.get('next')
    if not url:
        abort(404)
    if not is_safe_redirect_url(url):
        abort(401)
    return redirect(url)


def is_safe_redirect_url(target):
    """
    Based on https://security.openstack.org/guidelines/dg_avoid-unvalidated-redirects.html
    """
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return redirect_url.scheme in ('http', 'https') and host_url.netloc == redirect_url.netloc


if __name__ == '__main__':
    app.run()
