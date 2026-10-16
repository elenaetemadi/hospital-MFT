import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment

patients = []
doctors = Doctor.doctors

# ---------------- Main Window ----------------

win = tk.Tk()
win.title("Hospital Management")
win.geometry("500x350")

tk.Label(
    win,
    text="Hospital Management System",
    font=("Arial", 18, "bold")
).pack(pady=25)

# ---------------- Helper Functions ----------------

def create_window(title, size="850x550"):
    window = tk.Toplevel(win)
    window.title(title)
    window.geometry(size)
    return window

def add_field(parent, label, row):
    tk.Label(parent, text=label).grid(
        row=row, column=0, padx=8, pady=6, sticky="w"
    )
    entry = tk.Entry(parent, width=28)
    entry.grid(row=row, column=1, padx=8, pady=6)
    return entry

def refresh_table(table, data):
    for item in table.get_children():
        table.delete(item)

    for item in data:
        table.insert("", "end", values=item)

# ---------------- Patients Window ----------------

def open_patients():

    window = create_window("Patients")

    form = tk.LabelFrame(window, text="Register Patient")
    form.pack(fill="x", padx=10, pady=10)

    name = add_field(form, "Name", 0)
    national_id = add_field(form, "National ID", 1)
    phone = add_field(form, "Phone", 2)
    address = add_field(form, "Address", 3)
    patient_id = add_field(form, "Patient ID", 4)
    disease = add_field(form, "Disease", 5)
    birth_date = add_field(form, "Birth Date (YYYY-MM-DD)", 6)

    columns = ("name", "national_id", "phone", "patient_id",
               "disease", "birth_date")

    table = ttk.Treeview(
        window, columns=columns, show="headings", height=10
    )

    headings = {
        "name": "Name",
        "national_id": "National ID",
        "phone": "Phone",
        "patient_id": "Patient ID",
        "disease": "Disease",
        "birth_date": "Birth Date"
    }

    for column, heading in headings.items():
        table.heading(column, text=heading)
        table.column(column, width=120)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    def show_patients():
        data = []
        for p in patients:
            data.append((
                p.name,
                p.national_id,
                p.phone,
                p.patient_id,
                p.disease,
                p.birth_date
            ))
        refresh_table(table, data)

    def save_patient():
        try:
            birthday = date.fromisoformat(birth_date.get().strip())

            patient = Patient(
                national_id.get().strip(),
                name.get().strip(),
                phone.get().strip(),
                address.get().strip(),
                patient_id.get().strip(),
                disease.get().strip(),
                birthday
            )

            patients.append(patient)
            show_patients()
            messagebox.showinfo("Patient", "Patient registered successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        form, text="Save Patient", command=save_patient
    ).grid(row=7, column=0, columnspan=2, pady=10)

    tk.Button(
        window, text="Refresh", command=show_patients
    ).pack(pady=5)

    show_patients()

# ---------------- Doctors Window ----------------

def open_doctors():

    window = create_window("Doctors")

    form = tk.LabelFrame(window, text="Register Doctor")
    form.pack(fill="x", padx=10, pady=10)

    name = add_field(form, "Name", 0)
    national_id = add_field(form, "National ID", 1)
    phone = add_field(form, "Phone", 2)
    address = add_field(form, "Address", 3)
    specialty = add_field(form, "Specialty", 4)
    license_id = add_field(form, "License", 5)
    experience = add_field(form, "Experience (years)", 6)

    columns = ("name", "national_id", "phone",
               "specialty", "license", "experience")

    table = ttk.Treeview(
        window, columns=columns, show="headings", height=10
    )

    headings = {
        "name": "Name",
        "national_id": "National ID",
        "phone": "Phone",
        "specialty": "Specialty",
        "license": "License",
        "experience": "Experience"
    }

    for column, heading in headings.items():
        table.heading(column, text=heading)
        table.column(column, width=125)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    def show_doctors():
        data = []
        for d in doctors:
            data.append((
                d.name,
                d.national_id,
                d.phone,
                d.specialty,
                d.license,
                d.experience
            ))
        refresh_table(table, data)

    def save_doctor():
        try:
            doctor = Doctor(
                national_id.get().strip(),
                name.get().strip(),
                phone.get().strip(),
                address.get().strip(),
                specialty.get().strip(),
                license_id.get().strip(),
                int(experience.get())
            )

            show_doctors()
            messagebox.showinfo("Doctor", "Doctor registered successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        form, text="Save Doctor", command=save_doctor
    ).grid(row=7, column=0, columnspan=2, pady=10)

    tk.Button(
        window, text="Refresh", command=show_doctors
    ).pack(pady=5)

    show_doctors()

# ---------------- Appointments Window ----------------

def open_appointments():

    window = create_window("Appointments")

    form = tk.LabelFrame(window, text="Book Appointment")
    form.pack(fill="x", padx=10, pady=10)

    tk.Label(form, text="Patient").grid(
        row=0, column=0, padx=8, pady=6
    )

    patient_var = tk.StringVar()
    patient_box = ttk.Combobox(
        form,
        textvariable=patient_var,
        state="readonly",
        width=35
    )
    patient_box.grid(row=0, column=1, padx=8, pady=6)

    tk.Label(form, text="Doctor").grid(
        row=1, column=0, padx=8, pady=6
    )

    doctor_var = tk.StringVar()
    doctor_box = ttk.Combobox(
        form,
        textvariable=doctor_var,
        state="readonly",
        width=35
    )
    doctor_box.grid(row=1, column=1, padx=8, pady=6)

    appointment_date = add_field(form, "Date (YYYY-MM-DD)", 2)

    columns = ("appointment_id", "patient", "doctor", "date")

    table = ttk.Treeview(
        window, columns=columns, show="headings", height=12
    )

    for column, heading in (
        ("appointment_id", "Appointment ID"),
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("date", "Date")
    ):
        table.heading(column, text=heading)
        table.column(column, width=170)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    def update_choices():
        patient_box["values"] = [
            f"{p.patient_id} - {p.name}" for p in patients
        ]

        doctor_box["values"] = [
            f"{d.license} - {d.name}" for d in doctors
        ]

    def show_appointments():
        data = []
        for a in Appointment.appointments:
            data.append((
                a.appointment_id,
                a.patient.name,
                a.doctor.name,
                a.date
            ))
        refresh_table(table, data)

    def book_appointment():
        try:
            patient_index = patient_box.current()
            doctor_index = doctor_box.current()

            if patient_index == -1 or doctor_index == -1:
                raise ValueError("Select a patient and a doctor")

            selected_date = date.fromisoformat(
                appointment_date.get().strip()
            )

            patient = patients[patient_index]
            doctor = doctors[doctor_index]

            patient.book(doctor, selected_date)

            show_appointments()
            messagebox.showinfo(
                "Appointment", "Appointment booked successfully"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cancel_appointment():
        selected = table.selection()

        if not selected:
            messagebox.showerror(
                "Error", "Select an appointment from the table"
            )
            return

        appointment_id = table.item(
            selected[0], "values"
        )[0]

        for appointment in Appointment.appointments[:]:
            if str(appointment.appointment_id) == str(appointment_id):
                Appointment.appointments.remove(appointment)
                break

        show_appointments()
        messagebox.showinfo("Appointment", "Appointment cancelled")

    tk.Button(
        form, text="Book Appointment", command=book_appointment
    ).grid(row=3, column=0, columnspan=2, pady=8)

    buttons = tk.Frame(window)
    buttons.pack(pady=5)

    tk.Button(
        buttons, text="Refresh", command=show_appointments
    ).pack(side="left", padx=5)

    tk.Button(
        buttons, text="Cancel Selected Appointment",
        command=cancel_appointment
    ).pack(side="left", padx=5)

    update_choices()
    show_appointments()

# ---------------- Main Menu Buttons ----------------

tk.Button(
    win, text="Patients", width=25,
    command=open_patients
).pack(pady=8)

tk.Button(
    win, text="Doctors", width=25,
    command=open_doctors
).pack(pady=8)

tk.Button(
    win, text="Appointments", width=25,
    command=open_appointments
).pack(pady=8)

win.mainloop()