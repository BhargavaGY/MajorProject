import cv2
import easyocr
import pyttsx3

cap = cv2.VideoCapture(0)
# instance text detector
reader = easyocr.Reader(['en'], detector='dbnet18',gpu=True)

# def outputText(text):
#     tts = gTTS(text=text, lang='en', slow=False)
#
#     audio_bytes = io.BytesIO()
#     tts.write_to_fp(audio_bytes)
#     audio_bytes.seek(0)
#
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
#         temp_file.write(audio_bytes.read())
#         temp_file.flush()
#         temp_file.seek(0)
#
#         # Get the file name
#         temp_file_name = temp_file.name
#
#     # Play the audio file using playsound
#     playsound(temp_file_name)



# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 250)    # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Text to be converted into speech
# text = "This is the text to be converted into speech."

# Convert text to speech


frames = 0
while True:
    ret, img = cap.read()
    if frames // 10 == 0:

        # detect text on image
        text_ = reader.readtext(img)

        threshold = 0.50
        # draw bbox and text
        if text_:
            try:
                for t_, t in enumerate(text_):
                    # print(t)

                    bbox, text, score = t
                    if score > threshold and len(bbox) == 4:
                        print(text)
                        # cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
                        # cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
                        # outputText(text)
                        engine.say(text)

                        # Run the engine and wait for the speech to finish
                        engine.runAndWait()
            except cv2.error:
                continue
            except OSError:
                continue

    cv2.imshow(" ", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frames += 1

cap.release()
cv2.destroyAllWindows()
