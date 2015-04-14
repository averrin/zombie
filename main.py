# coding=utf8
from bottle import *
from dices import *
import random
import operator

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='.')

@route('/')
def index():
    res = '<title>Zombie Dice</title><link rel="stylesheet" href="/static/style.css">'
    dices = (
        request.query.red or 3, 
        request.query.yellow or 4, 
        request.query.green or 6
    )
    dices = list(map(int, dices))
    p_list = sorted(getStats(*dices).items(), key=lambda x: -float(x[1]))
    print(p_list)
    print(dices)
    _dices = []
    for i,d in enumerate(['red', 'yellow', 'green']):
        _dices.extend([d]*dices[i])
    pool = ', '.join(['<div class="dice shot %s"></div>' % d for d in _dices])
    res += '<div class="pool"><div class="label">in pool:</div>' + pool + '</div>'

    dices = (
        3 - int(request.query.red or 3), 
        4 - int(request.query.yellow or 4), 
        6 - int(request.query.green or 6)
    )
    _dices = []
    for i,d in enumerate(['red', 'yellow', 'green']):
        _dices.extend([d]*dices[i])
    pool = ', '.join(['<div class="dice brain %s"></div>' % d for d in _dices])
    print(pool)
    res += '<div class="table"><div class="label">on table:</div>' + pool + '<a href="/"><div class="dice clear"></div></a></div>'
    res += '<ul>'
    for dices, p in p_list:
        res += '<li>%s &mdash; <b>%s (%s%%)</b></li>' % (
            ', '.join(['<div class="dice %s %s"></div>' % (d, 
                {'shot': 'red', 'feet': 'yellow', 'brain': 'green'}[d]) for d in dices]), 
            p, round(float(p) * 100,2))
    res += '</ul>'
    res += """<script>
    function getQueryVariable(variable){
           var query = window.location.search.substring(1);
            var vars = query.split("&");
            for (var i=0;i<vars.length;i++) {
                    var pair = vars[i].split("=");
                    if(pair[0] == variable){return pair[1];}
            }
            return(false);
    }
     [].slice.call(document.querySelectorAll('.pool .dice')).forEach(function(e){
        e.addEventListener('click', function(){
          var q, q1;
          if(e.className.indexOf('red') !== -1){
            if(getQueryVariable('red')){
              var c = parseInt(getQueryVariable('red'));
              q1 = 'red=' + c;
              q = 'red=' + (c - 1);
              window.location = window.location.href.replace(q1, q);
            }else{
              q = 'red=2';
              if(window.location.href.indexOf('?') === -1){
              window.location = window.location + '?' + q;}else{
              window.location = window.location + '&' + q;
              }
            }
          }
         if(e.className.indexOf('yellow') !== -1){
            if(getQueryVariable('yellow')){
              var c = parseInt(getQueryVariable('yellow'));
              q1 = 'yellow=' + c;
              q = 'yellow=' + (c - 1);
              window.location = window.location.href.replace(q1, q);
            }else{
              q = 'yellow=3';
              if(window.location.href.indexOf('?') === -1){
              window.location = window.location + '?' + q;}else{
              window.location = window.location + '&' + q;
              }
            }
          }
            if(e.className.indexOf('green') !== -1){
            if(getQueryVariable('green')){
              var c = parseInt(getQueryVariable('green'));
              q1 = 'green=' + c;
              q = 'green=' + (c - 1);
              window.location = window.location.href.replace(q1, q);
            }else{
              q = 'green=5';
              if(window.location.href.indexOf('?') === -1){
              window.location = window.location + '?' + q;
              }else{
              window.location = window.location + '&' + q;
              }
            }
          }
        }, false);
     })
  </script>"""

    return res

run(port='80', reloader=True, host='0.0.0.0')
