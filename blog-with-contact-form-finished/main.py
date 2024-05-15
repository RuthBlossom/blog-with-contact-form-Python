from flask import Flask, render_template, request  # Importing necessary modules
import smtplib  # For sending emails
import requests  # For making HTTP requests

app = Flask(__name__)  # Creating a Flask application instance

# REPLACE THIS LINK WITH YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST.
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()  # Getting blog post data from an API
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"  # Email address from which emails will be sent
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"  # Password for the email address

@app.route('/')  # Route for the home page
def get_all_posts():
    return render_template("index.html", all_posts=posts)  # Rendering the home page template with blog post data


@app.route("/about")  # Route for the about page
def about():
    return render_template("about.html")  # Rendering the about page template


@app.route("/contact", methods=["GET", "POST"])  # Route for the contact page with support for GET and POST requests
def contact():
    if request.method == "POST":  # If a POST request is received (form submission)
        data = request.form  # Get the form data
        send_email(data["name"], data["email"], data["phone"], data["message"])  # Send email with form data
        return render_template("contact.html", msg_sent=True)  # Render contact page with a message indicating successful email sent
    return render_template("contact.html", msg_sent=False)  # Render contact page with no message initially

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"  # Compose email message
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to Gmail SMTP server
        connection.starttls()  # Start TLS encryption
        connection.login(OWN_EMAIL, OWN_PASSWORD)  # Login to the email account
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)  # Send email to yourself

@app.route("/post/<int:index>")  # Route for viewing a single blog post
def show_post(index):
    requested_post = None
    for blog_post in posts:  # Loop through all blog posts
        if blog_post["id"] == index:  # If the ID of a blog post matches the requested index
            requested_post = blog_post  # Set the requested post to the matching blog post
    return render_template("post.html", post=requested_post)  # Render the post page template with the requested post data

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode

