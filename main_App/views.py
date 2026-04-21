from django.shortcuts import render, redirect
from .models import Design
from .models import About_page
from .models import Service
from django.core.mail import send_mail
from .models import ContactMessage
from django.contrib import messages
# from shop import Product


# Create your views here.
def home(request):
    banners = Design.objects.filter(is_banner = True)
    featured = Design.objects.filter(is_featured = True )[:3]
    about = About_page.objects.first()
    services = Service.objects.all()
    
    return render(request,'home.html', {
        'banners': banners,
        'featured':featured,
        'about': about,
        'services': services
        })

def about(request):
    about = About_page.objects.first()
    return render(request, 'about.html', {'about': about})

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services':services})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']

        # Save message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )

        # Optional: send email
        full_message = f"From: {name} <{email}>\n\n{message_text}"
        try:
            send_mail(
                subject,
                full_message,
                'your-email@example.com',  # Replace with your from-email
                ['info@example.com'],       # Replace with your to-email
                fail_silently=True          # Avoid breaking page if email fails
            )
        except Exception as e:
            print("Email send failed:", e)

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Redirect to the same page

    context = {
        'brand_name': 'Alishba Design',
        'brand_slogan': 'Beauty in simplicity'
    }
    return render(request, 'contact.html', context)