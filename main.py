from flask import Flask, render_template, request
from flask_devices import Devices

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TEMPLATE_FOLDER'] = 'templates'
devices = Devices(app)
devices.add_pattern('mobile', 'iPhone|iPod|Android.*Mobile|Windows.*Phone|dream|blackberry|CUPCAKE|webOS|incognito|webmate', 'templates')
devices.add_pattern('tablet', 'iPad|Android', 'templates')
devices.add_pattern('hoge', 'hoge', 'templates')
devices.add_pattern('pc', '.*', 'templates')

@app.route("/", methods=['GET', 'POST'])
def index():
  print(request.DEVICE) # mobile, tablet, hoge, pc
  if request.DEVICE == 'mobile':
    return render_template('mobile.html')
  else:
    return render_template('index2.html')
    
if __name__ == '__main__':
  app.run()
