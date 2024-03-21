Simple Flask App

test_new.py: 
Demonstrates the use of escape from the markupsafe library to prevent Cross-Site Scripting (XSS) vulnerabilities. It takes a user-provided name as input, escapes any potentially harmful characters, and displays a greeting message.

Key Features:
XSS Protection: The escape function ensures that user input is treated as text and not interpreted as HTML code, mitigating XSS attacks.
Simple Flask Example: This code provides a clear and concise example of using Flask and markupsafe for basic web development.


test.py:
the code demonstrates essential concepts for building web applications
Routing: Handles different URL patterns (/ in this case).
Dynamic Content: Generates greetings tailored to user-provided names.
XSS Prevention: Employs the escape function from markupsafe to prevent Cross-Site Scripting (XSS) vulnerabilities, ensuring user input is treated as plain text.
steps:
1. Save the code as app.py.
2. Run the application from the command line:
3. Open your local development server URL in your web browser to see the default "hello world" message.
4. To personalize the greeting, visit the URL, name=your_name (replace your_name with the desired name).

Key Features:
Offers two routes for displaying greetings:
/: Returns a generic "hello world" message.
/ with a name parameter (/?name=your_name): Greets the user by name with proper escaping.
Provides clear and concise code, making it easy to understand for Flask beginners.

test_rt.py:
Demonstates a basic route that dynamically retrieves a username from the URL path and displays a greeting message. It also emphasizes the importance of escaping user input to prevent Cross-Site Scripting (XSS) vulnerabilities.

Key Feature:
Routing with Path Variables: Captures a username from the URL path segment and personalizes the greeting message. 
