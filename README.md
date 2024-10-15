<h1>iDoc Medical Robot</h1>

<p>
  iDoc Medical Robot is a web-based chatbot framework designed to assist with medical-related queries and tasks. It is built using the Chainlit framework and integrates with language models such as <strong>llama-2-7b-chat</strong> to provide conversational AI support. The backend is implemented in Python and uses <strong>FASSI</strong> for database management.
</p>

<h2>Features</h2>
<ul>
  <li><strong>Interactive Chatbot</strong>: Handles user queries related to medical information and tasks.</li>
  <li><strong>LLM Integration</strong>: Uses <strong>llama-2-7b-chat</strong> models for intelligent responses.</li>
  <li><strong>Flexible Model Support</strong>: Works with both <strong>llama-2-7b-chat.ggmlv3.q8_0.bin</strong> and <strong>llama-2-7b-chat.ggmlv3.q4_0.bin</strong> models.</li>
  <li><strong>Python-Based Backend</strong>: Powered by Python for ease of development and deployment.</li>
  <li><strong>FASSI Database</strong>: Efficient database management for storing and retrieving data.</li>
</ul>

<h2>Prerequisites</h2>
<ul>
  <li><strong>Python 3.8+</strong></li>
  <li><strong>Chainlit Framework</strong>: Install via <code>pip install chainlit</code></li>
  <li><strong>llama-2-7b-chat Models</strong>: Download either the <code>ggmlv3.q8_0.bin</code> or <code>ggmlv3.q4_0.bin</code> model.</li>
  <li><strong>FASSI</strong>: Ensure FASSI is installed and configured for database management.</li>
</ul>

<h2>Setup and Installation</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/Sanil07/idoc-medicalRobot.git
cd idoc-medicalRobot</code></pre>
  </li>
  <li>Create and activate a virtual environment (optional but recommended):
    <pre><code>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate</code></pre>
  </li>
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Download the <strong>llama-2-7b-chat</strong> model you want to use:
    <ul>
      <li><code>ggmlv3.q8_0.bin</code> for higher precision</li>
      <li><code>ggmlv3.q4_0.bin</code> for better performance on lower-end machines.</li>
    </ul>
  </li>
  <li>Configure FASSI for database management (if required, follow the documentation on configuring FASSI).</li>
  <li>Run the application:
    <pre><code>python app.py</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<p>
  Once the application is running, access the chatbot by navigating to the provided URL. The chatbot can handle various medical queries and tasks, backed by the llama-2-7b-chat models.
</p>

<h2>Model Selection</h2>
<ul>
  <li><strong>llama-2-7b-chat.ggmlv3.q8_0.bin</strong>: Offers better accuracy but requires more resources.</li>
  <li><strong>llama-2-7b-chat.ggmlv3.q4_0.bin</strong>: Optimized for performance on lower-resource environments.</li>
</ul>

<h2>Contributing</h2>
<p>
  Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
</p>

<h2>License</h2>
<p>
  This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.
</p>
