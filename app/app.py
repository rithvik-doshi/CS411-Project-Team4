from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():

    return render_template("index.html", team_num="Team 4")


@app.route("/search", methods=["POST"])
def search():

    username = request.form["username"]
    # sanitize the username to only alphanumerics
    username = re.sub(r'\W+', '', username)

    res = api_query(username)

    return render_template("search.html", username=username,
                           email=res["email"],
                           lastlogin=res["last-login"],
                           prov=res["provisioned"],
                           acclvl=res["access-level"])


def api_query(username):

    print("new fake api call!")

    fakeresults = {
        "last-login": "29 days ago",
        "provisioned": "March 16th 2021",
        "access-level": "3"
    }

    fakeresults["email"] = username + "@bu.edu"

    return fakeresults


if __name__ == "__main__":
    app.run(debug=True)
