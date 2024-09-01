This assignment was done without the help of without any LLM's. So baiscally i created my lame dataset which looks like this {
        "scenario": "The patient is not breathing",
        "response": "Patient is not breathing. Please start CPR immediately. Push hard and fast in the center of the chest."
    },
    {
        "scenario": "The patient is choking",
        "response": "Patient is choking. Perform the Heimlich maneuver. Place a fist just above the navel and thrust inward and upward."
    },
    So for better experience we can use data from this dataset only for testing purpose. So basically what I did in this project is i created my own index file and kind of db's(faiss is not a vector db) and then played with threads as mentioned in the assignment.
