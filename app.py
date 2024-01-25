import pandas as pd
import streamlit as st

st.divider()
name,photo = st.columns([2,1])
st.write('\n')
name.title('PARVATHALA CHARANSAI')
photo.image('https://res.cloudinary.com/dkh9qnxkd/image/upload/v1706102159/Picsart_24-01-24_18-45-28-814_k5dqdz.png',width=110)
st.divider()

page = st.sidebar.radio('Select Page', ['Home', 'Projects','Feedback'])

if page == 'Home':

    st.header('My Details')

    if st.button('Show Details'):
        with st.expander('Personal Details'):
            st.write('Name : Charansai Parvathala')
            st.caption('Software Engineering Student - pursuing b.tech 2nd year')
            st.caption('In Audisankara college of engineering and technology')
            st.write('Address : Momidi, Chillakur, Nellore 524412')
            st.write('Phone : 8367454451')
            st.write('Mail : charansaiparvathala@gmail.com')

        with st.expander('Educational Details'):
            data = {'Education': ['B.Tech', 'Intermediate', '10th'],'Course': ['CSE','MPC','Regular'],
                    'College Name': ['Audisankara college of engineering and technology',
                                     'Sri Balaji junior college', 'ZPHS Govt (Varagali)'],
                    'Percentage': ['80%', '60%', '87%']}
            st.table(pd.DataFrame(data))

        with st.expander('Family Details'):
            st.write('Mother Name: Sunithamma')
            st.caption('Domestic engineer')
            st.write('Father Name: Radhakrishnaiah')
            st.caption('Former')
            st.write('Sister Name: Lohitha')
            st.caption('Nurse')
    st.divider()
    st.header('My Skills')

    if st.button('Show skills'):
        st.subheader('Technical Skills :')

        with st.expander('C'):
            st.write('I posses very good skills in C')
            st.progress(100)

        with st.expander('Java'):
            st.write('I have very good skills in Java')
            st.write('Including GUI , Graphics')
            st.progress(100)

        with st.expander('SQL'):
            st.write('I can work on databases with SQL')
            st.progress(100)

        with st.expander('DSA'):
            st.write('I can implement data structures using C & JAVA')
            st.progress(95)

        with st.expander('Problem Solving'):
            st.write('I have a good problem solving ability')
            st.progress(80)

        st.subheader('Personal Skills :')

        with st.expander('Communication skills'):
            st.write('Telugu')
            st.progress(100)
            st.write('English')
            st.progress(95)
            st.write('Hindi')
            st.progress(60)

        with st.expander('LeaderShip Skills'):
             st.write('I have good leadership Skills')
             st.progress(75)
    st.divider()
    st.header('Certificates')

    rad = st.selectbox('Select Option To View', ['Default', 'C', 'SQL', 'Problem Solving'], index=0)

    if rad == 'C':
        st.markdown("**C** Certification From **Sololearn**\n\n")
        st.markdown("Sololearn is an application\n"
"we can learn many programing languages from it\n"
"While I am learning C certification it was very fun to learn in sololearn")
        
        st.link_button('See C certificate', 'https://www.sololearn.com/en/certificates/CC-FLQMAH71')

    if rad == 'SQL':
        st.markdown("**SQL Basic** Certification From **Hackerrank**\n\n"
        "HackerRank is well known platform to everyone.\n"
        "Learning SQL in HackerRank is very challenging and exciting")
        
        st.link_button('See SQL Certificate', 'https://www.hackerrank.com/certificates/0b7851c7519e')

    if rad == 'Problem Solving':
        st.markdown("**Problem Solving Basic** certification from **Hackerrank**\n\n"
        "While learning Problem solving Certificate from Hackerrank\n"
   "It was very challenging and difficult to learn\n"
 "But i would like to learn more difficult courses in future")
        st.link_button('See P&S certificate', 'https://www.hackerrank.com/certificates/82e28a3a07c4')

if page == 'Projects':
    st.header('Projects :')
    project = st.selectbox('select project',['Default','Ride WebPage','Caculator','Guessing Game'])

    if project== 'Default':
       st.caption('Select a project from above menu')
    if project == 'Ride WebPage':
        st.write('***Ride Booking & Registration Page (HTML&CSS)***')

        with st.expander('Detailed Description'):
            st.markdown("**Key Features:**")
            st.markdown("1. **Easy Registration:** Simple sign-up for rides, making the onboarding process hassle-free.")
            st.markdown("2. **Seat Booking Made Simple:** Enjoy the convenience of straightforward seat booking with an easy-to-use layout.")
            st.markdown("3. **Real-time Vehicle Tracking:** Stay updated on your journey with real-time vehicle tracking, ensuring a reliable travel experience.")

            st.markdown("**Adaptable Design:**")
            st.markdown("The webpage adjusts seamlessly to laptops, mobiles, and tablets, ensuring a great user experience on any device.")

            st.markdown("**User-Focused:**")
            st.markdown("From registration to tracking, the webpage prioritizes user ease, offering an intuitive and enjoyable journey.")

            st.markdown("**Visual Appeal:**")
            st.markdown("Enhanced by CSS, the webpage boasts a clean and engaging design, contributing to an overall pleasant experience.")

            st.markdown("**In Conclusion:**")
            st.markdown("Our HTML and CSS-powered webpage simplifies the user experience, combining functionality and aesthetics for a delightful journey across devices.")

        st.write('**Check Out Project WebPage here**')
        st.link_button('Visit Page','https://charansaiparvathala.github.io/HTML-CSS-Projects/index.html')

    if project == 'Caculator':
        st.write('***Calculator Using Java with GUI***')

        with st.expander('Detailed Description'):
            st.markdown("**Java GUI Calculator**\n\n"
                        "Welcome to our Java Calculator with a Graphical User Interface (GUI). This calculator is designed to perform basic arithmetic operations with ease.\n\n"
                        "**Challenges Faced:**\n"
                        "During the development of this calculator, we encountered challenges like handling double decimals, double operators, and preventing division by zero.\n\n"
                        "**Key Features:**\n"
                        "- **User-Friendly Interface:** The GUI provides a straightforward platform for performing calculations.\n"
                        "- **Basic Arithmetic Operations:** Addition, subtraction, multiplication, and division are supported.\n"
                        "- **Error Prevention:** Special attention has been given to handling edge cases like double decimals, double operators, and preventing division by zero.\n"
                        "- **Visual Appeal:** The calculator includes a clean and visually appealing design to enhance the user experience.\n\n"
                        "**Why Use Our Calculator?**\n"
                        "- **Ease of Use:** Perform calculations effortlessly with a user-friendly interface.\n"
                        "- **Error-Free Operation:** The calculator is designed to handle challenging scenarios, ensuring accurate results.\n"
                        "- **Visual Design:** Enjoy a visually appealing calculator that makes the experience more enjoyable.\n\n"
                        "**Conclusion:**\n"
                        "Experience the convenience of a Java GUI Calculator that not only performs calculations but also addresses challenges for a smoother user experience.")
        st.write('**Check out Source Code here :**')
        st.link_button('Source Code','https://github.com/CharansaiParvathala/JavaProjects/blob/JavaCalculator/JavaCalculator.java')
    if project == 'Guessing Game':
        st.write('***Guessing Game Using Java with GUI***')

        with st.expander('Detailed Description'):
            st.markdown("**Java GUI Guessing Game with Graphics**\n\n"
                        "Welcome to our Java Guessing Game! This interactive game is designed with a Graphical User Interface (GUI) to make the experience enjoyable and visually engaging.\n\n"
                        "**How to Play:**\n"
                        "1. **Launch the Game:** Open the Java application to start the guessing game.\n"
                        "2. **User-Friendly Interface:** Encounter an intuitive interface with graphics that guide you through the game.\n"
                        "3. **Guess the Number:** Enter your guess in the provided input field to predict the correct number.\n"
                        "4. **Feedback with Graphics:** Receive instant feedback through graphics that visually represent your guess. The game dynamically adjusts the visuals to make the experience interactive.\n"
                        "5. **Winning Moment:** Celebrate your victory when you correctly guess the number! The game will display a cheerful message and graphics to mark your success.\n"
                        "6. **Play Again:** Enjoy the replayability! Reset the game for a new round, challenging yourself to improve your guessing skills.\n\n"
                        "**Key Features:**\n"
                        "- **User-Friendly Interface:** The GUI provides a straightforward platform for an enjoyable gaming experience.\n"
                        "- **Visual Feedback:** Graphics enhance the feedback, making it easy to understand your progress in the game.\n"
                        "- **Dynamic Adjustments:** The game adapts dynamically to your inputs, creating a responsive and engaging environment.\n\n"
                        "**Why Play Our Guessing Game?**\n"
                        "- **Interactive Learning:** Understand Java GUI concepts in a practical setting.\n"
                        "- **Visual Appeal:** Graphics add an extra layer of fun, making the game visually appealing.\n"
                        "- **Accessible to All:** Designed with simplicity, making it accessible to players of all skill levels.\n\n"
                        "**Conclusion:**\n"
                        "Dive into the world of Java GUI gaming with our Guessing Game. Experience the perfect blend of simplicity, interactivity, and visual appeal. Happy guessing!")
        st.write('**Check Source Code here :**')
        st.link_button('Code','https://github.com/CharansaiParvathala/JavaProjects/blob/JavaCalculator/JavaGuessingGame.java')

if page == 'Feedback':
   feed = st.slider('Give Me your rating on this Page',min_value=0,max_value=100,value=50)
   if feed < 30:
      st.warning('Sorry for the disappointment')
   if feed > 90:
      st.success('Thank you for giving your valuable Rating')
   elif feed == 50:
      pass
   elif feed < 50:
      st.markdown('**Give me Suggestion So that I can improve the webpage:**')
      st.text_area('Submit your suggestion')
      if st.button('Submit')
         st.info('Your Feedback noted Thankyou for suggestion')
   elif feed > 60:
      char = st.chat_input('Any Suggestions To improve the site')
        if char:
           st.info('Your Feedback noted Thankyou for suggestion')
    
   