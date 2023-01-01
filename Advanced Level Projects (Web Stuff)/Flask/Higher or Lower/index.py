from flask import Flask
app = Flask(__name__)

correct_number = 6


@app.route("/")
def index_page() -> str:
    return "<h1>Guess The Number Between 1 to 9!</h1>" \
           "<img width=400 src='https://media2.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid" \
           "=ecf05e47m3izhx4almbd5jls22lz5g7ef96rlzqmmek15ry7&rid=200w.webp&ct=g'> "


@app.route('/<int:number>')
def result(number):
    if number == correct_number:
        return "<h1 style='color:green;font-size:50'>Correct!!</h1>" \
               "<img width=400 src='https://media0.giphy.com/media/3o7abKhOpu0NwenH3O/200w.webp?cid" \
               "=ecf05e47bnmjo9v2dc5qyg55lljm0q16hrn90eifb0gspt7b&rid=200w.webp&ct=g'> "
    if number < correct_number:
        return "<h1 style='color:red;font-size:50'>Too Lower</h1>" \
               "<img width=400 src='https://media3.giphy.com/media/2sfEg0Yv4c8E5VT7s3/200w.webp?cid" \
               "=ecf05e47fuwq7kyfra3b8456fqu5dxi2tvuvw8qvuq8dghej&rid=200w.webp&ct=g'> "
    if number > correct_number:
        return "<h1 style='color:red;font-size:50'>Too Higher</h1>" \
               "<img width=400 src='https://media1.giphy.com/media/d8EN0mls2eoAFLRiX8/200w.webp?cid" \
               "=ecf05e47hmup80rz1vsvwyvi3grsutyfxj8xz8qu2p29vszc&rid=200w.webp&ct=g'> "


if __name__ == '__main__':
    app.run(debug=True)
