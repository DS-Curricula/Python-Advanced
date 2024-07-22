import streamlit as st

# Create five columns with equal width
col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")

# Column 1 content
with col1:
    # Add a header to the first column
    st.header("Column 1")
    # Add some text content to the first column
    st.write("Content for column 1")

# Column 2 content
with col2:
    # Add a header to the second column
    st.header("Column 2")
    # Add some text content to the second column
    st.write("Content for column 2")

# Column 3 content
with col3:
    # Add a header to the third column
    st.header("Column 3")
    # Add some text content to the third column
    st.write("Content for column 3")

# Column 4 content
with col4:
    # Add a header to the fourth column
    st.header("Column 4")
    # Add some text content to the fourth column
    st.write("Content for column 4")

# Column 5 content
with col5:
    # Add a header to the fifth column
    st.header("Column 5")
    # Add some text content to the fifth column
    st.write("Content for column 5")
