import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.contacts = {}

        # Setting up the main window
        self.root = root
        self.root.title("Contact Book")

        # Adding buttons for different actions
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        if not name:
            return

        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists!")
            return

        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_list = "\n".join([f"{name}: {details['phone']}" for name, details in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
        if not search_term:
            return

        results = [f"{name}: {details}" for name, details in self.contacts.items()
                   if search_term in name or search_term in details['phone']]
        
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No matching contacts found!")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter name of the contact to update:")
        if not name or name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        phone = simpledialog.askstring("Input", "Enter new phone number:")
        email = simpledialog.askstring("Input", "Enter new email:")
        address = simpledialog.askstring("Input", "Enter new address:")

        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter name of the contact to delete:")
        if not name or name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        del self.contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
