<br />
<p align="center">  
  <h1 align="center">POLLS</h1>
  <p align="center">
    A simple polls app developed with Django. 
    <br />
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

It's a simple Django app, where users can vote and display results of multiple polls. The admin area also allows adding more polls.

### Built With

- Python
  - Django

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running, follow these simple steps;

### Prerequisites

- Python
- Pipenv

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/.git
   ```
2. Install pip packages
   ```sh
   pipenv install
   ```

<!-- USAGE EXAMPLES -->

## Usage

- In the terminal, run

  ```sh
  pipenv shell #To create a virtual environment

  pipenv install #To install packages

  python manage.py runserver # This should be run in the directory containing 'manage.py' file i.e '/pollster/pollster'
  ```

- Voilà! The project should be live on the default port, 8000.
