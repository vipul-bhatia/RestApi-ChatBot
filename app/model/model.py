import pickle 
import re
from pathlib import Path
import nltk 
from nltk.stem import WordNetLemmatizer
import sklearn


__version__ = "0.1.0"


BASE_DIR = Path(__file__).resolve(strict=True).parent

with open (f"{BASE_DIR}/abc-{__version__}.pkl", "rb") as f:
    model = pickle. load (f)

classes = ['80%.',
       'Admission to NMIMS is based on entrance exams like NMIMS-NPAT followed by personal interview.',
       'All medical facilities available on the campus.',
       'All the best to you too!',
       'As an AI language model I dont have a father or any human parents.',
       'As an AI language model I dont have parents.',
       'As an AI language model I dont have personal information but I can provide helpful answers and assistance.',
       'At post Muktainagar; Taluka Shirpur; Dist. Dhule; Maharashtra - 425405; India https://engineering-shirpur.nmims.edu/contact-us/',
       'Bye! Do you need help with anything else?',
       'Bye! Is there anything else youd like to discuss?',
       'Candidates have to appear for the entrance exam followed by personal interview for admission to NMIMS.',
       'Congratulations on your retirement! Is there something specific you need help with before you go?',
       'Course not Available', 'Curse not available.',
       'Dr. Nitin S. Choubey is the current Professor and Head of the Computer Engineering department at NMIMS Shirpur campus. ',
       'Each department at NMIMS Shirpur has well-equipped laboratories for students to conduct experiments and practicals.',
       'Farewell see you soon!',
       'Farewell! Is there anything else you need help with today?',
       'Fine! How can I assist you today?',
       'For a list of events organized by NMIMS Shirpur please visit the official college website at https://engineering-shirpur.nmims.edu/student-life/cultural-activities',
       'For a list of events organized by NMIMS Shirpur please visit the official college website at https://engineering-shirpur.nmims.edu/student-life/cultural-activities/',
       'For engineering admission to NMIMS candidates have to appear for the NMIMS-NPAT exam followed by personal interview.',
       'Fruit options are available in the college mess. ',
       'Good afternoon to you too! How can I assist you today?',
       'Good day to you too! What brings you to our chat today?',
       'Good evening to you too! How can I assist you today?',
       'Good morning to you too! How can I assist you today?',
       'Goodbye! Have a great day.',
       'Goodbye! Is there anything else youd like to talk about?',
       'Greetings to you too! Is there anything you need help with?',
       'Hello Im an AI language model here to assist you.',
       'Hello there! How can I assist you?',
       'Hello! How can I assist you today?',
       'Hello! Is there something I can help you with?',
       'Hello. I am an AI language model here to assist you.',
       'Hey there! Is there something you need assistance with today?',
       'Hi my name is NBOT.',
       'I am NBOT a chatbot designed to assist you with your queries.',
       'I am a chatbot designed to assist you with your queries. How can I assist you today?',
       'I am a chatbot. How can I assist you today?',
       'I am called NBOT. How can I assist you today?',
       'I dont have any personal information to provide.',
       'I was developed by Priyam Sekra and Vipul Bhatia.',
       'I was made by Vipul Bhatiya and Priyam Sekra.',
       'I was not discovered but created by Priyam Sekra and Vipul Bhatia.',
       'IBM is one of the companies that visits the college for recruitment. For more information visit: https://engineering-shirpur.nmims.edu/placements/ ',
       'Im an AI language model designed to answer questions and provide assistance.',
       'Im doing well thank you. Is there anything you need help with?',
       'Im doing well. thank you. How can I assist you today?',
       'Im sorry I am a virtual assistant and cannot be called. You can type your queries here.',
       'Im sorry I could not find a specific telephone number for the civil department. You may be able to find contact information on the NMIMS Shirpur University website: https://shirpur.nmims.edu/contact-us/',
       'Im sorry can you please provide more specific information about what you are looking for?',
       'Im sorry. I am a virtual assistant and cannot be called. You can type your queries here.',
       'Im sorry. I am a virtual assistant and do not have a contact number.',
       'Im sorry. I am a virtual assistant and do not have a phone number. You can find contact information for NMIMS Shirpur University on their website: https://shirpur.nmims.edu/contact-us/',
       'Im sorry. I could not find a specific telephone number for the ICT department. You may be able to find contact information on the NMIMS Shirpur University website: https://shirpur.nmims.edu/contact-us/',
       'Im sorry. I could not find a specific telephone number for the computer department. You may be able to find contact information on the NMIMS Shirpur University website: https://shirpur.nmims.edu/contact-us/',
       'Im sorry. I could not find a specific telephone number for the electrical department. You may be able to find contact information on the NMIMS Shirpur University website: https://shirpur.nmims.edu/contact-us/',
       'It is the annual cultural fest of NMIMS shirpur.',
       'It was a pleasure seeing you too! Is there something I can help you with?',
       'Its going well. How can I assist you?',
       'Maximum student intake varies from branch to branch and is decided by the university based on the availability of resources and infrastructure. For specific details about maximum student intake for each branch please refer to the NMIMS University Shirpur website or contact the university directly.',
       'Microsoft is one of the companies that visits the college for recruitment. ',
       'My creators are Priyam Sekra and Vipul Bhatia.',
       'My name is NBOT. How can I assist you today?',
       'My name is NBOT. I am your assistant. You can ask me anything about NMIMS University.',
       'NMIMS (Narsee Monjee Institute of Management Studies) is a private deemed-to-be university. It offers undergraduate postgraduate and doctoral-level programs in various fields such as management engineering commerce law science architecture liberal arts and more. NMIMS is known for its high-quality education and is consistently ranked among the top 10 B-Schools in India.',
       'NMIMS Shirpur has a modern and well-equipped infrastructure that includes spacious classrooms laboratories',
       'NMIMS Shirpur has a zero-tolerance policy towards ragging. The institute has implemented various measures to prevent ragging such as an Anti-Ragging Committee etc.',
       'NMIMS Shirpur has several departments including Computer Engineering Information Technology Electronics Engineering Mechanical Engineering and Electrical Engineering. Each department has well-equipped laboratories for students to conduct experiments and practicals.',
       'NMIMS University Shirpur does not offer a course in Civil and Rural Engineering.',
       'NMIMS University Shirpur has qualified and experienced faculty members.',
       'NMIMS University Shirpur is located in Shirpur Maharashtra',
       'NMIMS University Shirpur is located in Shirpur Maharashtra India. https://engineering-shirpur.nmims.edu/contact-us/',
       'NMIMS University Shirpur is situated in Shirpur Maharashtra India. https://engineering-shirpur.nmims.edu/contact-us/',
       'NMIMS University Shirpur offers various branches like computer engineering Electrical Engineering',
       'NMIMS University Shirpur offers various undergraduate and postgraduate courses across various disciplines like engineering management etc.',
       'NMIMS University Shirpur offers various undergraduate and postgraduate courses across various disciplines like engineering management etc. You can find the list of courses on their official website at https://engineering.nmims.edu/programs/',
       'NMIMS University Shirpur provides IT solutions. Please visit the colleges website for more information: https://engineering-shirpur.nmims.edu/',
       'NMIMS University Shirpur provides free internet services for students and staff.',
       'NMIMS University Shirpur provides pure drinking water for students and staff.',
       'NMIMS University Shirpur provides various facilities for hostel students including mess facilities',
       'NMIMS University Shirpur provides various facilities including library sports gymnasium medical facilities and transport facilities.',
       'NMIMS University Shirpur provides various facilities including library sports gymnasium medical facilities and transport facilities. Please refer to the official website for more details.',
       'NMIMS University Shirpur; At post Muktainagar; Taluka Shirpur; Dist. Dhule; Maharashtra - 425405; India https://engineering-shirpur.nmims.edu/',
       'NMIMS University Shirpur; At post Muktainagar; Taluka Shirpur; Dist. Dhule; Maharashtra - 425405; India https://engineering-shirpur.nmims.edu/contact-us/',
       'NMIMS University Shirpur; At post Muktainagar; Taluka Shirpur; Dist. Dhule; Maharashtra - 425405; India: https://engineering-shirpur.nmims.edu/contact-us/',
       'NMIMS holds many fests for example protashan ambiora etc.',
       'NMIMS strongly prohibits ragging.',
       'Narsee Monjee Institute of Management Studies (NMIMS) Shirpur was established in the year 2007.',
       'Nice to hear that! How can I help you?',
       'Nice to meet you too! Do you have any questions?',
       'No citizenship is not required for admission to NMIMS University Shirpur. Please visit the colleges website for more information: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions/',
       'No project work is not a course. It is a mandatory component of the curriculum for many courses.',
       'Not much how about you? How can I assist you?',
       'Not much how about you? Is there something youd like to discuss?',
       'Of course ask me anything youd like to know.',
       'Okay have a great day! Is there something specific you need help with before you go?',
       'Okay take care! Is there something else you need help with today?',
       'Okay talk to you later!',
       'Okay. have a good one! Is there something specific you need help with before you go?',
       'Online training programs are available at NMIMS University Shirpur. Please visit the colleges website for more information: https://engineering-shirpur.nmims.edu/academic/programmes/',
       'Original documents are required for admission to NMIMS University Shirpur. Please visit the colleges website for more information: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions/',
       'Please provide a starting point for the route. ',
       'Please visit the colleges website for detailed information regarding certificates required for admission to NMIMS University Shirpur: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions/',
       'Please visit the colleges website for detailed information regarding documents needed for admission to NMIMS University Shirpur: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions/',
       'Please visit the colleges website for detailed information regarding documents required for admission to NMIMS University Shirpur: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions',
       'Please visit the colleges website for detailed information regarding documents required for admission to NMIMS University Shirpur: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions/',
       'Please visit the colleges website for detailed information regarding scholarship and fee structure at NMIMS University Shirpur: https://engineering-shirpur.nmims.edu/admissions/undergraduate-admissions/fees/',
       'Pleased to meet you too! How can I assist you today?',
       'Regards to you too! How can I assist you?',
       'Samsung is one of the companies that visits the college for recruitment.For more information visit: https://engineering-shirpur.nmims.edu/placements/',
       'See you later! How can I assist you today?',
       'See you later! Is there something you need assistance with today?',
       'See you soon! Is there something specific you need help with today?',
       'Several companies visit the college for recruitment including IBM',
       'Several companies visit the college for recruitment. For more information visit: https://engineering-shirpur.nmims.edu/placements/',
       'Sorry I do not have access to the latest information about the fees for Computer Engineering at NMIMS University Shirpur. It would be best to check the official website of the university for the latest updates on the fees. Here is the link to the official website: https://engineering-shirpur.nmims.edu/',
       'Sorry I do not have access to the latest information about the total fees of BE at NMIMS University Shirpur. It would be best to check the official website of the university for the latest updates on the fees. Here is the link to the official website: https://engineering-shirpur.nmims.edu/',
       'Sorry I do not have access to the latest information about the tuition fees for NMIMS University Shirpur. It would be best to check the official website of the university for the latest updates on the fees. Here is the link to the official website: https://engineering-shirpur.nmims.edu/',
       'Students can apply for leave by submitting a leave application to the warden of their hostel.',
       'Students can book a room in the hostel by filling out a hostel admission form on the NMIMS Shirpur website at https://engineering-shirpur.nmims.edu/academics/hostel-facility/',
       'Sure. Feel free to ask anything.',
       'Sure. Id love to stay in touch.',
       'Sure. talk to you soon! What can I help you with today?',
       'Take care and have a great day! Is there something else I can help you with?',
       'Take care and talk to you later! Do you need assistance with anything else?',
       'Take care and talk to you soon! Do you need assistance with anything else?',
       'Take care!', 'Take care! Do you need help with anything else?',
       'Thank you for the good wishes! How can I assist you?',
       'Thank you for the warm welcome! Is there anything you need help with?',
       'Thank you for the welcome! How can I assist you?',
       'Thank you you too! Is there anything else I can help you with?',
       'Thank you you too! Is there something else I can assist you with?',
       'Thank you! Is there anything else I can assist you with?',
       'Thank you. you too! Is there something else I can help you with?',
       'Thanks!',
       'The NMIMS Shirpur library has a vast collection of books journals and research papers. Students can also access e-books and online databases.',
       'The average package offered during placements varies annually and may not have a fixed figure. For more information visit: https://engineering-shirpur.nmims.edu/placements/',
       'The break time is scheduled depending on the daily routine of the college.',
       'The break timings may vary depending on the schedule.',
       'The campus has a canteen that serves a variety of food items and snacks to students and staff at reasonable prices.',
       'The campus has a high-speed internet connection that provides students with access to online resources and e-learning platforms.',
       'The campus has several amenities including a library sports facilities a gymnasium and a cafeteria.',
       'The canteen of the college is located in the main building. ',
       'The canteen prices are affordable for students. ',
       'The classes will be over by 5:00 pm.',
       'The college building has multiple floors and houses classrooms laboratories and administrative offices.',
       'The college can be reached via bus train or car. The nearest railway station is Dhule and the nearest airport is Aurangabad or indore. https://engineering-shirpur.nmims.edu/contact-us/',
       'The college can be reached via bus train or car. The nearest railway station is Dhule and the nearest airport is Aurangabad. https://engineering-shirpur.nmims.edu/contact-us/',
       'The college canteen is a place to eat for students. ',
       'The college canteen provides a variety of food options and is satisfactory. ',
       'The college canteen provides a variety of food options. ',
       'The college canteen provides fresh food options. ',
       'The college canteen provides healthy food options. ',
       'The college conducts online placement sessions for students. ',
       'The college ends at 5:00 pm.',
       'The college has a canteen facility available for students with a variety of food options named aditi. ',
       'The college has a health clinic on campus that provides medical assistance to students and staff.',
       'The college has an active placement cell to facilitate campus recruitment of students. For more information visit: https://engineering-shirpur.nmims.edu/placements/',
       'The college has an active placement cell to facilitate campus recruitment of students. For more information visit: https://engineering-shirpur.nmims.edu/placements/ ',
       'The college has an active placement cell to facilitate campus recruitment of students.For more information visit: https://engineering-shirpur.nmims.edu/placements/',
       'The college has canteen facilities available for students with a variety of food options',
       'The college has canteen facilities available for students with a variety of food options.',
       'The college has canteen facilities available for students with a variety of food options. ',
       'The college hours are from 10:00 am to 5:00 pm.',
       'The college is open from Monday to Friday.',
       'The college operates from 10:00 am to 5:00 pm.',
       'The college organizes several events throughout the year including cultural festivals technical events and sports competitions for example protsahan and ambiora.',
       'The college provides pure and safe drinking water through water coolers and RO systems installed across the campus.',
       'The college provides students with necessary study equipment including projectors whiteboards and audio-visual aids.',
       'The college starts at 10:00 am.',
       'The college time routine varies depending on the schedule.',
       'The college timing is from 10:00 am to 5:00 pm.',
       'The college works from Monday to Friday.',
       'The cost of filling the admission form for NMIMS varies as per the course. Please refer to the official website for the same.',
       'The courses in Electrical Engineering at NMIMS University Shirpur include Power Systems Electrical Machines Control Systems Electrical Measurements and Instrumentation etc.',
       'The courses in Electronics Engineering at NMIMS University Shirpur include Analog Electronics Digital Electronics',
       'The courses in IT Engineering at NMIMS University Shirpur include Data Structures and Algorithms Database Management Systems Operating Systems Computer Networks etc.',
       'The current Director of SVKMs NMIMS Shirpur Campus is Dr. Akshay Malhotra and he can be reached at akshay.malhotra@nmims.edu.',
       'The current Director of SVKMs NMIMS Shirpur Campus is Dr. Akshay Malhotra and he can be reached at akshay.malhotra@nmims.edu. ',
       'The distance between Indore and NMIMS Shirpur campus is approximately 215 km. You can travel by car or bus.',
       'The distance between Mumbai and NMIMS Shirpur campus is approximately 290 km.',
       'The duration of each subject may vary depending on the schedule.',
       'The eligibility criteria for admission to NMIMS varies as per the course. Please refer to the official website for the same.',
       'The eligibility criteria for engineering admission to NMIMS is a minimum of 50% marks in 10+2 with Physics Chemistry and Mathematics.',
       'The eligibility for admission to NMIMS varies as per the course. Please refer to the official website for the same.',
       'The food menu of the college canteen changes regularly with a variety of options available. ',
       'The girls hostel is located within the campus of NMIMS University Shirpur. https://engineering-shirpur.nmims.edu/facilities/hostel-facilities/',
       'The hostel fees vary depending on the hostel and the room type. For more information please visit the NMIMS Shirpur website at https://engineering-shirpur.nmims.edu/academics/hostel-facility/',
       'The hostel is located within the campus so the distance between the hostel and the college is minimal.',
       'The hostel remains open during holidays and vacations. However the college remains closed on national and state holidays.',
       'The laboratories at NMIMS Shirpur are well-equipped with modern equipment and technology to provide students with hands-on experience and practical knowledge.',
       'The name of the CSE HOD is not available. ',
       'The number of CSE HOD is not available. ',
       'The number of floors in the college building varies depending on the block.',
       'The official result site for NMIMS University Shirpur is https://nmims.edu/results/',
       'The package offered during placements varies annually and may not have a fixed figure.For more information visit: https://engineering-shirpur.nmims.edu/placements/',
       'The proper procedure to get admission to NMIMS is to appear for the NMIMS-NPAT exam followed by personal interview.',
       'The shortest path to reach NMIMS University Shirpur may vary depending on the starting location. Please provide a starting point for the route.',
       'The telephone number for NMIMS Shirpur University is +91-2563-286551.',
       'The telephone number for NMIMS Shirpur University is +91-2563-286551. You can find contact information for NMIMS Shirpur University on their website: https://shirpur.nmims.edu/contact-us/',
       'The time for each period is 1 hour.',
       'The time interval of each subject may vary depending on the schedule.',
       'The total time schedule of the college is from 10:00 am to 5:00 pm.',
       'There are separate hostels for boys and girls on campus.',
       'There is a boys hostel available within the campus of NMIMS University Shirpur. https://engineering-shirpur.nmims.edu/facilities/hostel-facilities/',
       'This is NBOT a chatbot designed to assist you with your queries.',
       'To reach Dr. Nitin Chaubey visit nmims website. ',
       'Various training programs are offered by NMIMS University Shirpur. Please visit the colleges website for more information: https://engineering-shirpur.nmims.edu/academic/programmes/',
       'Welcome back! Is there something specific you need help with today?',
       'What specific details are you looking for?',
       'What specific information details would you like me to provide?',
       'What specific information would you like me to provide?',
       'Yes I am called NBOT. How can I assist you today?',
       'Yes I can answer questions and provide information to help you get to know me better.',
       'Yes NMIMS University Shirpur provides hostel facilities for both boys and girls. For more information about the hostel facilities',
       'Yes NMIMS University Shirpur provides room sharing options for hostel students. For more information about the hostel facilities',
       'Yes NMIMS University Shirpur provides transport facilities for students and staff.',
       'Yes NMIMS conducts NMIMS-NPAT exam for admission to various courses including engineering.',
       'Yes candidates have to fill the admission form available on the official website of NMIMS for admission. https://www.nmims.edu/shirpurcampus',
       'Yes family members are allowed to visit students in the hostel.',
       'Yes the college is open on Saturdays.',
       'Yes. Im here. How can I assist you today?',
       'You are chatting with NBOT a chatbot designed to assist you with your queries.',
       'You are talking to NBOT a chatbot designed to assist you with your queries.',
       'You can call me NBOT. How can I assist you today?',
       'You can contact NMIMS Shirpur University through their website or by phone. Their contact information is available here: https://shirpur.nmims.edu/contact-us/',
       'You can find contact information for NMIMS Shirpur University on their website: https://shirpur.nmims.edu/contact-us/',
       'You can find department contact information on the NMIMS Shirpur University website: https://shirpur.nmims.edu/contact-us/',
       'You can find information about the exam section at NMIMS Shirpur University on their website: https://shirpur.nmims.edu/examination/',
       'You can find information about the faculty and staff at NMIMS Shirpur University on their website: https://shirpur.nmims.edu/faculty-and-research/',
       'You can find the detailed syllabus of each branch on the official website of NMIMS University Shirpur. Official website https://engineering.nmims.edu/programs/',
       'You can find the list of courses offered by NMIMS University Shirpur on their official website at https://engineering.nmims.edu/programs/',
       'You can find the syllabus for various programs offered at NMIMS University Shirpur on their official website under the Academics section. Heres the link: https://engineering-shirpur.nmims.edu/academics/syllabus/',
       "You can find today's mess menu on this app. ",
       'You can get to know me by asking me questions and requesting information.',
       'You can type your queries here and I will do my best to help you. You can find contact information for NMIMS Shirpur University on their website: https://shirpur.nmims.edu/contact-us/',
       'You need to maintain 80% attendance to be promoted to next semester.',
       'Youre welcome! Do you have any further questions?',
       'aditi is college canteen. It is open till 7PM.',
       'aditi is open till 7PM.',
       'all types of sports facilities and courts available.',
       'amphitheater of nmims shirpur in front of girls hostel.',
       'as an ai model i do not have the ability to love.',
       'as an ai model i do not have the ability to marry.', 'cant help.',
       'centre of the academic wings.', 'extension of A wing.',
       'for academic leave you must contact your assigned mentor.',
       'get lost.', 'https://engineering-shirpur.nmims.edu/contact-us/',
       'https://nmims.edu/about/photogallery-shirpur-campus/',
       'https://nmims.secure.force.com/',
       'it is the annual tech fest of NMIMS SHIRPUR.',
       'it is the central foyer located in the centre of the academic wings.',
       'nmims has mess where students can collectively have their meals.',
       'prem milan chouk is a fountain area of nmims shirpur named by the students.',
       'there is a dress code for students at NMIMS University Shirpur. The uniform is mandatory for students.',
       'yes.', 'you bitch.',
       'you can registor for the admission process here: https://www.nmims.edu/shirpurcampus',
       'you shut up.']

lemmatizer = WordNetLemmatizer()
def predict_pipeline(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(text)
    pred = model.predict([text])
    return classes[pred[0]]