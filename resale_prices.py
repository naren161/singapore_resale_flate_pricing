import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings("ignore")
import numpy as np 
import pickle
from PIL import Image

def town_mapping(town_map):
    town_mapping_dict = {
        'ANG MO KIO': 0, 'BEDOK': 1, 'BISHAN': 2, 'BUKIT BATOK': 3, 'BUKIT MERAH': 4,
        'BUKIT PANJANG': 5, 'BUKIT TIMAH': 6, 'CENTRAL AREA': 7, 'CHOA CHU KANG': 8,
        'CLEMENTI': 9, 'GEYLANG': 10, 'HOUGANG': 11, 'JURONG EAST': 12, 'JURONG WEST': 13,
        'KALLANG/WHAMPOA': 14, 'MARINE PARADE': 15, 'PASIR RIS': 16, 'PUNGGOL': 17,
        'QUEENSTOWN': 18, 'SEMBAWANG': 19, 'SENGKANG': 20, 'SERANGOON': 21, 'TAMPINES': 22,
        'TOA PAYOH': 23, 'WOODLANDS': 24, 'YISHUN': 25
    }
    return town_mapping_dict.get(town_map, -1)  # Return -1 for unknown towns

def flat_type_mapping(flt_type):
    flat_type_mapping_dict = {
        '3 ROOM': 2, '4 ROOM': 3, '5 ROOM': 4, '2 ROOM': 1, 'EXECUTIVE': 5,
        '1 ROOM': 0, 'MULTI-GENERATION': 6
    }
    return flat_type_mapping_dict.get(flt_type, -1)  # Return -1 for unknown flat types

def flat_model_mapping(fl_m):
    flat_model_mapping_dict = {
        'Improved': 5, 'New Generation': 12, 'Model A': 8, 'Standard': 17,
        'Simplified': 16, 'Premium Apartment': 13, 'Maisonette': 7,
        'Apartment': 3, 'Model A2': 10, 'Type S1': 19, 'Type S2': 20,
        'Adjoined flat': 2, 'Terrace': 18, 'DBSS': 4, 'Model A-Maisonette': 9,
        'Premium Maisonette': 15, 'Multi Generation': 11, 'Premium Apartment Loft': 14,
        'Improved-Maisonette': 6, '2-room': 0, '3Gen': 1
    }
    return flat_model_mapping_dict.get(fl_m, -1)



def selling_price(town,flat_type,floor_area_sqm,flat_model,lease_commence_date
                  ,year,storey_start,storey_end,remaining_lease_year,remaining_lease_month):
    town = town_mapping(town)
    flat_type = flat_type_mapping(flat_type)
    floor_area_sqm = int(floor_area_sqm)
    flat_model = flat_model_mapping(flat_model)
    lease_commence_date = int(lease_commence_date)
    year = int(year)
    storey_start = int(storey_start)
    storey_end = int(storey_end)
    remaining_lease_year = int(remaining_lease_year)
    remaining_lease_month = int(remaining_lease_month)
    
    with open(r"C:\Users\Happy\Desktop\Naren Baskar\singapore resaleflat prices\Singapore_Resale_Flat_Prices_Model_1.pkl",'rb') as x:
      model = pickle.load(x)

    data = np.array([[town,flat_type,floor_area_sqm,flat_model,lease_commence_date
                ,year,storey_start,storey_end,remaining_lease_year,remaining_lease_month]])
    predict = model.predict(data)
    price = np.exp(predict[0])
    return round(price)

st.set_page_config(layout="wide")

st.title("SINGAPORE RESALE FLAT PRICES PREDICTION")
st.write("")

with st.sidebar:
    select = option_menu("MAIN MENU",['HOME','PRICE PREDICTION'])
        
if select == "HOME":
    image_resale = Image.open(r"C:\Users\Happy\Desktop\Naren Baskar\singapore resaleflat prices\resale.jpg")
    st.image(image_resale)
    
    st.header("Welcome to Singapore Resale Property Prediction")
    st.write("")
    st.write("")
    st.header("Discover Insights into Singapore Resale Market")
    st.write("")
    st.write("***Are you looking to buy or sell a resale property in Singapore? Our advanced prediction tool helps you make informed decisions by providing insights and forecasts on property prices. Whether you're a prospective buyer, a seller, or simply curious about the real estate market, you've come to the right place!***")
    st.write("")
    st.header("What can you do here?")
    st.write("")
    st.header("Predict property price")
    st.write("")
    st.write("***Use our intuitive tool to predict the resale price of HDB flats based on various features such as location, flat type, size, and more. Get a quick estimate to aid your decision-making process.***")
    st.write("")
    st.header("Market Trends")
    st.write("")
    st.write("***Analyze historical data and trends in Singapore's resale property market. Understand how different factors influence property prices and stay updated with the latest market insights.***")
    st.write("")
    st.header("Compare Properties")
    st.write("")
    st.write("***Compare different properties based on predicted prices, features, and locations. Make comparisons easily to find the best options that meet your needs.***")
    st.write("")
    st.header("Get Started Ready to get started?")
    st.write("")
    st.write("***Simply enter your property details in the prediction tool and see how our advanced algorithms can help you make informed decisions.***")
    st.header("NEED HELP ?")
    st.write("")
    st.write("***If you have any questions or need assistance, please refer to our Help Center or contact our support team at support@example.com.***")
    
elif select == "PRICE PREDICTION":
    col1,col2 = st.columns(2)
    
    with col1:
        
       town = st.selectbox("Select the town",['ANG MO KIO' ,'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG',
                                                'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG',
                                                'HOUGANG', 'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE',
                                                'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON',
                                                'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
       
       flat_type = st.selectbox("Select the flat_type",['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])  
            
       floor_area_sqm = st.number_input("select the value for floor_area_sqm (min : 34.5 /max : 158.5 )") 
       
       flat_model = st.selectbox("Select the flat_model",['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                            'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2', 'Type S1',
                                                            'Type S2', 'Adjoined flat', 'Terrace' 'DBSS', 'Model A-Maisonette',
                                                            'Premium Maisonette', 'Multi Generation', 'Premium Apartment Loft',
                                                            'Improved-Maisonette', '2-room', '3Gen'])
       
       lease_commence_date = st.number_input("Selec the lease_commence_date (min:1966/max:2020)")
       
    with col2:
        
        year=st.number_input("Selec the year min:2015/max:2024")
        storey_start = st.number_input("Enter the value for storey start")
        storey_end = st.number_input("Enter the value for storey End")
        remaining_lease_year = st.number_input("Enter the value for remaining lease year max:97/min:15.5")
        remaining_lease_month = st.number_input("Enter the value for remaining lease month max:20.5/min:0.0")
        
    button = st.button("Predicting the Selling Price",use_container_width=True)
    
    if button:
        predict_selling_price = selling_price(town,flat_type,floor_area_sqm,flat_model,lease_commence_date
                  ,year,storey_start,storey_end,remaining_lease_year,remaining_lease_month)
        
        st.write("## :green[**The Predicted Price is :**]",predict_selling_price)
        
                  
                                              
        
        
 
