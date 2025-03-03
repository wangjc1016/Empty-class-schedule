from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域访问

# 提供前端页面
@app.route('/')
def index():
    return render_template('index.html')

# 代理 ICS 文件的接口
@app.route('/proxy_ics', methods=['GET'])
def proxy_ics():
    ics_url = request.args.get('url')
    if not ics_url:
        return jsonify({"error": "No ICS URL provided"}), 400
    try:
        response = requests.get(ics_url, timeout=10)
        response.raise_for_status()
        return response.text, 200, {'Content-Type': 'text/calendar'}
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013, debug=True)