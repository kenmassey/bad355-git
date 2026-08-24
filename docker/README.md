# Business Analytics Workspace Setup Guide

To ensure a seamless experience with identical software configurations 
across all operating systems, our course utilizes a pre-configured **Docker** container. 

It's an environment (toolbox) that includes: Python, R, Octave, DuckDB, etc.

---

## Prerequisites & Installation by Operating System

Follow the instructions for your specific operating system to install Docker and set up your workspace.

---

### Option A: Windows 10 / 11

1. **Download & Install Docker Desktop:**
   - Download the installer from [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).
   - Run the installer. Ensure the option **"Use WSL 2 instead of Hyper-V"** is checked during setup.
   - Restart your computer if prompted.

2. **Verify Docker Desktop is Running:**
   - Launch **Docker Desktop** from your Start Menu.
   - Wait until the status icon in the bottom corner turns green / shows "Engine Running".

3. **Open Terminal:**
   - Open **PowerShell** or **Windows Terminal** from your Start Menu.

---

### Option B: macOS (Apple Silicon M1/M2/M3/M4 or Intel)

1. **Download & Install Docker Desktop:**
   - Download the appropriate installer for your Mac architecture (Apple Silicon vs. Intel Chip) from [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
   - Open the downloaded `.dmg` file and drag **Docker** to your **Applications** folder.

2. **Launch Docker Desktop:**
   - Open **Docker** from your Applications folder or Spotlight (`Cmd + Space`).
   - Accept the service agreement and wait for the whale icon in your top menu bar to stay steady.

3. **Open Terminal:**
   - Open **Terminal** (or **iTerm2**) from your Applications / Utilities folder or Spotlight.

---

### Option C: Debian Linux

You can set up Docker using native Debian packages in a few terminal commands:

1. **Install Docker Engine and Docker Compose:**
   Open your terminal and run:
   ```bash
   sudo apt update && sudo apt install -y docker.io docker-compose
   ```
2. **Configure Non-Root Docker Access:**
   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```

3. **Verify Installation:**
   ```bash
   docker compose version
   ```

---

### Option D: Chromebooks (ChromeOS)

Chromebooks run Docker inside the built-in Linux subsystem.

1. **Enable Linux on ChromeOS:**
   - Open your Chromebook **Settings**.
   - Go to **About ChromeOS** > **Linux development environment** and select **Turn On**.
   - Follow the prompt (allocating at least 20 GB of disk space is recommended).

2. **Install Docker inside the Linux Terminal:**
   - Open the **Terminal** app from your Chromebook app drawer.
   - Update and install Docker & Compose:
     ```bash
     sudo apt update && sudo apt install -y docker.io docker-compose
     ```
   - Grant your Linux user access to Docker:
     ```bash
     sudo usermod -aG docker $USER
     newgrp docker
     ```

3. **Verify Installation:**
   ```bash
   docker compose version
   ```

---

## Quick Start Guide (All Operating Systems)

Once Docker is installed and running on your machine, launch the environment using the following steps:

### Step 1: Create Your Course Directory & Configuration

Open your terminal application (**PowerShell** on Windows, **Terminal** on Mac/Debian/Chromebook) 
and run the combined command below. 

```bash
mkdir -p ~/cn-analytics 
cd ~/cn-analytics 
```

---

### Step 2: Save the compose file.
Download [docker-compose.yml](https://github.com/kenmassey/bad355/blob/main/docker/docker-compose.yml) and save it
to your newly created *cn-analytics* folder.

---

### Step 3: Launch the Environment

Run the following command inside your `~/cn-analytics` directory:

```bash
docker compose up -d
```

Docker will download the container image
and start the JupyterLab server.

---

### Step 4: Access JupyterLab

1. Go to a browser (Firefox or Chrome)
   ```text
   http://localhost:8888
   ```

---

### Stop 5: Clone the class github repository

From JupyterLab, open a *Terminal* and enter:

```bash
git clone https://github.com/kenmassey/bad355-git.git
```

This will make a copy of shared class files in a folder called
bad355 within your work folder.

---

## Working with Files & Data Persistence

- **Local File Sync:** The directory `~/cn-analytics` on your machine 
maps directly to `/home/jovyan/work` inside JupyterLab. 
Any file saved inside `work/` in JupyterLab is saved locally on your computer.

You should periodically back up your files do another location, e.g.
Dropbox or USB.

---

## Stopping and Restarting

- **To Stop the Container:**
  Open a new terminal in `~/cn-analytics` and run:
  ```bash
  docker compose down
  ```
