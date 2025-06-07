# Setting Up schedule_daily_update.py as a Windows Scheduled Task

This guide explains how to schedule the `schedule_daily_update.py` script to run automatically using Windows Task Scheduler.

---

## 1. Verify Script Execution

First, ensure your script runs from the command line:

python jobs\schedule_daily_update.py

If you use a virtual environment, activate it before running the script.

---

## 2. Open Task Scheduler

- Press `Win + S` and search for **Task Scheduler**.
- Open the Task Scheduler application.

---

## 3. Create a New Task

1. In the right pane, click **Create Task**.
2. On the **General** tab, enter a name (e.g., `Daily Python Update`).

---

## 4. Set the Trigger

1. Go to the **Triggers** tab.
2. Click **New**.
3. Set **Begin the task** to `On a schedule`.
4. Choose **Daily** and set the time (e.g., 6:00 AM).
5. Click **OK**.

---

## 5. Set the Action

1. Go to the **Actions** tab.
2. Click **New**.
3. Set **Action** to `Start a program`.
4. In **Program/script**, enter the path to your Python executable, e.g.:

C:\Path\To\python.exe

5. In **Add arguments (optional)**, enter:

jobs\schedule_daily_update.py

6. In **Start in (optional)**, enter the full path to your project directory (where `jobs` is located).

---

## 6. (Optional) Use a Virtual Environment

If you use a virtual environment, set **Program/script** to the Python executable inside your virtual environment.

---

## 7. Additional Settings

- On the **Conditions** tab, check **Wake the computer to run this task** if you want the task to run while the computer is asleep.
- On the **Settings** tab, check **Run task as soon as possible after a scheduled start is missed** to ensure the task runs if the computer was off at the scheduled time.

---

## 8. Save and Test

- Click **OK** to save the task.
- Right-click your task and choose **Run** to test it.

---

**Note:**  
- The task will not run if the computer is shut down at the scheduled time.
- If the computer is asleep or hibernating, enabling the wake option allows the task to run.

