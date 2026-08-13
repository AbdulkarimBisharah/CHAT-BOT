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
    # STUDENT FAQ (from FAQ21.docx) - cross-assignment common questions.
    # Answers that ARE confirmed by the briefs / the lecturer are verified=True.
    # Anything the briefs don't state (AI %, exam, exact word count, MyTIMeS
    # mechanics) is verified=False and points the student to the lecturer,
    # so the bot shows a "please double-check" note instead of guessing.
    # ========================================================================
    {
        "id": "faq-individual-or-group",
        "source": "Assignment 1, 2 & 3 briefs",
        "keywords": ["individual or group", "is this group", "is it individual",
                     "group or individual", "solo", "by myself", "alone", "on my own",
                     "can i do it individually", "do it alone"],
        "question": "Is this an individual or group assignment?",
        "answer": ("It depends on the assignment: Assignment 1 is INDIVIDUAL (done on your "
                   "own), while Assignments 2 and 3 are GROUP assignments done in groups of 3 "
                   "to 5 students."),
        "verified": True,
    },
    {
        "id": "faq-referencing",
        "source": "Assignment 1 brief (Harvard) and Assignment 2 & 3 briefs (IEEE)",
        "keywords": ["referencing", "reference style", "referencing style", "citation style",
                     "how to cite", "harvard", "ieee referencing", "cite", "cite images",
                     "cite websites", "websites as references", "how many references",
                     "number of references", "sources"],
        "question": "Which referencing style should I use?",
        "answer": ("Assignment 1 uses HARVARD-style citations and references. Assignments 2 "
                   "and 3 use IEEE-format in-text citations and references. Cite ALL non-original "
                   "material, including images and figures you didn't make. You may use reputable "
                   "websites as sources, but prefer credible/academic references. There's no fixed "
                   "minimum number - use as many credible sources as your work genuinely needs."),
        "verified": True,
    },
    {
        "id": "faq-formatting",
        "source": "Assignment 2 & 3 briefs (report/manuscript formatting)",
        "keywords": ["font", "font size", "formatting", "format", "times new roman",
                     "line spacing", "spacing", "figures", "tables", "label figures",
                     "label tables", "report format", "how to format", "will formatting affect",
                     "does formatting matter"],
        "question": "What font and formatting should I use?",
        "answer": ("Formatting depends on the task. Assignment 2 report: Times New Roman 12pt, "
                   "1.5 line spacing, justified; each task starts on a new page; all figures and "
                   "tables must be clearly labelled. Assignment 3 manuscript (A3.4): strict IEEE "
                   "format, maximum 6 pages. Assignment 1: a PDF with a cover page and Harvard "
                   "references. Yes - formatting affects your marks: groups lose marks for not "
                   "following the required format."),
        "verified": True,
    },
    {
        "id": "faq-word-page-limit",
        "source": "Assignment briefs (page limits)",
        "keywords": ["word count", "word limit", "how many words", "how many pages",
                     "page limit", "exceed word limit", "exceed the limit", "does word count include",
                     "word count references", "word count tables", "how long should the report",
                     "length"],
        "question": "How many pages or words should the report be?",
        "answer": ("The briefs use PAGE limits, not word counts. The Assignment 3 manuscript "
                   "(A3.4) has a maximum of 6 pages in IEEE format. Assignments 1 and 2 don't set "
                   "a fixed word count - focus on fully and concisely covering every required "
                   "section rather than hitting a word target. If you specifically need a word "
                   "limit, confirm it with your lecturer."),
        "verified": True,
    },
    {
        "id": "faq-late-submission",
        "source": "Assignment 1, 2 & 3 briefs (late submission)",
        "keywords": ["late", "late submission", "submit late", "miss deadline", "missed deadline",
                     "grace period", "penalty for late", "what happens if i submit late",
                     "extension", "after deadline"],
        "question": "What happens if I submit late?",
        "answer": ("All late submissions face mark deductions. The briefs don't mention a grace "
                   "period, so aim to submit on time. If you have a genuine reason (for example a "
                   "medical issue), contact your lecturer as early as possible - the lecturer, not "
                   "this assistant, decides on any extension."),
        "verified": True,
    },
    {
        "id": "faq-submission-mechanics",
        "source": "General module info (MyTIMeS) + lecturer contact",
        "keywords": ["resubmit", "re-submit", "replace file", "replace submission", "reupload",
                     "re-upload", "wrong file", "submitted wrong file", "submission successful",
                     "how do i know submitted", "did my submission go through", "confirm submission",
                     "change my submission"],
        "question": "Can I replace my file / how do I know my submission worked?",
        "answer": ("Assignments are submitted as PDF to MyTIMeS. You can normally replace or "
                   "re-upload your file before the deadline, and MyTIMeS shows a confirmation once "
                   "an upload completes. If you submitted the wrong file or aren't sure it went "
                   "through, upload the correct file again before the deadline. If you still need "
                   "help, email the lecturer: Sumathi.balakrishnan@taylors.edu.my."),
        "verified": False,
    },
    {
        "id": "faq-ai-usage",
        "source": "Taylor's University / module academic-integrity policy (confirm with lecturer)",
        "keywords": ["ai", "chatgpt", "chat gpt", "generative ai", "gen ai", "use ai",
                     "ai allowed", "ai assistance", "declare ai", "ai grammar", "ai code",
                     "ai generated", "ai images", "percentage of ai", "ai percentage", "% of ai",
                     "how much ai", "copilot", "gemini", "llm"],
        "question": "Can I use ChatGPT / generative AI, and how much is allowed?",
        "answer": ("Use of AI (ChatGPT, generative AI, etc.) is governed by Taylor's University "
                   "and this module's academic-integrity policy - not by this assistant. Do NOT "
                   "assume a specific 'percentage of AI' is allowed; that has to be confirmed. As a "
                   "safe rule: the submitted work must be your own, any AI assistance must be "
                   "declared where the policy requires it, and AI-generated text, code or images "
                   "can't be passed off as your original work. Check the exact rules with your "
                   "lecturer (Sumathi.balakrishnan@taylors.edu.my) before relying on AI."),
        "verified": False,
    },
    {
        "id": "faq-high-mark",
        "source": "Assignment marking rubrics (Section 3.0 of each brief)",
        "keywords": ["high mark", "get an a", "how to get a", "score well", "do well",
                     "top marks", "best grade", "highest marks", "most important criteria",
                     "important criteria", "how to score", "outstanding", "what gets high marks"],
        "question": "What do I need to do to get a high mark?",
        "answer": ("There's no shortcut to a guaranteed grade - aim to reach the 'Outstanding' "
                   "band of the published rubric on every criterion. Across the assignments the "
                   "rubric rewards: choosing an IoT opportunity that delivers real value; managing "
                   "resources and risks and integrating sensors, actuators and communication "
                   "protocols into a working system; a clear demonstration with justified tool "
                   "choices; and well-structured documentation/manuscript. Follow the required "
                   "format, cite properly, keep Turnitin similarity below 20%, and fully address "
                   "every listed requirement. (This assistant explains the rubric; it can't promise "
                   "a specific grade.)"),
        "verified": True,
    },
    {
        "id": "faq-group-contribution",
        "source": "Common questions (peer review) + lecturer contact",
        "keywords": ["contribute", "not contributing", "member not contributing",
                     "equal contribution", "everyone contribute", "peer review", "peer evaluation",
                     "conflict", "group conflict", "dispute", "same mark", "individual contribution",
                     "does everyone get the same mark", "lazy member", "free rider"],
        "question": "What if a group member does not contribute?",
        "answer": ("Every member is expected to contribute. If someone isn't contributing, fill "
                   "in the peer-review / peer-evaluation form so it's on record, and raise it with "
                   "your lecturer (Sumathi.balakrishnan@taylors.edu.my) - the lecturer handles "
                   "disputes and non-contribution, not this assistant. Marks can be adjusted based "
                   "on peer evaluation and actual contribution, so document who did what."),
        "verified": True,
    },
    {
        "id": "faq-change-groups",
        "source": "Common questions (group changes)",
        "keywords": ["choose group", "choose own group", "pick group members", "change group",
                     "change groups", "switch group", "switch groups", "move group",
                     "new group", "can i change groups", "different group next assignment"],
        "question": "Can I choose or change my group?",
        "answer": ("You cannot change groups between assignments - you stay in the same group "
                   "for the continuous project. For how groups are formed or who is in your group, "
                   "check with your lecturer. Note that group work applies to Assignments 2 and 3; "
                   "Assignment 1 is done individually."),
        "verified": True,
    },
    {
        "id": "faq-continuous",
        "source": "Common questions (A2 and A3 are continuous)",
        "keywords": ["continuous", "continuation", "build on", "assignment 2 and 3",
                     "a2 and a3", "linked", "connected", "same project", "carry over",
                     "related assignments", "follow on"],
        "question": "Are Assignments 2 and 3 continuous?",
        "answer": ("Yes - Assignments 2 and 3 are continuous: they build on the same IoT "
                   "idea/project. A3.1 even asks you to manage the resources and risks of the IoT "
                   "idea you proposed in Assignment 2, so keep your project consistent across A2 "
                   "and A3. (Assignment 1 is where you first propose the idea.)"),
        "verified": True,
    },
    {
        "id": "faq-who-submits",
        "source": "Assignment briefs + lecturer (confirm)",
        "keywords": ["who should submit", "who submits", "who hands in", "all members submit",
                     "everyone submit", "only group leader", "group leader submit",
                     "do all group members submit", "one submission"],
        "question": "Who should submit - everyone or just the group leader?",
        "answer": ("For the individual Assignment 1, each student submits their own work. For the "
                   "group Assignments 2 and 3, you submit one set of deliverables per group "
                   "(typically the group leader submits on the group's behalf). To be safe, confirm "
                   "with your lecturer whether every member also needs to upload a copy."),
        "verified": False,
    },
    {
        "id": "faq-lecturer-contact",
        "source": "Common questions (lecturer email)",
        "keywords": ["consultation", "contact lecturer", "email", "lecturer email",
                     "teacher email", "reach lecturer", "sumathi", "appointment", "meet lecturer",
                     "ask lecturer", "get consultation", "help from lecturer", "who do i ask"],
        "question": "How can I get a consultation / what is the lecturer's email?",
        "answer": ("For a consultation, email the lecturer: Sumathi.balakrishnan@taylors.edu.my. "
                   "Use email to arrange a consultation, or to confirm anything this assistant "
                   "can't verify from the coursework briefs."),
        "verified": True,
    },
    {
        "id": "faq-exam",
        "source": "Not stated in the coursework briefs - confirm with lecturer",
        "keywords": ["exam", "final exam", "is there an exam", "do we have an exam", "test",
                     "quiz", "written exam", "sit an exam"],
        "question": "Do we have an exam for this module?",
        "answer": ("The coursework briefs I have don't mention an exam - this module is assessed "
                   "through Assignments 1, 2 and 3. Whether there is any exam should be confirmed "
                   "with your lecturer (Sumathi.balakrishnan@taylors.edu.my) or on MyTIMeS."),
        "verified": False,
    },
    {
        "id": "faq-presentation-general",
        "source": "Assignment 3 brief, A3.3",
        "keywords": ["how many slides", "number of slides", "slides count", "when is presentation",
                     "when is our presentation", "presentation when", "q and a", "q&a", "questions after",
                     "demo fails", "demo does not work", "system does not work", "system doesn't work",
                     "backup demo", "if demo fails", "does everyone present", "everyone present"],
        "question": "How long is the presentation, how many slides, and what if the demo fails?",
        "answer": ("The Assignment 3 presentation (A3.3) runs 20-30 minutes and ALL group members "
                   "must present, using PowerPoint or Canva; submit your slides to the slides "
                   "folder. There's no fixed slide count - use enough to cover the suggested "
                   "outline clearly. Presentations start from 10th July 2026 (confirm your group's "
                   "exact slot with your lecturer). Because live demos can fail, keep a backup: a "
                   "recorded video and well-labelled screenshots/photos of your working Tinkercad "
                   "or Wokwi proof of concept, so you can still show it works."),
        "verified": True,
    },

    {
        "id": "submission-platform",
        "source": "General module info",
        "keywords": ["mytimes", "where submit", "submission platform", "upload",
                     "portal", "how to submit", "file format", "what format", "pdf submit"],
        "question": "Where and in what format do I submit my work?",
        "answer": ("Assignments are submitted as softcopy PDF to MyTIMeS. Assignment 3 also "
                   "requires the Turnitin Originality Report (PDF, similarity below 20%) and "
                   "slides submitted to the slides folder."),
        "verified": True,
    },

    # ---- Assignments 1, 2 and 3 (and the student FAQ) are loaded above. ----
    # To add a new fact, copy any block, give it a new "id", and fill in the fields.
]
