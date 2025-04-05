
import os
import groq
from groq import Groq

client = Groq(
    api_key=os.("GROQ_API_KEY4"),
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
