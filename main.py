
from flask import Flask, json, render_template, request, jsonify
from math import ceil
from PIL import Image

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=("GET",))
def index():
    return render_template('index.html')


@app.route('/generate', methods=("POST",))
def generator():
    if len(request.files) == 0:
        return jsonify({"msg": "Image is required!", "error": True, "data": None}), 400

    try:
        chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        mode = 25
        new_width = 150

        if "chars" in request.form:
            chars = list(str(request.form["chars"]).replace(" ", ""))
            mode = ceil(255/len(chars))

        if "width" in request.form:
            new_width = int(request.form["width"])

        print("chars", chars, type(chars))
        print("mode", mode, type(mode))
        print("new_window", new_width, type(new_width))

        image = Image.open(request.files["image"])
        width, height = image.size
        ratio = height/width
        new_height = int(new_width * ratio)
        # resizing
        image = image.resize((new_width, new_height))
        # grayscale
        image = image.convert("L")
        pixels = image.getdata()
        coverted_img = "".join([chars[pixel//mode] for pixel in pixels])

        return jsonify({
            "msg": "Image succesfully converted ASCII Art!",
            "error": False,
            "data": "\n".join(
                [coverted_img[index:(index+new_width)] for index in range(0, len(coverted_img), new_width)]
            )
        }), 201
    except Exception as ex:
        print(ex)
        return jsonify({"msg": "Something went wrong.. Please try again!", "error": True, "data": None}), 500


if __name__ == "__main__":
    app.run(debug=True)
