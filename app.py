import streamlit as st
import pandas as pd
import subprocess
import os
import time

st.set_page_config(page_title="Align Tech - Credit Note Automation", layout="wide")

# Helpers
def show_pdf(file_path):
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return
    import base64
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def show_csv(file_path):
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return
    df = pd.read_csv(file_path)
    st.dataframe(df, use_container_width=True, height=600)

def run_agent():
    if os.path.exists(".adk/session.db"):
        os.remove(".adk/session.db")
    
    process = subprocess.Popen(
        ["adk", "run", "."],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    
    # Send the prompt
    process.stdin.write("Analyze SFDC Ticket #61860676\nexit\n")
    process.stdin.flush()
    
    for line in process.stdout:
        # Filter out some of the noisy ADK startup logs for a cleaner demo
        if "UserWarning" in line or "EXPERIMENTAL" in line or "tail -F" in line:
            continue
        yield line
        time.sleep(0.02) # Slightly slow down for visual streaming effect

# Definitions
TICKET_OPTIONS = {
    "File1-SFDC-Credit-Request-Ticket.pdf": "Sample Data/File1-SFDC-Credit-Request-Ticket.pdf",
}

KNOWLEDGE_OPTIONS = {
    "File2-CuCo-2025-Master-Policy.pdf": "Policy_Documents/File2-CuCo-2025-Master-Policy.pdf",
    "File4-Exception-&-Goodwill-Approval-Matrix.pdf": "Policy_Documents/File4-Exception-&-Goodwill-Approval-Matrix.pdf",
    "File5-SAP-Transactional-Export.csv": "Sample Data/File5-SAP-Transactional-Export.csv",
    "File6-Prior-Credit-History-Log.csv": "Sample Data/File6-Prior-Credit-History-Log.csv",
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://www.aligntech.com/assets/images/logo.png", width=200) # Optional branding
    st.title("Credit Note Automation")
    st.markdown("---")
    
    st.subheader("1. Select SFDC Ticket")
    selected_ticket = st.radio("Open Tickets", list(TICKET_OPTIONS.keys()))
    
    st.subheader("2. Knowledge Sources")
    selected_knowledge = st.radio("Reference Documents", list(KNOWLEDGE_OPTIONS.keys()))
    
    st.markdown("---")
    analyze_btn = st.button("🚀 Analyze Selected Ticket", type="primary", use_container_width=True)

# --- MAIN LAYOUT ---
st.title("Command Center: Credit Processing")

# Top row: Viewer and Agent Output
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("Document Preview")
    
    # Determine which document to show (prioritize knowledge source if clicked recently, 
    # but Streamlit runs top-down so we can just use a segmented control to toggle views)
    view_toggle = st.segmented_control(
        "Select view:",
        options=["SFDC Ticket", "Knowledge Source"],
        default="SFDC Ticket"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    if view_toggle == "SFDC Ticket":
        show_pdf(TICKET_OPTIONS[selected_ticket])
    else:
        k_path = KNOWLEDGE_OPTIONS[selected_knowledge]
        if k_path.endswith(".pdf"):
            show_pdf(k_path)
        else:
            show_csv(k_path)

with col2:
    st.subheader("Agent Live Execution Stream")
    stream_container = st.container(height=600, border=True)
    
    if analyze_btn:
        with stream_container:
            with st.spinner("Initializing Multi-Agent System..."):
                st.write_stream(run_agent())
            st.success("Execution Complete!")

st.divider()

# Bottom row: ZMEMO Output
st.subheader("Generated ZMEMO Batch Interface")

if analyze_btn:
    if os.path.exists("output_zmemo.csv"):
        df_out = pd.read_csv("output_zmemo.csv")
        st.dataframe(df_out, use_container_width=True)
        
        col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
        col_metrics1.metric("Rows Processed", len(df_out))
        if 'ZPR0 KOMV-KBETR(02)' in df_out.columns:
            total_credit = df_out['ZPR0 KOMV-KBETR(02)'].sum()
            col_metrics2.metric("Total Credit Generated", f"€{total_credit:,.2f}")
    else:
        st.warning("No ZMEMO output file was generated.")
else:
    st.info("Click 'Analyze Selected Ticket' to generate the ZMEMO output.")

