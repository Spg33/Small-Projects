# open, read and split a text file

with open("filename.txt", "r") as file:  # Replace "filename.txt" with the file.extention intended to use
    file_text = file.read()
usernames = file_text.split()

# Function that counts a user's failed login attempts

def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
    if counter >= 3:
        return "User tried to login 3 or more times, therefore their account has to be locked!"
    else:
        return "The user has logged in successfully!"
        
# Call the function

login_check(usernames, "user") # Replace the "user" with the username
