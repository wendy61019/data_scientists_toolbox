import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 

#建立函式：將查詢的敘述轉化成水平長條圖的圖檔
def plot_horizontal_bars(sql_query: str, fig_name: str, shareyaxis: bool=False):
    connection = sqlite3.connect("data/kaggle_survey.db")
    response_counts = pd.read_sql(sql_query, con=connection)
    connection.close()
    fig, axes = plt.subplots(ncols=3, figsize=(32, 8), sharey=shareyaxis)     
    survey_years = [2020, 2021, 2022]
    for i in range(len(survey_years)):
        survey_year = survey_years[i]
        response_counts_year = response_counts[response_counts["surveyed_in"] == survey_year]
        y = response_counts_year["response"].values
        width = response_counts_year["response_count"].values
        axes[i].barh(y, width)
        axes[i].set_title(f"{survey_year}")
    plt.tight_layout()
    fig.savefig(f"{fig_name}.png")

#查詢從事資料科學⼯作的職缺抬頭（title）有哪些？
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q5' AND surveyed_in IN (2020, 2021)) OR
       (question_index = 'Q23' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_titles")

#查詢從事資料科學⼯作的⽇常內容是什麼？
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q23' AND surveyed_in = 2020) OR
       (question_index = 'Q24' AND surveyed_in = 2021) OR
       (question_index = 'Q28' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_tasks", shareyaxis=True)

#查詢想要從事資料科學⼯作，需要具備哪些技能與知識？（程式語⾔）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q7' AND surveyed_in IN (2020, 2021)) OR
       (question_index = 'Q12' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_programming_languages")

#查詢想要從事資料科學⼯作，需要具備哪些技能與知識？（資料庫）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q29A' AND surveyed_in = 2020) OR
       (question_index = 'Q32A' AND surveyed_in = 2021) OR
       (question_index = 'Q35' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_databases")

#查詢想要從事資料科學⼯作，需要具備哪些技能與知識？（視覺化）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q14' AND surveyed_in IN (2020, 2021)) OR
       (question_index = 'Q15' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_visualizations")

#查詢想要從事資料科學⼯作，需要具備哪些技能與知識？（機器學習）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q17' AND surveyed_in IN (2020, 2021)) OR
       (question_index = 'Q18' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_machine_learnings")

#進階分析

#查詢想要從事資料科學⼯作，需要具備哪些技能與知識？（雲端平台）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q26A' AND surveyed_in = 2020) OR
       (question_index = 'Q27A' AND surveyed_in = 2021) OR
       (question_index = 'Q31' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_cloud_computing_platforms")

#查詢想要從事資料科學⼯作，需要具備哪些技能與知識？（雲端產品）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q27A' AND surveyed_in = 2020) OR
       (question_index = 'Q29A' AND surveyed_in = 2021) OR
       (question_index = 'Q33' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_cloud_computing_products")

#查詢企業目前對機器學習的應用階段有哪些？（機器學習成熟度）
sql_query = """
SELECT surveyed_in,
       question_type,
       response,
       response_count
  FROM aggregated_responses
 WHERE (question_index = 'Q22' AND surveyed_in = 2020) OR
       (question_index = 'Q23' AND surveyed_in = 2021) OR
       (question_index = 'Q27' AND surveyed_in = 2022)
 ORDER BY surveyed_in,
          response_count;
"""
plot_horizontal_bars(sql_query, "business_machine_learning_adoption")