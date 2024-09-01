AI Receptionist
**This assignment was done without the help of without any LLM's**. So baiscally i created my lame dataset which looks like this {
        "scenario": "The patient is not breathing",
        "response": "Patient is not breathing. Please start CPR immediately. Push hard and fast in the center of the chest."
    },
    {
        "scenario": "The patient is choking",
        "response": "Patient is choking. Perform the Heimlich maneuver. Place a fist just above the navel and thrust inward and upward."
    },
    So for better experience we can use data from this dataset only for testing purpose. So basically what I did in this project is i created my own index file and kind of db's(faiss is not a vector db) and then played with threads as mentioned in the assignment.
   ** Procedure for cloning the assignment**
   1. run "git clone https://github.com/l-ordkp/Smallest-Assignment.git" on your terminal
   2. then open this folder using terminal and create a virtual env using command "python3 -m venv venv"
   3. then download all the requirements using the command "pip install -r requirements.txt"
   4. After installing all the requirements run the command "streamlit run .\main.py "
   5. Click on the link on your terminal which will open the UI in your browser.
   6. To escape it use "ctrl+c"
    
