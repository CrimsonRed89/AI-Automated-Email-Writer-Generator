from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import tkinter as tk
import pyperclip
import pyautogui

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from selenium.webdriver.chrome.options import Options

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

model.eval()

def generate_email_response(recipient_name, specific_topic, your_name, your_position, your_company, desired_outcome ,max_length=200, temperature=0.7):
    prompt = f"Dear {recipient_name},\n\nI hope this email finds you well. I wanted to reach out regarding {specific_topic}.\n\nIf you have any questions or require further clarification, please feel free to ask.\n\nThank you for your time and attention to this matter. I look forward to {desired_outcome}.\n\nBest regards,\n\n{your_name}\n{your_position}\n{your_company}\n"
    
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text
    output = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        do_sample=True,
    )

    # Decode the generated text
    generated_email = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_email

##You Can Give the reason and desired outcomes as per your choice

# Example usage
recipient_mail = "daddyseva53@gmail.com"
recipient_name = "Mr Danny"
specific_topic = "Apology for office leave"
your_name = "Johndoe"
your_position = "Intern"
your_company = "Google"
desired_outcome ="No action would be Taken and i'll be held free"
generated_email = generate_email_response(recipient_name, specific_topic, your_name, your_position, your_company, desired_outcome )

pyperclip.copy(generated_email)

url = "https://www.trash-mail.com/compose-mail/"
path = "C:\\Users\\KIIT\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(url)
time.sleep(1)

From = To = driver.find_element(by = "xpath", value = '//*[@id="form-from"]')
To.send_keys(your_name)
time.sleep(2)

To = driver.find_element(by = "xpath", value = '//*[@id="form-to"]')
To.send_keys(recipient_mail)
time.sleep(2)

sub = driver.find_element(by = "xpath", value = '//*[@id="form-subject"]')
sub.send_keys(specific_topic)

write = driver.find_element(by = "xpath", value = '//*[@id="editor"]')
write.click()
time.sleep(2)

pyautogui.hotkey('ctrl', 'v')

send = driver.find_element(by = "xpath", value = '//*[@id="send-mails"]')
send.click()

time.sleep(5)

driver.close()

