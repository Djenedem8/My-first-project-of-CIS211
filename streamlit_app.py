import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title =' Dienebou Sacko | Portfolio',
  page_icon='❤️',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('🌍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏚️ Home', '👩 About', '💼 Projects', '⛷️ Skills' ,'📑 Resume', '📨 Contact' ])

# Home Page
if page == '🏚️ Home':
  st.markdown('<p class="main-header">Dienebou Sacko</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Business Student in Accounting | Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.83', '📚')
  with col2:
      st.metric('Projects', '6', '💻')
  with col3:
      st.metric('Skills', '7+', '🚀')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my futre business plan!👌')
    st.write('''
                I am a Business Student at Medgar Ever College. Currently learning Principle of Management,
                Accounting, payroll, Taxation, and Audit to build my future business as known as Bogolan Fashion Clothing.
            
                📕 **Current Focus:** Doing management plan of my future business.
            
                📚 **Currently Learning:** Principle of Mangement (M200).
                🚓 **Fun Fact:** I can travel to go to Africa by Car!
            ''')
  with col2:
    # Placeholder for image
    st.image('https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=1600', use_column_width=True)

# About Page
elif page == '👩 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2025 - Present: Medgar Evers College'):
    st.write('''
                - Major: Business Administration In Accounting
                - Relevant Coursework: Principles Of Management, Accounting 311, CIS211, Macroeconomics, Taxation,
                - Activities: Basketball Team, Football Team, Run participant
            ''')

  with st.expander('2018 - 2020: ASA College '):
    st.write('''
                - Graduated with honors
                - AP Computer Science A (Score: 5)
                - Founded Coding Club
            ''')

  st.subheader('Interests & Hobbies ✈️')
  interests = ['Pay Roll', 'Taxation', 'Budget Management', 'Football', 'Travel', 'Baseball']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
        st.image('https://payrollnorth.ca/_next/image?url=https:%2F%2Fcdn.durable.co%2Fgetty%2F1c1gNeTMGFtrYGog2OZOhM6rIxZN2J5ViLSSGQRKbU9ywn8nPup35PzF0QaS62yZ.jpeg&w=1920&q=90', use_column_width = True)

    with col2:
        st.subheader('📲 A payroll calculator ')
        st.write('Automated payroll systems and software that use to calcul wages')
        st.caption('**Technologies:** Digital Systems, Tax Withholding, Direct deposit')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('https://wallpapercave.com/wp/wp3730548.jpg', use_column_width = True)
    with col2:
      st.subheader('🧾 Form 1040 from IRS')
      st.write('Download a PDF of the 1040 tax form on the IRS')
      st.caption('**Technologies:** E-filing, data analytics, AI')

elif page == '⛷️ Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Accounting Skills')

  skills_data = {
    'Taxation' : 86,
    'Macroenomic' : 80,
    'Accounting' : 90,
    'CIS211' : 90,
    'Principles Of Management' : 80
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('GDP')
    st.info('Monetaire Value')
    st.warning('Aduit')

  with col2:
    st.success('Quickbook')
    st.info('Software Developed')
    st.warning('Intuit.com')
    
  with col3:
    st.success('Spreadsheet')
    st.info('Analyze Data')
    st.warning('Microsoft Excel')

elif page == '📑 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('Resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📨 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:** djenebouena2008@yahoo.fr

        🖇️ **LinkedIn:** [linkedin.com/in/dienebousacko](https://linkedin.com)

        🖥️ **Github:** [https://github.com/djenedem8](https://github.com)

        🌐 **Instagram:** [@boudjenesacko](https://instagram.com)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍🎓 Student',
            '🎵 Music',
            '🍕 Lunch break',
            '🎮 Gaming',
            '😴 Sleeping'
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().year} Dienebou Sacko </center>',
        unsafe_allow_html = True
    )
    



      









