# CardiaGuard: Pill Scanner and Medication Reminder for Atrial Fibrillation Patients

## Project Overview

CardiaGuard is a Python-based prototype designed to assist Atrial Fibrillation (AFIB) patients with medication management. The system uses computer vision to identify pills via webcam and includes a reminder system to ensure timely medication intake. If a patient fails to confirm taking their medication within a specified time, an email alert is sent to a caregiver.

## Features

- **Pill Classification**: CNN model (MobileNetV2) trained to classify pills (aspirin, warfarin, unknown).
- **Real-Time Pill Scanner**: OpenCV-based webcam capture with on-screen predictions.
- **Medication Reminder System**: Scheduled reminders using the `schedule` library.
- **Confirmation Workflow**: Patients must show the pill to the webcam for confirmation.
- **Caregiver Alerts**: Email notifications sent via SMTP if medication is missed.
- **Dataset Auto-Download**: Script to download and organize open-license pill images.

## Project Structure

```
CardiaGuard/
├── Cardiguard-project.ipynb    # Main Jupyter Notebook with all code
├── dataset_downloader.py       # Script to download and organize dataset
├── .env                        # Environment variables (email credentials)
├── data/
│   ├── train/
│   │   ├── aspirin/
│   │   ├── warfarin/
│   │   └── unknown/
│   └── val/
│       ├── aspirin/
│       ├── warfarin/
│       └── unknown/
├── pill_classifier_mobilenetv2.h5      # Initial trained model
├── pill_classifier_mobilenetv2_ft.h5   # Fine-tuned model
└── README.md
```

## Requirements

- Python 3.7+
- Anaconda or virtual environment
- Webcam for real-time scanning
- Gmail account for email notifications (with app password)

## Installation

1. **Clone or Download the Project**:
   - Place all files in a directory named `CardiaGuard`.

2. **Create Conda Environment**:
   ```bash
   conda create -n cardiaguard-proto python=3.8
   conda activate cardiaguard-proto
   ```

3. **Install Dependencies**:
   ```bash
   pip install tensorflow opencv-python matplotlib pandas scikit-learn python-dotenv schedule smtplib
   ```

4. **Set Up Environment Variables**:
   - Edit `.env` file with your email credentials:
     ```
     EMAIL_USER=your_email@gmail.com
     EMAIL_PASS=your_app_password
     CAREGIVER_EMAIL=caregiver@example.com
     ```
   - For Gmail, generate an app password: [Google App Passwords](https://support.google.com/accounts/answer/185833)

5. **Download Dataset**:
   - Run the dataset downloader:
     ```bash
     python dataset_downloader.py
     ```
   - This creates the `data/train/` and `data/val/` folders with sample images (replace with real pill images for production).

## Usage

### Running in VS Code

1. Open `Cardiguard-project.ipynb` in VS Code.
2. Select the `cardiaguard-proto` kernel (or create one).
3. Run cells sequentially:
   - Cell 1: Imports & Config
   - Cell 2: Dataset Download (if not done)
   - Cell 3: Data Generators
   - Cell 4: Model Training
   - Cell 5: Train & Save Model
   - Cell 6: Load Model & Predict Function
   - Cell 7: Webcam Scanner
   - Cell 8: Reminder System
   - Cell 9: Caregiver Notification
   - Final Cell: Full System Test

### Running in Jupyter Notebook

1. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
2. Open `Cardiguard-project.ipynb`.
3. Run cells as above.

## How It Works

1. **Training**: The model is trained on pill images using MobileNetV2 transfer learning.
2. **Inference**: Real-time webcam feed predicts pill classes with confidence scores.
3. **Reminders**: Scheduled jobs trigger at set times (e.g., daily at 8 AM).
4. **Confirmation**: Patient shows pill to camera; system confirms within timeout (default 30s).
5. **Alerts**: If not confirmed, email is sent to caregiver.

## Testing

- **Unit Tests**: Test individual functions like `predict_image()`, `run_scanner()`.
- **Integration Tests**: Run full workflow in demo mode.
- **Webcam Test**: Ensure camera permissions and OpenCV installation.
- **Email Test**: Verify SMTP settings with a test email.

## Troubleshooting

- **Webcam Issues**: Ensure camera is not used by other apps. Check permissions.
- **Model Loading Errors**: Verify model files exist and TensorFlow version compatibility.
- **Email Failures**: Check `.env` credentials, enable less secure apps or use app passwords.
- **Dataset Errors**: Ensure `data/` folder structure is correct.
- **Kernel Issues**: Restart kernel or recreate environment if imports fail.

## Future Enhancements

- **UI Development**: Add a simple GUI with Tkinter or Flask web app.
- **Mobile App**: Port to Android/iOS for on-the-go use.
- **Advanced Features**: Voice reminders, multi-language support, integration with EHR systems.
- **Security**: Encrypt sensitive data, add user authentication.
- **Scalability**: Support more pill types, cloud deployment.

## Contributing

- Fork the repository.
- Create a feature branch.
- Submit a pull request with detailed description.

## License

This project uses open-license datasets. Code is provided as-is for educational purposes.

## Contact

For questions or support, please open an issue on the repository.
