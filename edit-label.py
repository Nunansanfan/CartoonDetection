import os

path_to_txt_files = r"C:\Users\Nunan\Documents\GitHub\CartoonDetection\raw_dataset\labels\label_Rhino"  # Insert your path to text files here
label_id = 13  # Insert your label id here (0 ==  BigHero6_Baymax, ... etc)

txt_file_list = []
for root, dir, files in os.walk(path_to_txt_files):
    txt_file_list = [ fi for fi in files if fi.endswith(".txt") ]


for file in txt_file_list:
    print("Editing: ", end="")
    print(path_to_txt_files + "\\" + file + " ...", end="")
    with open(path_to_txt_files + "\\" + file, "r+") as f:
        yoloenc = f.readline().split()
        yoloenc[0] = str(label_id)
        
        # https://stackoverflow.com/questions/2424000/read-and-overwrite-a-file-in-python
        f.seek(0)
        f.write(yoloenc[0] + " " + yoloenc[1] + " " + yoloenc[2] + " " + yoloenc[3] + " " + yoloenc[4])
        f.truncate()
        f.close()
    
    print("Done!")

print("All files has been edited with a new label id")        
        
        