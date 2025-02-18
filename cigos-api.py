from flask import Flask, request
app = Flask(__name__)
@app.route("/endpoint", methods=["POST"])
def receive_file():
    if "file" not in request.files:
        return "No file uploaded", 400
    file = request.files["file"]
    file_content = file.read().decode("utf-8")
    print("Received data:")
    print(file_content)
    return "Data received and displayed successfully", 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)