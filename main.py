from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

MY_EMAIL = "sarahmatheww2000@gmail.com"
MY_PASSWORD = "sarah@123"

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/contact")
def contact_me():
    return render_template("contact.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data["name"], data["email"], data["phone"], data["text"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(name, email, phone, message):
    email_message = f"Subject: New Message\n\n Name:{name}\nEmail:{email}Phone number:{phone}Message:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, "bhatshobharani@gmail.com", email_message)


if __name__ == "__main__":
    app.run(debug=True)
