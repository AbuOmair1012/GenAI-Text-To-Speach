from google import genai
from google.genai import types
import wave

# The client gets the API key from the environment variable `GEMINI_API_KEY`.

GEMINI_API_KEY = "AIzaSyA49kAeKe7-IyPQKiNuijx9Gd4GHBvYwz4"
TEXT_EN = "We are a powerful team: Abdullah, AI Engineer; Faisal, Data Scientist; and Ahmad, Full-Stack Developer. Together, we are shaping the future by building an innovative application that leverages AI to revolutionize the entertainment and education sectors."
TEXT_AR = "نحن فريق قوي يضم: عبد الله – مهندس ذكاء اصطناعي، فيصل – عالِم بيانات، وأحمد – مطوّر متكامل. نعمل معًا لصناعة المستقبل عبر تطوير تطبيق مبتكر يوظّف تقنيات الذكاء الاصطناعي لإحداث ثورة في مجالي الترفيه والتعليم."
client = genai.Client(api_key=GEMINI_API_KEY)

# response = client.models.generate_content(model="gemini-2.5-flash", contents="Explain how AI works in a few words")
# print(response.text)


# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

response = client.models.generate_content(
   model="gemini-2.5-flash-preview-tts",
   contents=TEXT_AR,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
                # language_code='ar-EG',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='TTS_AR.wav'
wave_file(file_name, data) # Saves the file to current directory