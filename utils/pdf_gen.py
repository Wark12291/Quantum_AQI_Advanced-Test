from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
import datetime

def generate_enhanced_pdf_report(title, metadata, summary_stats, df):
    """
    Generate a professional PDF report optimized for a single-page layout.
    """
    buffer = BytesIO()
    # Maximize vertical space with tighter margins
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=30, bottomMargin=30, leftMargin=40, rightMargin=40)
    styles = getSampleStyleSheet()

    # Custom Styles
    neon_blue = colors.HexColor("#00f3ff")
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        textColor=colors.HexColor("#00bfff"),
        fontSize=20,
        alignment=1,
        spaceAfter=15
    )

    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        textColor=colors.grey,
        fontSize=9,
        alignment=1,
        spaceAfter=15
    )

    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        textColor=neon_blue,
        fontSize=14,
        spaceBefore=10,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=11
    )
    
    table_header_style = ParagraphStyle(
        'TableHeaderStyle',
        parent=styles['Normal'],
        textColor=colors.white,
        fontSize=10,
        fontName='Helvetica-Bold'
    )

    table_cell_style = ParagraphStyle(
        'TableCellStyle',
        parent=styles['Normal'],
        fontSize=8,
        leading=10
    )

    story = []

    # Title
    story.append(Paragraph(title.upper(), title_style))
    
    # Metadata
    for line in metadata:
        story.append(Paragraph(line, header_style))
    
    story.append(Spacer(1, 5))

    # Summary Section
    story.append(Paragraph("SUMMARY STATISTICS", section_style))
    for stat in summary_stats:
        story.append(Paragraph(f"• {stat}", body_style))
    
    story.append(Spacer(1, 15))

    # Detailed Data Section
    story.append(Paragraph("DETAILED DATA VIEW", section_style))
    story.append(Spacer(1, 5))

    # Prepare Table Data with Paragraphs for wrapping
    table_data = []
    
    # Header Row
    header_row = [Paragraph(col, table_header_style) for col in df.columns]
    table_data.append(header_row)
    
    # Data Rows
    for _, row in df.iterrows():
        table_data.append([Paragraph(str(val), table_cell_style) for val in row.values])
    
    # Optimized column widths (Total ~532 pts for 40pt margins)
    # Letter width is 612. 612 - 40 - 40 = 532.
    col_widths = [100, 35, 90, 120, 180] 
    
    table = Table(table_data, hAlign='LEFT', colWidths=col_widths, repeatRows=1)
    
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), neon_blue),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f0faff")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#c0e0f0")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fdff")])
    ]))

    story.append(table)

    doc.build(story)
    buffer.seek(0)
    return buffer

def generate_pdf_report(data_dict, title="AQI Report"):
    """
    Legacy support for simple reports.
    """
    from reportlab.pdfgen import canvas
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    p.setFont("Helvetica-Bold", 24)
    p.drawString(50, height - 50, title)
    
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 80, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    y = height - 120
    p.setFont("Helvetica", 14)
    for key, value in data_dict.items():
        p.drawString(50, y, f"{key}: {value}")
        y -= 25
        
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
