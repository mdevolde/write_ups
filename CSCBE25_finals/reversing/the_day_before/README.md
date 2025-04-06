# The day before

**Category:** Reversing 
**Challenge Name:** The day before
**Tools:** dnSpy

## How I solved it

### Goal

Click on an unclickable button to print the flag on the screen.

---

### Step-by-step

### Step-by-step

1. **Initial inspection**
   - The binary provided was a Windows executable built with .NET.
   - I opened it with **dnSpy**, a powerful .NET decompiler and debugger.

2. **Finding the checkbox**
   - Browsing through the decompiled C# code, I located `Form1`, the main UI form.
   - Inside `Form1`, I found the `InitializeComponent()` method, which defines the UI elements and their properties.

3. **Modifying the form**
   - The checkbox controlling access to the flag was named `showflag`.
   - In the original code, this checkbox was either disabled or hidden.
   - I modified the method to explicitly enable and check it at launch by adding:

     ```csharp
     this.showflag.Checked = true;
     this.showflag.Enabled = true;
     ```

4. **Saving and running**
   - After editing the method in dnSpy, I saved the modified assembly and ran it.
   - The checkbox was now enabled and already checked.
   - As soon as the application loaded, the flag was displayed.

