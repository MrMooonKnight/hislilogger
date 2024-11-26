---

# **HisLiLigogger \- Documentation**

---

# **Introduction** 

Hislilogger is a comprehensive digital forensics tool designed to extract, process, and visualise key pieces of forensic data from a user's system. It is built using Python and Flask and provides a web-based interface where you can analyse various forensic artefacts such as browser history, bookmarks, system services, installed software, and more.

---

# **Use Case** 

Hislilogger is ideal for:

* **Digital forensic investigators**: who need to gather and analyse key forensic data from a system.  
* **Researchers**: interested in studying user activity patterns and software usage.  
* **System administrators**: who want an overview of system services, installed software, and user activity.

---

# **Purpose** 

The purpose of Hislilogger is to provide a user-friendly tool that simplifies the process of gathering and analysing forensic data. The project covers:

* **Browser history**: Extract Firefox browsing history.  
  **Purpose:** 

  Extracts Firefox browsing history

  **Key Functions:**

  \- copy\_database(): Creates safe copy of Firefox database  
  \- extract\_history(): Retrieves browsing history with timestamps  
  \- save\_to\_json(): Exports data in structured JSON format

  **Output:** 

  Timestamped JSON files in /data/firefox/history/  
* **Bookmarks**: Extract Firefox bookmarks.  
  **Purpose:** 

  Retrieves Firefox bookmarks

  **Key Functions:**

  \- copy\_database(): Creates safe copy of Firefox database  
  \- extract\_bookmarks(): Retrieves bookmark data  
  \- save\_to\_json(): Exports formatted bookmark data

  **Output:** 

  Timestamped JSON files in /data/firefox/bookmarks/  
* **Bash history**: Extract the command history from Bash or Zsh shells.

  **Purpose:** 

  Retrieves command-line history

  **Key Functions:**

  \- read\_bash\_history(): Extracts bash history

  \- parse\_history(): Processes history entries

  \- save\_to\_json(): Stores command history

  **Output:** 

  Timestamped JSON files in /data/bash\_history/

* **Recently used files**: Retrieve metadata from files that were recently accessed in the system.

  **Purpose:** 

  Tracks recently accessed files

  **Key Functions:**

  \- parse\_xbel\_file(): Processes XBEL format

  \- save\_to\_json(): Stores recent file access data

  **Output:** 

  Timestamped JSON files in /data/recently\_used/

* **System services**: List all system services (active, inactive, etc.).

  **Purpose:**

  Lists system services and their states

  **Key Functions:**

  \- run\_systemctl\_command(): Executes systemctl queries

  \- parse\_services\_output(): Processes command output

  \- save\_services\_to\_json(): Stores service information

  **Output:** 

  Timestamped JSON files in /data/services/

* **Installed software**: List all installed software with version details.

  **Purpose:** 

  Catalogs installed software

  **Key Functions:**

  \- run\_dpkg\_query\_command(): Queries package manager

  \- parse\_software\_output(): Processes package information

  \- save\_software\_to\_json(): Stores software inventory

  **Output:** 

  Timestamped JSON files in /data/softwares/

* ### **Web Interface (app.py)**

  **Purpose:** 

  Provides web-based data visualization

  **Key Features:**

  \- Dashboard for all collected data  
  \- Individual views for each data type  
  \- Data filtering and sorting   
  \- JSON data export options

  **Routes:**

  \- /: Main dashboard  
  \- /firefox/history: Browser history view  
  \- /firefox/bookmarks: Bookmarks view  
  \- /services: System services view  
  \- /softwares: Installed software view  
  \- /bash-history: Command history view  
  \- /recently-used: Recent files view

---

# **File Structure** {#file-structure}

| hislilogger ├── application│   ├── app.py                      \# Main Flask application│   ├── data                        \# Directory for storing the extracted data│   │   ├── bash\_history            \# Stores extracted Bash history in JSON format│   │   ├── firefox│   │       ├── bookmarks           \# Stores extracted Firefox bookmarks in JSON format│   │       └── history             \# Stores extracted Firefox history in JSON format│   │   ├── recently\_used           \# Stores extracted recently used files in JSON format│   │   ├── services                \# Stores extracted system services in JSON format│   │   └── softwares               \# Stores extracted installed software data in JSON format│   ├── getBashHistory.py           \# Script for extracting Bash history│   ├── getBookmarks.py             \# Script for extracting Firefox bookmarks│   ├── getHistory.py               \# Script for extracting Firefox browsing history│   ├── getRecentlyUsed.py          \# Script for extracting metadata from recently used files│   ├── getServices.py              \# Script for extracting system services│   ├── getSoftwares.py             \# Script for extracting installed software│   ├── requirements.txt            \# Project dependencies│   └── templates                   \# HTML templates for rendering the web interface│       ├── index.html              \# Homepage│       ├── firefoxhistory.html     \# Firefox history page│       ├── firefoxbookmarks.html   \# Firefox bookmarks page│       ├── bashhistory.html        \# Bash history page│       ├── services.html           \# System services page│       ├── softwares.html          \# Installed software page│       └── view\_\*.html             \# View templates for displaying extracted data├── README.md                       \# Project README└── setup.py                        \# Setup script for installing and running the project |
| :---- |

# 

# 

# 

# 

# **Technical Implementation** 

## **Data Storage**

| Data Structure:/data/  ├── firefox/  │   ├── history/  │   └── bookmarks/  ├── services/  ├── softwares/  ├── bash\_history/  └── recently\_used/ |
| :---- |

## **Database Handling**

* Uses SQLite for Firefox data  
* Implements safe database copying  
* Maintains data integrity  
* Handles concurrent access

  ## **Web Framework**

* Flask-based implementation  
* Jinja2 templating  
* Bootstrap for responsive design  
* AJAX for dynamic updates

  ## **Data Processing**

* JSON format for flexibility  
* Timestamp-based organization  
* Error handling and logging  
* Data validation

---

# **Detailed Explanation of Scripts** {#detailed-explanation-of-scripts}

### **app.py** {#app.py}

This is the main Flask application that provides the web interface and handles various routes for viewing and updating different types of data (e.g., Firefox history, bookmarks, Bash history, etc.). The key routes in `app.py` include:

* `/firefox_history`: Displays Firefox browsing history.  
* `/firefox_bookmarks`: Displays Firefox bookmarks.  
* `/bash_history`: Displays Bash shell history.  
* `/services`: Displays system services.  
* `/softwares`: Displays installed software.  
  This script also includes functionality for updating each dataset by running the respective Python scripts using `subprocess`.

### **getBashHistory.py** {#getbashhistory.py}

This script extracts the command history from the `.bash_history` or `.zsh_history` files in the user's home directory. It processes the command history, reverses it to show the most recent commands first, and stores the data in JSON format under `application/data/bash_history`.

Key functions:

* **`process_history`**: Reads the shell history and saves it as a JSON file.  
* **`print_banner`**: Displays a banner using `pyfiglet`.

### **getBookmarks.py** {#getbookmarks.py}

This script extracts Firefox bookmarks from the `places.sqlite` database located in the user's Firefox profile. It retrieves the URLs and the time they were added and stores the data in JSON format.

Key functions:

* **`extract_bookmarks`**: Queries the Firefox database to extract bookmarks.  
* **`copy_database`**: Copies the `places.sqlite` database to the project directory to prevent corruption.

### **getHistory.py** {#gethistory.py}

This script extracts the browsing history from Firefox using the same `places.sqlite` database as the bookmarks. It retrieves URLs along with the timestamp of when they were visited and stores this data in JSON format.

Key functions:

* **`extract_history`**: Queries the Firefox database to extract browsing history.  
* **`copy_database`**: Copies the `places.sqlite` database to the project directory.

### **getRecentlyUsed.py** {#getrecentlyused.py}

This script parses the `recently-used.xbel` file located in the user's home directory. This file contains metadata about recently accessed files. The script extracts the file paths and timestamps of the last accessed files and saves them in JSON format.

Key functions:

* **`parse_xbel_file`**: Parses the XBEL file and extracts metadata.  
* **`save_to_json`**: Saves the extracted data to a JSON file.

### **getServices.py** {#getservices.py}

This script runs the `systemctl list-unit-files --type=service` command to retrieve a list of all system services, including their states (enabled, disabled, etc.). The output is then parsed and saved in JSON format.

Key functions:

* **`run_systemctl_command`**: Runs the `systemctl` command to list services.  
* **`parse_services_output`**: Parses the output of the `systemctl` command.

### **getSoftwares.py** {#getsoftwares.py}

This script runs the `dpkg-query -l` command (on Linux systems) to list all installed software and their versions. The output is parsed and saved in JSON format.

Key functions:

* **`run_dpkg_query_command`**: Runs the `dpkg-query` command to list installed software.

* ## **`parse_software_output`**: Parses the output of the `dpkg-query` command.

## 

# **Hislilogger Installation and Setup Guide**

## **Overview**

setup.py is the installation and management script for HisliLogger. It provides various command-line options to download, install, and run the application with proper configuration.

## **Prerequisites** {#prerequisites}

Ensure you have the following installed:

* **Python 3.6+**  
* **pyfiglet**  
* **Git**  
* **pip** (Python package installer)  
* Python virtual environment  
* fastfetch

## **Features**

* Automated project installation  
* Project download from GitHub  
* Dependencies installation  
* Virtual environment setup  
* Application startup management  
* Colourful CLI interface

## **Command-Line Options**

python setup.py \[-h\] \[-a\] \[-d\] \[-i\] \[-s\] \[-r\]

Options:  
\-h, \--help     : Show help message  
\-a  –auto     : Automated Installation (recommended for new users)  
\-d, \--download : Download project from GitHub  
\-i, \--install  : Install requirements  
\-s, \--start    : Start the application  
\-r, \--restart  : Restart the application

## **Installation Methods**

### **1\. Automated Installation (Recommended)**

| python setup.py \-a |
| :---- |

Running the script with the `-a` option automates the entire process, including:

* **Downloading the Project**: The script will clone the Hislilogger repository from GitHub if it doesn’t already exist locally.  
* **Setting Up the Virtual Environment**: The script will create a virtual environment in the `application/venv` directory.  
* **Installing Dependencies**: The script will execute `pip install -r requirements.txt` to install all the required Python libraries (e.g., Flask, pyfiglet, colorama).  
* **Sets Permissions.**  
* **Starting the Application**: Once the setup is complete, the Flask application will start automatically, and you can access it through your web browser.

| *http://127.0.0.1:5000/* |
| :---- |

## 

### **2\. Manual Step-by-Step Installation**

| \# Step 1: Download the projectpython setup.py \-d\# Step 2: Install requirementspython setup.py \-i\# Step 3: Start the applicationpython setup.py \-s |
| :---- |

## **What Happens During Installation**

1. **Project Download (-d)**

   * Checks if project directory exists  
   * Clones repository from GitHub  
   * Creates necessary directories  
2. **Requirements Installation (-i)**

   * Creates Python virtual environment  
   * Instals dependencies from requirements.txt  
   * Configures fastfetch permissions  
3. **Application Start (-s)**

   * Activates virtual environment  
   * Runs fastfetch system information  
   * Starts Flask application

## **Directory Structure After Setup**

./application/  
├── venv/                 \# Virtual environment  
├── data/                 \# Data storage  
├── static/               \# Static files  
├── templates/            \# HTML templates  
├── fastfetch             \# System information tool  
└── various Python files

## **Troubleshooting**

### **Common Issues and Solutions**

1. **Permission Errors**

| \# Run with sudo if neededsudo python setup.py \-a |
| :---- |

2. **Virtual Environment Issues**

| \# Manual virtual environment creationpython3 \-m venv ./application/venvsource ./application/venv/bin/activate |
| :---- |

3. **Download Failed**

| \# Clean and retryrm \-rf ./applicationpython setup.py \-d |
| :---- |

## **Usage Examples**

### **First-time Installation**

| \# For new users, use automated installationgit clone https://github.com/yourusername/hislilogger.gitcd hisliloggerpython setup.py \-a |
| :---- |

### **Updating Existing Installation**

| \# Remove old installation and reinstallpython setup.py \-dpython setup.py \-ipython setup.py \-s |
| :---- |

### **Quick Start (After Installation)**

| \# Just start the applicationpython setup.py \-s |
| :---- |

### **Restart Application**

| \# Restart if neededpython setup.py \-r |
| :---- |

## **Important Notes**

1. **System Requirements**

   * Python 3.8 or higher  
   * Git installed  
   * Internet connection for initial download  
   * Linux-based operating system  
2. **Directory Permissions**

   * Ensure write permissions in installation directory  
   * fastfetch requires execution permissions  
3. **Virtual Environment**

   * Automatically created in ./application/venv  
   * Isolates project dependencies  
   * Activated automatically when starting  
4. **Post-Installation**

   * Access web interface at [http://localhost:5000](http://localhost:5000)  
   * All data will be stored in ./application/data  
   * Configuration files in project root

---

# **Conclusion** {#conclusion}

Hislilogger is a robust and user-friendly digital forensics tool designed to simplify the process of extracting, analysing, and visualising forensic data. Its modular design and intuitive web interface make it accessible to a wide range of users, including digital forensic investigators, researchers, and system administrators.

The tool's ability to handle browser artefacts, system services, installed software, and command history demonstrates its versatility. With features like automated JSON data export, responsive web design, and streamlined setup via the `setup.py` script, Hislilogger ensures both functionality and ease of use.

The `setup.py` script simplifies the installation process of Hislilogger, offering both automated and manual options (-a, \-d, \-i, \-s, \-r)  to cater to different user preferences and virtual environments. The Flask-based web interface further enhances usability, providing dynamic updates, filtering, and a centralised dashboard for data analysis.

By leveraging Python, Flask, and modern development practices, Hislilogger empowers users to gather and interpret key forensic insights quickly and efficiently, making it an indispensable tool in the digital forensics domain.

---


