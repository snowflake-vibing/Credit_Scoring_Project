"""
Big Data Credit Risk Dataset Generator
======================================
Công cụ sinh dữ liệu tín dụng quy mô lớn (Big Data: 100,000 đến 5,000,000 dòng)
Phục vụ đề tài: Mô Hình Chấm Điểm Tín Dụng & Thẩm Định Rủi Ro Vỡ Nợ
Môn học: Dữ Liệu Lớn & Trí Tuệ Nhân Tạo Trong Kinh Doanh (Big Data Analytics & AI)

Mục đích:
- Tạo bộ dữ liệu quy mô hàng triệu bản ghi (Big Data Scale) mô phỏng trung thực thị trường tài chính ngân hàng.
- Duy trì phân phối thực nghiệm chuẩn xác:
  + Tỷ lệ nợ xấu tự nhiên (Baseline Default Rate) ~ 21.8%
  + Tương quan kinh tế chặt chẽ giữa DTI, Lãi suất, Điểm tín dụng CIC và Xác suất vỡ nợ.
- Hỗ trợ cả 2 chế độ:
  1. Chạy độc lập qua dòng lệnh (CLI): Xuất ra tệp CSV / Parquet
  2. Tích hợp trực tiếp trên Databricks / Apache Spark bằng hàm `generate_bigdata_spark(spark, n_rows)`
"""

import argparse
import sys
import time
import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def generate_credit_data_pandas(n_rows: int = 1_000_000, seed: int = 42) -> pd.DataFrame:
    """Sinh dữ liệu lớn bằng NumPy vectorized (tốc độ cực nhanh: ~2-3 giây cho 1,000,000 dòng)."""
    np.random.seed(seed)
    
    # 1. Độ tuổi (18 - 75, trung vị ~27)
    age = np.random.gamma(shape=9.0, scale=3.0, size=n_rows).astype(int)
    age = np.clip(age, 18, 75)
    
    # 2. Thu nhập hàng năm (Log-normal: 10,000 - 300,000, trung vị ~55,000)
    income = np.random.lognormal(mean=10.92, sigma=0.52, size=n_rows)
    income = np.round(np.clip(income, 8_000, 350_000), 0)
    
    # 3. Tình trạng sở hữu nhà ở
    home_ownership_types = ['RENT', 'MORTGAGE', 'OWN', 'OTHER']
    home_probs = [0.505, 0.410, 0.078, 0.007]
    home_ownership = np.random.choice(home_ownership_types, size=n_rows, p=home_probs)
    
    # 4. Thâm niên công tác (năm, phụ thuộc vào độ tuổi)
    emp_len = np.random.exponential(scale=4.5, size=n_rows)
    max_emp_len = np.maximum(age - 18, 0)
    emp_len = np.round(np.clip(emp_len, 0.0, max_emp_len), 1)
    
    # 5. Mục đích vay vốn
    intents = ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT']
    intent_probs = [0.20, 0.18, 0.17, 0.17, 0.16, 0.12]
    loan_intent = np.random.choice(intents, size=n_rows, p=intent_probs)
    
    # 6. Hạng tín dụng nội bộ sơ bộ (A đến G)
    grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    grade_probs = [0.32, 0.32, 0.20, 0.11, 0.03, 0.01, 0.01]
    loan_grade = np.random.choice(grades, size=n_rows, p=grade_probs)
    
    # 7. Số tiền đăng ký vay (1,000 - 35,000)
    loan_amnt = np.random.gamma(shape=4.2, scale=2300, size=n_rows)
    loan_amnt = np.round(np.clip(loan_amnt, 1_000, 35_000), 0)
    
    # 8. Lãi suất khoản vay (phụ thuộc vào xếp hạng tín dụng)
    grade_mean_rates = {'A': 7.45, 'B': 10.95, 'C': 13.45, 'D': 15.35, 'E': 17.15, 'F': 18.75, 'G': 20.25}
    base_rate = np.array([grade_mean_rates[g] for g in loan_grade])
    loan_int_rate = base_rate + np.random.normal(0, 1.25, size=n_rows)
    loan_int_rate = np.round(np.clip(loan_int_rate, 5.42, 23.22), 2)
    
    # 9. Tỷ lệ nợ trên thu nhập (DTI raw)
    loan_percent_income = np.round(loan_amnt / income, 2)
    
    # 10. Lịch sử ghi nhận nợ xấu trên CIC ('Y' / 'N')
    # Nhóm hạng D-G có tỷ lệ nợ xấu trên CIC cao hơn
    grade_default_probs = {'A': 0.05, 'B': 0.12, 'C': 0.22, 'D': 0.35, 'E': 0.50, 'F': 0.65, 'G': 0.75}
    prob_hist_default = np.array([grade_default_probs[g] for g in loan_grade])
    cb_default = np.where(np.random.rand(n_rows) < prob_hist_default, 'Y', 'N')
    
    # 11. Thâm niên lịch sử giao dịch tín dụng (năm)
    cred_hist = np.random.normal(loc=(age - 18) * 0.38, scale=2.5, size=n_rows)
    cred_hist = np.clip(cred_hist, 1, np.maximum(age - 18, 1)).astype(int)
    
    # 12. Xác định nhãn mục tiêu (loan_status: 0 hoặc 1) qua mô hình xác suất Logit
    # Rủi ro tăng khi: DTI cao, Lãi suất cao, Có nợ xấu CIC, Thuê nhà (RENT), Mục đích Medical/DebtConsolidation
    intent_risk = {
        'MEDICAL': 0.45, 'DEBTCONSOLIDATION': 0.55, 'HOMEIMPROVEMENT': 0.30,
        'PERSONAL': 0.05, 'EDUCATION': -0.20, 'VENTURE': -0.35
    }
    intent_offset = np.array([intent_risk[i] for i in loan_intent])
    
    z = (
        -3.284 
        + 6.20 * loan_percent_income 
        + 0.11 * (loan_int_rate - 11.0)
        + 1.35 * (cb_default == 'Y')
        + 0.45 * (home_ownership == 'RENT')
        - 0.35 * (home_ownership == 'OWN')
        - 0.035 * emp_len
        + intent_offset
    )
    p_default = 1.0 / (1.0 + np.exp(-z))
    loan_status = (np.random.rand(n_rows) < p_default).astype(int)
    
    df = pd.DataFrame({
        'person_age': age,
        'person_income': income,
        'person_home_ownership': home_ownership,
        'person_emp_length': emp_len,
        'loan_intent': loan_intent,
        'loan_grade': loan_grade,
        'loan_amnt': loan_amnt,
        'loan_int_rate': loan_int_rate,
        'loan_status': loan_status,
        'loan_percent_income': loan_percent_income,
        'cb_person_default_on_file': cb_default,
        'cb_person_cred_hist_length': cred_hist
    })
    
    return df


def generate_bigdata_spark(spark_session, n_rows: int = 1_000_000):
    """
    Tạo DataFrame phân tán Apache Spark trực tiếp trên cụm Databricks.
    Dùng trong Notebook:
        from generate_bigdata import generate_bigdata_spark
        df_spark = generate_bigdata_spark(spark, n_rows=1000000)
    """
    print(f"⚡ [Databricks Spark] Đang sinh dữ liệu quy mô lớn ({n_rows:,} dòng)...")
    t0 = time.time()
    pdf = generate_credit_data_pandas(n_rows=n_rows)
    spark_df = spark_session.createDataFrame(pdf)
    elapsed = time.time() - t0
    print(f"✅ Hoàn thành sinh {n_rows:,} dòng trong {elapsed:.2f} giây!")
    return spark_df


def main():
    parser = argparse.ArgumentParser(description="Sinh dữ liệu lớn Credit Risk Dataset (Big Data Scale)")
    parser.add_argument("--rows", type=int, default=1_000_000, help="Số lượng dòng cần sinh (mặc định: 1,000,000)")
    parser.add_argument("--output", type=str, default="code/credit_risk_dataset_1M.csv", help="Đường dẫn file đầu ra")
    parser.add_argument("--format", type=str, choices=["csv", "parquet", "both"], default="csv", help="Định dạng tệp")
    parser.add_argument("--seed", type=int, default=42, help="Seed ngẫu nhiên")
    args = parser.parse_args()

    print("=" * 70)
    print("🚀 BIG DATA CREDIT RISK DATASET GENERATOR")
    print("=" * 70)
    print(f"📊 Số lượng dòng yêu cầu: {args.rows:,} dòng")
    print(f"🎯 Seed ngẫu nhiên:        {args.seed}")
    print(f"📁 Tệp xuất:              {args.output}")
    print("-" * 70)

    start_time = time.time()
    df = generate_credit_data_pandas(n_rows=args.rows, seed=args.seed)
    gen_time = time.time() - start_time
    print(f"⚡ Đã sinh xong dữ liệu trong: {gen_time:.2f} giây")

    # Thống kê cơ bản
    default_rate = df['loan_status'].mean() * 100
    print(f"📈 Tỷ lệ nợ xấu thực tế:      {default_rate:.2f}% (Chuẩn mục tiêu ~21.8%)")
    print(f"💾 Kích thước bộ nhớ RAM:     {df.memory_usage().sum() / (1024**2):.2f} MB")

    # Ghi tệp
    if args.format in ["csv", "both"]:
        print(f"💾 Đang ghi tệp CSV: {args.output} ...")
        df.to_csv(args.output, index=False)
        print("✅ Đã ghi xong CSV!")

    if args.format in ["parquet", "both"]:
        parquet_path = args.output.replace(".csv", ".parquet")
        print(f"💾 Đang ghi tệp Parquet nén: {parquet_path} ...")
        df.to_parquet(parquet_path, index=False, compression="snappy")
        print("✅ Đã ghi xong Parquet!")

    total_time = time.time() - start_time
    print("=" * 70)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ QUY TRÌNH TRONG {total_time:.2f} GIÂY!")
    print("=" * 70)


if __name__ == "__main__":
    main()
