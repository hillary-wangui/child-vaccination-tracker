# main.py

import hospital
import moh_branch
import hospital_moh_branch
import parent
import child
import vaccination_detail

def main_menu():
    while True:
        print("\n== Main Menu ==")
        print("1. Add Hospital")
        print("2. Add MoH Branch")
        print("3. Link Hospital to MoH Branch")
        print("4. Add Parent")
        print("5. Add Child")
        print("6. Add Vaccination Details")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            hospital.add_hospital()
        elif choice == '2':
            moh_branch.add_moh_branch()
        elif choice == '3':
            hospital_moh_branch.link_hospital_to_moh()
        elif choice == '4':
            parent.add_parent()
        elif choice == '5':
            child.add_child()
        elif choice == '6':
            vaccination_detail.add_vaccination_details()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
