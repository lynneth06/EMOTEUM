# EMOTEUM APPLICATION
EMOTEUM addresses emotional disconnect by offering a safe space for genuine self-expression through writing. Unlike social media, it promotes authenticity, emotional awareness, and healthy coping. With optional sharing, it fosters empathy and connection, helping users feel understood and supported through creativity and reflection.

OOP Concepts Used
1. Encapsulation

Encapsulation is used by keeping the data and methods inside classes. In the EMOTEUM Application, classes such as EmotionEntry, User, and Archive manage their own data and functions. Important information like emotion details, timestamps, privacy settings, and user credentials are controlled through methods, which helps protect the data from unauthorized modification and keeps the system organized.

2. Abstraction

Abstraction is applied by separating complex processes into simple and understandable classes. Each class only shows the necessary functions needed by the system. For example, the PromptEngine only focuses on generating therapeutic prompts, while the AccessControlManager handles authentication and permissions. This makes the application easier to maintain and improve.

3. Inheritance

Inheritance supports future expansion of the application by allowing new classes to reuse existing properties and methods from other classes. This reduces code duplication and allows developers to create additional features such as advanced emotion tracking, multimedia handling, or admin controls without rewriting the entire program structure.

4. Polymorphism

Polymorphism is used when different objects interact using common methods. For example, different emotion tags and prompts can be processed through the same functions without changing the program flow. This makes the system more flexible and allows the application to support different emotional categories and future feature additions easily.

Technologies Used
1. Python Programming Language

Python was used as the main programming language because it is simple, readable, and suitable for Object-Oriented Programming. It also allows easier implementation of data structures, authentication systems, and archive management.

2. Console-Based Interface

The application uses a console-based interface where users interact with the system through text menus and commands. This approach simplifies development while focusing on the functionality and logic of the application.

3. Object-Oriented Programming (OOP)

OOP concepts were used to organize the system into classes and objects. This improves maintainability, scalability, and code readability.

4. Built-in Python Libraries

The application uses Python built-in libraries such as:

datetime for timestamps and archive management
list for storing entries
dictionary for emotion classification and prompt mapping
Project Structure
EMOTEUM_APPLICATION/
│                                                                                                                                                                

├── emoteum.py

├── EmotionEntry Class

├── EmotionStorage Class

├── Tag Class

├── ClassificationSystem Class

├── Archive Class

├── EmotionTag Class

├── PromptRepository Class

├── PromptEngine Class

├── User Class

├── AccessControlManager Class

└── Main Application Runner

How To Run
   1. Requirement Python 3.x
   2. Clone this repository:
           Git clone https://github.com/lynneth06/EMOTEUM
Navigate the project folder:
    EMOTEUM
Run the Application:
     Python main.py
Running Test
Run automated test using pytest:
      Py-m pytest-v
Or run the test in the test folder:
      pytest test/
Export Report
Inside the application:
1. Go to the Report Tab 
2. Click Export Report
3. Output file will be saved as:
    Report.txt

Author
Developed as a school project by:
•	Jeralyn Luna (GitHub Profile of Luna)
(https://github.com/Jera-collab)
•	Lynneth Giba (GitHub Profile of Giba)
(https://github.com/lynneth06)

