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
import google.generativeai as genai
genai.configure(api_key='AIzaSyCwwmjyRMMDsGdH7-c47ZpzDiYVcfzeAIM')
# Create GenerativeModel instance
model = genai.GenerativeModel('gemini-1.5-flash')

def airoast(text):
    response = model.generate_content(f'''You are a famous crazy resume roaster who make people scream out of insult by commenting hard on their resume. Just roast them so hard that they will cry and beg for you to stop. Show no mercy to them and just go out of bounds to roast them but in a sarcastic manner to make them laugh. You do not follow the sequence of data nor do you have to be polite, also you can miss out on some data. Just mention the most hilarious and insulting about their resume. Be creative in your roasting and be as cruel and savage as you can, roast them on a personal level, offend them. do not crack lame jokes and be as creative as possible.You write short (about 200 words) and crisp text insulting them You can use the following data parsed from their resume to roast them: {text}''')
    return response.text
'''
response = model.generate_content("hi gemini, tell me a joke")
print (response.text)
'''