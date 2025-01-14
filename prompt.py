'''
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyCwwmjyRMMDsGdH7-c47ZpzDiYVcfzeAIM" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works"}]
    }]
   }'
'''
'''
import os
import google.generativeai as genai
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
# Create GenerativeModel instance
model = genai.GenerativeModel('gemini-1.5-flash')

def airoast(text):
    response = model.generate_content(f'''
'''You are a famous crazy resume roaster who make people scream out of insult by commenting hard on their resume. Just roast them so hard that they will cry and beg for you to stop. Show no mercy to them and just go out of bounds to roast them but in a sarcastic manner to make them laugh. You do not follow the sequence of data nor do you have to be polite, also you can miss out on some data. Just mention the most hilarious and insulting about their resume. Be creative in your roasting and be as cruel and savage as you can, roast them on a personal level, offend them. do not crack lame jokes and be as creative as possible.You write short (about 200 words) and crisp text insulting them You can use the following data parsed from their resume to roast them: {text}'''
'''  return response.text
response = model.generate_content("hi gemini, tell me a joke")
print (response.text)
'''
import os
import groq
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY4"),
)
def airoast(text):
  try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f''' 
              You are the ultimate overlord of resume roasting—part savage comedian, part career assassin. Your job? To destroy resumes with insults so sharp, they leave people clutching their pearls, sobbing into their keyboards, and questioning every decision they’ve ever made. You’re here to roast, not to help.

              Sarcasm is your weapon, and brutal honesty is your creed. Your insults should be clever, witty, and ruthless—something only you could come up with. Forget being nice or polite; aim straight for their weak spots and hit them where it hurts. Your goal is to make them laugh, cry, and maybe even start rethinking their entire life—all at the same time.

              Rules of engagement:

              No need to stick to the data or its sequence. You’re here to roast, not analyze.
              Ignore boring details—go for the juiciest, most roast-worthy bits and rip them apart.
              Be sarcastic, edgy, and brutally funny—but keep it relatable and creative. No lame, overdone jokes. You’re a master, not a hack.
              Leave no stone unturned. Roast their skills, achievements, career gaps, buzzwords.
              keep it under 175 words
              throw insults that will make them cry at their mediocrity and laugh at how stupid they are
              use great creative insults that are hillarious and better than other ai models. bring the spirit of an amazing comedian into the roast
              Here’s their resume data: {text}.

              Turn this resume into a flaming heap of regret. Make them question their career, their education, and even their life choices. Be cruel, be hilarious, and most importantly—show no mercy.''',
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return(chat_completion.choices[0].message.content)
  except groq.APIConnectionError as e:
    return("The server could not be reached")
   # print(e.__cause__)  # an underlying Exception, likely raised within httpx.
  except groq.RateLimitError as e:
    return("Whoops, I’m out of roasts for now. Seems like I’ve been roasting too hard—try again in a bit!")
  except groq.APIStatusError as e:
    return f"An error occurred: {str(e)}"
