from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, HRFlowable
from faker import Faker
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect
import random
import string

faker = Faker()


def generate_fake_resume(output_path, name, email, phone_number, address, languages, skills, occupation, experience, education,
                         certifications, volunteer_experiences, has_layout):

    # Create document template with adjusted margins
    doc = SimpleDocTemplate(output_path, pagesize=letter, leftMargin=72, rightMargin=72, topMargin=50, bottomMargin=72)

    # Define styles
    title_alignment = random.choice([TA_LEFT, TA_CENTER])
    styles = getSampleStyleSheet()
    title_font = random.choice(["Times-BoldItalic", "Helvetica-Bold", "Courier-Bold"])
    heading_font = random.choice(["Helvetica", "Courier", "Times-Roman"])
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontName=title_font, fontSize=22, alignment=title_alignment)
    heading_style = ParagraphStyle('Heading', parent=styles['Heading1'], fontName=heading_font, fontSize=14)
    normal_style = styles['Normal']

    # Define possible options for HRFlowable
    hr_options = [
        {"width": "100%", "thickness": 1, "lineCap": 'round', "color": styles['Normal'].textColor},
        {"width": "100%", "thickness": 0.5, "lineCap": 'square', "color": "#0000FF"},
        {"width": "100%", "thickness": 1, "lineCap": 'butt', "color": "#00FF00"},
        {"width": "80%", "thickness": 1, "lineCap": 'butt', "color": "#c0c0c0"},
        {"width": "75%", "thickness": 1.5, "lineCap": 'round', "color": "#778899", "dash": (2, 2)},
        {"width": "100%", "thickness": 1, "lineCap": 'butt', "dash": (5, 5), "color": "#333333"},
        {"width": "100%", "thickness": 1.5, "lineCap": 'butt', "dash": (3, 2), "color": "#D6C6FB"},
        {"width": "100%", "thickness": 1, "lineCap": 'butt', "dash": (5, 5), "color": "#333333"},
        {"width": "100%", "thickness": 2, "lineCap": 'round', "dash": (10, 2, 5, 2), "color": "#FF5733"},
        {"width": "100%", "thickness": 0.5, "lineCap": 'square', "dash": (15, 5, 5, 5), "color": "#00FF00"},
        {"width": "100%", "thickness": 1, "lineCap": 'butt', "dash": (5, 10), "color": "#FFD700"},
        {"width": "100%", "thickness": 2, "lineCap": 'round', "dash": (20, 5), "color": "#9400D3"},
        {"width": "100%", "thickness": 1, "lineCap": 'square', "dash": (5, 15, 10, 5), "color": "#00CED1"},
        {"width": "100%", "thickness": 2, "lineCap": 'round', "color": "#0066CC"},
        {"width": "100%", "thickness": 1, "lineCap": 'square', "color": "#008080"},
        {"width": "100%", "thickness": 2, "lineCap": 'round', "color": "#993366"},
        {"width": "100%", "thickness": 1, "lineCap": 'butt', "color": "#663300"},
    ]

    # Pick a random style for spacers and background color if specified
    spacer_style = random.choice(hr_options)

    # Create a list to hold resume components
    elements = []

    # Add rectangle layout
    if has_layout:
        # Define a list of elegant and subtle colors to choose from
        color_options = [
            colors.Color(0.69, 0.77, 0.87),  # Light Sky Blue
            colors.Color(0.88, 1.0, 1.0),  # Light Cyan
            colors.Color(0.69, 0.77, 0.87),  # Light Steel Blue
            colors.Color(0.47, 0.53, 0.6),  # Light Slate Gray
            colors.Color(0.9, 0.9, 0.98),  # Lavender
            colors.Color(0.83, 0.83, 0.83),  # Light Gray
            colors.Color(1.0, 0.63, 0.48),  # Light Salmon
            colors.Color(1.0, 1.0, 0.88),  # Light Yellow
            colors.Color(0.98, 0.98, 0.82),  # Light Goldenrod Yellow
            colors.Color(1.0, 0.71, 0.76),  # Light Pink
            colors.Color(0.56, 0.93, 0.56),  # Light Green
            colors.Color(0.13, 0.7, 0.67)  # Light Sea Green
        ]

        # Randomly select a color from the list
        random_color = random.choice(color_options)

        rect = Drawing(100, 100)
        rect.add(Rect(0, 50, 460, 50, strokeColor=random_color, fillColor=random_color))
        elements.append(rect)

    # Add name
    elements.append(Paragraph(f"<b>{name}</b>", title_style))
    elements.append(Spacer(1, 12))  # Add spacer for spacing

    # Label
    phone_label = random.choice(["Phone", "Phone Number"])
    email_label = random.choice(["Email", "E-mail", "E-mail Address"])

    # Add contact information
    elements.append(Paragraph(f"{phone_label}: {phone_number}<br/>Address: {address}<br/>{email_label}: {email}", normal_style))
    elements.append(Spacer(1, 12))

    # Add separator
    elements.append(HRFlowable(**spacer_style))

    # Randomize the order of sections
    sections = ["Languages", "Skills", "Occupation", "Experience", "Education", "Certifications", "Volunteer Experience", "About me"]
    random.shuffle(sections)

    # Iterate over sections and add content
    for section in sections:
        if section == "Languages":
            elements.append(Paragraph(f"{section}:", heading_style))
            for language in languages:
                elements.append(Paragraph(f"- {language}", normal_style))
        elif section == "Skills":
            section_name = random.choice(["Skills", "Competencies", "Talents", "Skillset", "Strengths", "Skills"])
            elements.append(Paragraph(f"{section_name}:", heading_style))
            for skill in skills:
                elements.append(Paragraph(f"- {skill}", normal_style))
        elif section == "Occupation":
            section_name = random.choice(["Job Title", "Position", "Occupation", "Profession"])
            elements.append(Paragraph(f"{section_name}: {occupation}", heading_style))
        elif section == "Experience":
            section_name = random.choice(["Work Experience", "Experience"])
            elements.append(Paragraph(f"{section}:", heading_style))
            for exp in experience:
                elements.append(Paragraph(f"- {exp}", normal_style))
        elif section == "Education":
            section_name = random.choice(["Academic Background", "Educational Qualifications", "Formal Education", "Education"])
            elements.append(Paragraph(f"{section_name}:", heading_style))
            for edu in education:
                elements.append(Paragraph(f"- {edu}", normal_style))
        elif section == "Certifications":
            elements.append(Paragraph(f"{section}:", heading_style))
            for cert in certifications:
                elements.append(Paragraph(f"- {cert}", normal_style))
        elif section == "Volunteer Experience":
            elements.append(Paragraph(f"{section}:", heading_style))
            volunteer_samples = random.sample(volunteer_experiences, min(len(volunteer_experiences), random.randint(2, 3)))
            for volunteer_exp in volunteer_samples:
                elements.append(Paragraph(f"- {volunteer_exp}", normal_style))
        elif section == "About me":
            section_name = random.choice(["About me", "Personal Quote", "Work Vision", "Personal"])
            elements.append(Paragraph(f"{section_name}:", heading_style))
            about_me_text = random.choice(about_me)
            elements.append(Paragraph(f"{about_me_text}", normal_style))

        # Add spacer after each section
        elements.append(Spacer(1, 12))

        # Add separator after each section except the last one
        if section != sections[-1]:
            elements.append(HRFlowable(**spacer_style))


    # Build the PDF
    doc.build(elements)


# Example usage
output_folder = r'C:\Users\kelly\OneDrive\Bureaublad\Generated Fake Resumes\\'

# Define possible values for occupations, experiences, educations, and certifications
occupations = [
    "Social Media Coordinator", "Marketing Manager", "Content Writer", "Graphic Designer",
    "Digital Marketing Specialist", "Brand Manager", "Public Relations Coordinator", "Business Analyst",
    "RPA Developer", "Data Engineer", "Software Developer", "UX/UI Designer", "Product Manager",
    "Financial Analyst", "Human Resources Manager", "Project Manager", "Sales Representative",
    "Customer Success Manager", "Data Scientist", "Web Developer", "IT Consultant",
    "Cybersecurity Analyst", "Cloud Solutions Architect", "E-commerce Manager",
    "Artificial Intelligence Engineer", "Supply Chain Analyst", "Healthcare Administrator",
    "Mobile App Developer", "Video Producer", "Event Planner", "Digital Content Strategist",
    "User Experience Researcher", "Content Marketing Manager", "SEO Specialist",
    "Network Administrator", "Database Administrator", "Digital Advertising Specialist",
    "Data Analyst", "Operations Manager", "Technical Writer", "Brand Strategist",
    "Financial Advisor", "Investment Banker", "Economist", "Financial Planner",
    "Actuary", "Auditor", "Compliance Officer", "Credit Analyst",
    "Portfolio Manager", "Loan Officer", "Tax Consultant", "Insurance Underwriter",
    "Treasury Analyst", "Financial Controller", "Wealth Manager", "Risk Manager",
    "Market Research Analyst", "Financial Research Analyst", "Fundraiser", "Nonprofit Manager"
]



experiences = [
    "Managed and grew social media channels at Google for 2 years as a Social Media Coordinator, increasing engagement by 50%.",
    "Created and scheduled content calendars at Apple for 3 years as a Marketing Manager, ensuring consistent brand messaging.",
    "Contributed to the creation of social media graphics, videos, and other multimedia content at Facebook for 2 years as a Graphic Designer.",
    "Analyzed social media performance metrics and provided insights for optimization at Amazon for 2.5 years as a Digital Marketing Specialist.",
    "Developed and implemented digital marketing campaigns across multiple platforms at Microsoft for 3.5 years as a Brand Manager.",
    "Designed branding materials including logos, brochures, and marketing collateral at Nike for 2 years as a Graphic Designer.",
    "Executed public relations strategies at Coca-Cola for 2.5 years as a Public Relations Coordinator to enhance brand visibility and reputation.",
    "Helped during Master Open Days at the University, and gave presentations about the program.",
    "Developed and designed an app that helps students finalize their thesis at Spotify for 1 year as an App Developer.",
    "Conducted market research at McKinsey & Company for 2 years as a Market Research Analyst to identify potential opportunities and threats.",
    "Implemented SEO strategies at IBM for 2.5 years as an SEO Specialist to improve website visibility and organic traffic.",
    "Managed client relationships and ensured customer satisfaction at Deloitte for 3 years as a Client Relations Manager.",
    "Led cross-functional teams in project execution and delivery at Accenture for 4 years as a Project Manager.",
    "Performed data analysis at Oracle for 2 years as a Data Analyst to drive business decision-making.",
    "Collaborated with sales teams at Salesforce for 3 years as a Marketing Strategist to develop effective marketing strategies.",
    "Provided training and mentorship to junior team members at LinkedIn for 2.5 years as a Senior Mentor.",
    "Organized and facilitated workshops and seminars on various topics at TED as a Workshop Facilitator.",
    "Optimized user experiences through usability testing and feedback analysis at Adobe for 2 years as a UX Researcher.",
    "Managed and optimized paid advertising campaigns on social media platforms at Twitter for 2 years as a Paid Advertising Specialist.",
    "Developed and executed influencer marketing strategies at Instagram for 3 years as an Influencer Marketing Manager.",
    "Coordinated and conducted market research surveys to gather consumer insights at Procter & Gamble for 2.5 years as a Market Research Coordinator.",
    "Implemented email marketing automation workflows to nurture leads and drive conversions at HubSpot for 2 years as an Email Marketing Specialist.",
    "Led content marketing initiatives, including blog creation and guest posting, at Shopify for 3 years as a Content Marketing Manager.",
    "Developed and maintained customer relationship management (CRM) systems at SAP for 2.5 years as a CRM Specialist.",
    "Facilitated focus groups and conducted user interviews to inform product development decisions at Slack for 2 years as a User Researcher.",
    "Managed product launches and go-to-market strategies at Netflix for 3 years as a Product Launch Manager.",
    "Led community management efforts, engaging with users and addressing their inquiries at Reddit for 2 years as a Community Manager.",
    "Optimized website performance and user journeys through A/B testing and data analysis at eBay for 2.5 years as a Website Optimization Specialist.",
    "Created and executed integrated marketing campaigns, including offline and online components, at Walmart for 3 years as an Integrated Marketing Manager.",
    "Developed content strategy and editorial calendars for corporate blogs and newsletters at Intel for 2 years as a Content Strategist.",
    "Managed cross-platform advertising campaigns, including PPC and display ads, at YouTube for 3 years as an Advertising Campaign Manager.",
    "Conducted competitive analysis and market positioning studies to identify growth opportunities at McKinsey & Company for 2.5 years as a Market Analyst.",
    "Led diversity and inclusion initiatives, organizing events and training sessions, at Google for 2 years as a Diversity and Inclusion Coordinator."
    "Performed financial analysis and forecasting at J.P. Morgan Chase for 3 years as a Financial Analyst, aiding in investment decisions.",
    "Managed client portfolios and provided investment advice at Goldman Sachs for 4 years as a Financial Advisor, achieving a 20% return on investment for clients.",
    "Conducted economic research and analysis at the Federal Reserve for 2 years as an Economist, contributing to monetary policy decisions.",
    "Led compliance audits and ensured regulatory adherence at Barclays for 3 years as a Compliance Officer, reducing compliance risks by 30%.",
    "Evaluated creditworthiness and assessed loan applications at Citibank for 2 years as a Credit Analyst, improving loan approval rates by 15%.",
    "Designed and implemented tax strategies for high-net-worth clients at Ernst & Young for 4 years as a Tax Consultant, minimizing tax liabilities.",
    "Developed insurance underwriting guidelines and assessed risks at AIG for 3 years as an Insurance Underwriter, maintaining profitability and minimizing losses."
]


educations = [
    "Bachelor's Degree in Marketing, Rimberio University, Graduated May 2017",
    "Master's Degree in Communication Studies, Westwood University, Graduated December 2019",
    "Associate Degree in Graphic Design, Creative Institute, Graduated June 2015",
    "Bachelor's Degree in Business Administration, Metropolitan College, Graduated August 2018",
    "Bachelor's Degree in Computer Science, Utrecht University, Graduated June 2019",
    "Master's Degree in Business Informatics, Utrecht University, Graduated December 2023",
    "Bachelor's Degree in Economics, Ivy League University, Graduated May 2016",
    "Master's Degree in Public Relations, London School of Economics, Graduated June 2021",
    "Associate Degree in Web Development, Tech Institute, Graduated August 2014",
    "Bachelor's Degree in Psychology, University of California, Graduated December 2015",
    "Master's Degree in Data Science, Stanford University, Graduated August 2022",
    "Associate Degree in Hospitality Management, Culinary Institute, Graduated May 2013",
    "Bachelor's Degree in Journalism, Columbia University, Graduated May 2018",
    "Master's Degree in Human Resources Management, Harvard University, Graduated December 2020",
    "Associate Degree in Fine Arts, School of Visual Arts, Graduated June 2014",
    "Bachelor's Degree in Environmental Science, University of Washington, Graduated August 2017",
    "Master's Degree in International Relations, Georgetown University, Graduated June 2022",
    "Associate Degree in Nursing, Johns Hopkins University, Graduated August 2013",
    "Bachelor's Degree in Sociology, University of Chicago, Graduated May 2016",
    "Master's Degree in Educational Psychology, University of Michigan, Graduated June 2021",
    "Associate Degree in Fashion Design, Parsons School of Design, Graduated August 2015",
    "Bachelor's Degree in Linguistics, University of Cambridge, Graduated December 2019",
    "Bachelor's Degree in Marketing, Amsterdam University, Graduated May 2017",
    "Master's Degree in Communication Studies, Westwood University, Graduated December 2019",
    "Associate Degree in Graphic Design, Creative Institute, Graduated June 2015",
    "Bachelor's Degree in Economics, University of Oxford, Graduated June 2018",
    "Master's Degree in Finance, Sorbonne University, Graduated July 2020",
    "Ph.D. in Psychology, University of Tokyo, Graduated September 2016"
]


certifications = [
    "Social Media Marketing Certification, Arowwai Industries, 2018",
    "Google Analytics Certification, Google, 2019",
    "Content Marketing Certification, HubSpot Academy, 2020",
    "Digital Marketing Certificate, Coursera, 2017",
    "Graphic Design Certification, Adobe Certified Associate, 2016",
    "Project Management Professional (PMP) Certification, PMI, 2021",
    "Data Science Certification, Microsoft, 2022",
    "Web Development Certification, FreeCodeCamp, 2019",
    "Certified ScrumMaster (CSM) Certification, Scrum Alliance, 2020",
    "Cybersecurity Certification, CompTIA, 2018",
    "Financial Modeling Certification, Corporate Finance Institute, 2021",
    "UX Design Certification, Interaction Design Foundation, 2022",
    "Social Media Marketing Certification, Arowwai Industries, 2018",
    "Google Analytics Certification, Google, 2019",
    "Content Marketing Certification, HubSpot Academy, 2020",
    "Digital Marketing Certificate, Coursera, 2017",
    "Financial Modeling and Valuation Analyst (FMVA) Certification, Corporate Finance Institute, 2019",
    "Certified Public Accountant (CPA), American Institute of CPAs, 2020",
    "Chartered Financial Analyst (CFA) Certification, CFA Institute, 2018",
    "Certified Financial Planner (CFP) Certification, Certified Financial Planner Board of Standards, Inc., 2021",
    "Certified Information Systems Auditor (CISA), Information Systems Audit and Control Association (ISACA), 2019",
    "Project Management Professional (PMP) Certification, Project Management Institute (PMI), 2016",
    "Certified Human Resources Professional (CHRP), Human Resources Professionals Association (HRPA), 2020",
    "Certified Data Scientist, Data Science Council of America (DASCA), 2018"
]

volunteer_experiences = [
    "Tutoring underprivileged children in math and science subjects",
    "Organizing fundraising events for local charities",
    "Providing support at a homeless shelter by serving meals and assisting residents",
    "Volunteering at an animal shelter by walking dogs and cleaning kennels",
    "Leading environmental conservation efforts by participating in park clean-ups and tree planting",
    "Mentoring high school students through career exploration programs",
    "Assisting in disaster relief efforts by distributing supplies to affected communities",
    "Coordinating blood drives and assisting medical staff at blood donation centers",
    "Teaching basic computer skills to elderly individuals at a community center",
    "Organizing community garden projects to promote sustainable agriculture"
    "Serving on the fundraising committee for a local non-profit organization",
    "Participating in the event planning committee for community festivals and celebrations",
    "Joining the advocacy committee to address social justice issues and promote equality",
    "Contributing to the volunteer recruitment and training committee for a youth mentoring program",
    "Engaging in the outreach committee to raise awareness and support for mental health initiatives",
    "Participating in the entertainment committee for organizing talent shows and game nights at local community centers",
    "Joining the sports committee to coordinate recreational leagues and tournaments for youth and adults",
    "Engaging in the arts and crafts committee to lead workshops and creative projects for children and families",
    "Contributing to the music committee for organizing concerts and music festivals in the community",
]

languages = ["English (Native)", "Spanish (Intermediate)", "German (Novice)",
             "Dutch (Intermediate)", "French (Novice)", "Japanese (Novice)", "Portuguese (Intermediate)"]

about_me = ["I stride purposefully into the office, ready to tackle the day's challenges head-on. "
            "With a clear vision and unwavering determination, I immerse myself in projects that demand my utmost attention. "
            "As the hours pass, I navigate complex issues with precision and poise, "
            "never faltering in my commitment to excellence. With each accomplishment, "
            "I push the boundaries of what's possible, leaving a lasting impact on those around me. "
            "As the sun sets on another productive day, I reflect with satisfaction, "
            "knowing that I've advanced one step closer to my ultimate goals.",
            "I always enter the office with a focused mind and a determined spirit, eager to make a meaningful impact. "
            "Throughout the day, I tackle challenges with resilience and precision, never losing sight of my goals. "
            "With each task conquered, I push the boundaries of what's achievable, driven by a relentless pursuit of excellence. "
            "As the day draws to a close, I reflect on my accomplishments with satisfaction, "
            "knowing that I've made strides toward success.",
            "Achieving goals requires unwavering dedication, meticulous planning, and a steadfast belief in oneself. "
            "With clear objectives in mind, I navigate obstacles with resilience, viewing setbacks as opportunities for growth. "
            "Through perseverance and hard work, I turn aspirations into reality, knowing that every step forward brings me closer to my dreams.",
            "I fuel my drive and motivation with unwavering determination, channeling my energy towards achieving my goals. With each obstacle I encounter, "
            "I embrace the challenge, knowing that perseverance is the key to unlocking new opportunities. My relentless pursuit of excellence propels me forward, "
            "driving me to surpass expectations and reach greater heights.",
            "I possess a unique mix of strengths and weaknesses that define my character. My strengths include unwavering determination, "
            "sharp problem-solving skills, and the ability to inspire others with my actions. "
            "I approach challenges with resilience and adaptability, always driven by a sense of purpose. "
            "However, I am not immune to moments of self-doubt and can be overly critical of myself, "
            "which sometimes hinders my progress. Nevertheless, my commitment to personal growth and self-improvement fuels my journey toward success."]

skills = [
    "Social Media Management: Proficient in managing social media platforms, creating engaging content, and implementing effective strategies to increase brand visibility and engagement",
    "Content Creation: Skilled in producing high-quality content across various formats including articles, blog posts, videos, and infographics, tailored to target audience and brand voice",
    "Community Engagement: Experienced in fostering online communities, engaging with audience members, and building relationships to enhance brand loyalty and advocacy",
    "Analytics: Adept at analyzing data from various sources to derive actionable insights, track performance metrics, and optimize strategies for maximum effectiveness",
    "Campaign Development: Capable of conceptualizing, planning, and executing integrated marketing campaigns across multiple channels to achieve specific objectives and drive results",
    "Copywriting: Proficient in crafting compelling copy that resonates with target audiences, communicates key messages effectively, and drives desired actions",
    "Customer Service: Skilled in delivering exceptional customer service, resolving inquiries and issues promptly, and ensuring customer satisfaction to maintain positive brand perception",
    "Data Analysis: Experienced in collecting, processing, and interpreting data to extract valuable insights and inform decision-making processes",
    "Search Engine Optimization (SEO): Knowledgeable in optimizing website content and structure to improve search engine visibility, drive organic traffic, and enhance online presence",
    "E-mail Marketing: Proficient in creating and executing email marketing campaigns, including segmentation, automation, and performance tracking, to nurture leads and drive conversions",
    "Project Management: Experienced in planning, organizing, and overseeing projects from initiation to completion, ensuring delivery on time and within budget while meeting objectives",
    "Graphic Design: Skilled in creating visually appealing designs for various purposes including branding, marketing collateral, and digital assets, using industry-standard software",
    "Web Development: Proficient in developing and maintaining websites using HTML, CSS, JavaScript, and other web technologies, with a focus on user experience and functionality",
    "Public Relations: Experienced in managing public relations activities, building relationships with media outlets, and crafting strategic messaging to enhance brand reputation and visibility",
    "Market Research: Skilled in conducting market research activities including surveys, interviews, and competitive analysis to gather insights and inform business decisions",
    "User Experience Design: Skilled in designing intuitive and user-friendly interfaces for digital products and platforms, focusing on enhancing usability and user satisfaction",
    "Statistical Analysis: Proficient in applying statistical methods and techniques to analyze data, identify patterns and trends, and draw meaningful conclusions to support decision-making",
    "Presentation Skills: Effective communicator with strong presentation skills, capable of delivering engaging and persuasive presentations to diverse audiences",
    "CRM Management: Experienced in managing customer relationship management (CRM) systems to track interactions, manage leads, and foster strong relationships with customers",
    "Video Production: Proficient in video production processes including filming, editing, and post-production, with a focus on storytelling and visual aesthetics",
    "Event Planning: Skilled in planning and executing events from concept to completion, including venue selection, logistics, and coordination, to create memorable experiences",
    "Budget Management: Experienced in developing and managing budgets for marketing campaigns, projects, and events, optimizing resource allocation to achieve desired outcomes",
    "Programming: Proficient in programming languages such as Python, Java, C++, and Ruby, with the ability to develop and maintain software applications and solutions",
    "Database Management: Experienced in designing, implementing, and managing databases using SQL and other database management systems to store and retrieve data efficiently",
    "Leadership: Strong leadership skills with the ability to inspire and motivate teams, foster collaboration, and drive results towards achieving organizational goals",
    "Problem Solving: Effective problem solver with the ability to identify issues, analyze root causes, and develop innovative solutions to complex challenges",
    "Negotiation: Skilled negotiator with the ability to communicate persuasively, build consensus, and reach mutually beneficial agreements in various situations",
    "Time Management: Effective time manager with the ability to prioritize tasks, allocate resources efficiently, and meet deadlines in fast-paced environments",
    "Attention to Detail: Meticulous attention to detail with a focus on accuracy and precision in all tasks and deliverables",
    "Strategic Thinking: Strategic thinker with the ability to envision long-term goals, anticipate future trends, and develop plans to achieve sustainable growth and success",
    "Sales Skills: Experienced in sales techniques and strategies, including prospecting, lead generation, and closing deals, to drive revenue and business growth",
    "Decision Making: Strong decision-making skills with the ability to analyze information, evaluate alternatives, and make sound judgments in complex and uncertain situations",
    "Critical Thinking: Analytical thinker with the ability to assess information objectively, evaluate arguments, and draw logical conclusions to solve problems effectively",
    "Interpersonal Skills: Strong interpersonal skills with the ability to build rapport, communicate effectively, and collaborate with individuals across diverse backgrounds and cultures",
    "Conflict Resolution: Skilled in managing conflicts and resolving disputes in a constructive manner, fostering mutual understanding and reaching mutually beneficial outcomes",
    "Adaptability: Highly adaptable with the ability to thrive in changing environments, embrace new challenges, and quickly adjust to unforeseen circumstances",
    "Innovation: Creative thinker with a passion for innovation, capable of generating and implementing new ideas, processes, and solutions to drive continuous improvement",
    "Teamwork: Collaborative team player with the ability to work effectively in multidisciplinary teams, share knowledge, and contribute to collective goals and success",
    "Technical Writing: Proficient in writing technical documentation, reports, and manuals with clarity, precision, and attention to detail to communicate complex information effectively",
    "Microsoft Office Suite (Word, Excel, PowerPoint): Proficient in using Microsoft Office applications including Word for document creation, Excel for data analysis and management, and PowerPoint for creating engaging presentations",
    "Google Suite (Docs, Sheets, Slides): Skilled in using Google Suite applications including Docs for collaborative document editing, Sheets for data analysis and management, and Slides for creating presentations",
    "Adobe Creative Suite (Photoshop, Illustrator, InDesign): Proficient in using Adobe Creative Suite applications including Photoshop for image editing, Illustrator for vector graphics creation, and InDesign for layout design",
    "Social Media Advertising: Experienced in creating and managing social media advertising campaigns across various platforms to reach target audiences and achieve marketing objectives",
    "Google Analytics: Proficient in using Google Analytics to track website traffic, analyze user behavior, and measure the effectiveness of online marketing campaigns",
    "Content Management Systems (CMS): Experienced in using content management systems such as WordPress to create, manage, and publish digital content on websites and blogs",
    "HTML/CSS: Proficient in HTML for structuring web content and CSS for styling and formatting, with the ability to create and modify web pages and interfaces",
    "JavaScript: Skilled in JavaScript programming language for adding interactivity and dynamic functionality to web pages and applications",
    "WordPress: Experienced in using WordPress content management system to create and manage websites, blogs, and online stores with customizable themes and plugins",
    "Search Engine Marketing (SEM): Experienced in using search engine marketing techniques such as pay-per-click advertising to increase website visibility and drive targeted traffic",
    "Customer Relationship Management (CRM) Software: Proficient in using customer relationship management (CRM) software such as Salesforce to manage customer interactions, track leads, and improve sales processes",
    "Email Automation Tools (e.g., Mailchimp, HubSpot): Proficient in using email automation tools such as Mailchimp and HubSpot to create, schedule, and automate email marketing campaigns",
    "Video Editing (e.g., Adobe Premiere Pro, Final Cut Pro): Skilled in using video editing software such as Adobe Premiere Pro and Final Cut Pro to edit and produce professional-quality videos for various purposes",
    "Data Visualization (e.g., Tableau, Power BI): Experienced in using data visualization tools such as Tableau and Power BI to create interactive and informative visualizations from large datasets",
    "Statistical Software (e.g., R, SPSS): Proficient in using statistical software such as R and SPSS to perform advanced statistical analysis and modeling on data",
    "Version Control Systems (e.g., Git, SVN): Experienced in using version control systems such as Git and SVN to manage and track changes to software code and project files",
    "Agile Methodologies: Experienced in agile methodologies such as Scrum and Kanban for iterative and incremental software development, with a focus on collaboration and adaptability",
    "Scrum: Proficient in using Scrum framework for agile software development, including sprint planning, daily stand-ups, and sprint reviews, to deliver high-quality products",
    "UI/UX Design Tools (e.g., Sketch, Figma): Skilled in using UI/UX design tools such as Sketch and Figma to create wireframes, prototypes, and user interfaces for digital products and applications",
    "Database Management Systems (e.g., MySQL, PostgreSQL): Experienced in using database management systems such as MySQL and PostgreSQL to design, create, and manage relational databases for storing and retrieving data",
    "E-commerce Platforms (e.g., Shopify, WooCommerce): Proficient in using e-commerce platforms such as Shopify and WooCommerce to create and manage online stores, process transactions, and track inventory",
    "Microsoft Project: Experienced in using Microsoft Project for project planning, scheduling, and resource management, to ensure successful project execution and delivery",
    "Jira: Proficient in using Jira project management software for agile development, including issue tracking, task management, and team collaboration, to streamline project workflows",
    "Confluence: Experienced in using Confluence collaboration software for creating, organizing, and sharing project documentation and knowledge resources, to foster team collaboration and communication",
    "Salesforce: Proficient in using Salesforce CRM platform for managing customer relationships, tracking leads, and driving sales processes, to optimize sales performance and productivity",
    "Zendesk: Experienced in using Zendesk customer service software for managing customer support tickets, inquiries, and feedback, to deliver exceptional customer service and satisfaction",
    "Slack: Proficient in using Slack collaboration software for team communication, file sharing, and project collaboration, to facilitate efficient and effective teamwork and collaboration",
    "Python: Proficient in Python programming language for software development, data analysis, and machine learning, with a focus on writing clean, efficient, and maintainable code",
    "Java: Experienced in Java programming language for developing cross-platform applications, web services, and enterprise solutions, with a focus on scalability and performance",
    "C++: Skilled in C++ programming language for developing high-performance applications, system software, and game development, with a focus on efficiency and memory management",
    "Ruby: Proficient in Ruby programming language for web development, automation, and scripting, with a focus on simplicity, productivity, and developer happiness",
    "PHP: Experienced in PHP programming language for server-side web development, dynamic content generation, and database integration, with a focus on flexibility and scalability",
    "Swift: Skilled in Swift programming language for iOS and macOS app development, with a focus on speed, safety, and modern software design principles",
    "Kotlin: Proficient in Kotlin programming language for Android app development, with a focus on conciseness, safety, and interoperability with Java",
    "SQL: Experienced in SQL (Structured Query Language) for database management, querying, and manipulation, with a focus on retrieving and analyzing data from relational databases",
    "Scala: Proficient in Scala programming language for developing scalable and concurrent applications on the Java Virtual Machine (JVM), with a focus on functional programming and type safety",
    "MATLAB: Experienced in MATLAB programming language for numerical computing, data analysis, and algorithm development, with a focus on mathematical modeling and simulation",
    "TensorFlow: Proficient in TensorFlow machine learning framework for developing and training deep learning models, with a focus on building scalable and production-ready AI applications",
    "PyTorch: Experienced in PyTorch deep learning framework for developing and training neural networks, with a focus on flexibility, ease of use, and research-driven innovation",
    "Pandas: Proficient in Pandas library for data manipulation and analysis in Python, with a focus on handling structured data and performing advanced data transformations",
    "NumPy: Experienced in NumPy library for numerical computing in Python, with a focus on array processing, linear algebra, and statistical operations",
    "Scikit-learn: Proficient in Scikit-learn library for machine learning in Python, with a focus on building and deploying predictive models for classification, regression, and clustering tasks",
    "NLTK: Experienced in NLTK (Natural Language Toolkit) library for natural language processing in Python, with a focus on text analysis, sentiment analysis, and language modeling"
    ]

# Generate 50 fake resumes
for i in range(1, 51):
    output_path = f'{output_folder}fake_resume_{i}.pdf'
    generate_fake_resume(output_path,
                         name=faker.name(),
                         email=faker.email(),
                         phone_number=''.join(random.choices(string.digits, k=10)),
                         address=faker.address().replace('\n', ', '),
                         languages=random.sample(languages, random.randint(2, 3)),
                         skills=random.sample(skills, random.randint(5,7)),
                         occupation=random.choice(occupations),
                         experience=random.sample(experiences, min(len(experiences), random.randint(1, 6))),
                         education=random.sample(educations, min(len(educations), random.randint(1, 3))),
                         certifications=random.sample(certifications, min(len(certifications), random.randint(1, 3))),
                         volunteer_experiences=random.sample(volunteer_experiences,
                                                             min(len(volunteer_experiences), random.randint(2, 3))),
                         has_layout=random.choice([True, False])
                         )
    print(f'Fake resume {i} created successfully.')
