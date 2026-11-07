import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class HospitalView:
    def __init__(self, patient_controller, doctor_controller,
                 appointment_controller, hospital_controller):

        self.patient_controller = patient_controller
        self.doctor_controller = doctor_controller
        self.appointment_controller = appointment_controller
        self.hospital_controller = hospital_controller

        self.window = tk.Tk()
        self.window.title("Hospital Management System")
        self.window.geometry("800x700")
        self.create_patient()
        self.create_doctor()
        self.create_appointment()
        self.create_hospital()
# -------------------- PATIENT --------------------

    def create_patient(self):
        window = tk.Toplevel(self.window)
        window.title("Patient")
        window.geometry("400x750")

        tk.Label(window, text="PATIENT", font=("Arial", 16)).pack(pady=10)

        tk.Label(window, text="National ID").pack()
        national_id = tk.Entry(window)
        national_id.pack()

        tk.Label(window, text="Name").pack()
        name = tk.Entry(window)
        name.pack()

        tk.Label(window, text="Family").pack()
        family = tk.Entry(window)
        family.pack()

        tk.Label(window, text="Phone").pack()
        phone = tk.Entry(window)
        phone.pack()

        tk.Label(window, text="Address").pack()
        address = tk.Entry(window)
        address.pack()

        tk.Label(window, text="Patient ID").pack()
        patient_id = tk.Entry(window)
        patient_id.pack()

        tk.Label(window, text="Disease").pack()
        disease = tk.Entry(window)
        disease.pack()

        tk.Label(window, text="Birth Date (YYYY-MM-DD)").pack()
        birth_date = tk.Entry(window)
        birth_date.pack()

        def save():
            try:
                birth = datetime.strptime(
                    birth_date.get(), "%Y-%m-%d"
                ).date()

                result = self.patient_controller.save_patient(
                    int(national_id.get()),
                    name.get(),
                    family.get(),
                    phone.get(),
                    address.get(),
                    int(patient_id.get()),
                    disease.get(),
                    birth
                )

                messagebox.showinfo("Patient", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def find():
            try:
                result = self.patient_controller.find_by_patient_id(
                    int(patient_id.get())
                )
                messagebox.showinfo("Patient", str(self.get_object(result)))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def delete():
            try:
                result = self.patient_controller.delete_by_patient_id(
                    int(patient_id.get())
                )
                messagebox.showinfo("Patient", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def show_all():
            try:
                result = self.patient_controller.find_all_patient()
                messagebox.showinfo("Patients", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))


        tk.Button(window, text="Save Patient", command=save).pack(pady=5)
        tk.Button(window, text="Find Patient", command=find).pack(pady=5)
        tk.Button(window, text="Delete Patient", command=delete).pack(pady=5)
        tk.Button(window, text="Show All Patients", command=show_all).pack(pady=5)


# -------------------- DOCTOR --------------------

    def create_doctor(self):
        window = tk.Toplevel(self.window)
        window.title("Doctor")
        window.geometry("400x750")

        tk.Label(window, text="DOCTOR", font=("Arial", 16)).pack(pady=10)

        tk.Label(window, text="National ID").pack()
        national_id = tk.Entry(window)
        national_id.pack()

        tk.Label(window, text="Name").pack()
        name = tk.Entry(window)
        name.pack()

        tk.Label(window, text="Family").pack()
        family = tk.Entry(window)
        family.pack()

        tk.Label(window, text="Phone").pack()
        phone = tk.Entry(window)
        phone.pack()

        tk.Label(window, text="Address").pack()
        address = tk.Entry(window)
        address.pack()

        tk.Label(window, text="Specialty").pack()
        specialty = tk.Entry(window)
        specialty.pack()

        tk.Label(window, text="License").pack()
        license_entry = tk.Entry(window)
        license_entry.pack()

        tk.Label(window, text="Appointment ID").pack()
        appointment_id_entry=tk.Entry(window)
        appointment_id_entry.pack()

        tk.Label(window, text="Experience").pack()
        experience = tk.Entry(window)
        experience.pack()

        def save():
            try:
                result = self.doctor_controller.save_doctor(
                    int(national_id.get()),
                    name.get(),
                    family.get(),
                    phone.get(),address.get(),
                    specialty.get(),
                    int(license_entry.get()),
                    int(experience.get())
                )

                messagebox.showinfo("Doctor", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def find():
            try:
                result = self.doctor_controller.find_by_license(
                    int(license_entry.get())
                )
                messagebox.showinfo("Doctor", str(self.get_object(result)))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def delete():
            try:
                result = self.doctor_controller.delete_by_license(
                    int(license_entry.get())
                )
                messagebox.showinfo("Doctor", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def show_all():
            try:
                result = self.doctor_controller.find_all_doctors()
                messagebox.showinfo("Doctors", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def examine():
            try:
                license = int(license_entry.get())
                appointment_id = int(appointment_id_entry.get())

                result = self.doctor_controller.examine(
                    license, appointment_id
                )

                messagebox.showinfo("Examine", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def prescribe():
            try:
                result = self.doctor_controller.prescribe()
                messagebox.showinfo("Prescribe", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def today_appointments():
            try:
                license = int(license_entry.get())

                result = self.appointment_controller.find_today_appointments(license)

                messagebox.showinfo("Today's Appointments", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))
        tk.Button(window, text="Save Doctor", command=save).pack(pady=5)
        tk.Button(window, text="Find Doctor", command=find).pack(pady=5)
        tk.Button(window, text="Delete Doctor", command=delete).pack(pady=5)
        tk.Button(window, text="Show All Doctors", command=show_all).pack(pady=5)
        tk.Button(window,text="Examine Patient",command=examine).pack(pady=5)
        tk.Button(window,text="Prescribe Patient",command=prescribe).pack(pady=5)
        tk.Button(window,text="Today Appointments",command=today_appointments).pack(pady=5)


    # -------------------- APPOINTMENT --------------------

    def create_appointment(self):
        window = tk.Toplevel(self.window)
        window.title("Appointment")
        window.geometry("400x650")

        tk.Label(window, text="APPOINTMENT", font=("Arial", 16)).pack(pady=10)

        tk.Label(window, text="Appointment ID").pack()
        appointment_id = tk.Entry(window)
        appointment_id.pack()

        tk.Label(window, text="Patient ID").pack()
        patient_id = tk.Entry(window)
        patient_id.pack()

        tk.Label(window, text="Doctor License").pack()
        doctor_license = tk.Entry(window)
        doctor_license.pack()

        tk.Label(window, text="Date and Time (YYYY-MM-DD HH:MM)").pack()
        appointment_date = tk.Entry(window)
        appointment_date.pack()

        tk.Label(window, text="Name").pack()
        name_entry = tk.Entry(window)
        name_entry.pack()

        tk.Label(window, text="Family").pack()
        family_entry = tk.Entry(window)
        family_entry.pack()

        def save():
            try:
                patient = self.patient_controller.find_by_patient_id(
                    int(patient_id.get())
                )
                patient = self.get_object(patient)

                doctor = self.doctor_controller.find_by_license(
                    int(doctor_license.get())
                )
                doctor = self.get_object(doctor)

                date_time = datetime.strptime(
                    appointment_date.get(), "%Y-%m-%d %H:%M"
                )

                result = self.appointment_controller.save_appointment(
                    int(appointment_id.get()),
                    doctor,
                    patient,
                    date_time
                )

                messagebox.showinfo("Appointment", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def find():
            try:
                result = self.appointment_controller.find_by_appointment_id(
                    int(appointment_id.get())
                )
                messagebox.showinfo("Appointment", str(self.get_object(result)))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def delete():
            try:
                result = self.appointment_controller.delete_appointment(
                    int(appointment_id.get())
                )
                messagebox.showinfo("Appointment", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def show_all():
            try:
                result = self.appointment_controller.find_all_appointments()
                messagebox.showinfo("Appointments", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def find_doctor():
            try:
                name = name_entry.get()
                family = family_entry.get()

                result = self.appointment_controller.find_doctor(
                    name, family
                )

                messagebox.showinfo("Doctor Appointments", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def find_patient():
            try:
                name = name_entry.get()
                family = family_entry.get()

                result = self.appointment_controller.find_patient(
                    name, family
                )

                messagebox.showinfo("Patient Appointments", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))
        tk.Button(window, text="Save Appointment", command=save).pack(pady=5)
        tk.Button(window, text="Find Appointment", command=find).pack(pady=5)
        tk.Button(window, text="Delete Appointment", command=delete).pack(pady=5)
        tk.Button(window, text="Show All Appointments", command=show_all).pack(pady=5)
        tk.Button(window,text="Find Doctor Appointments",command=find_doctor).pack(pady=5)
        tk.Button(window,text="Find Patient Appointments",command=find_patient).pack(pady=5)

    # -------------------- HOSPITAL --------------------

    def create_hospital(self):
        window = tk.Toplevel(self.window)
        window.title("Hospital")
        window.geometry("400x350")

        tk.Label(window, text="HOSPITAL", font=("Arial", 16)).pack(pady=15)

        def show_patients():
            try:
                result = self.hospital_controller.find_all_patient()
                messagebox.showinfo("Patients", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def show_doctors():
            try:
                result = self.hospital_controller.find_all_doctor()
                messagebox.showinfo("Doctors", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        def show_appointments():
            try:
                result = self.hospital_controller.find_all_appointment()
                messagebox.showinfo("Appointments", str(result))

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(window, text="Show All Patients",
                  command=show_patients).pack(pady=10)

        tk.Button(window, text="Show All Doctors",
                  command=show_doctors).pack(pady=10)

        tk.Button(window, text="Show All Appointments",
                  command=show_appointments).pack(pady=10)

    # -------------------- HELPER --------------------

    def get_object(self, result):
        if isinstance(result, tuple):
            return result[0]
        return result

    # -------------------- INITIALIZE --------------------

    def __init__(self, patient_controller, doctor_controller,
                 appointment_controller, hospital_controller):

        self.patient_controller = patient_controller
        self.doctor_controller = doctor_controller
        self.appointment_controller = appointment_controller
        self.hospital_controller = hospital_controller

        self.window = tk.Tk()
        self.window.title("Hospital Management System")
        self.window.geometry("400x400")

        tk.Label(
            self.window,
            text="HOSPITAL MANAGEMENT SYSTEM",
            font=("Arial", 16)
        ).pack(pady=30)

        tk.Button(
            self.window,
            text="Patient",
            width=25,
            command=self.create_patient
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="Doctor",
            width=25,
            command=self.create_doctor
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="Appointment",
            width=25,
            command=self.create_appointment
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="Hospital",
            width=25,
            command=self.create_hospital
        ).pack(pady=10)

    def run(self):
        self.window.mainloop()

