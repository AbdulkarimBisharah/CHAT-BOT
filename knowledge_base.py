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
    # ASSIGNMENT 2 - PARTIAL. Only the blank brief/template was available.
    # Treat as unverified until the lecturer confirms real module values.
    # ========================================================================
    {
        "id": "a2-overview",
        "source": "Assignment 2 brief (Assessment Task 2) - template",
        "keywords": ["assignment 2", "a2", "task 2", "assessment task 2",
                     "architecture", "second assignment", "what is a2"],
        "question": "What is Assignment 2 about?",
        "answer": ("Assessment Task 2 is a group assignment based on MLO2: design the "
                   "architecture, algorithms and technology needed to develop an IoT system for "
                   "a real-world problem. Part 1 covers system architecture and technology stack "
                   "(hardware, software platforms, communication protocols, data storage). Part "
                   "2 covers algorithm design and implementation (control algorithms, data "
                   "processing, mobile app functionality, and security)."),
        "verified": False,
    },
    {
        "id": "a2-weightage",
        "source": "Assignment 2 brief (Assessment Task 2) - template",
        "keywords": ["assignment 2 weightage", "a2 worth", "a2 weight",
                     "how much is assignment 2"],
        "question": "How much is Assignment 2 worth?",
        "answer": ("The Assignment 2 template lists a weightage of 30% (Part 1: 15%, Part 2: "
                   "15%), with a hand-in date of Week 12, Friday. Please confirm the exact date "
                   "with your lecturer, as this comes from the template rather than a finalised "
                   "brief."),
        "verified": False,
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

    # ---- PLACEHOLDER: copy this block for Assignment 1 once uploaded ----
    # {
    #     "id": "a1-overview",
    #     "source": "Assignment 1 brief",
    #     "keywords": ["assignment 1", "a1", "task 1", "first assignment"],
    #     "question": "What is Assignment 1 about?",
    #     "answer": "FILL IN from the Assignment 1 brief.",
    #     "verified": False,
    # },
]
