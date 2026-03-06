from django.db import IntegrityError

try:
    # Your save operation here
    new_entry.save()
except IntegrityError:
    # Handle the duplicate case (e.g., display an error message to the user)
    print("This value already exists. Please choose a different one.")

