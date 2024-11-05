from helpers import Helper
class Cli(Helper):

    def main(self):
        Helper.welcome()
        while True:
            Helper.menu()
            choice = input("> ")
            if choice == "1":
                Helper.list_doctors()
            elif choice == "2":
                Helper.list_patients()
            elif choice == "3":
                Helper.list_appointments()
            elif choice == "4":
                Helper.find_doctor_by_name()
            elif choice == "5":
                Helper.find_patient_by_name()
            elif choice == "6":
                Helper.find_appointment_by_date_and_time()
            elif choice == "7":
                Helper.create_doctor()
            elif choice == "8":
                Helper.create_patient()
            elif choice == "9":
                Helper.create_appointment()
            elif choice == "10":
                Helper.update_doctor()
            elif choice == "11":
                Helper.update_patient()
            elif choice == "12":
                Helper.update_appointment()
            elif choice == "13":
                Helper.delete_doctor()
            elif choice == "14":
                Helper.delete_patient()
            elif choice == "15":
                Helper.delete_appointment()
            elif choice == "16":
                Helper.find_patients_by_doctor_name()
            elif choice == "17":
                Helper.exit_program()
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    cli = Cli()
    cli.main()