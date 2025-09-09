from flask import Flask, render_template
app = Flask("__main__")

@app.route('/')
def index():
    return render_tzw3nemplate('index.html')

if __name__=="__main__":
    app.run(debug=True)


