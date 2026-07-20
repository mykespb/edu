#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# progide-hist.py
# 2026-06-25 2026-06-25 1.3

# ~ Изучаем среды и инструменты программирования и проектирования. 
# ~ Весь вывод на английском; формат list[dict].
# ~ Перечисли 40 наиболее популярных за 30 лет. Укажи:
# ~ - name: название
# ~ - years: годы использования
# ~ - company: компания-разработчик
# ~ - proglangs: для каких языков программирования
# ~ - techno: для каких технологий
# ~ - netmode:есть ли сетевой режим
# ~ - musermode: есть ли многопользовательский режим
# ~ - aimode: есть ли объединение с ИИ

# ---------------------------------------------------

data = [
{
"name": "Visual Studio",
"years": "1997-2026",
"company": "Microsoft",
"proglangs": ["C++", "C#", "F#", "Visual Basic", "TypeScript", "Python"],
"techno": [".NET", "Cloud", "Desktop", "Web", "Mobile", "Gaming"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Visual Studio Code",
"years": "2015-2026",
"company": "Microsoft",
"proglangs": ["JavaScript", "TypeScript", "Python", "C++", "Go", "Rust", "Java"],
"techno": ["Web", "Cloud", "Serverless", "Cross-platform", "DevOps"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "IntelliJ IDEA",
"years": "2001-2026",
"company": "JetBrains",
"proglangs": ["Java", "Kotlin", "Scala", "Groovy"],
"techno": ["Enterprise Java", "Android", "Web", "Cloud", "Spring Framework"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Eclipse",
"years": "2001-2026",
"company": "Eclipse Foundation",
"proglangs": ["Java", "C++", "PHP", "Python"],
"techno": ["Desktop", "Enterprise Java", "Embedded Systems", "Web"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Xcode",
"years": "2003-2026",
"company": "Apple",
"proglangs": ["Swift", "Objective-C", "C++", "C"],
"techno": ["iOS", "macOS", "watchOS", "tvOS", "visionOS"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "Android Studio",
"years": "2013-2026",
"company": "Google",
"proglangs": ["Java", "Kotlin", "C++"],
"techno": ["Android OS", "Mobile", "Android TV", "Wear OS"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "PyCharm",
"years": "2010-2026",
"company": "JetBrains",
"proglangs": ["Python", "JavaScript", "SQL", "HTML/CSS"],
"techno": ["Data Science", "Machine Learning", "Web Development", "Django", "Flask"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "WebStorm",
"years": "2010-2026",
"company": "JetBrains",
"proglangs": ["JavaScript", "TypeScript", "HTML/CSS"],
"techno": ["Frontend", "Node.js", "React", "Angular", "Vue", "Next.js"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "GitLab",
"years": "2011-2026",
"company": "GitLab Inc.",
"proglangs": ["Polyglot", "YAML"],
"techno": ["DevOps", "CI/CD", "Version Control", "Cloud Native"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "GitHub",
"years": "2008-2026",
"company": "Microsoft",
"proglangs": ["Polyglot", "Markdown"],
"techno": ["Version Control", "CI/CD", "DevOps", "Open Source hosting"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Docker",
"years": "2013-2026",
"company": "Docker Inc.",
"proglangs": ["Agnostic"],
"techno": ["Containerization", "Microservices", "Cloud Native", "DevOps"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Kubernetes",
"years": "2014-2026",
"company": "CNCF / Google",
"proglangs": ["YAML", "Go"],
"techno": ["Container Orchestration", "Cloud Compute", "Microservices"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Jira",
"years": "2002-2026",
"company": "Atlassian",
"proglangs": ["Agnostic"],
"techno": ["Agile Project Management", "Issue Tracking", "Software Architecture Design"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Enterprise Architect",
"years": "2000-2026",
"company": "Sparx Systems",
"proglangs": ["C++", "Java", "C#", "PHP", "Python"],
"techno": ["UML Modeling", "SysML", "Software Design", "Business Architecture"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "No"
},
{
"name": "Figma",
"years": "2016-2026",
"company": "Figma Inc.",
"proglangs": ["Agnostic"],
"techno": ["UI/UX Design", "Prototyping", "Design Systems", "Handoff"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "MATLAB",
"years": "1996-2026",
"company": "MathWorks",
"proglangs": ["MATLAB"],
"techno": ["Signal Processing", "Control Systems", "Data Analysis", "AI & Math"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "Simulink",
"years": "1996-2026",
"company": "MathWorks",
"proglangs": ["MATLAB", "C/C++ code generation"],
"techno": ["Model-Based Design", "Simulation", "Embedded Systems Systems Engineering"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "Postman",
"years": "2012-2026",
"company": "Postman Inc.",
"proglangs": ["JavaScript"],
"techno": ["API Development", "REST", "GraphQL", "gRPC", "API Testing"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Sublime Text",
"years": "2008-2026",
"company": "Sublime HQ",
"proglangs": ["Python", "C++", "JavaScript", "Polyglot"],
"techno": ["Text Editing", "Scripting", "Web Development"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "Atom",
"years": "2014-2022",
"company": "GitHub / Microsoft",
"proglangs": ["JavaScript", "HTML/CSS", "Polyglot"],
"techno": ["Web Development", "Hackable Text Editing"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "No"
},
{
"name": "Notepad++",
"years": "2003-2026",
"company": "Don Ho",
"proglangs": ["C++", "C", "Java", "HTML/CSS", "Polyglot"],
"techno": ["Source Code Editing", "Scripting", "Configuration Management"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "Vim",
"years": "1996-2026",
"company": "Bram Moolenaar / Community",
"proglangs": ["Polyglot"],
"techno": ["Terminal Code Editing", "Server Administration", "Scripting"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "Neovim",
"years": "2014-2026",
"company": "Community Open Source",
"proglangs": ["Lua", "Polyglot"],
"techno": ["Terminal Code Editing", "Scripting", "Highly Custom IDEs"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "NetBeans",
"years": "1996-2026",
"company": "Sun Microsystems / Apache",
"proglangs": ["Java", "PHP", "C++", "HTML5"],
"techno": ["Enterprise Java", "Desktop GUI", "Web Development"],
"netmode": "Yes",
"musermode": "No",
"aimode": "No"
},
{
"name": "Delphi (RAD Studio)",
"years": "1996-2026",
"company": "Borland / Embarcadero",
"proglangs": ["Object Pascal", "C++"],
"techno": ["Windows Desktop", "Cross-platform Mobile", "Database client-server"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "Borland C++ Builder",
"years": "1997-2008",
"company": "Borland",
"proglangs": ["C++", "C"],
"techno": ["Windows GUI Apps", "Desktop Engineering", "Rapid App Development"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "Microsoft Visual SourceSafe",
"years": "1996-2005",
"company": "Microsoft",
"proglangs": ["Agnostic"],
"techno": ["Early Version Control", "Windows Desktop Teams"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "No"
},
{
"name": "Adobe Dreamweaver",
"years": "1997-2024",
"company": "Macromedia / Adobe",
"proglangs": ["HTML", "CSS", "JavaScript", "PHP"],
"techno": ["WYSIWYG Web Design", "Early Frontend E-commerce"],
"netmode": "Yes",
"musermode": "No",
"aimode": "No"
},
{
"name": "Unity",
"years": "2005-2026",
"company": "Unity Technologies",
"proglangs": ["C#"],
"techno": ["Game Development", "3D/2D Engines", "AR/VR Integration"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Unreal Engine",
"years": "1998-2026",
"company": "Epic Games",
"proglangs": ["C++", "Blueprints"],
"techno": ["AAA Game Development", "Virtual Production", "CGI Simulation"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "Jupyter Notebook",
"years": "2014-2026",
"company": "Project Jupyter / Community",
"proglangs": ["Python", "R", "Julia"],
"techno": ["Data Science", "Machine Learning Experiments", "Academic Research"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "DBeaver",
"years": "2010-2026",
"company": "DBeaver Corporation",
"proglangs": ["SQL"],
"techno": ["Database Administration", "Data Analysis", "NoSQL Management"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "Qt Creator",
"years": "2009-2026",
"company": "The Qt Company",
"proglangs": ["C++", "QML", "Python"],
"techno": ["Embedded Systems GUI", "Cross-platform Automotive UI Desktop"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "Ansible",
"years": "2012-2026",
"company": "Red Hat",
"proglangs": ["YAML", "Python"],
"techno": ["Infrastructure as Code", "Configuration Deployment Automation", "DevOps"],
"netmode": "Yes",
"musermode": "No",
"aimode": "Yes"
},
{
"name": "Terraform",
"years": "2014-2026",
"company": "HashiCorp",
"proglangs": ["HCL"],
"techno": ["Cloud Provisioning Infrastructure as Code DevOps Multi-Cloud"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "SoapUI",
"years": "2005-2026",
"company": "SmartBear Software",
"proglangs": ["Groovy", "XML"],
"techno": ["SOAP API Web Services Integration Testing Enterprise Architecture"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "RStudio (Posit)",
"years": "2011-2026",
"company": "Posit, PBC",
"proglangs": ["R", "Python"],
"techno": ["Statistical Computing Data Visualization Business Intelligence Data Science"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
},
{
"name": "WebRatio",
"years": "2001-2026",
"company": "WebRatio s.r.l.",
"proglangs": ["Java", "IFML", "BPMN"],
"techno": ["Model-Driven Web Engineering Low-Code Solutions Enterprise App Design"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "No"
},
{
"name": "Rational Rose",
"years": "1996-2010",
"company": "Rational Software / IBM",
"proglangs": ["C++", "Java", "Ada"],
"techno": ["UML Object-Oriented Analysis Software Architecture Design Blueprinting"],
"netmode": "No",
"musermode": "No",
"aimode": "No"
},
{
"name": "Cursor",
"years": "2023-2026",
"company": "Anysphere",
"proglangs": ["TypeScript", "JavaScript", "Python", "Polyglot"],
"techno": ["AI-native Code Generation Context-aware Software Engineering Web Cloud"],
"netmode": "Yes",
"musermode": "Yes",
"aimode": "Yes"
}
]

# ---------------------------------------------------

from collections import Counter, defaultdict
from pprint import pprint

# ---------------------------------------------------

print("\n#1. все по годам")

data.sort(key = lambda x: x['years'] )

print( *(f"{ide['years']:10} : {ide['name']}" for ide in data), sep="\n")

# ~ #1. все по годам
# ~ 1996-2005  : Microsoft Visual SourceSafe
# ~ 1996-2010  : Rational Rose
# ~ 1996-2026  : MATLAB
# ~ 1996-2026  : Simulink
# ~ 1996-2026  : Vim
# ~ 1996-2026  : NetBeans
# ~ 1996-2026  : Delphi (RAD Studio)
# ~ 1997-2008  : Borland C++ Builder
# ~ 1997-2024  : Adobe Dreamweaver
# ~ 1997-2026  : Visual Studio
# ~ 1998-2026  : Unreal Engine
# ~ 2000-2026  : Enterprise Architect
# ~ 2001-2026  : IntelliJ IDEA
# ~ 2001-2026  : Eclipse
# ~ 2001-2026  : WebRatio
# ~ 2002-2026  : Jira
# ~ 2003-2026  : Xcode
# ~ 2003-2026  : Notepad++
# ~ 2005-2026  : Unity
# ~ 2005-2026  : SoapUI
# ~ 2008-2026  : GitHub
# ~ 2008-2026  : Sublime Text
# ~ 2009-2026  : Qt Creator
# ~ 2010-2026  : PyCharm
# ~ 2010-2026  : WebStorm
# ~ 2010-2026  : DBeaver
# ~ 2011-2026  : GitLab
# ~ 2011-2026  : RStudio (Posit)
# ~ 2012-2026  : Postman
# ~ 2012-2026  : Ansible
# ~ 2013-2026  : Android Studio
# ~ 2013-2026  : Docker
# ~ 2014-2022  : Atom
# ~ 2014-2026  : Kubernetes
# ~ 2014-2026  : Neovim
# ~ 2014-2026  : Jupyter Notebook
# ~ 2014-2026  : Terraform
# ~ 2015-2026  : Visual Studio Code
# ~ 2016-2026  : Figma
# ~ 2023-2026  : Cursor

# ---------------------------------------------------

print("\n# 2. все иишечки")

ai = list(filter(lambda x: x['aimode'] == 'Yes', data))

ai.sort(key = lambda x: x['years'] )

print( *(f"{ide['years']:10} : {ide['name']}" for ide in ai), sep="\n")

# ~ ## 2. все иишечки
# ~ 1996-2026  : MATLAB
# ~ 1996-2026  : Simulink
# ~ 1996-2026  : Delphi (RAD Studio)
# ~ 1997-2026  : Visual Studio
# ~ 1998-2026  : Unreal Engine
# ~ 2001-2026  : IntelliJ IDEA
# ~ 2001-2026  : Eclipse
# ~ 2002-2026  : Jira
# ~ 2003-2026  : Xcode
# ~ 2005-2026  : Unity
# ~ 2008-2026  : GitHub
# ~ 2010-2026  : PyCharm
# ~ 2010-2026  : WebStorm
# ~ 2010-2026  : DBeaver
# ~ 2011-2026  : GitLab
# ~ 2011-2026  : RStudio (Posit)
# ~ 2012-2026  : Postman
# ~ 2012-2026  : Ansible
# ~ 2013-2026  : Android Studio
# ~ 2013-2026  : Docker
# ~ 2014-2026  : Kubernetes
# ~ 2014-2026  : Neovim
# ~ 2014-2026  : Jupyter Notebook
# ~ 2014-2026  : Terraform
# ~ 2015-2026  : Visual Studio Code
# ~ 2016-2026  : Figma
# ~ 2023-2026  : Cursor

# ---------------------------------------------------

print("\n# 3. все современные питоновские иишечки")

aipm = [ ide for ide in ai if 'Python' in ide['proglangs'] and '2026' in ide['years'] ]

print( *(f"{ide['years']:10} : {ide['name']}" for ide in aipm), sep="\n")

# ~ # 3. все современные питоновские иишечки
# ~ 1997-2026  : Visual Studio
# ~ 2001-2026  : Eclipse
# ~ 2010-2026  : PyCharm
# ~ 2011-2026  : RStudio (Posit)
# ~ 2012-2026  : Ansible
# ~ 2014-2026  : Jupyter Notebook
# ~ 2015-2026  : Visual Studio Code
# ~ 2023-2026  : Cursor

# ---------------------------------------------------
print()

