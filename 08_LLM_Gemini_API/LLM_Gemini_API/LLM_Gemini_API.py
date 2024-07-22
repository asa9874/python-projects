import google.generativeai as genai
 
GOOGLE_API_KEY="Gemini 키를 입력해주세요"
 
genai.configure(api_key=GOOGLE_API_KEY)
 
model = genai.GenerativeModel('gemini-pro')
 
response = model.generate_content("gemini의 강점을 알려줘")
 
print(response.text)
