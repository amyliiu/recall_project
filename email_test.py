import smtplib, ssl
import json
import time
from watch import check_for_new_recalls
import os

with open('./knight/data.json') as f:
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
Important notification! The following product has been recalled in your state of {state}. Please ensure you take the necessary precautions in tracking and avoiding the product.

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


    context = ssl.create_default_context()
    message = email(state, product_description, reason_for_recall, classification, distribution_pattern) # get email

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo("mylowercasehost")
        server.starttls(context=context)
        server.ehlo("mylowercasehost")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, message)
        print("emails sent")



def send_email2(email_ad, state):
    message ="" #
    file_path=os.path.join("./knight/recalldata",state.upper() + ".json")
    print("HIII")
    print(file_path)
    state_data = load_data(file_path) #

    port = 587
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "food.recall12345@outlook.com"
    password = "testing$12"
    context = ssl.create_default_context()
    message_combined = """Subject: Welcome - Stay Informed About Food Recalls!\n
    
Welcome! We are excited to have you join our community committed to ensuring food safety and staying up to date with the latest food recalls.

By subscribing, you wll now receive timely alerts about food recalls in your local area, helping you and your loved ones stay informed and safe. Our platform offers easy-to-use tools to filter through recalls based on various factors, so you can quickly identify the products that matter most to you.

Here is what you can expect from us:

Local Notifications: You will be notified of recalls specific to your area.
Detailed Recall Insights: Get in-depth information on each food recall, including reasons for recall and impacted products.
Customizable Filters: Search and filter food recalls based on criteria such as product type, brand, region, and more.
We are here to help you navigate food recalls easily and confidently.

"""


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
    new_emails = current_emails - known_emails
    if new_emails:
        for email in new_emails:
            send_email2(email, find_state_by_email('./knight/data.json', email))
        known_emails.update(new_emails)
    #else:
        #print("no new email")


def check_empty_dict1(): 
    dict1 = check_for_new_recalls(0)

    for state, recalls in dict1.items():
        if isinstance(recalls, list) and recalls:
            print(f"The list for state '{state}' is not empty.")
            for recall in recalls:
                classification = recall.get('classification')
                product_description = recall.get('product_description')
                reason_for_recall = recall.get('reason_for_recall')
                classification = recall.get('classification')
                distribution_pattern = recall.get('distribution_pattern')
                send_email1(state, product_description, reason_for_recall, classification, distribution_pattern)
 
known_emails = {item["email"] for item in data}
check_empty_dict1() ##
while True:
    check_for_new_emails('./knight/data.json', known_emails)
    time.sleep(5)
    
