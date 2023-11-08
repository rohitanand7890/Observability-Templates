import streamlit as st

st.set_page_config(
    page_title="Observability Templates",
    page_icon="👋",
)

st.write("# Welcome to Observability Template! 👋")

st.sidebar.success("Select a Template above.")

st.markdown(
    """
    ## Observability Templates
    
    #### Customer Engagement/ Sentiment
    - Click-through Rate  
    - Engagement Graph(DAU)  
    - Survey Response  
    - Word Cloud  
    - #Todo: Sankey  

    #### DORA metric (TBD)
    #### Security Issues
    #### Bug
    #### A/B Testing template
    #### Page performance
    #### Code coverage/ 


    **👈 Select a Template from the sidebar** 
    ### 
"""
)
