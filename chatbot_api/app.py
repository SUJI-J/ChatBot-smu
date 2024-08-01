from flask import Flask, request, jsonify, abort, render_template
import socket
import json

host = "127.0.0.1"
port = 5050

app = Flask(__name__)


def get_answer_from_engine(bottype, query):
    mySocket = socket.socket()
    mySocket.connect((host, port))

    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    mySocket.close()

    return ret_data


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        question = request.form
        print(question)
        answer = get_answer_from_engine(bottype='TEST', query=question['query'])
        print(answer)
        return render_template("result.html", send_question=question, send_answer=answer)
    # elif bot_type == 'QUICK':
    #     with open("/Users/uzald/PycharmProjects/ChatBot/chatbot_api/static/json/quick_reply.json","r",encoding="utf-8") as json_file:
    #         jdata = json.load(json_file)
    #     return jdata
    #


@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
    body = request.get_json()

    try:
        if bot_type == 'TEST':
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return json.dumps(ret, ensure_ascii=False)

        elif bot_type == "KAKAO":
            pass

        elif bot_type == "NAVER":
            pass

        else:
            abort(404)

    except Exception as ex:
        abort(500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
