import streamlit as st
from api_calling_2 import hints_gen , sol_gen
from PIL import Image


st.title("AI Code Debugger")
st.markdown("Upload upto 3 images for the Solution of your code")
st.divider()
with st.sidebar:
    st.header("Control")
    images = st.file_uploader(
        "Upload the photos of your Code",
        type= ['jpg', 'jpeg','png'],
        accept_multiple_files = True
    )
    pil_images=[]

    for img in images:
        pil_img= Image.open(img)
        pil_images.append(pil_img)
    if images:
        if len(images)>3:
            st.error("Upload at max 3 photos")
        else:
            col=st.columns(len(images))
            st.subheader("Uploaded files")
            for i, img in enumerate(images):
               with col[i]:
                 st.image(img) 
    #dificulity
    selected_option = st.selectbox(
        "Enter the result you want",
        ["Hints", "Solution"],
        index= None
    ) 
    pressed= st.button("Click the button to initiate the AI", type = "primary")

if pressed:
    if not images:
        st.error("You must upload at least 1 image")
    elif not selected_option:
        st.error("You must choose an option")
    else:
        
        with st.container(border=True):
            st.text("Your uploaded code will be processed...")

       
        if selected_option == "Hints":
            with st.container(border=True):
                st.subheader("Hints")
                with st.spinner("AI is generating hints..."):
                    gen_hints = hints_gen(pil_images)
                    st.markdown(gen_hints)

        elif selected_option == "Solution":
            with st.container(border=True):
                st.subheader("Correct Code")
                with st.spinner("AI is re-writing your code..."):
                    solution = sol_gen(pil_images, selected_option)
                    st.markdown(solution)
