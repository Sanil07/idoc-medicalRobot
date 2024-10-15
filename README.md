iDoc Medical Robot
iDoc Medical Robot is a web-based chatbot framework designed to assist with medical-related queries and tasks. It is built using the Chainlit framework and integrates with language models such as llama-2-7b-chat to provide conversational AI support. The backend is implemented in Python and uses FASSI for database management.

Features
Interactive Chatbot: Handles user queries related to medical information and tasks.
LLM Integration: Uses llama-2-7b-chat models for intelligent responses.
Flexible Model Support: Works with both llama-2-7b-chat.ggmlv3.q8_0.bin and llama-2-7b-chat.ggmlv3.q4_0.bin models.
Python-Based Backend: Powered by Python for ease of development and deployment.
FASSI Database: Efficient database management for storing and retrieving data.
Prerequisites
Python 3.8+
Chainlit Framework: Install via pip install chainlit
llama-2-7b-chat Models: Download either the ggmlv3.q8_0.bin or ggmlv3.q4_0.bin model.
FASSI: Ensure FASSI is installed and configured for database management.
Setup and Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Sanil07/idoc-medicalRobot.git
cd idoc-medicalRobot
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Download the llama-2-7b-chat model you want to use:

ggmlv3.q8_0.bin for higher precision
ggmlv3.q4_0.bin for better performance on lower-end machines.
Configure FASSI for database management (if required, follow the documentation on configuring FASSI).

Run the application:

bash
Copy code
python app.py
Usage
Once the application is running, access the chatbot by navigating to the provided URL. The chatbot can handle various medical queries and tasks, backed by the llama-2-7b-chat models.

Model Selection
You can choose between two models for chatbot responses:

llama-2-7b-chat.ggmlv3.q8_0.bin: Offers better accuracy but requires more resources.
llama-2-7b-chat.ggmlv3.q4_0.bin: Optimized for performance on lower-resource environments.
Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
