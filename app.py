import streamlit as st
import openai
st.title("🤖 Data Science BOT 🤖")
# Set OpenAI API key
openai.api_key = "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"

# Function to search word information
def search_word_information():
    # Page title with improved formatting
    st.markdown("---")  # Separator line

    # # User input with placeholder text
    # word = st.text_input("Say something", " ")

    # # Search button to the right with search emoji
    # if st.button("🔍 Search", key="search_button"):
    #     if word:
    #         # Requesting response from OpenAI API
    #         with st.spinner("Generating response..."):
    #             response = openai.Completion.create(
    #                 model="gpt-3.5-turbo-instruct",
    #                 prompt=f"{word}",
    #                 max_tokens=150,
    #                 n=1,
    #                 stop=None,
    #                 temperature=0.7,
    #             )

    #         # Displaying the response
    #         st.success("🚀 PoliticallyCorrectDishwasher SAYS:")
    #         st.info(response.choices[0].text)
    #     else:
    #         st.warning("Please enter a query before searching.")

# Improved layout with better spacing
#st.set_page_config(layout="centered", page_title="Data Science BOT", page_icon="🤖")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Anything"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Execute the data science BOT function
search_word_information()
