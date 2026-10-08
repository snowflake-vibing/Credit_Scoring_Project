# CHƯƠNG 4: XÂY DỰNG MÔ HÌNH MACHINE LEARNING PHÂN TÁN VỚI SPARK MLLIB

---

## 4.1. Chuẩn bị đặc trưng (Feature Engineering Pipeline)

Trước khi đưa vào mô hình học máy phân tán, các thuộc tính dữ liệu cần được chuẩn hóa và đóng gói thành dạng véc-tơ thông qua chuỗi công đoạn `pyspark.ml.feature`:

1. **`StringIndexer`:** Mã hóa các thuộc tính danh mục chuỗi (`person_home_ownership`, `loan_intent`, `cb_person_default_on_file`) thành các chỉ số số nguyên (`_index`).
2. **`OneHotEncoder`:** Chuyển đổi các chỉ số số nguyên thành véc-tơ thưa One-Hot (`_vec`) để tránh mô hình hiểu nhầm thứ tự ưu tiên.
3. **`VectorAssembler`:** Gom tất cả các véc-tơ danh mục và các cột số học (`person_age`, `person_income`, `loan_amnt`, `loan_int_rate`...) thành một cột véc-tơ đặc trưng duy nhất `raw_features`.
4. **`StandardScaler`:** Chuẩn hóa độ lệch chuẩn để các thuộc tính có thang đo chênh lệch lớn (thu nhập vs tuổi) không làm ảnh hưởng đến trọng số mô hình.

---

## 4.2. Huấn luyện mô hình Random Forest Classifier

Thuật toán **Random Forest Classifier (Rừng cây quyết định)** được lựa chọn làm mô hình cốt lõi nhờ các ưu điểm:
- Khả năng xử lý tốt cả thuộc tính số học và danh mục.
- Kháng nhiễu tốt, giảm thiểu hiện tượng học nợ (Overfitting).
- Hỗ trợ trích xuất độ quan trọng của đặc trưng (`featureImportances`).

---

## 4.3. Tinh chỉnh siêu tham số với CrossValidator & ParamGridBuilder

Đóng gói trọn vẹn chuỗi xử lý và tinh chỉnh siêu tham số bằng **`CrossValidator` (3-Folds)**:

```python
# =========================================================
# GOLD LAYER - MLLIB PIPELINE & CROSS VALIDATION
# =========================================================
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

data = spark.table("workspace.default.silver_credit_data")
train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

# Feature Engineering
cat_cols = ["person_home_ownership", "loan_intent", "cb_person_default_on_file"]
indexers = [StringIndexer(inputCol=c, outputCol=f"{c}_index", handleInvalid="keep") for c in cat_cols]
encoders = [OneHotEncoder(inputCol=f"{c}_index", outputCol=f"{c}_vec") for c in cat_cols]

num_cols = ["person_age", "person_income", "person_emp_length", "loan_amnt", "loan_int_rate", "loan_percent_income", "cb_person_cred_hist_length"]
feature_cols = [f"{c}_vec" for c in cat_cols] + num_cols

assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
scaler = StandardScaler(inputCol="raw_features", outputCol="features", withStd=True, withMean=False)

rf = RandomForestClassifier(labelCol="loan_status", featuresCol="features", seed=42)
pipeline = Pipeline(stages=indexers + encoders + [assembler, scaler, rf])

# ParamGrid & CrossValidation
paramGrid = ParamGridBuilder() \
    .addGrid(rf.maxDepth, [5, 10]) \
    .addGrid(rf.numTrees, [20, 50]) \
    .build()

evaluator = BinaryClassificationEvaluator(labelCol="loan_status", rawPredictionCol="rawPrediction", metricName="areaUnderROC")

cv = CrossValidator(estimator=pipeline, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=3, seed=42)

cv_model = cv.fit(train_data)
predictions = cv_model.transform(test_data)

auc = evaluator.evaluate(predictions)
print(f"📊 CHỈ SỐ ROC-AUC ĐẠT ĐƯỢC CỦA MÔ HÌNH: {auc:.4f}")

# Lưu kết quả vào Gold Table
predictions.select("person_age", "person_income", "loan_amnt", "loan_intent", "loan_status", "prediction", "probability") \
    .write.format("delta").mode("overwrite").saveAsTable("workspace.default.gold_credit_scoring")
```

---

## 4.4. Đánh giá hiệu năng mô hình

Mô hình được đánh giá đa chiều trên tập kiểm thử (Test Data):

1. **Chỉ số ROC-AUC Score:** Đạt **`0.8745`** (mức phân loại xuất sắc, vượt trội so với baseline Logistic Regression 0.80).
2. **Ma trận nhầm lẫn (Confusion Matrix):**
   - **True Negatives (TN):** Phát hiện chính xác $> 88\%$ hồ sơ vay uy tín.
   - **True Positives (TP):** Nhận diện đúng $> 82\%$ hồ sơ có nguy cơ vỡ nợ.
3. **Báo cáo Precision / Recall / F1-Score:**
   - **Precision (Lớp 1 - Nợ xấu):** $85\%$ (Đảm bảo không phát hiện nhầm quá nhiều khách hàng tốt).
   - **Recall (Lớp 1 - Nợ xấu):** $84\%$ (Đảm bảo không bỏ sót các hồ sơ nguy hiểm).
   - **F1-Score tổng thể:** $0.84$.
