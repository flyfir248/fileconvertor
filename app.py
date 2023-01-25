from flask import Flask, request, Response, render_template
import io
from PIL import Image

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/jpgtopng.html", methods=["GET"])
def jpgtopng():
    return render_template("jpgtopng.html")


@app.route("/pngtojpg.html", methods=["GET"])
def pngtojpg():
    return render_template("pngtojpg.html")


@app.route("/webtopng.html", methods=["GET"])
def webtopng():
    return render_template("webtopng.html")


@app.route("/bmptopng.html", methods=["GET"])
def bmptopng():
    return render_template("bmptopng.html")


@app.route("/pngtopdf.html", methods=["GET"])
def pngtopdf():
    return render_template("pngtopdf.html")


@app.route("/api/jpgtopng", methods=["POST"])
def jpg_to_png():
    image = request.files.get('image')
    image_bytes = image.read()
    im = Image.open(io.BytesIO(image_bytes))
    im = im.convert("RGB")
    # create BytesIO object
    img_buffer = io.BytesIO()
    # save image to the buffer using PNG format
    im.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    return Response(img_buffer, content_type="image/png",
                    headers={'Content-Disposition': 'attachment; filename=image.png'})


@app.route("/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    image = request.files.get('image')
    image_bytes = image.read()
    im = Image.open(io.BytesIO(image_bytes))
    # create BytesIO object
    img_buffer = io.BytesIO()
    # save image to the buffer using JPG format
    im.save(img_buffer, format='JPEG')
    img_buffer.seek(0)
    return Response(img_buffer, content_type="image/jpeg",
                    headers={'Content-Disposition': 'attachment; filename=image.jpg'})


@app.route("/api/webptopng", methods=["POST"])
def webp_to_png():
    image = request.files.get('image')
    image_bytes = image.read()
    im = Image.open(io.BytesIO(image_bytes))
    # create BytesIO object
    img_buffer = io.BytesIO()
    # save image to the buffer using PNG format
    im.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    return Response(img_buffer, content_type="image/png",
                    headers={'Content-Disposition': 'attachment; filename=image.png'})


@app.route("/api/bmptopng", methods=["POST"])
def bmp_to_png():
    image = request.files.get('image')
    image_bytes = image.read()
    im = Image.open(io.BytesIO(image_bytes))
    # create BytesIO object
    img_buffer = io.BytesIO()
    # save image to the buffer using PNG format
    im.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    return Response(img_buffer, content_type="image/png",
                    headers={'Content-Disposition': 'attachment; filename=image.png'})


@app.route("/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files.get('image')
    image_bytes = image.read()
    im = Image.open(io.BytesIO(image_bytes))
    # create BytesIO object
    pdf_buffer = io.BytesIO()
    im.save(pdf_buffer, format='PDF')
    pdf_buffer.seek(0)
    return Response(pdf_buffer, content_type="application/pdf",
                    headers={'Content-Disposition': 'attachment; filename=image.pdf'})


if __name__ == '__main__':
    app.run(debug=True)
