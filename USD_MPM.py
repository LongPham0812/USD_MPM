import tkinter as tk
import tkinter.font as font
import os.path
import re

class First_Error(Exception):
    pass

class Last_Error(Exception):
    pass

class Email_Error(Exception):
    pass

class ID_Error(Exception):
    pass

class Length_Error(Exception):
    pass

class FileFoundError(Exception):
    pass

class Quan_Error(Exception):
    pass

class USD_MPM:
    def __init__(self):
        # Start screen
        self.window = tk.Tk()
        self.window.title("USD Meal Plan Maker")
        self.window.iconphoto(True, tk.PhotoImage(file = "USD_logo.png"))

        self.start_screen()

        self.window.mainloop()

    def start_screen(self):
        # label frame
        self.start_label_frame = tk.Frame(self.window, width = 400, height = 200)
        self.start_label_frame.grid(row = 1, column = 1)
        self.welcome_label = tk.Label(self.start_label_frame, text = "Welcome to the", font = font.Font(size = 10)).grid(row = 2, column = 1)
        self.USD_label = tk.Label(self.start_label_frame, text = "University of San Diego", font = font.Font(size = 20)).grid(row = 3, column = 1)
        self.MPM_label = tk.Label(self.start_label_frame, text = "Meal Plan Maker", font = font.Font(size = 20)).grid(row = 4, column = 1)
        self.click_label = tk.Label(self.start_label_frame, text = "Click anywhere to start.", font = font.Font(size = 10)).grid(row = 5, column = 1)

        # button frame
        self.start_button_frame = tk.Frame(self.window, width = 400, height = 200)
        self.start_button_frame.grid(row = 2, column = 1)
        self.add_button = tk.Button(self.start_button_frame, text = "Add New Meal Plan", font = font.Font(size = 10), command = self.start_add_handler).grid(row = 1, column = 1)
        self.edit_button = tk.Button(self.start_button_frame, text = "Edit Existing Meal Plan", font = font.Font(size = 10), command = self.start_edit_handler).grid(row = 2, column = 1)

    def start_add_handler(self):
        # go to add enter layout
        self.start_label_frame.destroy()
        self.start_button_frame.destroy()
        self.add_enter_screen()

    def start_edit_handler(self):
        # go to edit enter layout
        self.start_label_frame.destroy()
        self.start_button_frame.destroy()
        self.edit_enter_screen()

    def add_enter_screen(self):
        # label and entry frame
        self.add_entry_frame = tk.Frame(self.window, width = 400, height = 200)
        self.add_entry_frame.grid(row = 1, column = 1)

        self.add_first_name = tk.Label(self.add_entry_frame, text = "First Name:", font = font.Font(size = 10)).grid(row = 1, column = 1)
        self.first_var = tk.StringVar()
        self.add_first_name_entry = tk.Entry(self.add_entry_frame, textvariable = self.first_var).grid(row = 1, column = 2)
        
        self.add_last_name = tk.Label(self.add_entry_frame, text = "Last Name:", font = font.Font(size = 10)).grid(row = 2, column = 1)
        self.last_var = tk.StringVar()
        self.add_last_name_entry = tk.Entry(self.add_entry_frame, textvariable = self.last_var).grid(row = 2, column = 2)
        
        self.add_email = tk.Label(self.add_entry_frame, text = "Email:", font = font.Font(size = 10)).grid(row = 3, column = 1)
        self.email_var = tk.StringVar()
        self.add_email_entry = tk.Entry(self.add_entry_frame, textvariable = self.email_var).grid(row = 3, column = 2)
        
        self.add_id = tk.Label(self.add_entry_frame, text = "Student ID:", font = font.Font(size = 10)).grid(row = 4, column = 1)
        self.id_var = tk.StringVar()
        self.add_id_entry = tk.Entry(self.add_entry_frame, textvariable = self.id_var).grid(row = 4, column = 2)

        self.error_frame = tk.Frame(self.window)
        self.error_frame.grid(row = 2, column = 1)
        self.error_label = tk.Label(self.error_frame, font = font.Font(size = 10))
        self.label_grid = False

        # button frame
        self.add_enter_button_frame = tk.Frame(self.window, width = 400, height = 200)
        self.add_enter_button_frame.grid(row = 3, column = 1)
        self.add_enter_enter_button = tk.Button(self.add_enter_button_frame, text = "Enter", font = font.Font(size = 10), command = self.add_enter_enter_handler).grid(row = 1, column = 1)
        self.add_enter_quit_button = tk.Button(self.add_enter_button_frame, text = "Quit", font = font.Font(size = 10), command = self.add_enter_quit_handler).grid(row = 1, column = 2)

    def process_add_input(self):
        if self.first_var.get() == "":
            raise First_Error

        if self.last_var.get() == "":
            raise Last_Error
        
        if re.fullmatch("[A-Za-z]+@sandiego\.edu", self.email_var.get()) is None:
            raise Email_Error
        
        try:
            int(self.id_var.get())
        except:
            raise ID_Error

        if len(str(self.id_var.get())) != 9:
            raise Length_Error
    
        if os.path.isfile(self.first_var.get() + "_" + self.last_var.get() + "_" + self.email_var.get() + "_" + self.id_var.get() + ".txt"):
            raise FileFoundError

    def add_enter_enter_handler(self):
        # go to add layout
        try:
            self.process_add_input()
            self.add_entry_frame.destroy()
            self.add_enter_button_frame.destroy()
            self.error_frame.destroy()
            self.add_screen()
        except First_Error:
            self.error_label.grid(row = 1, column = 1)
            self.error_label['text'] = "Error: No input for first name entry"
        except Last_Error:
            self.error_label.grid(row = 1, column = 1)
            self.error_label['text'] = "Error: No input for last name entry"
        except Email_Error:
            self.error_label.grid(row = 1, column = 1)
            self.error_label['text'] = "Error: Email not in format '...@sandiego.edu'"
        except ID_Error:
            self.error_label.grid(row = 1, column = 1)
            self.error_label['text'] = "Error: Student ID not in all numbers"
        except Length_Error:
            self.error_label.grid(row = 1, column = 1)
            self.error_label['text'] = "Error: Student ID not nine characters long"
        except FileFoundError:
            self.error_label.grid(row = 1, column = 1)
            self.error_label['text'] = "Error: Student information already exists"

    def add_enter_quit_handler(self):
        # go back to start layout
        self.add_entry_frame.destroy()
        self.add_enter_button_frame.destroy()
        self.error_frame.destroy()
        self.start_screen()

    def add_screen(self):
        # label and entry frame
        self.pay_method_frame = tk.Frame(self.window, width = 400, height = 200)
        self.pay_method_frame.grid(row = 1, column = 1)
        
        self.meal_plan_label = tk.Label(self.pay_method_frame, text = "Enter desired amount\nof meal plan meals:", font = font.Font(size = 10)).grid(row = 1, column = 1)
        self.meal_plan_var = tk.StringVar()
        self.meal_plan_entry = tk.Entry(self.pay_method_frame, textvariable = self.meal_plan_var)
        self.meal_plan_entry.grid(row = 1, column = 2)
        self.meal_plan_entry.bind("<Key>", self.change_to_calc)

        self.guest_meal_label = tk.Label(self.pay_method_frame, text = "Enter desired amount\nof guest meals:", font = font.Font(size = 10)).grid(row = 2, column = 1)
        self.guest_meal_var = tk.StringVar()
        self.guest_meal_entry = tk.Entry(self.pay_method_frame, textvariable = self.guest_meal_var)
        self.guest_meal_entry.grid(row = 2, column = 2)
        self.guest_meal_entry.bind("<Key>", self.change_to_calc)
        
        self.dining_dollars_label = tk.Label(self.pay_method_frame, text = "Enter desired amount\nof dining dollars:", font = font.Font(size = 10)).grid(row = 3, column = 1)
        #self.dollar_sign_label = tk.Label(self.pay_method_frame, text = "$", font = font.Font(size = 10)).grid(row = 3, column = 2)
        self.dining_dollars_var = tk.StringVar()
        self.dining_dollars_entry = tk.Entry(self.pay_method_frame, textvariable = self.dining_dollars_var)
        self.dining_dollars_entry.grid(row = 3, column = 2)
        self.dining_dollars_entry.bind("<Key>", self.change_to_calc)
        
        self.equivalencies_label = tk.Label(self.pay_method_frame, text = "Enter desired amount\nof meal plan equivalencies:", font = font.Font(size = 10)).grid(row = 4, column = 1)
        self.equivalencies_var = tk.StringVar()
        self.equivalencies_entry = tk.Entry(self.pay_method_frame, textvariable = self.equivalencies_var)
        self.equivalencies_entry.grid(row = 4, column = 2)
        self.equivalencies_entry.bind("<Key>", self.change_to_calc)

        self.cost_error_label = tk.Label(self.pay_method_frame, font = font.Font(size = 10))
        
        # button frame
        self.add_button_frame = tk.Frame(self.window, width = 400, height = 200)
        self.add_button_frame.grid(row = 2, column = 1)
        self.add_calc_create_button = tk.Button(self.add_button_frame, text = "Calculate Cost", font = font.Font(size = 10), command = self.add_calculate_handler)
        self.add_calc_create_button.grid(row = 1, column = 2)
        self.add_quit_button = tk.Button(self.add_button_frame, text = "Quit", font = font.Font(size = 10), command = self.add_quit_handler).grid(row = 1, column = 3)
    
    def process_pay_input(self):
        self.is_dd = False

        self.meal_type = "meal plan meal"
        try:
            self.meal_plan_int = int(self.meal_plan_var.get())
        except:
            raise ValueError
        if self.meal_plan_int <= 0 or self.meal_plan_int > 135:
            self.quantity = "1 and 135"
            raise Quan_Error

        self.meal_type = "guest meal"
        try:
            self.guest_meal_int = int(self.guest_meal_var.get())
        except:
            raise ValueError
        if self.guest_meal_int < 0 or self.guest_meal_int > 20:
            self.quantity = "0 and 20"
            raise Quan_Error
        
        try:
            self.dollars_double = float(self.dining_dollars_var.get())
        except:
            self.is_dd = True
            raise ValueError
        if self.dollars_double < 0.0 or self.dollars_double > 5000.0:
            self.quantity = "0.00 and 5000.00"
            raise Quan_Error

        self.meal_type = "meal plan equivalencies"
        try:
            self.equivalencies_int = int(self.equivalencies_var.get())
        except:
            raise ValueError
        if self.equivalencies_int < 0 or self.equivalencies_int > 105:
            self.quantity = "0 and 105"
            raise Quan_Error
    
    def change_to_calc(self, event):
        self.add_calc_create_button['text'] = "Calculate Cost"
        self.add_calc_create_button['command'] = self.add_calculate_handler

    def add_calculate_handler(self):
        try:
            self.process_pay_input()
            self.add_calc_create_button['text'] = "Create"
            self.add_calc_create_button['command'] = self.add_create_handler
            self.cost = (float(self.meal_plan_var.get()) + float(self.guest_meal_var.get())) * 11.50 + float(self.dining_dollars_var.get()) + float(self.equivalencies_var.get()) * 10
            self.cost_error_label.grid(row = 5, column = 1)
            self.cost_error_label['text'] = "Meal Plan Cost: $" + f'{self.cost:.2f}'
        except ValueError:
            self.cost_error_label.grid(row = 5, column = 1)
            if self.is_dd:
                self.cost_error_label['text'] = "Error: Input for dining dollars is empty\nor not a valid decimal number"
                self.is_dd = False
            else:
                self.cost_error_label['text'] = "Error: Input for " + self.meal_type + " is\nempty or not a valid number"
        except Quan_Error:
            self.cost_error_label.grid(row = 5, column = 1)
            self.cost_error_label['text'] = "Error: Input for " + self.meal_type + " should be\nbetween " + self.quantity + "."

    def add_create_handler(self):
        # go to confirm add layout
        self.mp_file = open(self.first_var.get() + "_" + self.last_var.get() + "_" + self.email_var.get() + "_" + self.id_var.get() + ".txt", "w")
        self.mp_file.write(self.first_var.get() + "\n")
        self.mp_file.write(self.last_var.get() + "\n")
        self.mp_file.write(self.email_var.get() + "\n")
        self.mp_file.write(self.id_var.get() + "\n")
        self.mp_file.write(self.meal_plan_var.get() + "\n")
        self.mp_file.write(self.guest_meal_var.get() + "\n")
        self.mp_file.write(f'{float(self.dining_dollars_var.get()):.2f}' + "\n")
        self.mp_file.write(self.equivalencies_var.get() + "\n")
        self.mp_file.write(f'{self.cost:.2f}' + "\n")
        self.mp_file.close()

        self.pay_method_frame.destroy()
        self.add_button_frame.destroy()
        self.conf_add_screen()
    
    def add_quit_handler(self):
        # go back to start layout
        self.pay_method_frame.destroy()
        self.add_button_frame.destroy()
        self.start_screen()

    def conf_add_screen(self):
        # label frame
        self.conf_add_frame = tk.Frame(self.window)
        self.conf_add_frame.grid(row = 1, column = 1)
        self.conf_add_label = tk.Label(self.conf_add_frame, text = "Meal plan successfully created and added.\nThank you.", font = font.Font(size = 10)).grid(row = 1, column = 1)

        # button frame
        self.conf_add_button_frame = tk.Frame(self.window)
        self.conf_add_button_frame.grid(row = 2, column = 1)
        self.conf_add_quit_button = tk.Button(self.conf_add_button_frame, text = "Quit", font = font.Font(size = 10), command = self.conf_add_quit_handler).grid(row = 1, column = 1)

    def conf_add_quit_handler(self):
        # go back to start layout
        self.conf_add_frame.destroy()
        self.conf_add_button_frame.destroy()
        self.start_screen()

    def edit_enter_screen(self):
        # label and entry frame
        self.edit_entry_frame = tk.Frame(self.window, width = 400, height = 200)
        self.edit_entry_frame.grid(row = 1, column = 1)

        self.edit_first_name = tk.Label(self.edit_entry_frame, text = "First Name:", font = font.Font(size = 10)).grid(row = 1, column = 1)
        self.e_first_var = tk.StringVar()
        self.e_first_var.set("Long")
        self.edit_first_name_entry = tk.Entry(self.edit_entry_frame, textvariable = self.e_first_var).grid(row = 1, column = 2)
        
        self.edit_last_name = tk.Label(self.edit_entry_frame, text = "Last Name:", font = font.Font(size = 10)).grid(row = 2, column = 1)
        self.e_last_var = tk.StringVar()
        self.e_last_var.set("Pham")
        self.edit_last_name_entry = tk.Entry(self.edit_entry_frame, textvariable = self.e_last_var).grid(row = 2, column = 2)
        
        self.edit_email = tk.Label(self.edit_entry_frame, text = "Email:", font = font.Font(size = 10)).grid(row = 3, column = 1)
        self.e_email_var = tk.StringVar()
        self.e_email_var.set("longpham@sandiego.edu")
        self.edit_email_entry = tk.Entry(self.edit_entry_frame, textvariable = self.e_email_var).grid(row = 3, column = 2)
        
        self.edit_id = tk.Label(self.edit_entry_frame, text = "Student ID:", font = font.Font(size = 10)).grid(row = 4, column = 1)
        self.e_id_var = tk.StringVar()
        self.e_id_var.set("009462970")
        self.edit_id_entry = tk.Entry(self.edit_entry_frame, textvariable = self.e_id_var).grid(row = 4, column = 2)

        self.e_error_frame = tk.Frame(self.window)
        self.e_error_frame.grid(row = 2, column = 1)
        self.e_error_label = tk.Label(self.e_error_frame, font = font.Font(size = 10))
        self.e_label_grid = False

        # button frame
        self.edit_enter_button_frame = tk.Frame(self.window, width = 400, height = 200)
        self.edit_enter_button_frame.grid(row = 3, column = 1)
        self.edit_enter_enter_button = tk.Button(self.edit_enter_button_frame, text = "Enter", font = font.Font(size = 10), command = self.edit_enter_enter_handler).grid(row = 1, column = 1)
        self.edit_enter_quit_button = tk.Button(self.edit_enter_button_frame, text = "Quit", font = font.Font(size = 10), command = self.edit_enter_quit_handler).grid(row = 1, column = 2)

    def process_edit_input(self):
        if self.e_first_var.get() == "":
            raise First_Error

        if self.e_last_var.get() == "":
            raise Last_Error
        
        if re.fullmatch("[A-Za-z]+@sandiego\.edu", self.e_email_var.get()) is None:
            raise Email_Error
        
        try:
            int(self.e_id_var.get())
        except:
            raise ID_Error

        if len(str(self.e_id_var.get())) != 9:
            raise Length_Error
    
        if not os.path.isfile(self.e_first_var.get() + "_" + self.e_last_var.get() + "_" + self.e_email_var.get() + "_" + self.e_id_var.get() + ".txt"):
            raise FileNotFoundError

    def edit_enter_enter_handler(self):
        # go to edit layout
        try:
            self.process_edit_input()
            self.edit_entry_frame.destroy()
            self.edit_enter_button_frame.destroy()
            self.e_error_frame.destroy()
            self.e_mp_file = open(self.e_first_var.get() + "_" + self.e_last_var.get() + "_" + self.e_email_var.get() + "_" + self.e_id_var.get() + ".txt", "r")
            self.edit_screen()
        except First_Error:
            self.e_error_label.grid(row = 1, column = 1)
            self.e_error_label['text'] = "Error: No input for first name entry"
        except Last_Error:
            self.e_error_label.grid(row = 1, column = 1)
            self.e_error_label['text'] = "Error: No input for last name entry"
        except Email_Error:
            self.e_error_label.grid(row = 1, column = 1)
            self.e_error_label['text'] = "Error: Email not in format '...@sandiego.edu'"
        except ID_Error:
            self.e_error_label.grid(row = 1, column = 1)
            self.e_error_label['text'] = "Error: Student ID not in all numbers"
        except Length_Error:
            self.e_error_label.grid(row = 1, column = 1)
            self.e_error_label['text'] = "Error: Student ID not nine characters long"
        except FileNotFoundError:
            self.e_error_label.grid(row = 1, column = 1)
            self.e_error_label['text'] = "Error: Student information does not exist"

    def edit_enter_quit_handler(self):
        # go back to start layout
        self.edit_entry_frame.destroy()
        self.edit_enter_button_frame.destroy()
        self.e_error_frame.destroy()
        self.start_screen()

    def edit_screen(self):
        # label and entry frame
        self.stu_info_frame = tk.Frame(self.window, width = 400, height = 200)
        self.stu_info_frame.grid(row = 1, column = 1)

        self.stu_info_list = []
        for line in self.e_mp_file:
            spl = line.split("\n")
            self.stu_info_list.append(spl)

        self.e_mp_file.close()

        self.stu_name = tk.Label(self.stu_info_frame, text = self.stu_info_list[0][0] + " " + self.stu_info_list[1][0], font = font.Font(size = 10)).grid(row = 1, column = 1)
        self.stu_email = tk.Label(self.stu_info_frame, text = self.stu_info_list[2][0], font = font.Font(size = 10)).grid(row = 2, column = 1)
        self.stu_id = tk.Label(self.stu_info_frame, text = self.stu_info_list[3][0], font = font.Font(size = 10)).grid(row = 3, column = 1)

        self.edit_mp_frame = tk.Frame(self.window, width = 400, height = 200)
        self.edit_mp_frame.grid(row = 2, column = 1)

        self.add_del_mp_label = tk.Label(self.edit_mp_frame, text = "Add/Delete\nmeal plan meals:", font = font.Font(size = 10)).grid(row = 1, column = 1)
        self.add_del_mp_var = tk.StringVar()
        self.add_del_mp_entry = tk.Entry(self.edit_mp_frame, textvariable = self.add_del_mp_var)
        self.add_del_mp_entry.grid(row = 1, column = 2)
        self.add_del_mp_entry.bind("<Key>", self.e_change_to_calc)
        self.old_mp_label = tk.Label(self.edit_mp_frame, text = "Old Amount: " + self.stu_info_list[4][0], font = font.Font(size = 10)).grid(row = 1, column = 3)
        self.new_mp_label = tk.Label(self.edit_mp_frame, text = "New Amount: --", font = font.Font(size = 10))
        self.new_mp_label.grid(row = 1, column = 4)
        
        self.add_del_gm_label = tk.Label(self.edit_mp_frame, text = "Add/Delete\nguest meals:", font = font.Font(size = 10)).grid(row = 2, column = 1)
        self.add_del_gm_var = tk.StringVar()
        self.add_del_gm_entry = tk.Entry(self.edit_mp_frame, textvariable = self.add_del_gm_var)
        self.add_del_gm_entry.grid(row = 2, column = 2)
        self.add_del_gm_entry.bind("<Key>", self.e_change_to_calc)
        self.old_gm_label = tk.Label(self.edit_mp_frame, text = "Old Amount: " + self.stu_info_list[5][0], font = font.Font(size = 10)).grid(row = 2, column = 3)
        self.new_gm_label = tk.Label(self.edit_mp_frame, text = "New Amount: --", font = font.Font(size = 10))
        self.new_gm_label.grid(row = 2, column = 4)
        
        self.add_del_dd_label = tk.Label(self.edit_mp_frame, text = "Add/Delete\ndining dollars:", font = font.Font(size = 10)).grid(row = 3, column = 1)
        self.add_del_dd_var = tk.StringVar()
        self.add_del_dd_entry = tk.Entry(self.edit_mp_frame, textvariable = self.add_del_dd_var)
        self.add_del_dd_entry.grid(row = 3, column = 2)
        self.add_del_dd_entry.bind("<Key>", self.e_change_to_calc)
        self.old_dd_label = tk.Label(self.edit_mp_frame, text = "Old Amount: $" + self.stu_info_list[6][0], font = font.Font(size = 10)).grid(row = 3, column = 3)
        self.new_dd_label = tk.Label(self.edit_mp_frame, text = "New Amount: --", font = font.Font(size = 10))
        self.new_dd_label.grid(row = 3, column = 4)
        
        self.add_del_mpe_label = tk.Label(self.edit_mp_frame, text = "Add/Delete\nmeal plan equivalencies:", font = font.Font(size = 10)).grid(row = 4, column = 1)
        self.add_del_mpe_var = tk.StringVar()
        self.add_del_mpe_entry = tk.Entry(self.edit_mp_frame, textvariable = self.add_del_mpe_var)
        self.add_del_mpe_entry.grid(row = 4, column = 2)
        self.add_del_mpe_entry.bind("<Key>", self.e_change_to_calc)
        self.old_mpe_label = tk.Label(self.edit_mp_frame, text = "Old Amount: " + self.stu_info_list[7][0], font = font.Font(size = 10)).grid(row = 4, column = 3)
        self.new_mpe_label = tk.Label(self.edit_mp_frame, text = "New Amount: --", font = font.Font(size = 10))
        self.new_mpe_label.grid(row = 4, column = 4)
        
        self.cost_ref_err_label = tk.Label(self.edit_mp_frame, text = "Cost: --", font = font.Font(size = 10))

        # button frame
        self.edit_button_frame = tk.Frame(self.window, width = 400, height = 200)
        self.edit_button_frame.grid(row = 3, column = 1)
        self.edit_calc_conf_button = tk.Button(self.edit_button_frame, text = "Calculate Cost/Refund", font = font.Font(size = 10), command = self.edit_calculate_handler)
        self.edit_calc_conf_button.grid(row = 1, column = 1)
        self.edit_quit_button = tk.Button(self.edit_button_frame, text = "Quit", font = font.Font(size = 10), command = self.edit_quit_handler).grid(row = 1, column = 2)

    def process_changes(self):
        self.e_is_dd = False

        self.e_meal_type = "meal plan meal"
        try:
            self.add_del_mp_int = int(self.add_del_mp_var.get())
        except:
            raise ValueError
        if int(self.stu_info_list[4][0]) + self.add_del_mp_int < 0 or int(self.stu_info_list[4][0]) + self.add_del_mp_int > 135:
            self.quan_add = str(135 - int(self.stu_info_list[4][0]))
            self.quan_del = "-" + self.stu_info_list[4][0]
            raise Quan_Error

        self.e_meal_type = "guest meal"
        try:
            self.add_del_gm_int = int(self.add_del_gm_var.get())
        except:
            raise ValueError
        if int(self.stu_info_list[5][0]) + self.add_del_gm_int < 0 or int(self.stu_info_list[5][0]) + self.add_del_gm_int > 20:
            self.quan_add = str(20 - int(self.stu_info_list[5][0]))
            self.quan_del = "-" + self.stu_info_list[5][0]
            raise Quan_Error
    
        try:
            self.add_del_dd_double = float(self.add_del_dd_var.get())
        except:
            self.e_is_dd = True
            raise ValueError
        if float(self.stu_info_list[6][0]) + self.add_del_dd_double < 0.0 or float(self.stu_info_list[6][0]) + self.add_del_dd_double > 5000.0:
            self.quan_add = str(5000.00 - float(self.stu_info_list[6][0]))
            self.quan_del = "-" + self.stu_info_list[6][0]
            raise Quan_Error

        self.e_meal_type = "meal plan equivalencies"
        try:
            self.add_del_mpe_int = int(self.add_del_mpe_var.get())
        except:
            raise ValueError
        if int(self.stu_info_list[7][0]) + self.add_del_mpe_int < 0 or int(self.stu_info_list[7][0]) + self.add_del_mpe_int > 105:
            self.quan_add = str(105 - int(self.stu_info_list[7][0]))
            self.quan_del = "-" + self.stu_info_list[7][0]
            raise Quan_Error

    def e_change_to_calc(self, event):
        self.edit_calc_conf_button['text'] = "Calculate Cost/Refund"
        self.edit_calc_conf_button['command'] = self.edit_calculate_handler

    def edit_calculate_handler(self):
        try:
            self.process_changes()
            self.edit_calc_conf_button['text'] = "Confirm Edits"
            self.edit_calc_conf_button['command'] = self.edit_conf_handler
            self.cost_ref = (float(self.add_del_mp_var.get()) + float(self.add_del_gm_var.get())) * 11.50 + float(self.add_del_dd_var.get()) + float(self.add_del_mpe_var.get()) * 10
            self.cost_ref_err_label.grid(row = 5, column = 1)
            if self.cost_ref < 0.0:
                self.cost_ref_err_label['text'] = "Refund: $" + f'{self.cost_ref * -1.0:.2f}'
            else:
                self.cost_ref_err_label['text'] = "Cost: $" + f'{self.cost_ref:.2f}'
            self.new_mp_label['text'] = "New Amount: " + str(int(self.stu_info_list[4][0]) + int(self.add_del_mp_var.get()))
            self.new_gm_label['text'] = "New Amount: " + str(int(self.stu_info_list[5][0]) + int(self.add_del_gm_var.get()))
            self.new_dd_label['text'] = "New Amount: $" + str(float(self.stu_info_list[6][0]) + float(self.add_del_dd_var.get()))
            self.new_mpe_label['text'] = "New Amount: " + str(int(self.stu_info_list[7][0]) + int(self.add_del_mpe_var.get()))
        except ValueError:
            self.cost_ref_err_label.grid(row = 5, column = 1)
            if self.e_is_dd:
                self.cost_ref_err_label['text'] = "Error: Input for dining dollars is empty\nor not a valid decimal number"
                self.e_is_dd = False
            else:
                self.cost_ref_err_label['text'] = "Error: Input for " + self.e_meal_type + " is\nempty or not a valid number"
        except Quan_Error:
            self.cost_ref_err_label.grid(row = 5, column = 1)
            self.cost_ref_err_label['text'] = "Error: Input for " + self.e_meal_type + " should be\nbetween " + self.quan_del + " and " + self.quan_add + "."

    def edit_conf_handler(self):
        # go back to conf edit layout
        self.e_mp_file = open(self.e_first_var.get() + "_" + self.e_last_var.get() + "_" + self.e_email_var.get() + "_" + self.e_id_var.get() + ".txt", "w")
        self.e_mp_file.write(self.stu_info_list[0][0] + "\n")
        self.e_mp_file.write(self.stu_info_list[1][0] + "\n")
        self.e_mp_file.write(self.stu_info_list[2][0] + "\n")
        self.e_mp_file.write(self.stu_info_list[3][0] + "\n")
        self.e_mp_file.write(str(int(self.stu_info_list[4][0]) + int(self.add_del_mp_var.get())) + "\n")
        self.e_mp_file.write(str(int(self.stu_info_list[5][0]) + int(self.add_del_gm_var.get())) + "\n")
        self.e_mp_file.write(f'{(float(self.stu_info_list[6][0]) + float(self.add_del_dd_var.get())):.2f}' + "\n")
        self.e_mp_file.write(str(int(self.stu_info_list[7][0]) + int(self.add_del_mpe_var.get())) + "\n")
        self.e_mp_file.write(f'{(float(self.stu_info_list[8][0]) + float(self.cost_ref)):.2f}' + "\n")
        self.e_mp_file.close()
        
        self.stu_info_frame.destroy()
        self.edit_mp_frame.destroy()
        self.edit_button_frame.destroy()
        self.conf_edit_screen()

    def edit_quit_handler(self):
        # go back to start layout
        self.stu_info_frame.destroy()
        self.edit_mp_frame.destroy()
        self.edit_button_frame.destroy()
        self.start_screen()

    def conf_edit_screen(self):
        # label frame
        self.conf_edit_frame = tk.Frame(self.window)
        self.conf_edit_frame.grid(row = 1, column = 1)
        self.conf_edit_label = tk.Label(self.conf_edit_frame, text = "Meal plan successfully edited.\nThank you.", font = font.Font(size = 10)).grid(row = 1, column = 1)

        # button frame
        self.conf_edit_button_frame = tk.Frame(self.window)
        self.conf_edit_button_frame.grid(row = 2, column = 1)
        self.conf_edit_quit_button = tk.Button(self.conf_edit_button_frame, text = "Quit", font = font.Font(size = 10), command = self.conf_edit_quit_handler).grid(row = 1, column = 1)

    def conf_edit_quit_handler(self):
        # go back to start layout
        self.conf_edit_frame.destroy()
        self.conf_edit_button_frame.destroy()
        self.start_screen()

if __name__ == "__main__":
    MPM = USD_MPM()