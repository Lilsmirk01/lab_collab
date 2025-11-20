# Install clipspy first if not installed:
# pip install clipspy

import tkinter as tk
from clipspy import Environment

# -------------------------
# Setup CLIPS Environment
# -------------------------
env = Environment()

# Define simple rules for COVID-19 diagnosis
env.build("""
(deftemplate symptom
   (slot name)
   (slot value))

(defrule covid_positive
   (symptom (name fever) (value yes))
   (symptom (name cough) (value yes))
   =>
   (assert (diagnosis covid)))
   
(defrule covid_negative
   (symptom (name fever) (value no))
   (symptom (name cough) (value no))
   =>
   (assert (diagnosis healthy)))

(deffacts initial-facts
   (symptom (name fever) (value unknown))
   (symptom (name cough) (value unknown)))
""")

# -------------------------
# GUI using Tkinter
# -------------------------
def diagnose():
    fever = fever_var.get()
    cough = cough_var.get()
    
    # Reset environment
    env.reset()
    
    # Update facts
    env.assert_string(f"(symptom (name fever) (value {fever}))")
    env.assert_string(f"(symptom (name cough) (value {cough}))")
    
    # Run inference
    env.run()
    
    # Check result
    for fact in env.facts():
        if fact.template.name == "diagnosis":
            result_var.set(f"Diagnosis: {fact['diagnosis']}")
            return
    
    result_var.set("Diagnosis: Cannot determine")

# Tkinter window
root = tk.Tk()
root.title("COVID-19 Diagnosis Expert System")

tk.Label(root, text="Do you have fever?").grid(row=0, column=0)
tk.Label(root, text="Do you have cough?").grid(row=1, column=0)

fever_var = tk.StringVar(value="no")
cough_var = tk.StringVar(value="no")
result_var = tk.StringVar()

tk.OptionMenu(root, fever_var, "yes", "no").grid(row=0, column=1)
tk.OptionMenu(root, cough_var, "yes", "no").grid(row=1, column=1)

tk.Button(root, text="Diagnose", command=diagnose).grid(row=2, column=0, columnspan=2)
tk.Label(root, textvariable=result_var, fg="blue").grid(row=3, column=0, columnspan=2)

root.mainloop()
