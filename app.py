from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Flask will now print to console
app.logger.info("Starting Flask app...")

@app.route('/')
def index():
    app.logger.info("Rendering the form...")
    return render_template('form.html')  # Renders the form

@app.route('/submit-item', methods=['POST'])
def submit_item():
    app.logger.info("Form submitted.")
    item_name = request.form.get('item_name')
    quantity = request.form.get('quantity')
    app.logger.info(f"Received: item name - {item_name}, quantity - {quantity}")
    return "Form submitted"  # Or redirect to another page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
