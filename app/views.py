from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
from .models import UserAccounts
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def index(request, page):
    if page == "index":
        user_data = request.session.get('user')  # This is a dictionary or None
        return render(request, 'index.html', user_data)

    elif page == "login":
        if request.method == "GET":
            if 'user' in request.session:
                return redirect('index')
            else:
                return render(request, 'login.html')
        
        elif request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not (email and password):
                messages.error(request, "All fields are required.")
                return render(request, "login.html")


            try:
                user = UserAccounts.objects.get(email=email)

                if check_password(password, user.password):
                    request.session['user'] = {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                    }
                    return redirect('index')  # Or your home page
                else:
                    messages.error(request, "Invalid email or password.")
                    return render(request, 'login.html')
            
            except UserAccounts.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return render(request, 'login.html')

    elif page == "register":
        if request.method == "GET":
            if 'user' in request.session:
                return redirect('index')
            else:
                return render(request, "register.html")
    
        elif request.method =="POST":
            name = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if not (name and email and password):
                messages.error(request, "All fields are required.")
                return render(request, "register.html")

            try:
                # Check if email already exists
                if UserAccounts.objects.filter(email=email).exists():
                    messages.error(request, "Email already registered.")
                    return render(request, "register.html")

                # Create new user
                user = UserAccounts(username=name, email=email, password=make_password(password)) 
                user.save()

                messages.success(request, "Account created successfully. Please login.")
                return redirect("login") 

            except Exception as e:
                messages.error(request, f"Something went wrong: {str(e)}")
                return render(request, "register.html")
            
    elif page == "logout":
        if 'user' in request.session:
            del request.session['user']
            messages.info(request, "You have been logged out successfully.")

        return redirect('index')

    else:
        return render(request, '404.html')

def admin(request):
    users = UserAccounts.objects.all()
    return render(request, 'admin_page.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(UserAccounts, id=user_id)
    user.delete()
    return redirect('admin')

def update_user(request, user_id):
    user = get_object_or_404(UserAccounts, id=user_id)
    if request.method == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('admin')
    return render(request, 'update.html', {'user': user})