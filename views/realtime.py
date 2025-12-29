import streamlit as st
import utils.api as api
import config
import utils.pdf_gen as pdf_gen

def show_realtime():
    st.markdown("## 🌍 Real-Time AQI Monitor")
    
    st.markdown("""
    <a href="?nav=home" target="_self">
        <button style="
            background: linear-gradient(45deg, #00f3ff, #bd00ff);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 0 10px rgba(189, 0, 255, 0.5);
        ">⬅ Back to Home</button>
    </a>
    <br><br>
    """, unsafe_allow_html=True)
        
    # Cities provided in user's specific order
    city_options = [c.title() for c in config.AQI_CITIES]
        
    # Auto-Analyze on selection by using session state or simply running logic if city is present
    # User requested "select one of it" - slide down options. 
    # We will show data immediately after selection.
    
    CITY_DISPLAY = st.selectbox("Select City", city_options, index=0)
    CITY = CITY_DISPLAY.lower()

    # REUSE EXISTING UTILS BUT ADAPT TO NEW UI
    # User provided direct requests logic, but best practice is to use our api.fetch_aqi
    # api.fetch_aqi returns data['data'] already.
    
    try:
        # Use existing API wrapper for better error handling/caching
        aqi_data = api.fetch_aqi(CITY)
        
        if not aqi_data:
            st.error("❌ AQI data unavailable. Try again later.")
            return

        # EXTRACT DATA
        raw_aqi = aqi_data.get("aqi", "N/A")
        try:
            aqi = round(float(raw_aqi), 2)
            if aqi == int(aqi): aqi = int(aqi)
        except:
            aqi = raw_aqi
        dominent = aqi_data.get("dominentpol", "N/A")
        iaqi = aqi_data.get("iaqi", {})

        # MAIN AQI CARD
        st.markdown(f"""
            <div class='neon-card'>
                <h2>🌬 Current AQI: <span style='color:#00eaff'>{aqi}</span></h2>
                <p>Dominant Pollutant: <b>{str(dominent).upper()}</b></p>
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("###  Detailed Pollutant Cards")
        st.write("")

        # POLLUTANT FULL NAMES & UNITS
        POLLUTANT_NAMES = {
            "PM25": "Fine Particulate Matter (PM2.5)",
            "PM10": "Coarse Particulate Matter (PM10)",
            "O3": "Ozone (O3)",
            "NO2": "Nitrogen Dioxide (NO2)",
            "SO2": "Sulfur Dioxide (SO2)",
            "CO": "Carbon Monoxide (CO)",
            "T": "Temperature (T)",
            "H": "Humidity (H)",
            "P": "Air Pressure (P)",
            "DEW": "Dew Point (DEW)",
            "W": "Wind Speed (W)"
        }

        UNIT_MAP = {
            "PM25": " µg/m³",
            "PM10": " µg/m³",
            "O3": " ppb",
            "NO2": " ppb",
            "SO2": " ppb",
            "CO": " ppm",
            "T": "°C",
            "H": "%",
            "P": " hPa",
            "DEW": "°C",
            "W": " m/s"
        }

        def format_val(v, code):
            try:
                num = float(v)
                rounded = round(num, 2)
                # If it's a whole number, show it as int
                if rounded == int(rounded):
                    rounded = int(rounded)
                return f"{rounded}{UNIT_MAP.get(code, '')}"
            except:
                return str(v)

        # Build pollutant list
        pollutants = []
        for pol, val in iaqi.items():
            code = pol.upper()
            raw_val = val.get("v", "N/A")
            pollutants.append({
                "FullName": POLLUTANT_NAMES.get(code, code),
                "Value": format_val(raw_val, code)
            })

        # DISPLAY CARDS
        cols = st.columns(3)

        for i, item in enumerate(pollutants):
            html = f"""
                <div class='neon-card' style="margin:10px; padding:15px; border-radius:10px; min-height:150px; transition: transform 0.3s; box-shadow: 0 0 10px rgba(0, 183, 235, 0.2);">
                    <h4 style='font-size:18px; color:#00b7eb; margin-bottom: 5px; text-shadow: 0 0 8px #00b7eb;'>{item['FullName']}</h4>
                    <p style='font-size:16px; color: #e0e0e0;'>Value: <b style='color: #ffffff; font-size: 18px; text-shadow: 0 0 5px #ffffff;'>{item['Value']}</b></p>
                </div>
            """
            cols[i % 3].markdown(html, unsafe_allow_html=True)

        st.write("")

        # ---------------------------------------------------------
        # PREMIUM BLUE-NEON PDF
        # ---------------------------------------------------------
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from io import BytesIO

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()

        neon_title = ParagraphStyle(
            'NeonTitle',
            parent=styles['Title'],
            textColor=colors.HexColor("#00bfff"),
            fontSize=28,
            alignment=1
        )

        section_head = ParagraphStyle(
            'SectionHead',
            parent=styles['Heading2'],
            textColor=colors.HexColor("#0099ff"),
            fontSize=18
        )

        story = []

        # Title with City Name
        report_title = f"AQI Forecast Report - {CITY_DISPLAY}"
        story.append(Paragraph(report_title, neon_title))
        story.append(Spacer(1, 20))

        # AQI Section
        story.append(Paragraph(f"<b>Current AQI:</b> <font color='#00aaff'>{aqi}</font>", section_head))
        # Ensure dominant is string
        dom_str = str(dominent).upper() if dominent else "N/A"
        story.append(Paragraph(f"<b>Dominant Pollutant:</b> {dom_str}", styles["Normal"]))
        story.append(Spacer(1, 15))

        story.append(Paragraph("<b>Pollutant Measurements</b>", section_head))
        story.append(Spacer(1, 10))

        # Pollutant Table
        table_data = [["Pollutant", "Value"]]
        for item in pollutants:
            table_data.append([item["FullName"], str(item["Value"])])

        table = Table(table_data, colWidths=[260, 100])

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#00bfff")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, 0), 13),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#e6f7ff")),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#00bfff")),
        ]))

        story.append(table)
        story.append(Spacer(1, 30))

        doc.build(story)
        pdf_data = buffer.getvalue()

        # PREMIUM NEON DOWNLOAD BUTTON
        # Fix: Targeting the inner button element more aggressively and handling hover states
        st.markdown("""
            <style>
                /* Target the specific Streamlit download button container */
                div[data-testid="stDownloadButton"] button {
                    background-image: linear-gradient(90deg, #00eaff, #008cff) !important;
                    background-color: transparent !important; /* Fallback */
                    color: white !important;
                    border: 1px solid #00bfff !important;
                    border-radius: 12px !important;
                    padding: 12px 25px !important;
                    font-size: 18px !important;
                    font-weight: bold !important;
                    box-shadow: 0px 0px 15px rgba(0, 191, 255, 0.6) !important;
                    transition: all 0.3s ease !important;
                    width: 100%;
                }
                
                div[data-testid="stDownloadButton"] button:hover {
                    background-image: linear-gradient(90deg, #00bfff, #007acc) !important;
                    box-shadow: 0px 0px 25px rgba(0, 234, 255, 0.9) !important;
                    transform: scale(1.02) !important;
                    color: #ffffff !important;
                    border-color: #00eaff !important;
                }
                
                div[data-testid="stDownloadButton"] button:active {
                    transform: scale(0.98) !important;
                }
                
                /* Ensure text inside is visible */
                div[data-testid="stDownloadButton"] button p {
                    color: white !important;
                    font-size: 18px !important;
                }
            </style>
        """, unsafe_allow_html=True)

        st.download_button(
            label="Download",
            data=pdf_data,
            file_name=f"{CITY}_AQI_Report.pdf",
            mime="application/pdf",
            help="Download the premium AQI Report",
            key="premium_pdf",
        )

    except Exception as e:
        st.error(f"❌ Error fetching AQI: {str(e)}")
