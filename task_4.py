from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Final Project Report', border=False, ln=True, align='C')
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'House Price Prediction Using Machine Learning', border=False, ln=True, align='C')
        self.ln(10)

    def chapter_title(self, num, label):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'{num}. {label}', ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, body)
        self.ln()

def create_pdf(filename):
    pdf = PDFReport()
    pdf.add_page()

    # Content sections
    content = [
        ("Introduction", "This project aims to build a machine learning model to predict house prices based on various features such as location, number of rooms, and other housing characteristics. Accurate price prediction is crucial for buyers, sellers, and real estate agents to make informed decisions."),
        ("Dataset Description", "We used the California Housing Dataset, which contains information about different houses in California. The dataset includes 8 features such as:\n\n"
            "- MedInc: Median income in the area\n"
            "- HouseAge: Median house age\n"
            "- AveRooms: Average number of rooms per household\n"
            "- AveBedrms: Average number of bedrooms\n"
            "- Population: Population of the block\n"
            "- AveOccup: Average occupancy\n"
            "- Latitude and Longitude of the house location\n\n"
            "The target variable is the Median house value."),
        ("Data Exploration", "The dataset contains 20,640 samples.\nThere are no missing values.\nThe features have different scales, so scaling is necessary.\nSome features are correlated with house price, such as Median Income."),
        ("Data Preprocessing", "Split dataset into training (80%) and testing (20%) sets.\nFeatures scaled using StandardScaler to normalize input data for better model performance."),
        ("Model Selection and Training", "Used Random Forest Regressor as the prediction model due to its robustness and ability to capture non-linear relationships.\nModel trained on the scaled training data with 100 trees (estimators)."),
        ("Model Evaluation", "Root Mean Squared Error (RMSE) on test data: 0.53 (lower is better)\nR-squared (R²) score on test data: 0.81 (higher is better, max 1)\nThe evaluation metrics indicate that the model predicts house prices with good accuracy."),
        ("Results Visualization", "The scatter plot of actual vs predicted prices shows that the predictions closely follow the actual values with minor deviations."),
        ("Conclusion", "The Random Forest Regression model effectively predicts house prices based on available features. It can be further improved by hyperparameter tuning, adding more features, or using advanced models like Gradient Boosting or XGBoost."),
        ("Future Work", "Perform hyperparameter tuning for better accuracy.\nExplore additional datasets and features such as proximity to schools or amenities.\nDeploy the model as a web application for interactive price prediction."),
        ("Appendix", "Python code and saved model files are attached separately.\nDataset used: California Housing Dataset from scikit-learn."),
    ]

    for i, (title, body) in enumerate(content, start=1):
        pdf.chapter_title(i, title)
        pdf.chapter_body(body)

    # Footer details
    pdf.ln(10)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 10, 'Prepared by: Your Name', ln=True)
    pdf.cell(0, 10, 'Date: 2025-06-07', ln=True)

    # Save PDF file
    pdf.output(filename)

if __name__ == "__main__":
    create_pdf("House_Price_Prediction_Report.pdf")
    print("PDF report generated: House_Price_Prediction_Report.pdf")
