import cv2
from detection import AccidentDetectionModel
import numpy as np
import mysql.connector
from datetime import datetime

# Initialize the accident detection model
model = AccidentDetectionModel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX

# Function to connect to MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="accident_detection",
            port=3306
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def save_accident_data(timestamp, location, severity_level, severity_score, video_path, accuracy):
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO accidents (timestamp, location, severity_level, severity_score, video_path, accuracy)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Convert numpy.float32 to Python float
        severity_score = float(severity_score)
        accuracy = float(accuracy)

        cursor.execute(query, (timestamp, location, severity_level, severity_score, video_path, accuracy))
        conn.commit()
        print("✅ Accident data saved to the database.")
    except mysql.connector.Error as err:
        print(f"❌ Error saving data to MySQL: {err}")
    finally:
        cursor.close()
        conn.close()
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO accidents (timestamp, location, severity_level, severity_score, video_path, accuracy)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (timestamp, location, severity_level, severity_score, video_path, accuracy))
        conn.commit()
        print("✅ Accident data saved to the database.")
    except mysql.connector.Error as err:
        print(f"❌ Error saving data to MySQL: {err}")
    finally:
        cursor.close()
        conn.close()

# Main function to process video and detect accidents
def startapplication():
    video = cv2.VideoCapture('cars.mp4')  # Use 'cars.mp4' or 0 for webcam
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Process the frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        # Predict accident
        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if pred == "Accident":
            prob = round(prob[0][0] * 100, 2)
            severity_score = prob
            severity_level = "high" if severity_score > 70 else "medium" if severity_score > 30 else "low"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            location = "Intersection A"  # Replace with actual location detection logic
            video_path = f"accident_{timestamp}.mp4"
            accuracy = 100.0  # Replace with actual accuracy calculation logic

            # Save the video
            out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame.shape[1], frame.shape[0]))
            out.write(frame)
            out.release()

            # Save data to the database
            save_accident_data(timestamp, location, severity_level, severity_score, video_path, accuracy)

            # Display the prediction on the frame
            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, f"{pred} {prob}%", (20, 30), font, 1, (255, 255, 0), 2)

        # Display the frame
        cv2.imshow('Video', frame)

        # Exit on 'q' key press
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break

    # Release resources
    video.release()
    cv2.destroyAllWindows()

# Run the application
if __name__ == '__main__':
    startapplication()