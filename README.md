# Gossip: Social blogging website

<h2>Overview</h2>

<p>This project is a Flask-based web application designed to serve as a dynamic and user-friendly blog platform.</br>
It allows users to create, read, update, and delete blog posts, offering a seamless experience for both content creators and readers.</p>

</p>

![image](https://github.com/Gabtoriel/webstack-portfolio-project/assets/99370798/198df4f5-3560-45da-9111-61d11ca76e6d)


![image](https://github.com/Gabtoriel/webstack-portfolio-project/assets/99370798/fcc42f0b-6ee5-43e7-a6b2-6a35eae8a7fa)


</p>

<h2>Key Features</h2>
<p>
<li>
  <b>User Authentication:</b> Seamlessly manage user accounts with secure registration, login, and session management functionalities provided by Flask-Login.
</li>
</p>

<p>
<li>
  <b>Content Management:</b> Effortlessly create, edit, and delete blog posts through a simple and intuitive interface designed for ease of use.
</li>
</p>

<p>
<li>
  <b>Responsive Design:</b> Ensure a consistent and optimized user experience across devices with Bootstrap, allowing users to access and interact with content on desktops, tablets, and smartphones alike.
</li>
</p>

<p>
<li>
<b>Database Flexibility:</b> Utilize SQLite during development for rapid prototyping and transition to PostgreSQL in production for scalability and performance enhancements.
</li>
</p>

<p>
<li>
<b>Search Capabilities:</b> Enhance content discoverability with planned integration of Elasticsearch, enabling users to quickly find relevant articles based on keywords and topics.
</li>
</p>

<p>
<h2>Why Choose Flask Blog?</h2>
</p>

<p>Flask Blog stands out with its simplicity, flexibility, and extensibility, making it an ideal choice for developers looking to build scalable web applications with Python. Whether you're a beginner exploring web development or an experienced developer seeking a lightweight yet powerful framework, Flask Blog offers a solid foundation to build upon.</p>


<h2>Technologies Used</h2>

<p>
  <li>
    <b>Flask:</b> A lightweight and versatile Python web framework for backend development.
  </li>
</p>
<p>
  <li>
    <b>SQLite and PostgreSQL:</b> Database systems chosen for development and production environments, respectively.
  </li>
</p>
<p>
  <li>
    <b>Bootstrap:</b> Frontend framework for creating responsive and mobile-first designs.
  </li>
</p>
<p>
  <li>
    <b>Flask-Login:</b> Provides user session management and authentication functionalities.
  </li>
</p>
<p>
  <li>
    <b>SQLAlchemy:</b> Python SQL toolkit and Object-Relational Mapping (ORM) for database management.
  </li>
</p>




<h2>Installation</h2>

<b>1. Clone the repository:</b>
   ```
   https://github.com/Gabtoriel/webstack-portfolio-project/
   cd webstack-portfolio-project
  ```
  

<b>2. Create a virtual environment and activate it:</b>

   ```
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate
   ```

<b>3. Install dependencies:</b>
   ```
   pip install -r requirements.txt
   ```

<b>4. Set up the database:</b>
   <ul>
     For SQLite (development):
     
       flask db upgrade
   </ul>

   <ul>
     For PostgreSQL (production), set your database URI in config.py and run migrations:
     
       flask db upgrade
   </ul>

<b>5. Set environment variables:</b>
   ```
   source ./setup.sh
   ```

<b>6. Start the Flask development server:</b>
   ```
   flask run
   ```

<b>7. Access the application in your web browser at</a> `http://localhost:5000`


<h2>Usage</h2>


<p>
  <li>
    Navigate to the homepage to view existing blog posts.
  </li>
</p>

<p>
  <li>
    Register an account or log in to create new posts or manage existing ones.
  </li>
</p>

<p>
  <li>
    Customize the application further as per your project requirements.
  </li>
</p>


<h2>License</h2>
This project is licensed under the MIT License. See the <a href="https://github.com/Gabtoriel/webstack-portfolio-project/blob/master/LICENSE">LICENSE</a> file for more details.

<h2>Acknowledgements</h2>
<p>
  <li>
    <a href="https://flask.palletsprojects.com/en/3.0.x/">Flask Documentation</a>
  </li>
</p>

<p>
  <li>
    <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">Bootstrap Documentation</a>
  </li>
</p>

<p>
  <li>
    <a href="https://docs.sqlalchemy.org/en/20/orm/quickstart.html">SQLAlchemy Documentation</a>
  </li>
</p>


<h2>Authors</h2>
<p>
  <li>
    <a href="https://github.com/Gabtoriel">Chibuike Eke</a>
  </li>
</p>

<p>
  <li>
    <a href="https://github.com/sohaib20022">Sohaib Bayou</a>
  </li>
</p>

<p>
  <li>
    <a href="https://github.com/1CyBeR-J1">Marvellous Ojeleke</a>
  </li>
</p>











