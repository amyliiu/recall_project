import smtplib, ssl
import json
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def email(status, state, product_description, reason_for_recall, classification, distribution_pattern):
    subject = ""
    if status == "Ongoing":
        subject = "New food recall - product"
    elif status == "Completed":
        subject = "Food recall status update - " + status
    elif status == "Terminated":
        subject = "Food recall status update - " + status
    else:
        subject = "Food recall status update - " + status
    message = f"""Subject: {subject} \n
States affected: {distribution_pattern}
Product description: {product_description}
Reason for recall: {reason_for_recall}
Classification type: {classification}
"""

    

    return message



def send_email1(state, product_description, reason_for_recall, classification, distribution_pattern):
    port = 587
    #state  product type product description classification -1 reason fro recall, classification 2 
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall1234@outlook.com"
    password = "testing$12"

    receiver_emails = get_emails_by_state(data, state) # based on where outbreak is - 

    print(receiver_emails)

    context = ssl.create_default_context()
    message = email("Completed", state, product_description, reason_for_recall, classification, distribution_pattern) # get email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo("mylowercasehost")
        server.starttls(context=context)
        server.ehlo("mylowercasehost")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, message)
        print(message)
        print("emails sent")



def send_email2(email_ad, state):

    message ="" #
    #print("works!")
    #print(email)
    #print(state + ".json")
    state_data = load_data(state.upper() + ".json")
    for item in state_data["results"]:
        message += item["recalling_firm"] + ", "

    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall1234@outlook.com"
    password = "testing$12"
    context = ssl.create_default_context()
    message_combined = """Subject: Products that are currently recalled in your area \n
    
     """ + message + """ """
    #message_combined = MIMEMultipart("alternative")

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo("mylowercasehost")
        server.starttls(context=context)
        server.ehlo("mylowercasehost")
        server.login(sender_email, password)
        server.sendmail(sender_email, email_ad, message_combined)
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


#def func (): #- returns list of new updates
    #if not empty - for item in list:
        #send_email(item["state"], item["product_description", item["reason_for_recall"], item["classification"], ["distribution_pattern"])

known_emails = {item["email"] for item in data}

send_email1("wa", "aaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa")

while True:
    check_for_new_emails('data.json', known_emails)
    #check_for_new_updates()
    time.sleep(5)
    

#send_email("ny")