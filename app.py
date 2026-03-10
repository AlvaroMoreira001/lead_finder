import sys
import asyncio

import streamlit as st
from services.lead_pipeline import LeadPipeline
from config.settings import MAX_BUSINESSES

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.title("LeadFinder PRO")

keyword = st.text_input("Nicho")

city = st.text_input("Cidade")

max_leads = st.number_input(
    "Quantidade de leads",
    min_value=1,
    max_value=MAX_BUSINESSES,
    value=min(20, MAX_BUSINESSES),
    step=1,
)

run = st.button("Buscar Leads")

if run:

    pipeline = LeadPipeline()

    with st.spinner("Gerando leads..."):

        file = pipeline.run(keyword, city, int(max_leads))

    st.success("Leads gerados")

    with open(file, "rb") as f:

        st.download_button("Baixar Excel", f, file.name)
