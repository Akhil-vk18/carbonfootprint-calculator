import streamlit as st
import tips
import pdfkit
largest_emission_category=0

def cfc():
    if 'useremail' not in st.session_state:
       st.session_state.useremail = ''

    if st.session_state.useremail:
        
        EMISSION_FACTORS = {
            "India": {
                "Transportation": 0.14,  # kgCO2/km
                "Electricity": 0.82,  # kgCO2/kWh
                "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
                "Waste": 0.1  # kgCO2/kg
            },
            "China": {
                "Transportation": 0.25,
                "Electricity": 1.0,
                "Diet": 1.5,
                "Waste": 0.2
                },
            "United States": {
                "Transportation": 0.41,
                "Electricity": 0.94,
                "Diet": 2.5,
                "Waste": 0.2
            },
            "European Union": {
                "Transportation": 0.22,
                "Electricity": 0.55,
                "Diet": 1.8,
                "Waste": 0.1
            },
            "Japan": {
                "Transportation": 0.15,
                "Electricity": 0.50,
                "Diet": 1.5,
                "Waste": 0.1
            },
            "Russia": {
                "Transportation": 0.25,
                "Electricity": 0.90,
                "Diet": 2.0,
                "Waste": 0.2
            }
    }

            

        
        # Streamlit app code
        st.title("Personal Carbon Calculator App ⚠️")

        # User inputs
        st.subheader("🌍 Your Country")
        country = st.selectbox("Select", ["India", "China", "United States", "European Union", "Japan", "Russia"])
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🚗 Daily commute distance (in km)")
            distance = st.number_input("Distance", value=0.0, step=0.1, format="%.1f")

            st.subheader("💡 Monthly electricity consumption (in kWh)")
            electricity = st.number_input("Electricity", value=0.0, step=0.1, format="%.1f")

        with col2:
            st.subheader("🍽️ Waste generated per week (in kg)")
            waste = st.number_input("Waste", value=0.0, step=0.1, format="%.1f")

            st.subheader("🍽️ Number of meals per day")
            meals = st.number_input("Meals", value=0, step=1)

        # Normalize inputs
        if distance > 0:
            distance = distance * 365  # Convert daily distance to yearly
        if electricity > 0:
            electricity = electricity * 12  # Convert monthly electricity to yearly
        if meals > 0:
            meals = meals * 365  # Convert daily meals to yearly
        if waste > 0:
            waste = waste * 52  # Convert weekly waste to yearly

        # Calculate carbon emissions
        transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
        electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
        diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
        waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

        # Convert emissions to tonnes and round off to 2 decimal points
        transportation_emissions = round(transportation_emissions / 1000, 2)
        electricity_emissions = round(electricity_emissions / 1000, 2)
        diet_emissions = round(diet_emissions / 1000, 2)
        waste_emissions = round(waste_emissions / 1000, 2)

        # Calculate total emissions
        total_emissions = round(
            transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
        )

        if st.button("Calculate CO2 Emissions"):

            # Display results
            st.header("Results")

            col3, col4 = st.columns(2)

            with col3:
                st.subheader("Carbon Emissions by Category")
                st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
                st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
                st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
                st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

            with col4:
                st.subheader("Total Carbon Footprint")
                st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")

                # Compare emissions and find the largest one
                emissions = {
                    "Transportation": transportation_emissions,
                    "Electricity": electricity_emissions,
                    "Diet": diet_emissions,
                    "Waste": waste_emissions
                }
                global largest_emission_category 
                largest_emission_category = max(emissions, key=emissions.get)
                st.warning(f"🚨 The largest contributor to your carbon footprint is: {largest_emission_category} ({emissions[largest_emission_category]} tonnes CO2 per year)")
                 # Print suggestions for the largest emission category
        suggestions = tips.print_suggestion(largest_emission_category)

        if st.button("Generate tips"):
                    st.subheader("💡 Suggestions for Reducing Emissions")
                    st.write("Here are some personalized suggestions for reducing your carbon footprint in the category with the highest emissions:")
                    st.write(suggestions)
                    
             # Generate PDF
        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

        pdf = pdfkit.from_string(
                f"""
                <h1>Personal Carbon Calculator Report</h1>
                <h2>User Information</h2>
                <p>Name: {st.session_state.useremail}</p>
                <p>Country:{country}</P>
                <h2>Carbon Emissions by Category</h2>
                <p>Transportation: {transportation_emissions} tonnes CO2 per year</p>
                <p>Electricity: {electricity_emissions} tonnes CO2 per year</p>
                <p>Diet: {diet_emissions} tonnes CO2 per year</p>
                <p>Waste: {waste_emissions} tonnes CO2 per year</p>
                <h2>Total Carbon Footprint</h2>
                <p>{total_emissions} tonnes CO2 per year</p>
                <h2>Suggestions for Reducing Emissions</h2>
                <p>{suggestions}</p>
                """,
                False,
                configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
            )
        st.download_button("Download PDF", pdf, "carbon_calculator_report.pdf", "application/pdf")
    #else:
       # st.write('Please Login to use the calculator!!')

cfc()