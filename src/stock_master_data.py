import sqlite3
import os

STOCKS = [
    # symbol, name, category
    ("HDFCBANK.NS", "HDFC Bank", "Banks & Financials"),
    ("ICICIBANK.NS", "ICICI Bank", "Banks & Financials"),
    ("SBIN.NS", "State Bank of India (SBI)", "Banks & Financials"),
    ("KOTAKBANK.NS", "Kotak Mahindra Bank", "Banks & Financials"),
    ("AXISBANK.NS", "Axis Bank", "Banks & Financials"),
    ("BAJFINANCE.NS", "Bajaj Finance", "Banks & Financials"),
    ("INDUSINDBK.NS", "IndusInd Bank", "Banks & Financials"),
    ("IDFCFIRSTB.NS", "IDFC First Bank", "Banks & Financials"),
    ("BANDHANBNK.NS", "Bandhan Bank", "Banks & Financials"),
    ("FEDERALBNK.NS", "Federal Bank", "Banks & Financials"),
    ("CANBK.NS", "Canara Bank", "Banks & Financials"),
    ("BANKBARODA.NS", "Bank of Baroda", "Banks & Financials"),
    ("PNB.NS", "Punjab National Bank (PNB)", "Banks & Financials"),
    ("AUBANK.NS", "AU Small Finance Bank", "Banks & Financials"),
    ("RBLBANK.NS", "RBL Bank", "Banks & Financials"),

    # IT & Technology
    ("TCS.NS", "Tata Consultancy Services", "IT & Technology"),
    ("INFY.NS", "Infosys", "IT & Technology"),
    ("HCLTECH.NS", "HCL Technologies", "IT & Technology"),
    ("WIPRO.NS", "Wipro", "IT & Technology"),
    ("TECHM.NS", "Tech Mahindra", "IT & Technology"),
    ("LTIM.NS", "LTIMindtree", "IT & Technology"),
    ("MPHASIS.NS", "Mphasis", "IT & Technology"),
    ("PERSISTENT.NS", "Persistent Systems", "IT & Technology"),
    ("COFORGE.NS", "Coforge", "IT & Technology"),
    ("BIRLASOFT.NS", "Birlasoft", "IT & Technology"),
    ("ZENSARTECH.NS", "Zensar Technologies", "IT & Technology"),
    ("SONATSOFTW.NS", "Sonata Software", "IT & Technology"),
    ("HEXAWARE.NS", "Hexaware Technologies", "IT & Technology"),
    ("LTTS.NS", "L&T Technology Services", "IT & Technology"),
    ("FIRSTSOURCE.NS", "Firstsource Solutions", "IT & Technology"),

    # Pharmaceuticals & Healthcare
    ("SUNPHARMA.NS", "Sun Pharma", "Pharmaceuticals & Healthcare"),
    ("DIVISLAB.NS", "Divi's Laboratories", "Pharmaceuticals & Healthcare"),
    ("CIPLA.NS", "Cipla Ltd", "Pharmaceuticals & Healthcare"),
    ("MAXHEALTH.NS", "Max Healthcare", "Pharmaceuticals & Healthcare"),
    ("TORNTPHARM.NS", "Torrent Pharma", "Pharmaceuticals & Healthcare"),
    ("DRREDDY.NS", "Dr. Reddy's Laboratories", "Pharmaceuticals & Healthcare"),
    ("APOLLOHOSP.NS", "Apollo Hospitals", "Pharmaceuticals & Healthcare"),
    ("MANKIND.NS", "Mankind Pharma", "Pharmaceuticals & Healthcare"),
    ("ZYDUSLIFE.NS", "Zydus Lifesciences", "Pharmaceuticals & Healthcare"),
    ("LUPIN.NS", "Lupin Ltd", "Pharmaceuticals & Healthcare"),
    ("AUROPHARMA.NS", "Aurobindo Pharma", "Pharmaceuticals & Healthcare"),
    ("BIOCON.NS", "Biocon Ltd", "Pharmaceuticals & Healthcare"),
    ("GLAND.NS", "Gland Pharma", "Pharmaceuticals & Healthcare"),
    ("ALKEM.NS", "Alkem Laboratories", "Pharmaceuticals & Healthcare"),
    ("GLENMARK.NS", "Glenmark Pharmaceuticals", "Pharmaceuticals & Healthcare"),

    # Electricals & Consumer Durables
    ("HAVELLS.NS", "Havells India", "Electricals & Consumer Durables"),
    ("DIXON.NS", "Dixon Technologies", "Electricals & Consumer Durables"),
    ("VOLTAS.NS", "Voltas Ltd", "Electricals & Consumer Durables"),
    ("KAYNES.NS", "Kaynes Technology", "Electricals & Consumer Durables"),
    ("BLUESTARCO.NS", "Blue Star Ltd", "Electricals & Consumer Durables"),
    ("WHIRLPOOL.NS", "Whirlpool", "Electricals & Consumer Durables"),
    ("BAJAJELEC.NS", "Bajaj Electricals", "Electricals & Consumer Durables"),
    ("ORIENTELEC.NS", "Orient Electric", "Electricals & Consumer Durables"),
    ("IFBIND.NS", "IFB Industries", "Electricals & Consumer Durables"),
    ("VGUARD.NS", "V-Guard Industries", "Electricals & Consumer Durables"),
    ("SYMPHONY.NS", "Symphony", "Electricals & Consumer Durables"),
    ("TTKPRESTIG.NS", "TTK Prestige", "Electricals & Consumer Durables"),
    ("CROMPTON.NS", "Crompton Greaves Consumer", "Electricals & Consumer Durables"),
    ("EUREKAFORBE.NS", "Eureka Forbes", "Electricals & Consumer Durables"),
    ("SCHAEFFLER.NS", "Schaeffler India", "Electricals & Consumer Durables"),

    # Real Estate
    ("DLF.NS", "DLF Ltd", "Real Estate"),
    ("GODREJPROP.NS", "Godrej Properties", "Real Estate"),
    ("OBEROIRLTY.NS", "Oberoi Realty", "Real Estate"),
    ("PRESTIGE.NS", "Prestige Estates", "Real Estate"),
    ("BRIGADE.NS", "Brigade Enterprises", "Real Estate"),
    ("SOBHA.NS", "Sobha Ltd", "Real Estate"),
    ("PHOENIXLTD.NS", "Phoenix Mills", "Real Estate"),
    ("MACROTECH.NS", "Macrotech Developers", "Real Estate"),
    ("ANANTRAJ.NS", "Anant Raj", "Real Estate"),
    ("PURVA.NS", "Puravankara", "Real Estate"),
    ("KOLTEPATIL.NS", "Kolte-Patil Developers", "Real Estate"),
    ("SUNTECK.NS", "Sunteck Realty", "Real Estate"),
    ("MAHLIFE.NS", "Mahindra Lifespace Developers", "Real Estate"),
    ("SHOBHA.NS", "Shobha Developers", "Real Estate"),
    ("SIGIND.NS", "Signature Global (India) Ltd", "Real Estate"),

    # Auto & Auto Ancillaries
    ("MARUTI.NS", "Maruti Suzuki", "Auto & Auto Ancillaries"),
    ("M&M.NS", "Mahindra & Mahindra", "Auto & Auto Ancillaries"),
    ("TATAMOTORS.NS", "Tata Motors", "Auto & Auto Ancillaries"),
    ("BAJAJ-AUTO.NS", "Bajaj Auto", "Auto & Auto Ancillaries"),
    ("EICHERMOT.NS", "Eicher Motors", "Auto & Auto Ancillaries"),
    ("ASHOKLEY.NS", "Ashok Leyland", "Auto & Auto Ancillaries"),
    ("HEROMOTOCO.NS", "Hero MotoCorp", "Auto & Auto Ancillaries"),
    ("TVSMOTOR.NS", "TVS Motor", "Auto & Auto Ancillaries"),
    ("ESCORTS.NS", "Escorts Kubota", "Auto & Auto Ancillaries"),
    ("FORCEMOT.NS", "Force Motors", "Auto & Auto Ancillaries"),
    ("SMLISUZU.NS", "SML Isuzu", "Auto & Auto Ancillaries"),
    ("ATULAUTO.NS", "Atul Auto", "Auto & Auto Ancillaries"),
    ("VSTTILLERS.NS", "V.S.T Tillers Tractors", "Auto & Auto Ancillaries"),
    ("GREAVESCOT.NS", "Greaves Cotton", "Auto & Auto Ancillaries"),
    ("AMARAJABAT.NS", "Amara Raja Energy & Mobility", "Auto & Auto Ancillaries"),

    # Metals & Mining
    ("TATASTEEL.NS", "Tata Steel", "Metals & Mining"),
    ("JSWSTEEL.NS", "JSW Steel", "Metals & Mining"),
    ("HINDALCO.NS", "Hindalco Industries", "Metals & Mining"),
    ("VEDL.NS", "Vedanta Ltd", "Metals & Mining"),
    ("COALINDIA.NS", "Coal India", "Metals & Mining"),
    ("NATIONALUM.NS", "National Aluminium", "Metals & Mining"),
    ("NMDC.NS", "NMDC Ltd", "Metals & Mining"),
    ("JINDALSTEL.NS", "Jindal Steel & Power", "Metals & Mining"),
    ("SAIL.NS", "Steel Authority of India", "Metals & Mining"),
    ("HINDZINC.NS", "Hindustan Zinc", "Metals & Mining"),
    ("MOIL.NS", "MOIL Ltd", "Metals & Mining"),
    ("RATNAMANI.NS", "Ratnamani Metals & Tubes", "Metals & Mining"),
    ("WELCORP.NS", "Welspun Corp", "Metals & Mining"),
    ("SHYAMMETL.NS", "Shyam Metalics", "Metals & Mining"),
    ("LLOYDSME.NS", "Lloyds Metals & Energy", "Metals & Mining"),
]

def insert_stock_master():
    db_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    db_path = os.path.join(db_dir, "nifty_stocks.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR REPLACE INTO stock (symbol, name, category) VALUES (?, ?, ?)",
        STOCKS
    )
    conn.commit()
    conn.close()
    print("Stock master data inserted.")

if __name__ == "__main__":
    insert_stock_master()