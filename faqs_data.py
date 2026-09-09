import streamlit as st

FAQS_DATABASE = [
    {
        "question": "How does SchemeSetu determine my eligibility?",
        "answer": "The application evaluates your profile inputs (age, gender, social category, income, sector) against the specific criteria rules stored in your database."
    },
    {
        "question": "Are applications submitted directly through this app?",
        "answer": "No. SchemeSetu is a discovery and matching engine. When you choose a scheme, you must use the provided official website link to submit your application on the secure government portal."
    },
    {
        "question": "What core documents are typically required?",
        "answer": "Standard documents include an Aadhaar card, income certificate, caste/category certificate (if applicable), passport-size photo, and a seeded bank account passbook."
    },
    {
        "question": "Is there any fee to apply for government schemes?",
        "answer": "Official Indian government schemes are entirely free to apply for. Never pay intermediaries or third-party agents who charge fees for processing government applications."
    },
    {
        "question": "How do I check if a scheme is active or closed?",
        "answer": "The app tracks status flags automatically; schemes marked as closed or discontinued are filtered into the inactive counter dashboard."
    },
    {
        "question": "Can I edit my profile details after searching for schemes?",
        "answer": "Yes, you can modify your age, income, category, or other inputs anytime on the sidebar or profile section to instantly update your matched schemes list."
    },
    {
        "question": "How are the scheme match scores calculated?",
        "answer": "Scores are computed by analyzing how well your specific profile attributes align with each scheme's eligibility requirements, such as target groups, age brackets, and financial limits."
    },
    {
        "question": "Are state-specific schemes included along with central schemes?",
        "answer": "Yes, the database contains a mix of central government initiatives and state-specific welfare schemes, which you can filter using the state selection dropdown."
    },
    {
        "question": "What should I do if an official government link is not opening?",
        "answer": "Government portals occasionally undergo maintenance. If a link fails, you can copy the scheme name and look it up directly on official national portals like myScheme or India.gov.in."
    },
    {
        "question": "How can I search for a specific scheme quickly?",
        "answer": "You can use the Direct Scheme Lookup search bar at the top of the app to type any keyword, scheme name, or department abbreviation for instant results."
    },
    {
        "question": "Do I need to link my bank account with Aadhaar for direct benefits?",
        "answer": "Yes, many Direct Benefit Transfer (DBT) schemes require your bank account to be seeded and linked with your Aadhaar number for seamless, electronic fund transfers."
    },
    {
        "question": "What should I do if my application gets rejected on the official portal?",
        "answer": "Check the specific rejection reason provided on the official portal, correct any document discrepancies or incorrect data fields, and reapply if the guidelines permit."
    },
    {
        "question": "Are there special relaxations for women or reserved social categories?",
        "answer": "Yes, many welfare and financial assistance schemes offer relaxed age thresholds, higher subsidy percentages, or exclusive reservations for women, SC/ST, OBC, and minority applicants."
    },
    {
        "question": "Where can I seek help or report issues regarding a specific scheme?",
        "answer": "Official helpline numbers, toll-free support lines, and grievance email contacts are typically provided on each scheme's official ministry website or portal."
    }
]

def render_faqs_tab():
    st.markdown("### ❓ Frequently Asked Questions & Guidelines")
    st.markdown("Find answers to common queries regarding scheme discovery, eligibility matching, and official applications.")
    
    for faq in FAQS_DATABASE:
        with st.expander(faq["question"]):
            st.write(faq["answer"])