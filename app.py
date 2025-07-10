import streamlit as st

st.title("SEO Content Generator")

product_title = st.text_input("Product Title")
product_desc = st.text_area("Description")
features = st.text_input("Features (comma separated)")

if st.button("Generate SEO"):
    prompt = f"""
    Create SEO content for:
    Title: {product_title}
    Description: {product_desc}
    Features: {features}
    """
    
    # Replace with your model call
    seo_content = "Sample SEO output based on your model"
    
    st.subheader("Generated SEO")
    st.text_area("Result", seo_content, height=200)