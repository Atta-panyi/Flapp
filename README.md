SIMPLE FLASK APP (FLAAP)

A. test_new.py: 
Flask Application with Secure User Input Handling - This application demonstrates a fundamental security practice in web development; escaping user input before displaying it in the template. This helps prevent potential cross-site scripting (XSS) vulnerabilities. It utilizes flask  for a lightweight web framework. It employs markupsafe.escape to sanitize user input within the hello route, and it also Includes a sample route (/) to greet users with the escaped name


Instructions: 
- Ensure you have Python 3 installed on your system. You can check by running python3 --version or python --version (if Python 3 is set as the default) in your terminal. If not installed, download it from https://www.python.org/downloads/.
- open text editor of choice. ( I use Vscode)
- Install the Flask framework using the pip package manager: Pip install Flask
- Create a new file and name it. (e.g, hello_app.py)
- Copy and paste the provided code into the hello_app.py file
- Save the file in a convenient location on your computer. 
- To run the application, execute the command  hello_app.py

This will start the Flask development server. You should see an output in the terminal indicating that the server is running, typically on http://127.0.0.1:5000/ (localhost, port 5000).


Access the application:
- Open a web browser and navigate to the URL displayed in the terminal output 
- You should see the message "Hello, World!" displayed in your browser.

 Dynamic name greetings (optional):This code  is set to greet someone named "World" by default. To personalize the greeting, append a name to the URL in your browser. For example, to greet someone named "Maria,"  append Maria after the URL. This will display "Hello, Maria!" in the browser.
When you're done  testing, you can stop the Flask development server by pressing Ctrl+C (Windows/Linux) or Command+C (macOS) in the terminal window.


B. test.py:
Flask Web Application, basic Routing using port =80 - The @app.route('/') decorator creates a route for the root URL (/).The hello (name) function takes a name argument and personalizes the greeting.
The if __name__ == '__main__': block configures the application to run on port 80, assuming you have the necessary permissions. 


Instructions: 
- Open a terminal or command prompt.
- Install Flask and MarkupSafe using the following command: pip install Flask MarkupSafe
-  Create a new Python file with a descriptive name (e.g., app.py).
- Paste the  code into the file.
- Save the file in a preferred location.
- Navigate to the directory where you saved the Python file in your terminal.
- Run the following command: python app.py
  

Access the Application:
- Open a web browser and type the address: http://localhost/
- To try the route that accepts a name, append a name to the URL: http://localhost/?name=Your%20Name

Security: Using escape() is important for preventing code injection attacks.

Debugging: Setting debug=True enables debugging features, but it's recommended to disable it in production for security reasons.

Accessing from Other Devices: If you want to access the application from other devices on your network, use your computer's IP address instead of localhost in the URL. 
   

C. test_rt.py: 
Running a  Flask User Profile Application - The application demonstrates how to create a user profile route in Flask.

Instructions:
- Ensure you have Python installed. 
- Install Flask using the following command in your terminal: pip install Flask
- Install MarkupSafe using the command: pip install MarkupSafe
- Create a new Python file (e.g., app.py or any preferred name).
- Paste the provided code into that file.
- Open your terminal or command prompt.
- Navigate to the directory where you saved the file 
- Execute the following command to start the Flask application: python app.py

Access the Application:
- Open a web browser and visit the following URL: http://127.0.0.1:5000/user/<username>
- Replace <username> with an actual username you want to display (e.g., Maria).

Development Mode: The debug=True argument enables development mode, which provides helpful error messages and automatic reloading upon code changes.

Customization: You can modify the code to add more features, routes, and templates as you learn more about Flask.

Troubleshooting: refer to the Flask documentation (https://flask.palletsprojects.com/) for more comprehensive information and troubleshooting guidance.

