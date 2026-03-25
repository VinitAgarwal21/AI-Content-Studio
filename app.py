import streamlit as st
from core.generator import generate_post
from core.formatter import format_post
from core.validator import validate_post

from components.linkedin_ui import render_linkedin_ui
from components.instagram_ui import render_instagram_ui
from components.twitter_ui import render_twitter_ui


def main():
    st.set_page_config(page_title="AI Content Studio")

    st.title("AI Content Studio")

    platform = st.radio(
        "Select Platform",
        ["LinkedIn", "Instagram", "X (Twitter)"],
        horizontal=True
    )

    st.markdown("---")

    if platform == "LinkedIn":
        data = render_linkedin_ui()

    elif platform == "Instagram":
        data = render_instagram_ui()

    else:
        data = render_twitter_ui()

    if st.button("Generate Post"):
        if not data.get("topic"):
            st.warning("Please enter a topic.")
            return

        with st.spinner("Generating..."):
            post = generate_post(data)

            is_valid, msg = validate_post(post, data["platform"])
            if not is_valid:
                st.error(msg)
                return

            post = format_post(post, data["platform"])

        st.markdown("Generated Content")
        st.success(post)


if __name__ == "__main__":
    main()