from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Import your RegistrationForm from forms.py
from .models import CustomUser  # Import your CustomUser model


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new CustomUser instance with the form data
            new_user = CustomUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                full_name=form.cleaned_data['full_name'],
                country=form.cleaned_data['country'],
                mobile_number=form.cleaned_data['mobile_number']
            )

            # Set the password for the user
            new_user.set_password(form.cleaned_data['password'])

            # Handle the optional identity document upload
            identity_document = form.cleaned_data['identity_document']
            if identity_document:
                new_user.identity_document = identity_document

            # Save the user to the database
            new_user.save()

            # You may also want to log the user in after registration
            # For example:
            # login(request, new_user)

            # Redirect to a success page or another URL
            return redirect('success_page')  # Replace 'success_page' with the actual URL name

    else:
        form = RegistrationForm()

    return render(request, 'pages/userRegistration.html', {'form': form})

def success_page_view(request):
    return render(request, 'pages/success_page.html')
