# Databricks notebook source
# MAGIC %md
# MAGIC TRỰC QUAN HÓA BRONZE LAYER (DATA QUALITY & MISSING VALUES)

# COMMAND ----------

# MAGIC %pip install seaborn
# MAGIC
# MAGIC import matplotlib.pyplot as plt
# MAGIC import seaborn as sns
# MAGIC from pyspark.sql.functions import col, count, when
# MAGIC
# MAGIC # 1. Đọc dữ liệu Bronze
# MAGIC df_bronze = spark.table("workspace.default.bronze_credit_data")
# MAGIC total_rows = df_bronze.count()
# MAGIC
# MAGIC # 2. Tính số lượng & phần trăm missing values cho từng cột
# MAGIC missing_exprs = [count(when(col(c).isNull(), c)).alias(c) for c in df_bronze.columns]
# MAGIC missing_df = df_bronze.select(missing_exprs).toPandas().T
# MAGIC missing_df.columns = ["Missing_Count"]
# MAGIC missing_df["Missing_Percentage"] = (missing_df["Missing_Count"] / total_rows) * 100
# MAGIC missing_df = missing_df.sort_values(by="Missing_Percentage", ascending=False)
# MAGIC
# MAGIC # 3. Vẽ biểu đồ Bar Chart kiểm tra chất lượng dữ liệu thô
# MAGIC plt.figure(figsize=(10, 5))
# MAGIC ax = sns.barplot(x=missing_df.index, y=missing_df["Missing_Percentage"], palette="Reds_r")
# MAGIC plt.xticks(rotation=45, ha="right", fontsize=10)
# MAGIC plt.ylabel("Tỷ lệ thiếu (%)", fontsize=12)
# MAGIC plt.title("BRONZE LAYER: ĐÁNH GIÁ TỶ LỆ DỮ LIỆU KHUYẾT THIẾU (MISSING VALUES)", fontsize=13, fontweight="bold")
# MAGIC plt.grid(axis="y", linestyle="--", alpha=0.7)
# MAGIC
# MAGIC for p in ax.patches:
# MAGIC     if p.get_height() > 0:
# MAGIC         ax.annotate(f"{p.get_height():.1f}%", (p.get_x() + p.get_width() / 2., p.get_height()),
# MAGIC                     ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=9)
# MAGIC
# MAGIC plt.tight_layout()
# MAGIC display(plt.show())

# COMMAND ----------

# MAGIC %md
# MAGIC TRỰC QUAN HÓA TẦNG SILVER (Phân tích chỉ số NPL & Đặc trưng Kinh doanh)

# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Đọc dữ liệu Silver đã làm sạch
df_silver_pdf = spark.table("workspace.default.silver_credit_data") \
    .groupBy("loan_intent", "person_home_ownership") \
    .agg({"loan_status": "avg", "loan_amnt": "avg"}) \
    .toPandas()

df_silver_pdf["NPL_Rate_Pct"] = df_silver_pdf["avg(loan_status)"] * 100

# 2. Biểu đồ cột ghép (Grouped Bar Chart) Tỷ lệ nợ xấu NPL theo Mục đích vay & Sở hữu nhà
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df_silver_pdf, 
    x="loan_intent", 
    y="NPL_Rate_Pct", 
    hue="person_home_ownership", 
    palette="Set2"
)
plt.title("SILVER LAYER: TỶ LỆ NỢ XẤU (NPL RATE %) THEO MỤC ĐÍCH VAY VÀ SỞ HỮU NHÀ Ở", fontsize=14, fontweight="bold")
plt.xlabel("Mục đích khoản vay", fontsize=12)
plt.ylabel("Tỷ lệ Nợ xấu (%)", fontsize=12)
plt.xticks(rotation=30)
plt.legend(title="Sở hữu nhà", loc="upper right")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
display(plt.show())

# COMMAND ----------

# MAGIC %md
# MAGIC TRỰC QUAN HÓA TẦNG GOLD (Phân tầng Rủi ro & Ma trận Quyết định Duyệt vay)

# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql.functions import col, when, udf
from pyspark.sql.types import DoubleType

# 1. Trích xuất xác suất nợ xấu và quy đổi Phân tầng Rủi ro
extract_prob = udf(lambda v: float(v[1]), DoubleType())

df_gold = spark.table("workspace.default.gold_credit_scoring") \
    .withColumn("default_probability", extract_prob(col("probability")))

df_decision = df_gold.withColumn("Risk_Segment", 
    when(col("default_probability") < 0.15, "1. Rủi ro Thấp")
    .when(col("default_probability") < 0.35, "2. Rủi ro Trung Bình")
    .when(col("default_probability") < 0.60, "3. Rủi ro Cao")
    .otherwise("4. Rủi ro Rất Cao")
).withColumn("Credit_Policy",
    when(col("Risk_Segment") == "1. Rủi ro Thấp", "Duyệt Tự Động (Auto-Approve)")
    .when(col("Risk_Segment") == "2. Rủi ro Trung Bình", "Duyệt Hạn Mức 70%")
    .when(col("Risk_Segment") == "3. Rủi ro Cao", "Thẩm Định Thủ Công")
    .otherwise("Từ Chối Vay (Reject)")
)

df_summary = df_decision.groupBy("Risk_Segment", "Credit_Policy").count().toPandas().sort_values(by="Risk_Segment")

# 2. Vẽ biểu đồ Tròn (Donut Chart) & Biểu đồ Cột ngang thể hiện Cơ cấu Duyệt vay
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: Biểu đồ Donut phân tầng rủi ro
colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c']
wedges, texts, autotexts = ax1.pie(
    df_summary['count'], 
    labels=df_summary['Risk_Segment'], 
    autopct='%1.1f%%',
    startangle=140, 
    colors=colors, 
    pctdistance=0.75,
    textprops=dict(color="black", fontweight="bold")
)
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
ax1.add_artist(centre_circle)
ax1.set_title("GOLD LAYER: CƠ CẤU PHÂN TẦNG RỦI RO TÍN DỤNG", fontsize=13, fontweight="bold")

# Subplot 2: Biểu đồ Cột thể hiện Quyết định Duyệt vay
sns.barplot(data=df_summary, y="Credit_Policy", x="count", palette=colors, ax=ax2)
ax2.set_title("QUYẾT ĐỊNH PHÊ DUYỆT TÍN DỤNG TỰ ĐỘNG", fontsize=13, fontweight="bold")
ax2.set_xlabel("Số lượng hồ sơ vay", fontsize=11)
ax2.set_ylabel("")
ax2.grid(axis="x", linestyle="--", alpha=0.5)

for p in ax2.patches:
    ax2.annotate(f"{int(p.get_width())} hồ sơ", (p.get_width(), p.get_y() + p.get_height() / 2.),
                 ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=10, fontweight="bold")

plt.tight_layout()
display(plt.show())

# COMMAND ----------

# MAGIC %md
# MAGIC TRỰC QUAN HÓA MA TRẬN NHẦM LẪN & HIỆU NĂNG MÔ HÌNH ML (CONFUSION MATRIX)

# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# 1. Chuyển kết quả dự báo từ PySpark sang Pandas để vẽ Confusion Matrix
predictions_pd = spark.table("workspace.default.gold_credit_scoring") \
    .select("loan_status", "prediction").toPandas()

y_true = predictions_pd["loan_status"]
y_pred = predictions_pd["prediction"]

cm = confusion_matrix(y_true, y_pred)

# 2. Vẽ Heatmap Ma trận nhầm lẫn (Confusion Matrix)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=["Trả đúng hạn (0)", "Vỡ nợ (1)"],
            yticklabels=["Trả đúng hạn (0)", "Vỡ nợ (1)"],
            annot_kws={"size": 14, "weight": "bold"})

plt.title("MA TRẬN NHẦM LẪN (CONFUSION MATRIX) - SPARK MLLIB", fontsize=13, fontweight="bold")
plt.xlabel("Nhãn Dự Báo từ Mô Hình (Predicted Label)", fontsize=11)
plt.ylabel("Nhãn Thực Tế (True Label)", fontsize=11)

plt.tight_layout()
display(plt.show())

# 3. In Báo cáo Chi tiết Precision, Recall, F1-Score
print("--- BÁO CÁO CHI TIẾT HIỆU NĂNG MÔ HÌNH ---")
print(classification_report(y_true, y_pred, target_names=["Khách hàng Tốt (0)", "Khách hàng Nợ xấu (1)"]))