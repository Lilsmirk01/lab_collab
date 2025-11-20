import tkinter as tk

# -------------------------
# Simple COVID-19 Expert System
# -------------------------
def diagnose():
    fever = fever_var.get()
    cough = cough_var.get()
    
    # Simple rules
    if fever == "yes" and cough == "yes":
        result_var.set("Diagnosis: COVID-19 (suspected)")
    elif fever == "no" and cough == "no":
        result_var.set("Diagnosis: Healthy")
    else:
        result_var.set("Diagnosis: Cannot determine, consult a doctor")

# Tkinter GUI
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
