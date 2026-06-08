import streamlit as st
import requests

st.title("🤖 كاشف الروابط الخبيثة (AI Model)")

url_input = st.text_input("أدخل الرابط هنا:", placeholder="http://google.com")

if st.button("افحص الرابط 🔍"):
    if url_input:
        with st.spinner('جاري الاتصال بالموديل...'):
            try:
               
                response = requests.post(
                    "https://url-classification-project.onrender.com/predict", 
                    json={"url": url_input}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if data["label"] == "Malicious":
                        st.error(f"⚠️ تحذير! هذا الرابط خبيث. (ثقة: {data['confidence']})")
                    else:
                        st.success(f"✅ هذا الرابط آمن. (ثقة: {data['confidence']})")
                        
                    st.json(data)
                else:
                    st.error("حدث خطأ في السيرفر!")
                    st.write(response.text)
                    
            except Exception as e:
                st.error(f"فشل الاتصال بالسيرفر. هل تأكدت من تشغيل uvicorn؟")
                st.error(e)
    else:
        st.warning("الرجاء إدخال رابط أولاً.")
