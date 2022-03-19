#!/usr/bin/env python
from flask import Flask, render_template, url_for, flash, redirect, request
from turbo_flask import Turbo

from forms import RegistrationForm, LoginForm, Board

from sys import path; path.insert(1, '/home/nls/py/pytools')
from nls_util import notify
from sys import path; path.insert(1, '/home/nls/py/pytools/mpvd')
from mpvd import MpvCtrl

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
turbo = Turbo(app)
usr = MpvCtrl()

@app.context_processor
def inject_loadavg():
  try:
    return {
        "bat": usr.get_battery(),
        "counter": usr.get_counter(),
        "is_auth": "yes" if usr.is_auth() else "no",
        }
  except BrokenPipeError:
    return {
        "bat":"N/A",
        "counter":"N/A",
        "is_auth":"N/A",
        }

@app.context_processor
def inject_mpv_info():
  return {
    "get_player_status":usr.mpv.get_player_status(),
    "counter":usr.get_counter(),
    "playing":not usr.mpv.core_idle,
  }

@app.context_processor
def inject_battery_info():
  from pandas import read_csv
  from json import dumps
  from plotly import utils
  from plotly.express import line, scatter
  import plotly.graph_objects as go
  df = read_csv("/tmp/batd.csv", names=["date", "bat", "bat_plugged", "cpu", "mem"]) #, parse_dates=True)
  bat_line_graph = line(df, x='date', y='bat', color="bat_plugged")#, color="charching")
  cpu_line_graph = line(df, x='date', y='cpu', color="bat_plugged")
  mem_line_graph = line(df, x='date', y='mem', color="bat_plugged")
  cpu_figure = go.Figure(data=[go.Mesh3d(x=df["date"], y=df["bat"], z=df["cpu"])],
    layout=go.Layout(height=800))
  mem_figure = go.Figure(data=[go.Mesh3d(x=df["date"], y=df["bat"], z=df["mem"])],
    layout=go.Layout(height=800))
  return {
      "bat_line_graph":dumps(bat_line_graph, cls=utils.PlotlyJSONEncoder), 
      "cpu_line_graph":dumps(cpu_line_graph, cls=utils.PlotlyJSONEncoder), 
      "mem_line_graph":dumps(mem_line_graph, cls=utils.PlotlyJSONEncoder), 
      "cpu_figure":dumps(cpu_figure, cls=utils.PlotlyJSONEncoder), 
      "mem_figure":dumps(mem_figure, cls=utils.PlotlyJSONEncoder), 
      }

@app.route("/")
def root():
  return redirect(url_for("board"))

PLAYLIST = {
    "LofiHiphop": "https://www.youtube.com/watch?v=5qap5aO4i9A"
    }

@app.route("/board", methods=['GET', 'POST'])
def board():
  form = Board()
  info = "hallo dynamic content"
  if not usr.is_auth():
    flash('not authenticated', 'danger')
  else:
    flash('authenticated', 'success')
  if form.validate_on_submit():
    if form.str_field.data != "":
      pass
      # usr.play(form.str_field.data)
    notify("form submited!", f"{form.str_field.data=}\n{form.bool_field.data=}")
  if request.method == 'POST':
    if request.form.get('toggle_btn'):
      try:
        usr.mpv.toggle()
      except BrokenPipeError:
        flash(f"Mpv not running", "danger")
        notify("Error","mpv probably not running")
      notify("I'm toggling")
    elif request.form.get('action2'):
      notify("action2")
    else:
      notify("unknown")
  return render_template('board.html', title='Board', form=form, info=info)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('board'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      usr.authenticate()
      return redirect(url_for('board'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)

@app.route('/plot')
def notdash():
  return render_template('battery_plot.html')


def update_load():
  from time import sleep
  with app.app_context():
    while True:
      sleep(1)
      turbo.push([turbo.replace(render_template('loadavg.html'), 'load'),
                  turbo.replace(render_template("battery_plot.html"), "load_battery_info"),
                  turbo.replace(render_template("dyn_board.html"), "load_board")
          ])

@app.before_first_request
def before_first_request():
  from threading import Thread
  Thread(target=update_load).start()

if __name__ == '__main__':
  app.run(host="192.168.43.66", debug=True)

