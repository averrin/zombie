# coding=utf8
from bottle import *
from dices import *
import random

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='.')

@route('/')
def index():
	dices = (
		request.query.red or 3, 
		request.query.yellow or 4, 
		request.query.green or 6
	)
	print(dices)
	p_list = getStats(*map(int, dices))
	_dices = (
		3 - int(request.query.red or 0), 
		4 - int(request.query.yellow or 0), 
		6 - int(request.query.green or 0)
	)
	dices = []
	for i,d in enumerate(['red', 'yellow', 'green']):
		dices.extend([d]*_dices[i])
	pool = ', '.join(['<div class="dice brain %s"></div>' % d for d in dices])
	print(pool)
	res = '<link rel="stylesheet" href="/static/style.css">' + pool
	res += '<ul>'
	for dices, p in p_list.items():
		res += '<li>%s &mdash; <b>%s</b></li>' % (', '.join(['<div class="dice %s %s"></div>' % (d, random.choice(['red','yellow','green'])) for d in dices]), p)
	res += '</ul>'
	return res

run(port='8888', reloader=True, host='0.0.0.0')