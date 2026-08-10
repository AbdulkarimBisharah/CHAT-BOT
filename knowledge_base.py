"""
============================================================================
ITS67404 IoT COURSEWORK ASSISTANT - KNOWLEDGE BASE
============================================================================

HOW TO EDIT (for the lecturer):
- Each dict below is one "fact" the chatbot can answer from.
- Copy an existing block, paste it, and change the fields. That's it.
- Fields:
    id       : a short unique name (no spaces)
    source   : where this fact comes from - shown to the student under the answer
    keywords : words a student might type. More = easier to find. Lowercase.
    question : a natural example question (used for matching + suggestions)
    answer   : what the bot replies. Keep it factual and short.
    verified : True  = confirmed from an uploaded brief (safe to trust)
               False = PLACEHOLDER, not yet confirmed - bot will warn the student
- To ADD a new assignment: copy any block, set verified=False until you paste
  the real dates/rules from that assignment's brief.
- After editing, save the file. No other code needs to change.
============================================================================
"""

KNOWLEDGE_BASE = [

    # ========================================================================
    # ASSIGNMENT 3 (Assessment Task 3) - VERIFIED from the official brief
    # ========================================================================
    {
        "id": "a3-overview",
        "source": "Assignment 3 brief (Assessment Task 3)",
        "keywords": ["assignment 3", "a3", "task 3", "assessment task 3",
                     "group assignment", "what is a3", "third assignment"],
        "question": "What is Assignment 3 about?",
        "answer": ("Assessment Task 3 is a group assignment where you construct an IoT "
                   "device or system for a specific application, present your findings, and "
                   "produce a publishable IEEE manuscript. It has four parts: A3.1 (resource "
                   "& risk management), A3.2 (proof of concept), A3.3 (presentation), and A3.4 "
                   "(manuscript). It is worth 40% of the module."),
        "verified": True,
    },
    {
        "id": "a3-weightage",
        "source": "Assignment 3 brief, cover sheet",
        "keywords": ["weightage", "weight", "worth", "percent", "percentage",
                     "how much", "marks", "a3 worth", "assignment 3 worth"],
        "question": "How much is Assignment 3 worth?",
        "answer": ("Assignment 3 is worth 40% of the module. It is split into four equal "
                   "parts of 10% each: A3.1 Resource & Risk Management, A3.2 Proof of Concept, "
                   "A3.3 Presentation, and A3.4 Manuscript."),
        "verified": True,
    },
    {
        "id": "a3-deadline",
        "source": "Assignment 3 brief, cover sheet",
        "keywords": ["deadline", "due", "due date", "hand in", "when due",
                     "submission date", "a3 deadline", "when is a3", "report due",
                     "presentation date"],
        "question": "When is Assignment 3 due?",
        "answer": ("The report hand-in date is Week 15, 27th July 2026. Presentations start "
                   "earlier, from 10th July. The assignment was handed out on 29th May 2026. "
                   "All late submissions face mark deductions."),
        "verified": True,
    },
    {
        "id": "a3-groupsize",
        "source": "Assignment 3 brief, instructions to students",
        "keywords": ["group size", "how many", "members", "group of", "team size",
                     "people per group", "how many students", "group members"],
        "question": "How many students per group?",
        "answer": ("Assignment 3 must be done in groups of 3 to 5 students. Complete the "
                   "cover sheet with all group members' names and Student IDs, and mark who "
                   "the Group Leader is. The cover sheet must be your first page."),
        "verified": True,
    },
    {
        "id": "a3-1",
        "source": "Assignment 3 brief, A3.1",
        "keywords": ["a3.1", "a31", "resource", "risk", "maintenance",
                     "resource management", "risk management", "part 1", "potential risks"],
        "question": "What is required for A3.1?",
        "answer": ("A3.1 (10%) - Maintenance: Manage resources and potential risks. Discuss "
                   "in detail the potential risks and resource-management factors of the IoT "
                   "idea you proposed in Assignment 2. Cover expandability, efficient resource "
                   "management, and risk reduction. Provide examples, detailed explanations, "
                   "and citations wherever possible."),
        "verified": True,
    },
    {
        "id": "a3-2",
        "source": "Assignment 3 brief, A3.2",
        "keywords": ["a3.2", "a32", "proof of concept", "poc", "demo", "prototype",
                     "wokwi", "tinkercad", "simulation", "part 2", "execute"],
        "question": "What is required for A3.2?",
        "answer": ("A3.2 (10%) - Execute the IoT application to deliver value. Demonstrate a "
                   "proof of concept for your idea. You may simulate data processing, interface "
                   "design, cloud integration, and security using online platforms or hardware. "
                   "Clearly explain the proof of concept in the report and attach a working, "
                   "accessible Tinkercad or Wokwi link. The demo must also be shown during the "
                   "presentation. Attach links and well-labelled photos of the prototype in the "
                   "report, and submit slides to the slides folder."),
        "verified": True,
    },
    {
        "id": "a3-2-tools",
        "source": "Assignment 3 brief, A3.2",
        "keywords": ["tools", "what tools", "platforms", "software", "which tools",
                     "allowed tools", "simulate", "cisco", "figma", "grafana",
                     "thingspeak", "google colab", "google cloud"],
        "question": "What tools can I use for the proof of concept?",
        "answer": ("Suggested tools include: Tinkercad (simulate Arduino boards and sensors), "
                   "Wokwi (IoT circuit simulation), Cisco Packet Tracer (model IoT networks / "
                   "smart home), Figma (design and prototype UIs), Grafana (dashboards for "
                   "time-series IoT data), ThingSpeak (collect, analyse and visualise sensor "
                   "data), Google Cloud (free tier for basic IoT experiments), and Google Colab "
                   "(simulate data processing, prediction, and filtering). Full integration "
                   "isn't required - together they should clearly demonstrate feasibility."),
        "verified": True,
    },
    {
        "id": "a3-3",
        "source": "Assignment 3 brief, A3.3",
        "keywords": ["a3.3", "a33", "presentation", "present", "slides", "powerpoint",
                     "canva", "how long", "presentation time", "part 3", "demo time"],
        "question": "What is required for A3.3?",
        "answer": ("A3.3 (10%) - Presentation. Present your project using PowerPoint or Canva. "
                   "ALL group members must take part. Each presentation is 20-30 minutes (30 "
                   "minutes including any demo). Suggested outline: 1) Title, members & IDs, "
                   "2) Introduction, 3) Literature review/current system, 4) Problem statement, "
                   "5) Objectives, 6) Methodology, 7) Architecture/Data Flow Diagram, 8) Results/"
                   "findings + proof-of-concept demo, 9) Discussion (limitations & future work), "
                   "10) Conclusion, 11) References."),
        "verified": True,
    },
    {
        "id": "a3-4",
        "source": "Assignment 3 brief, A3.4",
        "keywords": ["a3.4", "a34", "manuscript", "paper", "ieee", "publishable",
                     "documentation", "how many pages", "page limit", "format",
                     "turnitin", "part 4"],
        "question": "What is required for A3.4 (the manuscript)?",
        "answer": ("A3.4 (10%) - Manuscript of publishable material. Write a paper in IEEE "
                   "format, maximum 6 pages, following the suggested outline (Title, Abstract, "
                   "Introduction, Literature Review, Objectives, Methodology, Architecture/Data "
                   "Flow Diagram, Prototype, Discussion, Conclusion, References). You may add "
                   "relevant subsections. Check it with Turnitin and attach the similarity "
                   "report (must be below 20%). Marks are lost for not following IEEE formatting "
                   "strictly."),
        "verified": True,
    },
    {
        "id": "a3-4-ieee",
        "source": "Assignment 3 brief, A3.4",
        "keywords": ["ieee format", "ieee template", "manuscript format", "paper format",
                     "6 pages", "page limit", "formatting"],
        "question": "What format does the manuscript need?",
        "answer": ("IEEE format, maximum 6 pages. Get the IEEE template online and follow all "
                   "formatting guidelines strictly - groups lose marks for not complying. Attach "
                   "a Turnitin similarity report with similarity below 20%."),
        "verified": True,
    },
    {
        "id": "a3-deliverables",
        "source": "Assignment 3 brief, Section 4.0 Deliverables",
        "keywords": ["deliverables", "what to submit", "submit", "submission",
                     "hand in what", "pdf", "cover page", "mytimes", "what do i submit"],
        "question": "What do I need to submit for Assignment 3?",
        "answer": ("Submit softcopy PDF only to MyTIMeS: (1) the manuscript ready to be "
                   "published, (2) the assignment with cover page and group analysis, and (3) "
                   "the Turnitin Originality Report as a PDF with similarity below 20%. All "
                   "reports need a front cover with the coursework title, students' names and "
                   "IDs. Submit slides to the slides folder. Late submissions have marks "
                   "deducted."),
        "verified": True,
    },
    {
        "id": "a3-plagiarism",
        "source": "Assignment 3 brief, Section 5.0 Academic Integrity",
        "keywords": ["plagiarism", "cheating", "copy", "turnitin", "similarity",
                     "academic integrity", "penalty", "20%", "copy paste", "originality"],
        "question": "What is the plagiarism policy?",
        "answer": ("Plagiarism in all forms is forbidden. Copy-and-paste work is considered "
                   "plagiarism. Turnitin similarity must be below 20%. The minimum penalty is "
                   "loss of marks for the assignment, and submitting plagiarised work can result "
                   "in 0 marks - if this means a hurdle requirement is not met, it could cause "
                   "failure of the course. All non-original material must be fully credited."),
        "verified": True,
    },
    {
        "id": "a3-rubric",
        "source": "Assignment 3 brief, Section 3.0 Marking Rubrics",
        "keywords": ["rubric", "marking", "grading", "how graded", "criteria",
                     "how marks", "outstanding", "marking scheme", "how is it marked"],
        "question": "How is Assignment 3 marked?",
        "answer": ("Four criteria, 10 marks each (bands: Outstanding 9-10, Mastering 6-8, "
                   "Developing 4-5, Beginning 0-3): (1) Identify an opportunity that delivers "
                   "value when choosing an IoT application; (2) Manage resources and challenges "
                   "- integrate sensors, actuators and communication protocols into a cohesive "
                   "system; (3) Demonstration clarity - clear operation of the IoT system and "
                   "justified tool choices; (4) Producing documentation and a manuscript of "
                   "publishable material."),
        "verified": True,
    },
    {
        "id": "a3-mlo",
        "source": "Assignment 3 brief, Section 1.0 Learning Outcomes",
        "keywords": ["learning outcome", "mlo", "mlo3", "objective",
                     "learning objectives", "outcomes", "what will i learn"],
        "question": "What are the learning outcomes for Assignment 3?",
        "answer": ("Assignment 3 targets MLO3: apply a holistic view to construct an IoT "
                   "device/system for a specific application with appropriate digital tools and "
                   "technologies, while cooperating effectively in a group. You also report "
                   "findings through a presentation, and the group leader leads the team to "
                   "complete a manuscript of publishable material."),
        "verified": True,
    },

    # ========================================================================
    # ASSIGNMENT 1 (Assessment Task 1) - VERIFIED from the official brief
    # Individual assignment - MLO1. Handout 23 Apr 2026, due 3 Jun 2026 (Week 7).
    # ========================================================================
    {
        "id": "a1-overview",
        "source": "Assignment 1 brief (Assessment Task 1)",
        "keywords": ["assignment 1", "a1", "task 1", "assessment task 1",
                     "first assignment", "what is a1", "entrepreneurial", "purple cow",
                     "big idea", "propose"],
        "question": "What is Assignment 1 about?",
        "answer": ("Assessment Task 1 is an INDIVIDUAL assignment (MLO1): propose an IoT-based "
                   "system with an entrepreneurial mindset for a real-world problem. It has three "
                   "parts of 10% each: (1) Identify the problem in the chosen application area, "
                   "(2) Demonstrate an entrepreneurial mindset (a 'purple cow' idea, aligned with "
                   "relevant SDGs, with an IoT architecture diagram), and (3) Innovation "
                   "(functional & non-functional requirements, system scope, unique selling "
                   "points, and a 2-minute video pitch). It is worth 30% of the module."),
        "verified": True,
    },
    {
        "id": "a1-weightage",
        "source": "Assignment 1 brief, cover sheet",
        "keywords": ["assignment 1 weightage", "a1 worth", "a1 weight", "a1 marks",
                     "how much is assignment 1", "individual or group", "a1 individual",
                     "is a1 group"],
        "question": "How much is Assignment 1 worth and is it individual?",
        "answer": ("Assignment 1 is worth 30% of the module and must be done INDIVIDUALLY (not "
                   "in a group). It is split into three parts of 10% each: Identify the problem, "
                   "Demonstrate an entrepreneurial mindset, and Innovation."),
        "verified": True,
    },
    {
        "id": "a1-deadline",
        "source": "Assignment 1 brief, cover sheet",
        "keywords": ["a1 deadline", "a1 due", "when is a1", "when is assignment 1",
                     "assignment 1 due date", "a1 hand in", "assignment 1 deadline"],
        "question": "When is Assignment 1 due?",
        "answer": ("Assignment 1 was handed out on 23rd April 2026 and is due on 3rd June 2026 "
                   "(Week 7). All late submissions face mark deductions."),
        "verified": True,
    },
    {
        "id": "a1-requirements",
        "source": "Assignment 1 brief, Section 2.0",
        "keywords": ["a1 requirements", "a1 parts", "what does a1 need", "a1 video",
                     "video pitch", "two minute video", "2 minute video", "functional requirements",
                     "non functional requirements", "sdg", "architecture diagram a1", "scope",
                     "unique selling", "innovation a1"],
        "question": "What do I need to do for Assignment 1?",
        "answer": ("Assignment 1 has three parts (10% each): (1) Identify the problem - "
                   "investigate the background of a potential IoT application and state the "
                   "problems with current systems and the value your idea creates. (2) "
                   "Entrepreneurial mindset - propose an IoT solution through research, align it "
                   "with relevant Sustainable Development Goals (SDGs), make it a 'purple cow' "
                   "(uniquely remarkable) idea, and draw the IoT architecture diagram using any "
                   "suitable tool. (3) Innovation - list functional and non-functional "
                   "requirements in a table, define the system scope, describe each functional "
                   "requirement in a paragraph, and record a 2-minute video pitch showing your "
                   "solution's unique selling points and competitive advantages. Use HARVARD-"
                   "style citations and references."),
        "verified": True,
    },
    {
        "id": "a1-deliverables",
        "source": "Assignment 1 brief, Section 4.0 Deliverables",
        "keywords": ["a1 deliverables", "a1 submit", "what to submit a1", "a1 file name",
                     "a1 filename", "harvard", "a1 turnitin", "a1 pdf"],
        "question": "What do I submit for Assignment 1?",
        "answer": ("Submit softcopy PDF only to MyTIMeS, named YOURNAMEA1202604.PDF (for "
                   "example SUMATHIA1202604.PDF). Include a front cover page (coursework title, "
                   "your name and Student ID), all the required questions, a conclusion, and "
                   "Harvard-style references and citations. Attach the Turnitin Originality "
                   "Report (PDF) with similarity below 20%. Late submissions have marks deducted."),
        "verified": True,
    },
    {
        "id": "a1-rubric",
        "source": "Assignment 1 brief, Section 3.0 Marking Rubrics",
        "keywords": ["a1 rubric", "a1 marking", "how is a1 marked", "a1 grading",
                     "a1 criteria"],
        "question": "How is Assignment 1 marked?",
        "answer": ("Three criteria, 10 marks each (bands: Outstanding 9-10, Mastering 6-8, "
                   "Developing 3-5, Beginning 0-2): (1) Identify the problem related to the "
                   "chosen application - depth and insight of the problem statement and "
                   "background; (2) Demonstrate an entrepreneurial mindset - showing yourself as "
                   "an innovative 'agent of change'; (3) Innovation - unique selling points, "
                   "competitive advantages, functional/non-functional requirements, the video "
                   "pitch, and system scope."),
        "verified": True,
    },

    # ========================================================================
    # ASSIGNMENT 2 (Assessment Task 2) - VERIFIED from the official brief
    # Group assignment - MLO2. Due Week 12 (Friday). Weightage 30%.
    # ========================================================================
    {
        "id": "a2-overview",
        "source": "Assignment 2 brief (Assessment Task 2)",
        "keywords": ["assignment 2", "a2", "task 2", "assessment task 2",
                     "architecture", "second assignment", "what is a2", "smart home",
                     "technology stack", "algorithms"],
        "question": "What is Assignment 2 about?",
        "answer": ("Assessment Task 2 is a group assignment based on MLO2: design the complete "
                   "system architecture and outline the implementation for an IoT system that "
                   "solves a real-world problem (the sample problem is smart-home environmental "
                   "monitoring and control). Part 1 (15%) covers system architecture and the "
                   "technology stack - hardware components, software platforms, communication "
                   "protocols, and data storage/management. Part 2 (15%) covers algorithm design "
                   "and implementation - control algorithms, data processing/analysis, mobile "
                   "app functionality, and security considerations."),
        "verified": True,
    },
    {
        "id": "a2-weightage",
        "source": "Assignment 2 brief, cover sheet",
        "keywords": ["assignment 2 weightage", "a2 worth", "a2 weight", "a2 marks",
                     "how much is assignment 2"],
        "question": "How much is Assignment 2 worth?",
        "answer": ("Assignment 2 is worth 30% of the module, split into two equal parts of 15% "
                   "each: Part 1 - System Architecture and Technology Stack, and Part 2 - "
                   "Algorithm Design and Implementation Details."),
        "verified": True,
    },
    {
        "id": "a2-deadline",
        "source": "Assignment 2 brief, cover sheet",
        "keywords": ["a2 deadline", "a2 due", "when is a2", "when is assignment 2",
                     "assignment 2 due date", "a2 hand in", "assignment 2 deadline"],
        "question": "When is Assignment 2 due?",
        "answer": ("Assignment 2 is due in Week 12, on the Friday. All late submissions face "
                   "mark deductions - confirm the exact calendar date with your lecturer or on "
                   "MyTIMeS."),
        "verified": True,
    },
    {
        "id": "a2-part1",
        "source": "Assignment 2 brief, Part 1",
        "keywords": ["a2 part 1", "a2.1", "system architecture", "hardware", "sensors",
                     "communication protocol", "mqtt", "zigbee", "cloud platform",
                     "data storage", "technology stack"],
        "question": "What is required for Assignment 2 Part 1?",
        "answer": ("Part 1 (15%) - System Architecture and Technology Stack: produce a detailed "
                   "architecture diagram showing hardware (specific sensor models, "
                   "microcontroller/gateway, actuators), software platforms (cloud platform, "
                   "mobile app framework) and communication protocols (e.g. MQTT, Zigbee, "
                   "Z-Wave, Bluetooth), with the data flow between all components. Justify your "
                   "hardware, software-platform and communication-protocol choices (cost, power, "
                   "accuracy, range, security, scalability), address sensor placement, and "
                   "describe cloud data storage and management (e.g. time-series databases) "
                   "including encryption at rest and in transit."),
        "verified": True,
    },
    {
        "id": "a2-part2",
        "source": "Assignment 2 brief, Part 2",
        "keywords": ["a2 part 2", "a2.2", "algorithm", "control algorithm", "pid",
                     "data processing", "machine learning", "mobile app", "security",
                     "encryption", "authentication"],
        "question": "What is required for Assignment 2 Part 2?",
        "answer": ("Part 2 (15%) - Algorithm Design and Implementation: describe the control "
                   "algorithms for your actuators (e.g. temperature, air-quality and lighting "
                   "control, with pseudocode/flowcharts and strategies such as PID); explain "
                   "data processing and analysis (filtering/cleaning, aggregation, visualisation, "
                   "and possible machine learning for prediction/personalisation); detail the "
                   "mobile app features (real-time monitoring, remote control, scheduling, "
                   "notifications, personalisation); and outline security (device "
                   "authentication, data encryption, access control, secure firmware updates)."),
        "verified": True,
    },
    {
        "id": "a2-deliverables",
        "source": "Assignment 2 brief, Deliverables & Report Template",
        "keywords": ["a2 deliverables", "a2 submit", "what to submit a2", "a2 file name",
                     "a2 filename", "a2 format", "a2 template", "peer evaluation",
                     "a2 turnitin", "times new roman"],
        "question": "What do I submit for Assignment 2?",
        "answer": ("Submit one PDF report plus a presentation. The report uses Times New Roman "
                   "12pt, 1.5 line spacing, justified, and must contain: cover page (group "
                   "number, names, IDs, signatures), table of contents, the marking rubric, the "
                   "detailed task report (start each task on a new page, all figures/tables "
                   "labelled, IEEE-format in-text citations and references), the Turnitin report, "
                   "and a filled, signed peer-evaluation form. Turnitin similarity must be 20% "
                   "overall and below 2% from any single source. Name the file "
                   "Groupno._Assessment-02.pdf and submit to MyTIMeS."),
        "verified": True,
    },

    # ========================================================================
    # GENERAL MODULE INFO
    # ========================================================================
    {
        "id": "submission-platform",
        "source": "General module info",
        "keywords": ["mytimes", "where submit", "submission platform", "upload",
                     "portal", "how to submit"],
        "question": "Where do I submit my work?",
        "answer": ("Assignments are submitted as softcopy PDF to MyTIMeS. Assignment 3 also "
                   "requires the Turnitin Originality Report (PDF, similarity below 20%) and "
                   "slides submitted to the slides folder."),
        "verified": True,
    },

    # ---- Assignments 1, 2 and 3 are all loaded and verified above. ----
    # To add a new fact, copy any block, give it a new "id", and fill in the fields.
]
