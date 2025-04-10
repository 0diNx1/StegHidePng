from PIL import Image
import stepic  # pip3 install stepic

def optioN():
    print('''
[1]: Encode the image using text!

[2]: Extract data from the image!
''')
    try:
        select_option = int(input("Select the option: "))
    except ValueError:
        print("[-] Please enter a valid number.")
        return

    if select_option == 1:
        encode_with_text()
    elif select_option == 2:
        decode_the_img()
    else:
        print("[-] Invalid option selected.")

def encode_with_text():
    try:
        file_path_open = input("Enter the path of the original .png image file: ").strip() 
        if not file_path_open.endswith(".png"):
            print("[-] Only .png files are supported.")
            return
        
        org_img = Image.open(file_path_open)

        secret_msg = input("Enter the message you want to hide: ").strip() #input the secret msg
        if not secret_msg:
            print("[-] Aborting!! Input the message.")
            return

        encoded_img = stepic.encode(org_img, secret_msg.encode()) #encode the msg using the img.

        file_path_to_save = input("Enter the path and filename to save the encoded image (e.g., output.png): ").strip()
        if not file_path_to_save.endswith(".png"):
            print("[-] Output file must be end with [.png]")
            return

        encoded_img.save(file_path_to_save)  #saving the encode img.
        print("[+] Secret message hidden successfully!")

    except Exception as e:
        print(f"[-] Error occurred: {e}")

def decode_the_img():
    try:
        file_path_to_decode_img = input("Enter the full path of the encoded image: ").strip()
        if not file_path_to_decode_img.endswith(".png"):
            print("[-] Only .png files are supported.")
            return

        data_img = Image.open(file_path_to_decode_img)
        extract_hide_data = stepic.decode(data_img)
        print("[+] Hidden message extracted: ", extract_hide_data)

    except Exception as e:
        print(f"[-] Error occurred: {e}")

if __name__ == "__main__":
    optioN()
