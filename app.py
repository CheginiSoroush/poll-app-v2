from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# دیتابیس ما حالا فقط یه دیکشنری ساده پایتونه!
votes = {
    'option_a': 0,
    'option_b': 0
}

@app.route('/')
def get_results():
    option_a_votes = votes['option_a']
    option_b_votes = votes['option_b']

    return f'''
        <h1>Which technology do you prefer? (v2)</h1>
        <form action="/vote" method="post">
            <button name="vote" value="option_a">Option A: Docker</button>
            <span>(Votes: {option_a_votes})</span>
            <br><br>
            <button name="vote" value="option_b">Option B: Kubernetes</button>
            <span>(Votes: {option_b_votes})</span>
        </form>
        <hr>
        <form action="/reset" method="post">
            <button type="submit">Reset Votes</button>
        </form>
    '''

@app.route('/vote', methods=['POST'])
def vote():
    vote_option = request.form['vote']
    if vote_option in votes:
        votes[vote_option] += 1
    return redirect(url_for('get_results'))

@app.route('/reset', methods=['POST'])
def reset():
    votes['option_a'] = 0
    votes['option_b'] = 0
    return redirect(url_for('get_results'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)