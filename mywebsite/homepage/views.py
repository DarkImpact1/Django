from django.shortcuts import render
from django.http import HttpResponse
from .models import Project_Detail
import random
# Create your views here.

def home(request):
    # name = ['Mohit Dwivedi','Dark Impact','ezz_programming']

    project1 = Project_Detail()
    project1.name = "Saved Wi-Fi Password Extractor (Windows)"
    project1.image = "m-project1.jpg"
    project1.id = "modal-01"
    project1.href = "#modal-01"
    project1.description = "Developed a Python script capable of extracting saved passwords from Windows credentials and securely sending them to a designated email address. This utility enhances user convenience by centralizing password retrieval while prioritizing data privacy and security through controlled email transmission."
    project1.category = "Python"
    project1.link = "https://github.com/DarkImpact1/Saved_Wifi_ssid_pwd_Extractor"

    project2 = Project_Detail()
    project2.name = "Youtube Playlist Downloader"
    project2.image = "m-project2.jpg"
    project2.id = "modal-02"
    project2.href = "#modal-02"
    project2.description = "With Python, I'm creating a YouTube playlist downloader offering customization options. Users can select video quality, destination folder, and specify the number of videos to download. Utilizing the YouTube API and libraries like pytube, the project aims to streamline the process of building a personalized offline playlist."
    project2.category = "Python"
    project2.link = "https://github.com/DarkImpact1/YoutubePlaylistDownloader"

    project3 = Project_Detail()
    project3.name = "Email Automation"
    project3.id = "modal-03"
    project3.href = "#modal-03"
    project3.image = "m-project3.jpg"
    project3.description = "Automating email tasks using Python, my project simplifies communication. Leveraging libraries like smtplib and imaplib, it allows users to schedule, organize, and automate emails. With features like email categorization, auto-responses, and scheduled sending, the email manager enhances efficiency and communication management in a business or personal setting."
    project3.category = 'Python'
    project3.link = "https://github.com/DarkImpact1/email_manager"

    project4 = Project_Detail()
    project4.name = "Django"
    project4.id = "modal-04"
    project4.href = "#modal-04"
    project4.image = "m-project4.jpg"
    project4.description = "Crafting a dynamic portfolio using Django in Python, my project showcases web development skills. Utilizing Django's MVT architecture, I design an interactive and responsive portfolio website. Features include project showcases, a contact form, and an admin interface for easy content management and updates."
    project4.link = "https://github.com/DarkImpact1/Django"

    project5 = Project_Detail()
    project5.name = "Notepad (Clone) .. currently Halted"
    project5.id = "modal-05"
    project5.href = "#modal-05"
    project5.image = "m-project5.jpg"
    project5.description = "Developing a Python-based Notepad clone, I focus on replicating essential features like text editing, file handling, and user-friendly interface. Leveraging tkinter for GUI, the project emphasizes simplicity and efficiency, providing users with a lightweight yet functional text editor akin to the traditional Notepad."
    project5.category = "Python (Tkinter)"
    project5.link = "https://github.com/DarkImpact1/Notepad-Clone-Using-Python"

    project6 = Project_Detail()
    project6.name = "Virtual Assistant"
    project6.id = "modal-06"
    project6.href = "#modal-06"
    project6.image= "m-project6.jpg"
    project6.description = "Why to waste our energy when you have you assistance by your side 24 x 7.My Python-based virtual assistant integrates natural language processing and automation to execute tasks. Leveraging libraries like speech recognition and pyttsx3, the assistant responds to voice commands, handling functions like setting reminders, answering queries, and controlling system features. Aiming for enhanced user productivity, it's a versatile tool for daily tasks."
    project6.category = "Python"
    project6.link = "https://github.com/DarkImpact1/Virtual-Assistant"

    projects = [project1,project2,project3,project4,project5,project6]

    
    return render(request,'index.html', {'allprojects' : projects})
