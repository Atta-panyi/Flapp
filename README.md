SIMPLE FLASK APP (FLAAP)
  
Prerequisites:

Download and install Python from https://www.python.org/downloads/

Open your terminal and run (pip install Flask) to install Flask

Install Git and Clone  Repository

Create a Virtual Environment (Optional but Recommended)

Install Flask Within Virtual Environment (pip install Flask) if Created


A. test_new.py:

Flask Application with Secure User Input Handling - 
This application demonstrates a fundamental security practice in web development; escaping user input before displaying it in the template. This helps prevent potential cross-site scripting (XSS) vulnerabilities.
The application utilizes flask  for a lightweight web framework. It employs markupsafe.escape to sanitize user input within the hello route, and it also Includes a sample route (/) to greet users with the escaped name

Instructions: 

1. Replace 'your_name' in the "hello route" with the desired name to be displayed
2. Run the application from the command line
3. Visit the link displayed in the command line; e.g ( http://127.0.0.1:5000/)  in your web browser. You'll see the greeting with the escaped name


B. test.py:

Flask Web Application, Basic Routing using port =80 - 
The @app.route('/') decorator creates a route for the root URL (/).
The hello (name) function takes a name argument and personalizes the greeting.
The if __name__ == '__main__': block configures the application to run on port 80, assuming you have the necessary permissions. It should look like this; 

if __name__ == '__main__':  
app.run(debug=True, host='0.0.0.0', port=80) 
   


Instructions:

Run the flask application same as before. The only change is the (Optional Port 80)

Access the application:

1. Open your web browser and navigate to the url e.g. http://localhost:5000/. You should see "hello world".
2. To test the dynamic route, visit the provided URL
3. Input your name  after the URL and you will see the imputed name. e.g “hello Maria” 

C. test_rt.py:

Running a  Flask User Profile Application - 
The application demonstrates how to create a user profile route in Flask.

Instructions:

1. Run the flask app as usual, to access the application

2. Navigate to the directory containing the application files 

3. Run python app.py to start the Flask development server

4. Open your web browser to visit http://127.0.0.1:5000/user/<username>, replacing <username> with the desired name. The server runs in debug mode, which provides helpful error messages during development. However, disable it for production environments. 

This is a basic example. You can extend it to include more features like user authentication and handling different HTTP methods.

Note: 
The file main.py represents my mistakes. Holding on to them for reference !


