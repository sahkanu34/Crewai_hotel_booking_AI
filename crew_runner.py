import os
from pathlib import Path
import streamlit as st
from crewai.project.crew_loader import load_crew_and_kickoff

# Load secrets into environment variables
os.environ["MODEL"] = st.secrets["MODEL"]
os.environ["NVIDIA_NIM_API_KEY"] = st.secrets["NVIDIA_NIM_API_KEY"]
os.environ["CREWAI_TRACING_ENABLED"] = st.secrets["CREWAI_TRACING_ENABLED"]

# Path to crew.jsonc relative to this file, so it works regardless of cwd
CREW_PATH = Path(__file__).parent / "crew.jsonc"


def run_crew(customer_request: str) -> str:
    try:
        result = load_crew_and_kickoff(
            CREW_PATH,
            input_overrides={"customer_request": customer_request},
        )
        return str(result)
    except Exception as e:
        return f"Error running crew: {e}"