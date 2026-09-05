from supabase import create_client, Client
from schemes_data import SCHEMES_DATABASE

# Your Supabase Project Details
SUPABASE_URL = "https://eqlefszucdkwlydcrtdx.supabase.co"

# PASTE YOUR API KEY HERE (Found in Supabase: Project Settings -> API -> anon public key)
SUPABASE_KEY = "sb_publishable_gAjPwCPA24E9BNMMPBOrDQ_qRSS3RA_" 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_data():
    try:
        for s in SCHEMES_DATABASE:
            data = {
                "id": s['id'],
                "name": s['name'],
                "ministry": s['ministry'],
                "status": s['status'],
                "closed_date": s.get('closed_date'),
                "eligible_categories": s['eligible_categories'],
                "min_age": s['min_age'],
                "max_income": s['max_income'],
                "business_sectors": s['business_sectors'],
                "min_loan": s['min_loan'],
                "max_loan": s['max_loan'],
                "states": s['states'],
                "subsidy": s['subsidy'],
                "description": s['description'],
                "documents": s['documents'],
                "guidelines": s['guidelines'],
                "apply_link": s['apply_link']
            }
            supabase.table("schemes").upsert(data).execute()
        print("✅ Successfully uploaded all schemes to Supabase!")
    except Exception as e:
        print("❌ Error uploading to Supabase:", e)

if __name__ == "__main__":
    upload_data()