from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Renders the form

@app.route('/submit-item', methods=['POST'])
def submit_item():
    item_name = request.form.get('item_name')
    quantity = request.form.get('quantity')
    print(f"The item name is {item_name} and the quantity is {quantity}")
    return "Form submitted"  # Or redirect to another page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
