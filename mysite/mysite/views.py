import json
import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

DATA_FILE = os.path.join(settings.BASE_DIR, "mysite",  "notenepaldata.json")
with open(DATA_FILE, encoding="utf-8") as f:
    chatbot_data = json.load(f)


def home(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_message = request.POST.get("message")

        if user_name and user_email and user_message:
            send_mail(
                subject="User Message",
                message=f"Message from: {user_name}\nUser email: {user_email}\nUser message: {user_message}",
                from_email="birendrabohara091@gmail.com",
                recipient_list=["harishbohara524@gmail.com"],
            )

        user_ques = request.POST.get("title")
        if user_ques:
            question = user_ques  # save original user question
            user_words = user_ques.lower().split()
            reply = "I am learning. Please ask something about Notebook Hub."

            for item in chatbot_data:
                for pattern in item["pattern"]:
                    pattern_words = pattern.lower().split()
                    if any(word in user_words for word in pattern_words):
                        reply = item["answer"]
                        return JsonResponse({"reply": reply})
                        break
                if reply != "I am learning. Please ask something about Notebook Hub.":
                    break
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def page(request):
    return render(request, "page.html")


def loksewa(request):
    return render(request, "loksewa.html")


def class_11(request):
    return render(request, "class 11.html")


def class_12(request):
    return render(request, "class12.html")
