import smtplib, ssl
import json
import time
from watch import check_for_new_recalls
import os

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

def email(state, product_description, reason_for_recall, classification, distribution_pattern):
    subject = f"[UPDATE] New Food Recall in {state}"
    
    message = f"""Subject: {subject} \n
Hello,
This is the team from ______. The following product has been recalled in your state of {state}. Please ensure you take the necessary precautions in tracking and avoiding the product.

Product description: {product_description}
Reason for recall: {reason_for_recall}
Classification type: {classification}

Best,
______
"""

    return message



def send_email1(state, product_description, reason_for_recall, classification, distribution_pattern):
    port = 587
    #state  product type product description classification -1 reason fro recall, classification 2 
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall12345@outlook.com"
    password = "testing$12"

    receiver_emails = get_emails_by_state(data, state) # based on where outbreak is - 

    #print(receiver_emails)
    #print("HI I WORK2")
    context = ssl.create_default_context()
    message = email(state, product_description, reason_for_recall, classification, distribution_pattern) # get email
    #print(message)
    #print("HI I WORK 3")
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo("mylowercasehost")
        server.starttls(context=context)
        server.ehlo("mylowercasehost")
        server.login(sender_email, password)
        #print(sender_email)
        #print(receiver_emails[0])
        server.sendmail(sender_email, receiver_emails, message)
        #print(message)
        print("emails sent")



def send_email2(email_ad, state):

    message ="" #
    #print("works!")
    #print(email)
    #print(state + ".json")
    file_path=os.path.join("./knight/recalldata",state.upper() + ".json")
    print("HIII")
    print(file_path)
    state_data = load_data(file_path) #
    #print(state_data)
    #message += "In your state, "+ state_data
    #for item in state_data["results"]:
    #    message += item["recalling_firm"] + ", "

    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall12345@outlook.com"
    password = "testing$12"
    context = ssl.create_default_context()
    print("HIIIIIIIIIIII1")
    message_combined = """Subject: Welcome - Stay Informed About Food Recalls!\n
    
Welcome to _______! We are excited to have you join our community committed to ensuring food safety and staying up to date with the latest food recalls.

By subscribing, you wll now receive timely alerts about food recalls in your local area, helping you and your loved ones stay informed and safe. Our platform offers easy-to-use tools to filter through recalls based on various factors, so you can quickly identify the products that matter most to you.

Here is what you can expect from us:

Local Notifications: You will be notified of recalls specific to your area.
Detailed Recall Insights: Get in-depth information on each food recall, including reasons for recall and impacted products.
Customizable Filters: Search and filter food recalls based on criteria such as product type, brand, region, and more.
We are here to help you navigate food recalls easily and confidently.

Best Regards,
__________"""
    print("HIIIIIIIIIIII2")

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


def check_empty_dict1(): 
    dict1 = check_for_new_recalls(0)
    print(dict1)

    for state, recalls in dict1.items():
        if isinstance(recalls, list) and recalls:
            print(f"The list for state '{state}' is not empty.")
            for recall in recalls:
                classification = recall.get('classification')
                product_description = recall.get('product_description')
                reason_for_recall = recall.get('reason_for_recall')
                classification = recall.get('classification')
                distribution_pattern = recall.get('distribution_pattern')
                #print("HI I WORK")
                send_email1(state, product_description, reason_for_recall, classification, distribution_pattern)
                #print(f"Classification for state '{state}': {classification}")
    #- returns list of new updates
    #if not empty - for item in list:
        #send_email(item["state"], item["product_description", item["reason_for_recall"], item["classification"], ["distribution_pattern"])

known_emails = {item["email"] for item in data}
#check_empty_dict1()
#send_email1("wa", "aaaaa", "aaaaaaa", "aaaaaaa", "aaaaaaa")
while True:
    check_for_new_emails('data.json', known_emails)
    #check_for_new_updates()
    time.sleep(5)
    

#send_email("ny")