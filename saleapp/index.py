from flask import Flask, render_template, request
import dao


app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id=request.args.get("cate_id")
    name = "Pham Nam"

    products = dao.load_products(q=q, cate_id=cate_id)

    return render_template("index.html", products = products)


@app.route("/products/<int:id>")
def details(id):
    p = dao.get_product_by_id(id)
    return render_template("product-details.html", prods = p)

@app.context_processor
def common_attribute():
    return {
        "cates":dao.load_categorys()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
