import streamlit as st
import datetime
import re
import random
import numpy as np
from twilio.rest import Client
import sounddevice as sd
import face_recognition
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

# Sample registered user credentials for demonstration purposes
registered_users = {
    "john_doe": "password123",
    "jane_smith": "passw0rd456",
    # Add more registered users as needed
}


def is_valid_id_number(id_number):
    # ID Number validation: Should have exactly 13 characters
    return len(id_number) == 13

def is_valid_email(email):
    # Email validation using regular expression
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email)


def is_valid_username(username):
    # Username validation: Should have a combination of characters and numbers
    return bool(re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$", username))

def is_valid_password(password):
    # Password validation: 8 or more characters, at least one digit, one uppercase, one lowercase, and one special character
    return bool(re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%^*?&()-_=+[\]{}|;:'\",.<>/?])[A-Za-z\d@$!%^*?&()-_=+[\]{}|;:'\",.<>/?]{8,}$", password))


def about_page():
    st.title("About Online Voting System")
    st.write("Welcome to the Online Voting System! This platform allows registered users to cast their votes online.")
    st.write("With our secure and efficient system, we aim to provide a convenient way for voters to participate in elections from the comfort of their homes.")
    st.write("If you haven't registered yet, please proceed to the Registration page to create an account.")
    st.write("Once registered, you can log in and complete your personal information to become an eligible voter.")
    st.write("Happy voting!")
    
personal_info = {}
def send_otp(phone_number, otp):
    # Set up your Twilio account credentials
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"

    client = Client(account_sid, auth_token)

    # Send the OTP via SMS to the user's phone number
    message = client.messages.create(
        body=f"Your OTP for password reset is: {otp}",
        from_=twilio_phone_number,
        to=phone_number
    )
    

def login_page():
    st.title("Login Page")

    # Input fields for username and passworda
    username = st.text_input("ID Number")
    password = st.text_input("Password", type="password")

    if st.button("Forgot Password"):
        reset_method = st.radio("Reset Method:", ("Email", "Phone Number"))

        if reset_method == "Email":
            email = st.text_input("Please enter your registered email")
            if email and is_valid_email(email):
                # Add your logic here to send the reset link to the user's email
                # After sending the reset link, show a success message to the user
                st.success(f"An email with password reset instructions has been sent to {email}.")
                st.write("Please check your email and follow the instructions to reset your password.")
            elif email:
                st.warning("Invalid email address. Please enter a valid email.")
        else:  # Reset method is Phone Number
            phone_number = st.text_input("Please enter your registered phone number")
            if phone_number and len(phone_number) == 10 and phone_number.isdigit():
                # Generate a random 6-digit OTP
                otp = str(random.randint(100000, 999999))
                # Add your logic to send the OTP to the user's phone number
                send_otp(phone_number, otp)
                st.success("An OTP has been sent to your registered phone number.")
                otp_input = st.text_input("Please enter the OTP to reset your password.")
                # Here, you can add your logic to verify the OTP and reset the password accordingly
                # For example, you can check if the OTP entered by the user matches the generated OTP
                # If it matches, you can proceed with the password reset process
                # You may use a button to trigger the password reset after verifying the OTP.
            elif phone_number:
                st.warning("Invalid phone number. Please enter a valid 10-digit number.")



    # Login button
    if st.button("Login"):
        # Perform authentication checks
        if not username or not password:
            st.error("Please enter both username and password.")
            
        elif username not in registered_users:
            st.error("Username not found. Please register first.")
        elif registered_users[username] != password:
            st.error("Invalid password. Please try again.")
        else:
            st.success("Login successful!")
            # Perform any additional actions after successful login
            
            
# ... (Other parts of the code)

# Face Recognition VideoTransformer
class FaceRecognitionTransformer(VideoTransformerBase):
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        if registered_users["id_number"]["profile_image"] is not None:
            # Load the known profile image for face recognition
            known_image = face_recognition.load_image_file(registered_users["id_number"]["profile_image"])
            known_face_encoding = face_recognition.face_encodings(known_image)[0]
            self.known_face_encodings.append(known_face_encoding)
            self.known_face_names.append("id_number")

    def transform(self, frame):
        # Convert the frame to RGB format for face recognition
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the current face encoding with the known face encoding
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                name = self.known_face_names[matches.index(True)]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        return frame


def registration_page():
    st.title("User Registration")

    # Create a form for the registration page
    with st.form("registration_form"):
        # Input fields for first name, last name, and ID number in the first column
        col1, col2, col3 = st.columns(3)
        first_name = col1.text_input("First Name")
        last_name = col1.text_input("Last Name")
        id_number = col1.text_input("ID Number", max_chars=13)

        # Input fields for date of birth, race, and phone number in the second column
        dob = col2.date_input("Date of Birth", datetime.date.today())
        race_options = ["White", "Black", "Asian", "Mixed", "Other"]
        race = col2.selectbox("Race", race_options)
        phone_number = col2.text_input("Phone Number", max_chars=10)

        # Input fields for gender, age, provinces, address, district, and ward number in the third column
        gender_options = ["Male", "Female"]
        gender = col3.selectbox("Gender", gender_options)
        age = col3.number_input("Age", min_value=0, max_value=120, step=1)
        provinces = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "Northern Cape", "North West", "Western Cape"]
        province = col3.selectbox("Province", provinces)
        address = col3.text_input("Address")
        district = col3.text_input("District")
        ward_number = col1.text_input("Ward Number")
        

        # Input fields for email, username, password, and password confirmation
        email = col1.text_input("Email")
        # username = col1.text_input("Username")
        password = col2.text_input("Password", type="password")
        confirm_password = col2.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Register")
        if submitted:
            if not all([first_name, last_name, id_number, phone_number, email, password, confirm_password, gender, age, dob, race, province, address, district, ward_number]):
                st.error("Please fill in all the fields.")
            elif not is_valid_email(email):
                st.warning("Invalid email format. Please enter a valid email address.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            
            elif not is_valid_password(password):
                st.error("Invalid password. It should be at least 8 characters long and contain at least one digit, one uppercase letter, one lowercase letter, and one special character.")
            else:
                # Store the user information in the registered_users dictionary
                registered_users[first_name.lower() + "_" + last_name.lower()] = {
                    "Password": password,
                    "ID Number": id_number,
                    "Phone Number": phone_number,
                    "Email": email,
                    "Gender": gender,
                    "Age": age,
                    "Date of Birth": dob,
                    "Race": race,
                    "Province": province,
                    "Address": address,
                    "District": district,
                    "Ward Number": ward_number,
                    # Add more user information as needed
                }
        
    record_audio_button = st.button("Record Audio")
    audio_data = None

    if record_audio_button:
        with st.spinner("Recording..."):
            audio_data = record_audio()

    # Display the audio data as a waveform (optional)
    if audio_data is not None:
        st.write("Recorded Audio:")
        st.audio(audio_data, format="audio/wav")



    # Registration button
    if st.button("Register"):
        # Your registration logic goes here
        st.success("User registered successfully!")



# Function to record audio using sounddevice
def record_audio(sample_rate=44100, duration=5):
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    return audio_data.tobytes()

        # Registration button

def face_recognition_page():
    st.title("Face Recognition")

    # Initialize the webcam
    video_capture = cv2.VideoCapture(0)

    # Load the known profile image for face recognition
    known_image = face_recognition.load_image_file(registered_users["id_number"]["profile_image"])
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    # Flag to indicate if the photo has been taken
    photo_taken = False

    # Main face recognition loop
    while not photo_taken:
        # Capture each frame from the webcam
        ret, frame = video_capture.read()

        # Find face locations in the current frame
        face_locations = face_recognition.face_locations(frame)

        # If any face is found, try to recognize it
        if face_locations:
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for face_encoding in face_encodings:
                # Compare the current face encoding with the known face encoding
                matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

                name = "Unknown"
                if True in matches:
                    name = 'id_number'

                # Draw a rectangle around the face and display the name
                top, right, bottom, left = face_locations[0]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display the frame with recognized faces
        cv2.imshow('Video', frame)

        # Press 'q' to quit or 's' to take a picture
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            # Save the current frame as the profile image for face recognition
            registered_users["id_number"]["profile_image"] = "id_number.jpg"  # Replace with the appropriate file path
            cv2.imwrite("id_number.jpg", frame)  # Save the image
            st.success("Profile image saved.")
            photo_taken = True

    # Release the webcam and close the OpenCV window
    video_capture.release()
    cv2.destroyAllWindows()

# Initialize an empty dictionary to store user information
personal_info = {}

def personal_info_page():
    st.title("Personal Information")

    # Input fields for the personal information
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    id_number = st.text_input("ID Number")
    gender_options = ["Male", "Female"]
    gender = st.selectbox("Gender", gender_options)
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    min_dob = datetime.date.today() - datetime.timedelta(days=365 * 100)
    dob = st.date_input("Date of Birth", min_value=min_dob)
    race_options = ["White", "Black", "Asian", "Mixed", "Other"]
    race = st.selectbox("Race", race_options)
    phone_number = st.text_input("Phone Number")
    provinces = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "Northern Cape", "North West", "Western Cape"]
    province = st.selectbox("Province", provinces)
    address = st.text_input("Address")
    district =  st.text_input("District")
    wardNo = st.text_input("Ward Number")

    
    # Add more input fields as needed (Province, City/Town, ZipCode, Street Address, District, WardNo, etc.)

    # Save the user information when the user clicks the "Save" button
    if st.button("Save"):
        # Store the user information in the personal_info dictionary
        personal_info["First Name"] = first_name
        personal_info["Last Name"] = last_name
        personal_info["ID Number"] = id_number
        personal_info["Gender"] = gender
        personal_info["Age"] = age
        personal_info["Date of Birth"] = dob
        personal_info["Race"] = race
        personal_info["Phone Number"] = phone_number
        personal_info["Province"] = provinces
        personal_info["Address"] = address
        personal_info["District"] = district
        personal_info["Ward Number"] = wardNo
        
        st.success("Personal information saved!")
        
    

    # Display the user information from the personal_info dictionary
    if personal_info:
        st.header("User Information:")
        for key, value in personal_info.items():
            st.write(f"{key}: {value}")


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("", ("About","Login", "Register","Profile","Record"))
    
    if page == "About":
        about_page()
        
    elif page == "Login":
        login_page()
        
    elif page == "Register":
        registration_page()
        face_recognition_page()
        
    
    elif page == "Record":
        record_audio()
    
    else:
       personal_info_page()

if __name__ == "__main__":
    main()
