from flask import *
import boto3
import datetime
from model.model import BoardMsg

s3 = boto3.client(
    "s3",
    aws_access_key_id="AKIAUY7TTKFNVJXIU66I",
    aws_secret_access_key="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"
)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['JSON_SORT_KEYS'] = False 

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/api", methods=['POST'])
def leave_msg():
    message = request.form["text"]
    if "pic" not in request.files:
        BoardMsg.SaveMsg(message)
        # print("save msg")
        res = {"pic_src":""}
        return jsonify(res)
    else:
        file = request.files["pic"]
        file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        s3.upload_fileobj(file, "wehelpdima", file_name)
        BoardMsg.SaveMsg(message, file_name)
        # print("save msg and pic")
        res = {"pic_src":file_name}
        return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)