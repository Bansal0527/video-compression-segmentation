import cv2
import os

# --- Configuration ---
video_path = '/content/demo.mp4'      
output_folder = 'ORIGINAL_frames'        # Folder to save original frames
frame_interval = 30                      # Save every 30th frame (adjust as needed)

# --- Prepare output folder ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- Load video ---
cap = cv2.VideoCapture(video_path)
frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        frame_path = os.path.join(output_folder, f'frame_{saved_count:03d}.png')
        cv2.imwrite(frame_path, frame)
        print(f"Saved: frame_{saved_count:03d}.png")
        saved_count += 1

    frame_count += 1

cap.release()
print("Done saving original frames!")
