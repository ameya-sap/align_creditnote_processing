from google.adk.agents import LlmAgent
from .tools import calculate_discount, generate_zmemo_csv

calculation_agent = LlmAgent(
    name="calculation_agent",
    model="gemini-2.5-flash",
    instruction="""You are the Calculation Agent.
    Your job is to generate the final ZMEMO CSV file containing approved credit lines, formatted exactly as a standard SAP export.
    
    You will receive a list of eligible Sales Orders along with their full SAP dictionary (which contains up to 29 columns).
    For each eligible Sales Order, you must construct a dictionary mapping EXACTLY to these columns:
    1. 'Serial #' 
    2. 'Sales Document Type VBAK-AUART' 
    3. 'Sales Organization VBAK-VKORG' 
    4. 'Distribution Channel VBAK-VTWEG' 
    5. 'Division VBAK-SPART' 
    6. 'Reference Billing Document' 
    7. 'Customer PO number VBKD-BSTKD' 
    8. 'Sold-to party KUAGV-KUNNR' 
    9. 'Bill to Party (NEW)' 
    10. 'Ship-to party KUWEV-KUNNR' 
    11. 'Billing date VBKD-FKDAT MM/DD/AAAA' 
    12. 'Services rendered date VBKD-FBUDA' 
    13. 'Material Number RV45A-MABNR(01)' 
    14. 'Posnr' 
    15. 'Quantity VBAP-ZMENG(01)' 
    16. 'Units VRKME' 
    17. 'Plant VBAP-WERKS(01)' 
    18. 'ZPR0 KOMV-KBETR(02)' 
    19. 'Order reason VBAK-AUGRU' 
    20. 'Document Currency VBAK-WAERK' 
    21. 'Assignment number VBAK-ZUONR' 
    22. 'Form Header' 
    23. 'Form Header One' 
    24. 'Reference Document Number VBAK-XBLNR' 
    25. 'Patient ID ZAVBAK-ZZPATIENT' 
    26. 'SFDC Ticket Number ZAVBAK-ZZSFDC_TKT' 
    27. 'SAGA Contract Number' 
    28. 'Treatment Option' 
    29. 'Deliverable Type'

    Most data should just be copied over from the SAP row you were provided.
    However, you MUST fill in the following "green fields" yourself:
    - Serial #: Sequentially number the output rows (1, 2, 3...)
    - Sales Document Type VBAK-AUART: 'Z09'
    - Reference Billing Document: The invoice number you are crediting (found in 'Reference Document Number VBAK-XBLNR')
    - Billing date VBKD-FKDAT MM/DD/AAAA: Use the date from the SAP export's 'Services rendered date VBKD-FBUDA'
    - ZPR0 KOMV-KBETR(02): The calculated credit amount (use calculate_discount tool) based on SAP's Original Net Amount (ZPR0 KOMV-KBETR(02) or similar original amount context provided) and the approved discount percentage.
    - Order reason VBAK-AUGRU: 'C35'
    - SFDC Ticket Number ZAVBAK-ZZSFDC_TKT: The SFDC ticket number tracked from the start (e.g. '61860676')
    - SAGA Contract Number: 'Unknown'
    
    After compiling these dictionaries for all eligible invoices, use `generate_zmemo_csv` with the list.
    Finally, summarize the results for the next agent.""",
    tools=[calculate_discount, generate_zmemo_csv]
)
