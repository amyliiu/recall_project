import smtplib, ssl
import json
import time

with open('data.json') as f:
    data = json.load(f)

def load_data(file_path):
    with open(file_path) as f:
        return json.load(f)

receiver_email = []
def get_emails_by_state(data, target_state):
    receiver_email = []
    for item in data:
        if item["state"] == target_state:
            receiver_email.append(item["email"])
    return receiver_email

def find_state_by_email(file_path, target_email):
    data = load_data(file_path)
    for item in data:
        if item["email"] == target_email:
            return item["state"]
    return None

def email(status):
    subject = ""
    if status == "Ongoing":
        subject = "New food recall - product"
    elif status == "Completed":
        subject = "Food recall status update - " + status
    elif status == "Terminated":
        subject = "Food recall status update - " + status
    else:
        subject = "Food recall status update - " + status
    message = f"""Subject: {subject}
Test
Product name
Product type
classification
reason for recall
location """

    return message

#remove

def send_email1(state, product_type, product_description, reason_for_recall, classification):
    port = 587
    #state  product type product description classification -1 reason fro recall, classification 2 
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall12@outlook.com"
    password = "testing$12"

    receiver_email = get_emails_by_state(data, state) # based on where outbreak is - 

    print(receiver_email)

    context = ssl.create_default_context()
    message = email("Completed")
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo("mylowercasehost")
        server.starttls(context=context)
        server.ehlo("mylowercasehost")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print(message)
        print("email sent")

def send_email2(email, state):

    message2 ="" #
    #print("works!")
    #print(email)
    #print(state + ".json")
    state_data = load_data(state + ".json")
    for item in state_data["results"]:
        message2 += item["recalling_firm"] + ", "

    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall12@outlook.com"
    password = "testing$12"
    context = ssl.create_default_context()
    message22 = f"""Subject: Products that are currently recalled in your area

    """ + message2 + """
    """
    print(message22)
    
    #print(message)
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo("mylowercasehost")
        server.starttls(context=context)
        server.ehlo("mylowercasehost")
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message22)
        print("email sent")


def check_for_new_emails(file_path, known_emails):
    current = load_data(file_path)
    current_emails = {item["email"] for item in current}
    #current_emails = json.load(file_path)
    new_emails = current_emails - known_emails
    if new_emails:
        print("New emails added:", new_emails)
        print("EMAIL TO BE SENT")
        for email in new_emails:
            send_email2(email, find_state_by_email('data.json', email))
        known_emails.update(new_emails)
    else:
        print("no new email")


known_emails = {item["email"] for item in data}



while True:
    check_for_new_emails('data.json', known_emails)
    time.sleep(5)

#send_email("ny")