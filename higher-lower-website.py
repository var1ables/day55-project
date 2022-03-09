from flask import Flask
import random

random = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Guess a number between 0 and 9</h1>'\
           "<img src='https://www.pngkit.com/png/detail/381-3815811_9d5-badly-drawn-thinking-emoji.png'>"

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random:
        return "<h1 style='color:purple'> Too high, try again!</h1>" \
               "<img src='https://cdn.shopify.com/s/files/1/1061/1924/products/Tongue_Out_Emoji_1_grande.png?v=1571606093'>"


    if guess < random:
        return "<h1 style='color: red'> Too low, try again!</h1>" \
               "<img src='https://i.pinimg.com/736x/73/bc/96/73bc9635871138d57981b6c5dc2eb113.jpg'>"

    else:
        return "<h1 style='color: green'> You found me! </h1>" \
               "<img src='https://www.rocksdigital.com/wp-content/uploads/2018/02/emoji-marketing-tips-1.jpg'>"

if __name__ == '__main__':
    app.run(debug=True)