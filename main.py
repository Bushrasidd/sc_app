import os
from PIL import ImageGrab, Image
from datetime import datetime
import time
import hashlib
import io



# directory = "C:/Users/Bushra"
# folder_name = "Screenshots"
# path = os.path.join(directory, folder_name)
hash_temp = None

def image_hash(first_element):
    with open(first_element, 'rb') as f:
      return hashlib.md5(f.read()).hexdigest()


def save_sc(path, hash_temp):
    clipboard_image = ImageGrab.grabclipboard()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"sc{timestamp}.png"
    final_name= os.path.join(path, filename)
    
    if clipboard_image:
        if isinstance(clipboard_image, Image.Image):
            # Convert PIL Image to bytes for hashing
            img_bytes = io.BytesIO()
            clipboard_image.save(img_bytes, format='PNG')
            img_bytes.seek(0)
            hashed_file = hashlib.md5(img_bytes.getvalue()).hexdigest()
            
            print(f"Hash_temp value : {hash_temp}")
            
            if hash_temp == hashed_file:
                print("Screenshot is same as previous!! no need to store")
                return hash_temp
            else:
                print(f"hash_file : {hashed_file}")
                clipboard_image.save(final_name)
                print(f"\n final_name:  {final_name}")
                print("image saved successfully")
                hash_temp = hashed_file
                return hash_temp
                
        elif isinstance(clipboard_image, list):
            first_element = clipboard_image[0]
        
            try:
                print(f" \n element fetched {first_element}")

                image_to_save = Image.open(first_element)
                print("images loaded successfullly")
                hashed_file = image_hash(first_element)

                print(f"Hash_temp value : {hash_temp}")

                if hash_temp == hashed_file:
                    print("Screenshot is same as previous!! no need to store")
                    return hash_temp
                
                elif hash_temp != hashed_file:
                        print(f"hash_file : {hashed_file}")
                        
                        image_to_save.save(final_name)
                        print(f"\n final_name:  {final_name}")
                        print("image saved successfully")
                        hash_temp = hashed_file
                        return hash_temp
                
                else:
                    print("unexpected error")
                    return hash_temp              
                    
            except Exception as e:
                print(f"\n Error opening or saving the image from the path: {e}")
                return hash_temp
    else:
        print("No image found on clipboard")
        return hash_temp

def create_folder_and_save_sc(current_path, hash_temp):
    try:
        if not os.path.exists(current_path):
            os.mkdir(current_path)
            print("folder created successfully")
        else:
            print("Folder already exist")
        hash_temp = save_sc(current_path, hash_temp)
        print(f"preserved the value successfully: {hash_temp}")
        print(f"Performed action with path: {current_path}")
        return hash_temp
    except Exception as e:
        print(e)
        return hash_temp

def background_task(current_path, hash_temp,stop_flag):
    while not stop_flag.is_set():
        hash_temp = create_folder_and_save_sc(current_path, hash_temp)
        time.sleep(10)

















